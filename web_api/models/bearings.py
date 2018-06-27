# coding: utf-8
from sqlalchemy import Column, Date, DateTime, Index, Integer, Numeric, String, text
from web_api.databases.bearings import db


Base = db.Model
metadata = Base.metadata


def to_dict(self):
    return {c.name: getattr(self, c.name, None) for c in self.__table__.columns}

Base.to_dict = to_dict
Base.__bind_key__ = 'bearings'


class BuyerOrders(Base):
    __tablename__ = 'buyer_orders'

    id = Column(Integer, primary_key=True)
    uid = Column(Integer, nullable=False, index=True, server_default=text("'0'"))
    cid = Column(Integer, nullable=False, index=True, server_default=text("'0'"))
    status_delete = Column(Integer, nullable=False, server_default=text("'0'"))
    delete_time = Column(DateTime)
    create_time = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    update_time = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))


class Catalogue(Base):
    __tablename__ = 'catalogue'
    __table_args__ = (
        Index('product_brand', 'product_brand', 'product_model', unique=True),
    )

    id = Column(Integer, primary_key=True)
    product_brand = Column(String(16), nullable=False, server_default=text("''"))
    product_model = Column(String(32), nullable=False, index=True, server_default=text("''"))
    product_label = Column(String(32), nullable=False, server_default=text("''"))
    product_brand_old = Column(String(16), nullable=False, server_default=text("''"))
    product_model_old = Column(String(32), nullable=False, index=True, server_default=text("''"))
    product_class = Column(String(32), nullable=False, server_default=text("''"))
    ind = Column(Numeric(4, 0), nullable=False, server_default=text("'0'"))
    oud = Column(Numeric(4, 0), nullable=False, server_default=text("'0'"))
    wid = Column(Numeric(4, 0), nullable=False, server_default=text("'0'"))
    speed_g = Column(Numeric(6, 0), nullable=False, server_default=text("'0'"))
    speed_o = Column(Numeric(6, 0), nullable=False, server_default=text("'0'"))
    weight = Column(Numeric(8, 3), nullable=False, server_default=text("'0.000'"))
    serie = Column(String(32), nullable=False, server_default=text("''"))
    accuracy = Column(String(64), nullable=False, server_default=text("''"))
    preload = Column(String(64), nullable=False, server_default=text("''"))
    seal = Column(String(64), nullable=False, server_default=text("''"))
    angle = Column(String(64), nullable=False, server_default=text("''"))
    r_size = Column(String(64), nullable=False, server_default=text("''"))
    r_matel = Column(String(64), nullable=False, server_default=text("''"))
    assembly_no = Column(String(64), nullable=False, server_default=text("''"))
    assembly_type = Column(String(64), nullable=False, server_default=text("''"))
    note = Column(String(64), nullable=False, server_default=text("''"))
    tag = Column(String(256), nullable=False, server_default=text("''"))
    status_delete = Column(Integer, nullable=False, server_default=text("'0'"))
    delete_time = Column(DateTime)
    create_time = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    update_time = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))


class Category(Base):
    __tablename__ = 'category'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False, server_default=text("''"))
    main_id = Column(Integer, nullable=False, index=True, server_default=text("'0'"))
    status_delete = Column(Integer, nullable=False, server_default=text("'0'"))
    delete_time = Column(DateTime)
    create_time = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    update_time = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))


class Customer(Base):
    __tablename__ = 'customer'

    id = Column(Integer, primary_key=True)
    company_name = Column(String(100), nullable=False, server_default=text("''"))
    company_address = Column(String(100), nullable=False, server_default=text("''"))
    company_site = Column(String(100), nullable=False, server_default=text("''"))
    company_tel = Column(String(100), nullable=False, server_default=text("''"))
    company_fax = Column(String(100), nullable=False, server_default=text("''"))
    company_type = Column(Integer, nullable=False, server_default=text("'0'"))
    owner_uid = Column(Integer, nullable=False, server_default=text("'0'"))
    status_delete = Column(Integer, nullable=False, server_default=text("'0'"))
    delete_time = Column(DateTime)
    create_time = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    update_time = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))


