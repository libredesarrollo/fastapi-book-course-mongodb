from fastapi import APIRouter, Body, Depends, HTTPException, status, Path
from pymongo.database import Database
from bson import ObjectId

from mongo_db import get_mongo_database
from schemes import TaskWrite

mongo_task_router = APIRouter()

# CREATE
@mongo_task_router.post("/", status_code=status.HTTP_201_CREATED, summary="Crear una nueva tarea")
async def add_task(
    task: TaskWrite = Body(...),
    db: Database = Depends(get_mongo_database),
):
    """
    Crea una nueva tarea en la base de datos.
    """
    # task_dict = task.dict()
    task_dict = task.model_dump()
    insert_result = await db.tasks.insert_one(task_dict)
    return {
        "message": "Tarea añadida correctamente",
        "id": str(insert_result.inserted_id),
    }

# READ ALL
@mongo_task_router.get("/", summary="Obtener todas las tareas")
async def get_all_tasks(db: Database = Depends(get_mongo_database)):
    """
    Obtiene todas las tareas de la colección 'tasks'.
    """
    tasks_cursor = db.tasks.find()
    return await tasks_cursor.to_list(length=None)

# READ ONE
@mongo_task_router.get("/{task_id}", summary="Obtener una tarea")
async def get_task(
    task_id: str = Path(..., description="El ID de la tarea a obtener"),
    db: Database = Depends(get_mongo_database),
):
    """
    Obtiene una única tarea por su ID.
    """
    if not ObjectId.is_valid(task_id):
        raise HTTPException(status_code=400, detail=f"ObjectId inválido: {task_id}")
    
    task = await db.tasks.find_one({"_id": ObjectId(task_id)})
    
    if not task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Tarea con id {task_id} no encontrada"
        )
    return task

# UPDATE
@mongo_task_router.put("/{task_id}", summary="Actualizar una tarea")
async def update_task(
    task_id: str = Path(..., description="El ID de la tarea a actualizar"),
    task: TaskWrite = Body(...),
    db: Database = Depends(get_mongo_database),
):
    """
    Actualiza los campos de una tarea.
    """
    if not ObjectId.is_valid(task_id):
        raise HTTPException(status_code=400, detail=f"ObjectId inválido: {task_id}")

    # update_data = task.dict(exclude_unset=True)
    update_data = task.model_dump(exclude_none=True)

    if not update_data:
        raise HTTPException(status_code=400, detail="No se proporcionaron datos para actualizar")

    result = await db.tasks.update_one({"_id": ObjectId(task_id)}, {"$set": update_data})

    if result.matched_count == 0:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Tarea con id {task_id} no encontrada")
    
    if result.modified_count == 1:
        updated_task = await db.tasks.find_one({"_id": ObjectId(task_id)})
        return updated_task
    
    return {"message": "Los datos de la tarea eran los mismos, no se realizó ninguna actualización."}

# DELETE
@mongo_task_router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT, summary="Eliminar una tarea")
async def delete_task(
    task_id: str = Path(..., description="El ID de la tarea a eliminar"),
    db: Database = Depends(get_mongo_database),
):
    """
    Elimina una tarea de la base de datos.
    """
    if not ObjectId.is_valid(task_id):
        raise HTTPException(status_code=400, detail=f"ObjectId inválido: {task_id}")

    result = await db.tasks.delete_one({"_id": ObjectId(task_id)})

    if result.deleted_count == 0:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Tarea con id {task_id} no encontrada")
    
    return
