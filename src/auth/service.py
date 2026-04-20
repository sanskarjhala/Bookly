from src.auth.models import User
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlmodel import select
from src.auth.schemas import UserCreateModel
from src.auth.utlis import gnerate_password_hash


class UserService:

    async def get_user_by_email(self, email: str, session: AsyncSession):
        statement = select(User).where(User.email == email)
        result = await session.exec(statement=statement)
        return result.first()

    async def user_exists(self, email: str, session: AsyncSession):
        user = await self.get_user_by_email(email=email , session=session)
        if user is None:
            return False
        else:
            return True

    async def create_user(self, user_data: UserCreateModel, session: AsyncSession):
        user_data_dict = user_data.model_dump()

        new_user = User(**user_data)

        new_user.password_hash = gnerate_password_hash(user_data_dict["password"])

        session.add(new_user)
        await session.commit()
        return new_user