class CustomerContact(Base):
    __tablename__ = 'customer_contact'

    id = Column(Integer, primary_key=True)
    cid = Column(Integer, nullable=False, index=True, server_default=text("'0'"))
    name = Column(String(20), nullable=False, server_default=text("''"))
    salutation = Column(String(20), nullable=False, server_default=text("''"))
    mobile = Column(String(20), nullable=False, server_default=text("''"))
    tel = Column(String(20), nullable=False, server_default=text("''"))
    fax = Column(String(20), nullable=False, server_default=text("''"))
    department = Column(String(20), nullable=False, server_default=text("''"))
    address = Column(String(100), nullable=False, server_default=text("''"))
    note = Column(String(256), nullable=False, server_default=text("''"))
    status_default = Column(Integer, nullable=False, server_default=text("'0'"))
    status_delete = Column(Integer, nullable=False, server_default=text("'0'"))
    delete_time = Column(DateTime)
    create_time = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    update_time = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))


class CustomerInvoice(Base):
    __tablename__ = 'customer_invoice'

    cid = Column(Integer, primary_key=True)
    company_name = Column(String(100), nullable=False, server_default=text("''"))
    company_tax_id = Column(String(20), nullable=False, server_default=text("''"))
    company_address = Column(String(100), nullable=False, server_default=text("''"))
    company_tel = Column(String(100), nullable=False, server_default=text("''"))
    company_bank_name = Column(String(100), nullable=False, server_default=text("''"))
    company_bank_account = Column(String(100), nullable=False, server_default=text("''"))
    status_delete = Column(Integer, nullable=False, server_default=text("'0'"))
    delete_time = Column(DateTime)
    create_time = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    update_time = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))


class Delivery(Base):
    __tablename__ = 'delivery'

    id = Column(Integer, primary_key=True)
    sales_order_id = Column(Integer, index=True, server_default=text("'0'"))
    customer_cid = Column(Integer, index=True, server_default=text("'0'"))
    type_delivery = Column(Integer, nullable=False, server_default=text("'0'"))
    status_audit = Column(Integer, nullable=False, server_default=text("'0'"))
    status_confirm = Column(Integer, nullable=False, server_default=text("'0'"))
    status_delete = Column(Integer, nullable=False, server_default=text("'0'"))
    audit_time = Column(DateTime)
    confirm_time = Column(DateTime)
    delete_time = Column(DateTime)
    create_time = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    update_time = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))


class Inventory(Base):
    __tablename__ = 'inventory'

    id = Column(Integer, primary_key=True)
    product_id = Column(Integer, nullable=False, index=True)
    warehouse_id = Column(Integer, nullable=False)
    rack_id = Column(Integer, nullable=False)
    stock_qty = Column(Integer, nullable=False)
    note = Column(String(256), nullable=False, server_default=text("''"))
    status_delete = Column(Integer, nullable=False, server_default=text("'0'"))
    delete_time = Column(DateTime)
    create_time = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    update_time = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))


class Product(Base):
    __tablename__ = 'product'
    __table_args__ = (
        Index('product_brand', 'product_brand', 'product_model', unique=True),
    )

    id = Column(Integer, primary_key=True)
    category_id = Column(Integer, nullable=False, server_default=text("'0'"))
    product_brand = Column(String(16), nullable=False, server_default=text("''"))
    product_model = Column(String(32), nullable=False, index=True, server_default=text("''"))
    product_sku = Column(String(16), nullable=False, server_default=text("'Pcs'"))
    note = Column(String(64), nullable=False, server_default=text("''"))
    status_delete = Column(Integer, nullable=False, server_default=text("'0'"))
    delete_time = Column(DateTime)
    create_time = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    update_time = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))


