from sqlalchemy.orm import Session
from . import schemas, models
from tasks_api.task_list.models import TaskList
from tasks_api.users.models import User
from fastapi import HTTPException, status
from tasks_api import constants
from sqlalchemy import asc


def create_task(list_id: int, request: schemas.ShowTask, db: Session, current_user):
    user = db.query(User).filter(User.email == current_user.email).first()
    task_list = db.query(TaskList).filter(TaskList.id == list_id, TaskList.user_id == user.id)
    if not task_list.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=constants.MSG_TASK_LIST_NOT_FOUND2.format(list_id))

    new_task = models.Task(title=request.title, details=request.details, date_time=request.date_time,
                           list_id=list_id)
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task


def show_all_task(list_id: int, db: Session, current_user, date):
    user = db.query(User).filter(User.email == current_user.email).first()
    task_list = db.query(TaskList).filter(TaskList.id == list_id, TaskList.user_id == user.id).first()
    if not task_list:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=constants.MSG_TASK_LIST_NOT_FOUND2.format(list_id))

    task = db.query(models.Task).filter(models.Task.list_id == task_list.id)
    if not task:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=constants.MSG_TASK_LIST_NOT_FOUND2.format(list_id))
    if date:
        return task.order_by(asc(models.Task.date_time)).all()
    return task.order_by(asc(models.Task.title)).all()


def show_one_task(task_id: int, db: Session, current_user):
    user = db.query(User).filter(User.email == current_user.email).first()
    task = db.query(models.Task).filter(models.Task.id == task_id).first()
    if not task:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=constants.MSG_TASK_NOT_FOUND.format(task_id))

    task_list = db.query(TaskList).filter(TaskList.id == task.list_id, TaskList.user_id == user.id).first()
    if not task_list:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=constants.MSG_TASK_NOT_FOUND.format(task_id))

    return task


def update_task(task_id: int, request: schemas.ShowTask, starred, db: Session, current_user):
    user = db.query(User).filter(User.email == current_user.email).first()
    task_obj = db.query(models.Task).filter(models.Task.id == task_id).first()
    if not task_obj:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=constants.MSG_TASK_NOT_FOUND.format(task_id))

    task_list = db.query(TaskList).filter(TaskList.id == task_obj.list_id, TaskList.user_id == user.id).first()
    if not task_list:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=constants.MSG_TASK_NOT_FOUND.format(task_id))

    task = db.query(models.Task).filter(models.Task.id == task_id)

    task.update(
        {"title": request.title, "details": request.details, "date_time": request.date_time, "starred": starred},
        synchronize_session=False)
    db.commit()
    update_status = {
        "message": constants.MSG_TASK_UPDATED
    }
    return update_status


def delete_task(task_id: int, db: Session, current_user):
    user = db.query(User).filter(User.email == current_user.email).first()
    task_obj = db.query(models.Task).filter(models.Task.id == task_id).first()

    if not task_obj:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=constants.MSG_TASK_NOT_FOUND.format(task_id))

    task_list = db.query(TaskList).filter(TaskList.id == task_obj.list_id, TaskList.user_id == user.id).first()
    if not task_list:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=constants.MSG_TASK_NOT_FOUND.format(task_id))

    task = db.query(models.Task).filter(models.Task.id == task_id)
    task.delete(synchronize_session=False)
    db.commit()
    delete_status ={
        "message": constants.MSG_TASK_DELETED
    }
    return delete_status
