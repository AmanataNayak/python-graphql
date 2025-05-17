import strawberry
from strawberry import Schema


@strawberry.type
class Query:
    @strawberry.field
    def hello(self) -> str:
        return "world"
    
@strawberry.type
class Book:
    title: str
    author: str


@strawberry.type
class Mutation:
    @strawberry.mutation
    def add_book(self, title: str, author: str) -> Book:
        print(f'Addiding {title} by {author}')
        return Book(title=title, author=author)
    
    # mutation without return
    @strawberry.mutation
    def restart() -> None:
        print("Restatirng the server")

    

schema = Schema(query=Query, mutation=Mutation)