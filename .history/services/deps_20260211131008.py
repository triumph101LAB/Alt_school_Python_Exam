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
    if not user.role != UserRole.ADMIN:
        raise HTTPException(
          status_code= status.HTTP_403_FORBIDDEN,
          detail="You do not have the permission to perform this action"  
        )
def is_student_user(user_id:int):
    user = User = UserService.get_user(user_id)
    
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="user not found"
        )
        
    if user.role    
                