class Purchase(Base):
    __tablename__ = 'purchase'

    id = Column(Integer, primary_key=True)
    buyer_order_id = Column(Integer, index=True, server_default=text("'0'"))
    supplier_cid = Column(Integer, index=True, server_default=text("'0'"))
    type_delivery = Column(Integer, nullable=False, server_default=text("'0'"))
    status_audit = Column(Integer, nullable=False, server_default=text("'0'"))
    status_confirm = Column(Integer, nullable=False, server_default=text("'0'"))
    status_delete = Column(Integer, nullable=False, server_default=text("'0'"))
    audit_time = Column(DateTime)
    confirm_time = Column(DateTime)
    delete_time = Column(DateTime)
    create_time = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    update_time = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))


class Quote(Base):
    __tablename__ = 'quote'

    id = Column(Integer, primary_key=True)
    uid = Column(Integer, nullable=False, index=True, server_default=text("'0'"))
    cid = Column(Integer, nullable=False, index=True, server_default=text("'0'"))
    contact_id = Column(Integer, nullable=False)
    amount_product = Column(Numeric(10, 2), nullable=False, server_default=text("'0.00'"))
    amount_shipping = Column(Numeric(10, 2), nullable=False, server_default=text("'0.00'"))
    amount_adjustment = Column(Numeric(10, 2), nullable=False, server_default=text("'0.00'"))
    amount_quote = Column(Numeric(10, 2), nullable=False, server_default=text("'0.00'"))
    note = Column(String(256), nullable=False, server_default=text("''"))
    status_tax = Column(Integer, nullable=False, server_default=text("'0'"))
    status_audit = Column(Integer, nullable=False, server_default=text("'0'"))
    status_order = Column(Integer, nullable=False, server_default=text("'0'"))
    status_delete = Column(Integer, nullable=False, server_default=text("'0'"))
    expiry_date = Column(Date, nullable=False)
    audit_time = Column(DateTime)
    order_time = Column(DateTime)
    delete_time = Column(DateTime)
    create_time = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    update_time = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))


class QuoteItem(Base):
    __tablename__ = 'quote_item'

    id = Column(Integer, primary_key=True)
    quote_id = Column(Integer, nullable=False, index=True)
    product_id = Column(Integer, nullable=False, index=True)
    product_brand = Column(String(16), nullable=False, server_default=text("''"))
    product_model = Column(String(32), nullable=False, server_default=text("''"))
    product_sku = Column(String(16), nullable=False, server_default=text("'Pcs'"))
    product_note = Column(String(64), nullable=False, server_default=text("''"))
    quantity = Column(Integer, nullable=False, server_default=text("'0'"))
    unit_price = Column(Numeric(8, 2), nullable=False, server_default=text("'0.00'"))
    status_delete = Column(Integer, nullable=False, server_default=text("'0'"))
    delete_time = Column(DateTime)
    create_time = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    update_time = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))


class Rack(Base):
    __tablename__ = 'rack'

    id = Column(Integer, primary_key=True)
    warehouse_id = Column(Integer, nullable=False)
    name = Column(String(16), nullable=False, server_default=text("''"))
    status_delete = Column(Integer, nullable=False, server_default=text("'0'"))
    delete_time = Column(DateTime)
    create_time = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    update_time = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))


class Role(Base):
    __tablename__ = 'role'

    id = Column(Integer, primary_key=True)
    name = Column(String(20), nullable=False, unique=True, server_default=text("''"))
    note = Column(String(256), nullable=False, server_default=text("''"))
    create_time = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    update_time = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))


class SalesOrders(Base):
    __tablename__ = 'sales_orders'

    id = Column(Integer, primary_key=True)
    uid = Column(Integer, nullable=False, index=True, server_default=text("'0'"))
    cid = Column(Integer, nullable=False, index=True, server_default=text("'0'"))
    status_delete = Column(Integer, nullable=False, server_default=text("'0'"))
    delete_time = Column(DateTime)
    create_time = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    update_time = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))


