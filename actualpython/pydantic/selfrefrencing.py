# self referencing models
from pydantic import BaseModel
from typing import List, Optional

class Comment(BaseModel):
    id: int
    content: str
    replies: Optional[List['Comment']] = None

Comment.model_rebuild()

comment_data = {
    "id": 1,
    "content": "This is a comment",
    "replies": [
        {
            "id": 2,
            "content": "This is a reply to the comment",
            "replies": [
                {
                    "id": 3,
                    "content": "This is a reply to the reply",
                    "replies": []
                }
            ]
        }
    ]
}

comment = Comment(**comment_data)

print(comment)