from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey, Enum
from sqlalchemy.orm import relationship
from app import db, app
from enum import Enum as RoleEnum
from flask_login import UserMixin


class UserRole(RoleEnum):
    ADMIN = 1
    ORGANIZER = 2
    USER = 3


class User(db.Model, UserMixin):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    username = Column(String(50), nullable=False, unique=True)
    password = Column(String(50), nullable=False)
    avatar = Column(String(500), default='https://cdn.tienphong.vn/images/a6bf4f60924201126af6849ca45a39804ea063b1ca2743120ebbd3b897dd07f50f478ca4b5a866f499a417fe733ce7396593636e1df77de4bbaf7a780e1ca66f5d6241f9b42334e6e06c1be9adec76eb/e8e30fb8129eafc0f68f-7442-703.jpg')
    userrole = Column(Enum(UserRole), default=UserRole.USER)


class Category(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False, unique=True)
    products = relationship('Product', backref='category', lazy=True)


class Product(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False, unique=True)
    date = Column(String(100), nullable=False, unique=True)
    location = Column(String(255), nullable=False, unique=True)
    price = Column(Float, default=0)
    image = Column(String(500), nullable=True)
    active = Column(Boolean, default=True)
    category_id = Column(Integer, ForeignKey(Category.id), nullable=False)


