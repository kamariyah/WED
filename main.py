from fastapi import FastAPI

app = FastAPI()

posts = {}
last_added_post_id = -1

class CreatePostRequest():
 id: int
 author: str
 text: str
 keywords: str


class EditPostRequest():
    id:[int] = None
    author:[str] = None
    text:[str] = None
    keywords:[str] = None

# Модель данных для сущности Posts
class Post():
    id: int
    author: str
    text: str
    keywords: str

# Фиктивная база данных для демонстрации
db: [int, Post] = {}

# Создание таблицы в базе данных для сущности Posts
@app.on_event("startup")
async def startup_event():
    # Создаем таблицу если она не существует
    # Вместо этого могут быть использованы различные ORM или SQL-запросы
    pass

# Получение всех постов
@app.get("/posts")
async def get_posts():
    return list(db.values())

# Создание нового поста
@app.post("/posts")
async def create_post(post: Post):
    db[post.id] = post
    return post

# Получение поста по его id
@app.get("/posts/{post_id}")
async def get_post(post_id: int):
    return db.get(post_id)

# Обновление поста по его id
@app.put("/posts/{post_id}")
async def update_post(post_id: int, post: Post):
    if post_id in db:
        updated_post = post.copy(update={"id": post_id})
        db[post_id] = updated_post
        return updated_post
    else:
        return {"error": "Post not found"}

# Удаление поста по его id
@app.delete("/posts/{post_id}")
async def delete_post(post_id: int):
    if post_id in db:
        del db[post_id]
        return {"message": "Post deleted"}
    else:
        return {"error": "Post not found"}