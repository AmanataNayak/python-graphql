import strawberry
from strawberry import Schema

## Queries
def get_name() -> str:
    return "Strawberry"

class User:
    id: str
    name: str
    
    def __init__(self, id: str, name: str):
        self.id = id
        self.name = name

@strawberry.type(name="User")
class UserType:
    id: strawberry.ID
    name: str

FRUITS = [
    "Strawberry",
    "Apple",
    "Orange",
]


@strawberry.type
class Query:
    """
    query :
        query {
            name,
            age
        }
    """
    name: str = strawberry.field(resolver=get_name)

    @strawberry.field
    def age(self) -> int:
        return 20

    @strawberry.field(graphql_type=UserType)
    def user(self) -> User:
        return User(id='ringo189', name='Amanata')
    
    # Arguments: graphql fields can accept argument, usually to filter out or retrive specfic object
    @strawberry.field
    def fruit(self, startswith: str) -> str | None:
        """
        Query:
        {
            fruit(startswith: "A")
        }
        """
        for fruit in FRUITS:
            if fruit.startswith(startswith):
                return fruit
        return None
    
schema = Schema(query=Query)