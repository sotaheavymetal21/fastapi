# -*- coding: utf-8 -*-
import enum
# sqlalchemyライブラリから使用する型などをインポート
from sqlalchemy import Column, Integer, BigInteger, String,DateTime, Enum
# CURRENT_TIMESTAMP関数を利用するためにインポート
from sqlalchemy.sql.functions import current_timestamp
# Baseクラス作成用にインポート
from sqlalchemy.ext.declarative import declarative_base

# Baseクラスを作成
Base = declarative_base()

class GenderType(str, enum.Enum):
    men = "男"
    women = "女"
    they = "その他"

class JobType(str, enum.Enum):
    engineer = "エンジニア"
    designer = "デザイナー"
    projectmanager = "プロジェクトマネージャー"
    producer = "プロデューサー"
    oa = "OA"
    sales = "セールス"
    marketer = "マーケター"

# Baseクラスを継承したモデルを作成
# usersテーブルのモデルUsers
class Users(Base):
    __tablename__ = 'users'
    id = Column(BigInteger, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    birth = Column(DateTime,nullable=False)
    gender = Column(Enum(GenderType, values_callable = lambda x: [e.value for e in x]), nullable = False)
    mail = Column(String(255),nullable=False)
    job = Column(Enum(JobType, values_callable = lambda x: [e.value for e in x]), default = None)
    work_at = Column(DateTime, default = None)
    created_at = Column(DateTime, nullable = False, server_default=current_timestamp())
    updated_at = Column(DateTime)

class Divisions(Base):
    __tablename__ = 'divisions'
    id = Column(BigInteger,primary_key = True, autoincrement=True)
    name = Column(String(255),nullable = False, default = "1")
    leader_user_id = Column(BigInteger,nullable = False)
    start_at = Column(DateTime,nullable = False)

class Belongs(Base):
    __tablename__ = 'belongs'
    id = Column(BigInteger,nullable = False, default = 0, primary_key = True,autoincrement = True)
    user_id = Column(BigInteger, nullable = False, default = 1)
    division_id = Column(BigInteger,nullable = False)
    start_at = Column(DateTime)