if __name__ == '__main__':
    with app.app_context():
        db.create_all()

        # import hashlib
        # u = User(name='admin', username='admin', password=hashlib.md5('123456'.encode('utf-8')).hexdigest(), userrole = UserRole.ADMIN)
        #
        # db.session.add(u)
        # db.session.commit()


        # c1 = Category(name='Music Festival')
        # c2 = Category(name='Concert')
        # c3 = Category(name='Live Show')
        #
        # db.session.add_all([c1, c2, c3])
        # db.session.commit()

        # products = [{
        #     "name": "EM XINH SAY HI CONCERT",
        #     "date": "12:00 - 23:00, 13 tháng 09, 2025",
        #     "location": "Khu đô thị Vạn Phúc, Phường Hiệp Bình Phước, Quận Thủ Đức, Thành Phố Hồ Chí Minh",
        #     "price": "800000",
        #     "image": "https://cdn.tienphong.vn/images/a6bf4f60924201126af6849ca45a39804ea063b1ca2743120ebbd3b897dd07f50f478ca4b5a866f499a417fe733ce7396593636e1df77de4bbaf7a780e1ca66f5d6241f9b42334e6e06c1be9adec76eb/e8e30fb8129eafc0f68f-7442-703.jpg",
        #     "category_id": 1
        # }, {
        #     "name": "Lễ hội Âm nhạc Quốc tế 2025",
        #     "date": "17:00 - 23:00, 20 tháng 09, 2025",
        #     "location": "Phố đi bộ Nguyễn Huệ, Quận 1, Thành phố Hồ Chí Minh",
        #     "price": "500000",
        #     "image": "https://cdn.tienphong.vn/images/a6bf4f60924201126af6849ca45a39804ea063b1ca2743120ebbd3b897dd07f50f478ca4b5a866f499a417fe733ce7396593636e1df77de4bbaf7a780e1ca66f5d6241f9b42334e6e06c1be9adec76eb/e8e30fb8129eafc0f68f-7442-703.jpg",
        #     "category_id": 2
        # }, {
        #     "name": "Hội chợ Ẩm thực Quốc tế 2025",
        #     "date": "09:00 - 21:00, 25 tháng 09, 2025",
        #     "location": "Công viên 23/9, Quận 1, Thành phố Hồ Chí Minh",
        #     "price": "100000",
        #     "image": "https://cdn.tienphong.vn/images/a6bf4f60924201126af6849ca45a39804ea063b1ca2743120ebbd3b897dd07f50f478ca4b5a866f499a417fe733ce7396593636e1df77de4bbaf7a780e1ca66f5d6241f9b42334e6e06c1be9adec76eb/e8e30fb8129eafc0f68f-7442-703.jpg",
        #     "category_id": 1
        # }, {
        #     "name": "Triển lãm Ô tô Việt Nam 2025",
        #     "date": "10:00 - 20:00, 15 tháng 10, 2025",
        #     "location": "SECC, Quận 7, Thành phố Hồ Chí Minh",
        #     "price": "150000",
        #     "image": "https://cdn.tienphong.vn/images/a6bf4f60924201126af6849ca45a39804ea063b1ca2743120ebbd3b897dd07f50f478ca4b5a866f499a417fe733ce7396593636e1df77de4bbaf7a780e1ca66f5d6241f9b42334e6e06c1be9adec76eb/e8e30fb8129eafc0f68f-7442-703.jpg",
        #     "category_id": 2
        # }, {
        #     "name": "Đêm nhạc EDM Festival 2025",
        #     "date": "18:00 - 02:00, 28 tháng 09, 2025",
        #     "location": "SVĐ Phú Thọ, Quận 11, Thành phố Hồ Chí Minh",
        #     "price": "1200000",
        #     "image": "https://cdn.tienphong.vn/images/a6bf4f60924201126af6849ca45a39804ea063b1ca2743120ebbd3b897dd07f50f478ca4b5a866f499a417fe733ce7396593636e1df77de4bbaf7a780e1ca66f5d6241f9b42334e6e06c1be9adec76eb/e8e30fb8129eafc0f68f-7442-703.jpg",
        #     "category_id": 1
        # }, {
        #     "name": "Concert Sơn Tùng M-TP SKY Tour",
        #     "date": "19:00 - 23:00, 30 tháng 11, 2025",
        #     "location": "SVĐ Quốc gia Mỹ Đình, Hà Nội",
        #     "price": "1500000",
        #     "image": "https://cdn.tienphong.vn/images/a6bf4f60924201126af6849ca45a39804ea063b1ca2743120ebbd3b897dd07f50f478ca4b5a866f499a417fe733ce7396593636e1df77de4bbaf7a780e1ca66f5d6241f9b42334e6e06c1be9adec76eb/e8e30fb8129eafc0f68f-7442-703.jpg",
        #     "category_id": 1
        # }, {
        #     "name": "Ca nhạc Mỹ Tâm Live Concert",
        #     "date": "19:00 - 22:30, 05 tháng 10, 2025",
        #     "location": "SVĐ Mỹ Đình, Hà Nội",
        #     "price": "950000",
        #     "image": "https://cdn.tienphong.vn/images/a6bf4f60924201126af6849ca45a39804ea063b1ca2743120ebbd3b897dd07f50f478ca4b5a866f499a417fe733ce7396593636e1df77de4bbaf7a780e1ca66f5d6241f9b42334e6e06c1be9adec76eb/e8e30fb8129eafc0f68f-7442-703.jpg",
        #     "category_id": 1
        # }, {
        #     "name": "Vietnam Fashion Week 2025",
        #     "date": "18:00 - 22:00, 18 tháng 10, 2025",
        #     "location": "Nhà hát Lớn Hà Nội",
        #     "price": "600000",
        #     "image": "https://cdn.tienphong.vn/images/a6bf4f60924201126af6849ca45a39804ea063b1ca2743120ebbd3b897dd07f50f478ca4b5a866f499a417fe733ce7396593636e1df77de4bbaf7a780e1ca66f5d6241f9b42334e6e06c1be9adec76eb/e8e30fb8129eafc0f68f-7442-703.jpg",
        #     "category_id": 2
        # }, {
        #     "name": "Lễ hội Trung Thu Phố Cổ",
        #     "date": "16:00 - 22:00, 14 tháng 09, 2025",
        #     "location": "Phố Hàng Mã, Quận Hoàn Kiếm, Hà Nội",
        #     "price": "0",
        #     "image": "https://cdn.tienphong.vn/images/a6bf4f60924201126af6849ca45a39804ea063b1ca2743120ebbd3b897dd07f50f478ca4b5a866f499a417fe733ce7396593636e1df77de4bbaf7a780e1ca66f5d6241f9b42334e6e06c1be9adec76eb/e8e30fb8129eafc0f68f-7442-703.jpg",
        #     "category_id": 1
        # }, {
        #     "name": "Đêm nhạc Rap Việt",
        #     "date": "19:30 - 23:00, 21 tháng 09, 2025",
        #     "location": "Nhà hát Hòa Bình, Quận 10, Thành phố Hồ Chí Minh",
        #     "price": "700000",
        #     "image": "https://cdn.tienphong.vn/images/a6bf4f60924201126af6849ca45a39804ea063b1ca2743120ebbd3b897dd07f50f478ca4b5a866f499a417fe733ce7396593636e1df77de4bbaf7a780e1ca66f5d6241f9b42334e6e06c1be9adec76eb/e8e30fb8129eafc0f68f-7442-703.jpg",
        #     "category_id": 1
        # }, {
        #     "name": "Festival Trà Việt",
        #     "date": "09:00 - 19:00, 11 tháng 10, 2025",
        #     "location": "Đà Lạt, Lâm Đồng",
        #     "price": "80000",
        #     "image": "https://cdn.tienphong.vn/images/a6bf4f60924201126af6849ca45a39804ea063b1ca2743120ebbd3b897dd07f50f478ca4b5a866f499a417fe733ce7396593636e1df77de4bbaf7a780e1ca66f5d6241f9b42334e6e06c1be9adec76eb/e8e30fb8129eafc0f68f-7442-703.jpg",
        #     "category_id": 2
        # }, {
        #     "name": "Hội chợ Giáng Sinh 2025",
        #     "date": "10:00 - 22:00, 20 tháng 12, 2025",
        #     "location": "Phố đi bộ Hồ Gươm, Hà Nội",
        #     "price": "0",
        #     "image": "https://cdn.tienphong.vn/images/a6bf4f60924201126af6849ca45a39804ea063b1ca2743120ebbd3b897dd07f50f478ca4b5a866f499a417fe733ce7396593636e1df77de4bbaf7a780e1ca66f5d6241f9b42334e6e06c1be9adec76eb/e8e30fb8129eafc0f68f-7442-703.jpg",
        #     "category_id": 2
        # }]
        #
        # for p in products:
        #     prod = Product(**p)
        #     db.session.add(prod)
        #
        # db.session.commit()
