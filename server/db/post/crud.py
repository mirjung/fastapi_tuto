from sqlalchemy.orm import Session


from server.db.post.models import Post as PostModel
from server.db.post.schemas import PostCreate as PostCreateSchema

def get_post(db: Session, id: int):
    return db.query(PostModel).filter(PostModel.id == id).first()

def create_post(db: Session, posts: PostCreateSchema):
    new_data = PostModel(**posts.dict())
    db.add(new_data)
    db.commit()
    db.refresh(new_data)
    return new_data

def delete_post(db: Session, author_id: int):
    return db.query(PostModel).filter(PostModel.author_id == author_id).delete()

def update_post(db: Session, posts: PostCreateSchema, author_id: int):
    current_data = db.query(PostModel).filter(PostModel.author_id == author_id).first()
    new_data = posts.dict()
    for k, v in new_data.items():
        setattr(current_data, k, v)
        
    db.commit()
    return new_data