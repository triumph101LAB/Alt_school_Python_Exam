from fastapi import HTTPException, status
from schemas.user import UserRole, User
from services.user import UserService

def is_admint_user(user_id:int):
    user: User = UserService.get_user(user_id)
    
    if not user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User Not found"
        )
    if not user.role == UserRole.ADMIN:
        raise HTTPException(
          status_code= status.HTTP_43  
        )    