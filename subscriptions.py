import asyncio
from typing import AsyncGenerator
import strawberry
from strawberry import Schema

@strawberry.type
class Query:
    @strawberry.field
    def hello(self) -> str:
        return "Hello"

@strawberry.type
class Subscription:
    @strawberry.subscription
    async def count(self, target: int = 100) -> AsyncGenerator[int, None]:
        for i in range(target):
            yield i
            await asyncio.sleep(0.5)

schema = Schema(query=Query, subscription=Subscription)
