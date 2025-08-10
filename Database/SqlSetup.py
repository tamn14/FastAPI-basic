
# create_engine: Dùng để tạo một engine kết nối với database
from sqlalchemy import create_engine
# declarative_base: Dùng để tạo Base class, từ đó ta sẽ kế thừa để định nghĩa các model (các bảng trong DB).
from sqlalchemy.ext.declarative import declarative_base
# sessionmaker: Tạo ra các session – là đối tượng quản lý việc giao tiếp với database (truy vấn, thêm, sửa, xóa…).
from sqlalchemy.orm import sessionmaker


# string connection
SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:root@localhost/FastApiDB"

# Tạo engine kết nối
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={}, future=True
)

# Tạo sessionTạo session
SessionLocal = sessionmaker(
    autocommit=False, autoflush=False, bind=engine, future=True
)
# Tạo lớp cơ sở cho các model
Base = declarative_base()

# DB Utilities , Hàm tiện ích lấy session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()