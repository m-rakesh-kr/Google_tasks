from sqlalchemy import asc, desc
from sqlalchemy.orm import Session
from . import schemas, models
from tasks_api.users.models import User
from tasks_api.task_list.models import TaskList
from tasks_api.task.models import Task
from fastapi import HTTPException, status
from tasks_api import constants


def create_sub_task(task_id: int, request: schemas.ShowSubTask, db: Session, current_user):
    user = db.query(User).filter(User.email == current_user.email).first()
    task = db.query(Task).filter(Task.id == task_id).first()
    if not task:
        # It will check that Do tasks exists or not of given task_id.
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=constants.MSG_TASK_NOT_FOUND.format(task_id))
    task_list = db.query(TaskList).filter(TaskList.id == task.list_id, TaskList.user_id == user.id).first()
    if not task_list:
        # It will check that Do task_list exists or not of given task_id.
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=constants.MSG_TASK_NOT_FOUND.format(task_id))

    new_sub_task = models.SubTask(title=request.title, details=request.details, date_time=request.date_time,
                                  task_id=task_id)
    db.add(new_sub_task)
    db.commit()
    db.refresh(new_sub_task)
    return new_sub_task


def show_all_sub_task(task_id: int, db: Session, date, current_user):
    user = db.query(User).filter(User.email == current_user.email).first()
    sub_task = db.query(models.SubTask).filter(models.SubTask.task_id == task_id).first()
    if sub_task is None:
        # It will check that Do sub_task exists or not of given task_id.
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=constants.MSG_TASK_NOT_FOUND2.format(task_id))

    if sub_task.task.list.creator.id != user.id:
        # It will filter that Task_id which has been by user is being belonged that user or not
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=constants.MSG_TASK_NOT_FOUND2.format(task_id))

    sub_task_all = db.query(models.SubTask).filter(models.SubTask.task_id == task_id)
    if date:
        return sub_task_all.order_by(desc(models.SubTask.date_time)).all()
    return sub_task_all.order_by(asc(models.SubTask.title)).all()


def show_one_sub_task(sub_task_id: int, db: Session, current_user):
    user = db.query(User).filter(User.email == current_user.email).first()
    sub_task = db.query(models.SubTask).filter(models.SubTask.id == sub_task_id).first()
    if sub_task is None:
        # It will check that Do sub_task exists or not of given sub_task_id.
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=constants.MSG_SUB_TASK_NOT_FOUND.format(sub_task_id))
    if sub_task.task.list.creator != user:
        # It will filter that Task_id which has been by user is being belonged that user or not
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=constants.MSG_SUB_TASK_NOT_FOUND.format(sub_task_id))
    return sub_task


def update_sub_task(sub_task_id: int, request: schemas.ShowSubTask, starred, db: Session, current_user):
    user = db.query(User).filter(User.email == current_user.email).first()
    sub_task = db.query(models.SubTask).filter(models.SubTask.id == sub_task_id).first()
    if sub_task is None:
        # It will check that Do sub_task exists or not of given sub_task_id.
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=constants.MSG_SUB_TASK_NOT_FOUND.format(sub_task_id))
    if sub_task.task.list.creator.id != user.id:
        # It will filter that Task_id which has been by user is being belonged that user or not
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=constants.MSG_SUB_TASK_NOT_FOUND.format(sub_task_id))

    subtask = db.query(models.SubTask).filter(models.SubTask.id == sub_task_id)
    subtask.update(
        {"title": request.title, "details": request.details, "date_time": request.date_time, "starred": starred},
        synchronize_session="evaluate")
    db.commit()
    update_status = {
        "message": constants.MSG_SUB_TASK_UPDATED
    }
    return update_status


def delete_sub_task(sub_task_id: int, db: Session, current_user):
    user = db.query(User).filter(User.email == current_user.email).first()
    sub_task = db.query(models.SubTask).filter(models.SubTask.id == sub_task_id).first()
    if sub_task is None:
        # It will check that Do sub_task exists or not of given sub_task_id.
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=constants.MSG_SUB_TASK_NOT_FOUND.format(sub_task_id))
    if sub_task.task.list.creator.id != user.id:
        # It will filter that Task_id which has been by user is being belonged that user or not
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=constants.MSG_SUB_TASK_NOT_FOUND.format(sub_task_id))
    subtask = db.query(models.SubTask).filter(models.SubTask.id == sub_task_id)
    subtask.delete(synchronize_session="evaluate")
    db.commit()
    delete_status = {
        "message": constants.MSG_SUB_TASK_DELETED
    }
    return delete_status
