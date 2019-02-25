
from sqlalchemy import Column, String, Integer,create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# 创建对象的基类:
Base = declarative_base()

# # 定义Douban对象:
class Pengfu(Base):
    __tablename__ = 'pengfu'
    id = Column(Integer, primary_key=True)
    name = Column(String(150))
    title = Column(String(500))
    content = Column(String(500))
    img = Column(String(500))
    # __mapper_args__ = {"order_by": id.desc()}

    def to_dict(self):
        return {c.name: getattr(self, c.name, None) for c in self.__table__.columns}
    Base.to_dict = to_dict

engine = create_engine('mysql+mysqlconnector://root:158269@47.75.84.250:3306/lty')

# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)

# 创建session对象:
session = DBSession()

if __name__ == '__main__':
    results = session.query(Pengfu).order_by('-id').limit(10).offset(0).all()

    # results = session.query(Pengfu).all()
    print(results[0].to_dict())
    # print(results[0:10][::-1].to_dict())
    # 提交即保存到数据库:
    session.commit()
    # 关闭session:
    session.close()