class Supplier(Base):
    __tablename__ = 'supplier'

    id = Column(Integer, primary_key=True)
    company_name = Column(String(100), nullable=False, server_default=text("''"))
    company_address = Column(String(100), nullable=False, server_default=text("''"))
    company_site = Column(String(100), nullable=False, server_default=text("''"))
    company_tel = Column(String(100), nullable=False, server_default=text("''"))
    company_fax = Column(String(100), nullable=False, server_default=text("''"))
    company_type = Column(Integer, nullable=False, server_default=text("'0'"))
    owner_uid = Column(Integer, nullable=False, server_default=text("'0'"))
    status_delete = Column(Integer, nullable=False, server_default=text("'0'"))
    delete_time = Column(DateTime)
    create_time = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    update_time = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))


class SupplierContact(Base):
    __tablename__ = 'supplier_contact'

    id = Column(Integer, primary_key=True)
    cid = Column(Integer, nullable=False, index=True, server_default=text("'0'"))
    name = Column(String(20), nullable=False, server_default=text("''"))
    salutation = Column(String(20), nullable=False, server_default=text("''"))
    mobile = Column(String(20), nullable=False, server_default=text("''"))
    tel = Column(String(20), nullable=False, server_default=text("''"))
    fax = Column(String(20), nullable=False, server_default=text("''"))
    department = Column(String(20), nullable=False, server_default=text("''"))
    address = Column(String(100), nullable=False, server_default=text("''"))
    note = Column(String(256), nullable=False, server_default=text("''"))
    status_default = Column(Integer, nullable=False, server_default=text("'0'"))
    status_delete = Column(Integer, nullable=False, server_default=text("'0'"))
    delete_time = Column(DateTime)
    create_time = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    update_time = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))


class SupplierInvoice(Base):
    __tablename__ = 'supplier_invoice'

    cid = Column(Integer, primary_key=True)
    company_name = Column(String(100), nullable=False, server_default=text("''"))
    company_tax_id = Column(String(20), nullable=False, server_default=text("''"))
    company_address = Column(String(100), nullable=False, server_default=text("''"))
    company_tel = Column(String(100), nullable=False, server_default=text("''"))
    company_bank_name = Column(String(100), nullable=False, server_default=text("''"))
    company_bank_account = Column(String(100), nullable=False, server_default=text("''"))
    status_delete = Column(Integer, nullable=False, server_default=text("'0'"))
    delete_time = Column(DateTime)
    create_time = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    update_time = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String(20, u'utf8_bin'), nullable=False, server_default=text("''"))
    role_id = Column(Integer, nullable=False, server_default=text("'0'"))
    parent_id = Column(Integer, nullable=False, server_default=text("'0'"))
    status_delete = Column(Integer, nullable=False, server_default=text("'0'"))
    delete_time = Column(DateTime)
    create_time = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    update_time = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))


class UserAuth(Base):
    __tablename__ = 'user_auth'
    __table_args__ = (
        Index('type_auth', 'type_auth', 'auth_key', unique=True),
    )

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, nullable=False, index=True, server_default=text("'0'"))
    type_auth = Column(Integer, nullable=False, server_default=text("'0'"))
    auth_key = Column(String(60, u'utf8_bin'), nullable=False, server_default=text("''"))
    auth_secret = Column(String(60, u'utf8_bin'), nullable=False, server_default=text("''"))
    status_verified = Column(Integer, nullable=False, server_default=text("'0'"))
    create_time = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    update_time = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))


class Warehouse(Base):
    __tablename__ = 'warehouse'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False, unique=True, server_default=text("''"))
    address = Column(String(100), nullable=False, server_default=text("''"))
    linkman = Column(String(20), nullable=False, server_default=text("''"))
    tel = Column(String(20), nullable=False, server_default=text("''"))
    fax = Column(String(20), nullable=False, server_default=text("''"))
    status_delete = Column(Integer, nullable=False, server_default=text("'0'"))
    delete_time = Column(DateTime)
    create_time = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    update_time = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))
