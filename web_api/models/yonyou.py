# coding: utf-8
from sqlalchemy import BINARY, BigInteger, Column, DateTime, Float, Index, Integer, LargeBinary, Numeric, SmallInteger, String, TIMESTAMP, Table, Text, Unicode, UnicodeText, text
from sqlalchemy.dialects.mssql.base import BIT, UNIQUEIDENTIFIER
from web_api.databases.yonyou import db


Base = db.Model
metadata = Base.metadata


def to_dict(self):
    return {c.name: getattr(self, c.name, None) for c in self.__table__.columns}

Base.to_dict = to_dict
Base.__bind_key__ = 'yonyou'


class AAAccount(Base):
    __tablename__ = 'AA_Account'

    code = Column(Unicode(40))
    name = Column(Unicode(50))
    accountingyear = Column(Integer)
    shorthand = Column(Unicode(50))
    isquantity = Column(Integer)
    unit = Column(Unicode(50))
    isexchange = Column(Integer)
    isgatherprinting = Column(Integer)
    canmakedoc = Column(Integer)
    iscontrolled = Column(Integer)
    iscontrolledbussinesssys = Column(Integer)
    iscontrolledcash = Column(Integer)
    iscash = Column(Integer)
    isbank = Column(Integer)
    iscashequivalents = Column(Integer)
    isauxaccdepartment = Column(Integer)
    isauxaccperson = Column(Integer)
    isauxacccustomer = Column(Integer)
    isauxaccsupplier = Column(Integer)
    isauxaccproject = Column(Integer)
    isauxaccinventory = Column(Integer)
    isexauxacc1 = Column(Integer)
    isexauxacc2 = Column(Integer)
    isexauxacc3 = Column(Integer)
    isexauxacc4 = Column(Integer)
    isexauxacc5 = Column(Integer)
    isexauxacc6 = Column(Integer)
    isexauxacc7 = Column(Integer)
    isexauxacc8 = Column(Integer)
    isexauxacc9 = Column(Integer)
    isexauxacc10 = Column(Integer)
    isEndNode = Column(Integer)
    disabled = Column(Integer)
    depth = Column(Integer)
    inId = Column(Unicode(750))
    createdtime = Column(String(19, u'Chinese_PRC_CI_AS'))
    sequencenumber = Column(Integer)
    ts = Column(TIMESTAMP, nullable=False)
    updated = Column(String(19, u'Chinese_PRC_CI_AS'))
    updatedBy = Column(Unicode(32))
    IsAux = Column(Integer, nullable=False, server_default=text("((0))"))
    isFinalTransferExchange = Column(Integer)
    isBillingInfo = Column(Integer)
    Remainder = Column(Numeric(32, 15))
    ModifyLog = Column(Unicode(4000))
    id = Column(Integer, primary_key=True)
    idGatherPrintingAccountDTO = Column(Integer)
    idParent = Column(Integer)
    idaccounttypeDTO = Column(Integer)
    iddefaultcurrencyDTO = Column(Integer)
    bookformat = Column(Integer)
    dcdirection = Column(Integer)


class AAAccountAssociation(Base):
    __tablename__ = 'AA_AccountAssociation'

    code = Column(Unicode(30))
    name = Column(Unicode(200))
    currentaccountingyear = Column(Integer)
    createdtime = Column(String(19, u'Chinese_PRC_CI_AS'))
    sequencenumber = Column(Integer)
    ts = Column(TIMESTAMP, nullable=False)
    updated = Column(String(19, u'Chinese_PRC_CI_AS'))
    updatedBy = Column(Unicode(32))
    preaccountingyear = Column(Integer)
    idcurrentaccountDTO = Column(Integer)
    idpreaccountDTO = Column(Integer)
    id = Column(Integer, primary_key=True)


class AAAccountType(Base):
    __tablename__ = 'AA_AccountType'

    code = Column(Unicode(40))
    name = Column(Unicode(200))
    num = Column(Integer)
    trialbalancedirection = Column(Integer)
    firstnumber = Column(Integer)
    trialbalance = Column(Integer)
    accountClass = Column(Integer)
    createdtime = Column(String(19, u'Chinese_PRC_CI_AS'))
    sequencenumber = Column(Integer)
    ts = Column(TIMESTAMP, nullable=False)
    updated = Column(String(19, u'Chinese_PRC_CI_AS'))
    updatedBy = Column(Unicode(32))
    classcode = Column(Unicode(50))
    id = Column(Integer, primary_key=True)
    defaultdcdirection = Column(Integer)


t_AA_Account_Ext = Table(
    'AA_Account_Ext', metadata,
    Column('accountcode_lev1', Unicode(40)),
    Column('accountname_lev1', Unicode(200)),
    Column('accountcode_lev2', Unicode(40)),
    Column('accountname_lev2', Unicode(200)),
    Column('accountcode_lev3', Unicode(40)),
    Column('accountname_lev3', Unicode(200)),
    Column('accountcode_lev4', Unicode(40)),
    Column('accountname_lev4', Unicode(200)),
    Column('accountcode_lev5', Unicode(40)),
    Column('accountname_lev5', Unicode(200)),
    Column('accountcode_lev6', Unicode(40)),
    Column('accountname_lev6', Unicode(200)),
    Column('accountcode_lev7', Unicode(40)),
    Column('accountname_lev7', Unicode(200)),
    Column('accountcode_lev8', Unicode(40)),
    Column('accountname_lev8', Unicode(200)),
    Column('accountcode_lev9', Unicode(40)),
    Column('accountname_lev9', Unicode(200)),
    Column('accountcode_lev10', Unicode(40)),
    Column('accountname_lev10', Unicode(200)),
    Column('accountcode_lev11', Unicode(40)),
    Column('accountname_lev11', Unicode(200)),
    Column('accountcode_lev12', Unicode(40)),
    Column('accountname_lev12', Unicode(200)),
    Column('accountcode_lev13', Unicode(40)),
    Column('accountname_lev13', Unicode(200)),
    Column('accountcode_lev14', Unicode(40)),
    Column('accountname_lev14', Unicode(200)),
    Column('accountcode_lev15', Unicode(40)),
    Column('accountname_lev15', Unicode(200)),
    Column('depth', Unicode(10)),
    Column('createTime', String(19, u'Chinese_PRC_CI_AS')),
    Column('ts', TIMESTAMP),
    Column('accountid_lev1', Integer),
    Column('accountid_lev10', Integer),
    Column('accountid_lev11', Integer),
    Column('accountid_lev12', Integer),
    Column('accountid_lev13', Integer),
    Column('accountid_lev14', Integer),
    Column('accountid_lev15', Integer),
    Column('accountid_lev2', Integer),
    Column('accountid_lev3', Integer),
    Column('accountid_lev4', Integer),
    Column('accountid_lev5', Integer),
    Column('accountid_lev6', Integer),
    Column('accountid_lev7', Integer),
    Column('accountid_lev8', Integer),
    Column('accountid_lev9', Integer),
    Column('id', Integer)
)


class AAAssetClass(Base):
    __tablename__ = 'AA_AssetClass'

    code = Column(Unicode(30))
    name = Column(Unicode(400))
    depth = Column(Integer)
    inid = Column(Unicode(750))
    isendnode = Column(Integer)
    ispreset = Column(Integer)
    isdisPlay = Column(Integer)
    imageFile = Column(Unicode(500))
    defaultyears = Column(Integer)
    defaultmonths = Column(Integer)
    defaultnrvrate = Column(Numeric(9, 6))
    defaultoffsetinputtax = Column(Integer)
    defaultinputtaxrate = Column(Numeric(5, 2))
    ts = Column(TIMESTAMP, nullable=False)
    updated = Column(String(19, u'Chinese_PRC_CI_AS'))
    updatedBy = Column(Unicode(32))
    createdTime = Column(String(19, u'Chinese_PRC_CI_AS'))
    UsedYearAndMonth = Column(Unicode(200))
    id = Column(Integer, primary_key=True)
    idparent = Column(Integer)
    idassetprop = Column(Integer)
    iddeprmethod = Column(Integer)
    idBarCode = Column(Integer)
    idunit = Column(Integer)
    idLabelStyle = Column(Integer)
    idCardStyle = Column(Integer)


t_AA_AssetClass_Ext = Table(
    'AA_AssetClass_Ext', metadata,
    Column('assetClasscode_lev1', Unicode(40)),
    Column('assetClassname_lev1', Unicode(400)),
    Column('assetClasscode_lev2', Unicode(40)),
    Column('assetClassname_lev2', Unicode(400)),
    Column('assetClasscode_lev3', Unicode(40)),
    Column('assetClassname_lev3', Unicode(400)),
    Column('assetClasscode_lev4', Unicode(40)),
    Column('assetClassname_lev4', Unicode(400)),
    Column('assetClasscode_lev5', Unicode(40)),
    Column('assetClassname_lev5', Unicode(400)),
    Column('assetClasscode_lev6', Unicode(40)),
    Column('assetClassname_lev6', Unicode(400)),
    Column('assetClasscode_lev7', Unicode(40)),
    Column('assetClassname_lev7', Unicode(400)),
    Column('assetClasscode_lev8', Unicode(40)),
    Column('assetClassname_lev8', Unicode(400)),
    Column('assetClasscode_lev9', Unicode(40)),
    Column('assetClassname_lev9', Unicode(400)),
    Column('assetClasscode_lev10', Unicode(40)),
    Column('assetClassname_lev10', Unicode(400)),
    Column('assetClasscode_lev11', Unicode(40)),
    Column('assetClassname_lev11', Unicode(400)),
    Column('assetClasscode_lev12', Unicode(40)),
    Column('assetClassname_lev12', Unicode(400)),
    Column('assetClasscode_lev13', Unicode(40)),
    Column('assetClassname_lev13', Unicode(400)),
    Column('assetClasscode_lev14', Unicode(40)),
    Column('assetClassname_lev14', Unicode(400)),
    Column('assetClasscode_lev15', Unicode(40)),
    Column('assetClassname_lev15', Unicode(400)),
    Column('depth', Unicode(10)),
    Column('createTime', String(19, u'Chinese_PRC_CI_AS')),
    Column('ts', TIMESTAMP),
    Column('id', Integer),
    Column('assetClassid_lev1', Integer),
    Column('assetClassid_lev10', Integer),
    Column('assetClassid_lev11', Integer),
    Column('assetClassid_lev12', Integer),
    Column('assetClassid_lev13', Integer),
    Column('assetClassid_lev14', Integer),
    Column('assetClassid_lev15', Integer),
    Column('assetClassid_lev2', Integer),
    Column('assetClassid_lev3', Integer),
    Column('assetClassid_lev4', Integer),
    Column('assetClassid_lev5', Integer),
    Column('assetClassid_lev6', Integer),
    Column('assetClassid_lev7', Integer),
    Column('assetClassid_lev8', Integer),
    Column('assetClassid_lev9', Integer)
)


class AAAssetProp(Base):
    __tablename__ = 'AA_AssetProp'

    code = Column(Unicode(30))
    name = Column(Unicode(100))
    isdepr = Column(Integer)
    ispreset = Column(Integer)
    sequenceNumber = Column(Integer)
    ts = Column(TIMESTAMP, nullable=False)
    updated = Column(String(19, u'Chinese_PRC_CI_AS'))
    updatedBy = Column(Unicode(32))
    createdTime = Column(String(19, u'Chinese_PRC_CI_AS'))
    id = Column(Integer, primary_key=True)
    provisionway = Column(Integer)


t_AA_BOM = Table(
    'AA_BOM', metadata,
    Column('code', Unicode(32)),
    Column('name', Unicode(200)),
    Column('version', Unicode(30)),
    Column('produceQuantity', Numeric(28, 14)),
    Column('rationWage', Numeric(28, 14)),
    Column('rationCharge', Numeric(28, 14)),
    Column('rationManHour', Numeric(28, 14)),
    Column('isDefaultBom', Integer),
    Column('bomDepth', Integer),
    Column('disabled', Integer),
    Column('ts', TIMESTAMP),
    Column('updatedBy', Unicode(32)),
    Column('freeItem0', Unicode(300)),
    Column('freeItem1', Unicode(300)),
    Column('freeItem2', Unicode(300)),
    Column('freeItem3', Unicode(300)),
    Column('freeItem4', Unicode(300)),
    Column('freeItem5', Unicode(300)),
    Column('freeItem6', Unicode(300)),
    Column('freeItem7', Unicode(300)),
    Column('freeItem8', Unicode(300)),
    Column('freeItem9', Unicode(300)),
    Column('priuserdefnvc1', Unicode(500)),
    Column('priuserdefdecm1', Numeric(28, 14)),
    Column('priuserdefnvc2', Unicode(500)),
    Column('priuserdefdecm2', Numeric(28, 14)),
    Column('priuserdefnvc3', Unicode(500)),
    Column('priuserdefdecm3', Numeric(28, 14)),
    Column('priuserdefnvc4', Unicode(500)),
    Column('priuserdefdecm4', Numeric(28, 14)),
    Column('priuserdefnvc5', Unicode(500)),
    Column('priuserdefdecm5', Numeric(28, 14)),
    Column('producequantity2', Numeric(28, 14)),
    Column('rationcost', Numeric(28, 14)),
    Column('rationmaterial', Numeric(28, 14)),
    Column('cost', Numeric(28, 14)),
    Column('rateofexchange', Numeric(28, 14)),
    Column('yieldrate', Numeric(28, 14)),
    Column('iscostbom', Integer),
    Column('idsaleorder', Unicode(50)),
    Column('maker', Unicode(50)),
    Column('auditor', Unicode(50)),
    Column('reviser', Unicode(50)),
    Column('isorderbom', Integer),
    Column('customerName', Unicode(200)),
    Column('customerCode', Unicode(200)),
    Column('customerForShort', Unicode(200)),
    Column('pubuserdefnvc1', Unicode(500)),
    Column('pubuserdefnvc2', Unicode(500)),
    Column('pubuserdefnvc3', Unicode(500)),
    Column('pubuserdefnvc4', Unicode(500)),
    Column('pubuserdefnvc5', Unicode(500)),
    Column('pubuserdefnvc6', Unicode(500)),
    Column('pubuserdefdecm1', Numeric(28, 14)),
    Column('pubuserdefdecm2', Numeric(28, 14)),
    Column('pubuserdefdecm3', Numeric(28, 14)),
    Column('pubuserdefdecm4', Numeric(28, 14)),
    Column('pubuserdefdecm5', Numeric(28, 14)),
    Column('pubuserdefdecm6', Numeric(28, 14)),
    Column('priuserdefdecm6', Numeric(28, 14)),
    Column('priuserdefnvc6', Unicode(500)),
    Column('id', Integer, nullable=False),
    Column('idBomRelationDTO', Integer),
    Column('idmanufactureplant', Integer),
    Column('idinventory', Integer),
    Column('idmechiner', Integer),
    Column('idrouting', Integer),
    Column('idunit', Integer),
    Column('idunit2', Integer),
    Column('idwarehouse', Integer),
    Column('getbomchildunitmethod', Integer),
    Column('produceType', Integer),
    Column('voucherstate', Integer),
    Column('auditorid', Integer),
    Column('makerid', Integer),
    Column('madeDate', DateTime),
    Column('updated', DateTime),
    Column('voucherdate', DateTime),
    Column('auditeddate', DateTime),
    Column('createdtime', DateTime),
    Column('reviserid', Integer, server_default=text("(NULL)")),
    Column('ReviserDate', DateTime, server_default=text("(NULL)"))
)


t_AA_BOMChild = Table(
    'AA_BOMChild', metadata,
    Column('code', Unicode(32)),
    Column('name', Unicode(200)),
    Column('produceQuantity', Numeric(28, 14)),
    Column('rationQuantity', Numeric(28, 14)),
    Column('wasteRate', Numeric(28, 14)),
    Column('ts', TIMESTAMP),
    Column('updatedBy', Unicode(32)),
    Column('freeItem0', Unicode(300)),
    Column('freeItem1', Unicode(300)),
    Column('freeItem2', Unicode(300)),
    Column('freeItem3', Unicode(300)),
    Column('freeItem4', Unicode(300)),
    Column('freeItem5', Unicode(300)),
    Column('freeItem6', Unicode(300)),
    Column('freeItem7', Unicode(300)),
    Column('freeItem8', Unicode(300)),
    Column('freeItem9', Unicode(300)),
    Column('memo', Unicode(200)),
    Column('requiredquantity', Numeric(28, 14)),
    Column('requiredquantity2', Numeric(28, 14)),
    Column('rateofexchange', Numeric(28, 14)),
    Column('unitprice', Numeric(28, 14)),
    Column('cost', Numeric(28, 14)),
    Column('backflushmaterial', Integer),
    Column('defaultchoice', Integer),
    Column('priuserdefnvc1', Unicode(500)),
    Column('priuserdefnvc2', Unicode(500)),
    Column('priuserdefnvc3', Unicode(500)),
    Column('priuserdefnvc4', Unicode(500)),
    Column('priuserdefdecm1', Numeric(28, 14)),
    Column('priuserdefdecm2', Numeric(28, 14)),
    Column('priuserdefdecm3', Numeric(28, 14)),
    Column('priuserdefdecm4', Numeric(28, 14)),
    Column('pubuserdefnvc1', Unicode(500)),
    Column('pubuserdefnvc2', Unicode(500)),
    Column('pubuserdefnvc3', Unicode(500)),
    Column('pubuserdefnvc4', Unicode(500)),
    Column('pubuserdefdecm1', Numeric(28, 14)),
    Column('pubuserdefdecm2', Numeric(28, 14)),
    Column('pubuserdefdecm3', Numeric(28, 14)),
    Column('pubuserdefdecm4', Numeric(28, 14)),
    Column('BatchNumber', Unicode(100)),
    Column('FailDate', DateTime),
    Column('id', Integer, nullable=False),
    Column('idchildbom', Integer),
    Column('idbom', Integer),
    Column('idBomRelationDTO', Integer),
    Column('idinventory', Integer),
    Column('idproductprocess', Integer),
    Column('idunit', Integer),
    Column('idunit2', Integer),
    Column('idwarehouse', Integer),
    Column('bomchildattribute', Integer),
    Column('madeDate', DateTime),
    Column('updated', DateTime),
    Column('createdtime', DateTime)
)


t_AA_BankAccount = Table(
    'AA_BankAccount', metadata,
    Column('code', Unicode(50)),
    Column('name', Unicode(200)),
    Column('bankNo', Unicode(50)),
    Column('disabled', Integer),
    Column('ts', TIMESTAMP),
    Column('updatedBy', Unicode(32)),
    Column('isusingdeficitcontrol', Integer),
    Column('isusingbankcheck', Integer),
    Column('NewBalance', Numeric(38, 6)),
    Column('VirtualPay', Integer),
    Column('id', Integer, nullable=False),
    Column('idcurrency', Integer),
    Column('iddepartment', Integer),
    Column('idMarketingOrgan', Integer),
    Column('balancedirection', Integer),
    Column('bankName', Integer),
    Column('bankNoType', Integer),
    Column('madeDate', DateTime),
    Column('updated', DateTime),
    Column('dateofusingbankcheck', DateTime),
    Column('createdTime', DateTime)
)


t_AA_BarCodeInformation = Table(
    'AA_BarCodeInformation', metadata,
    Column('ts', TIMESTAMP, nullable=False),
    Column('updatedBy', Unicode(32)),
    Column('Code', Unicode(30)),
    Column('Name', Unicode(50)),
    Column('disabled', Integer),
    Column('fieldName', Unicode(60)),
    Column('formatCode', Unicode(60)),
    Column('VfieldName', Unicode(100)),
    Column('fieldType', Unicode(50)),
    Column('ControlType', Unicode(60)),
    Column('RefDTOName', Unicode(50)),
    Column('RefDataSource', Unicode(50)),
    Column('EnumName', Unicode(50)),
    Column('RefShowField', Unicode(50)),
    Column('id', Integer, nullable=False),
    Column('idInformationClass', Integer),
    Column('updated', DateTime),
    Column('madeDate', DateTime)
)


t_AA_BarCodeInformationClass = Table(
    'AA_BarCodeInformationClass', metadata,
    Column('ts', TIMESTAMP, nullable=False),
    Column('updatedBy', Unicode(32)),
    Column('Code', Unicode(30)),
    Column('Name', Unicode(50)),
    Column('InId', Unicode(560)),
    Column('IsEndNode', Integer),
    Column('disabled', Integer),
    Column('id', Integer, nullable=False),
    Column('idParent', Integer),
    Column('updated', DateTime),
    Column('madeDate', DateTime)
)


t_AA_BarCodeSectionInfo = Table(
    'AA_BarCodeSectionInfo', metadata,
    Column('code', Unicode(32)),
    Column('name', Unicode(200)),
    Column('length', Integer),
    Column('ts', TIMESTAMP, nullable=False),
    Column('updatedBy', Unicode(32)),
    Column('idsectionInfo', Integer),
    Column('id', Integer, nullable=False),
    Column('idBarCodeSolution', Integer),
    Column('fillType', Integer),
    Column('format', Integer),
    Column('madeDate', DateTime),
    Column('updated', DateTime),
    Column('createdTime', DateTime)
)


t_AA_BarCodeSolution = Table(
    'AA_BarCodeSolution', metadata,
    Column('ts', TIMESTAMP, nullable=False),
    Column('updatedBy', Unicode(32)),
    Column('code', Unicode(6)),
    Column('name', Unicode(50)),
    Column('length', Integer),
    Column('memo', Unicode(560)),
    Column('id', Integer, nullable=False),
    Column('BarCodeType', Integer),
    Column('codingType', Integer),
    Column('isLenFixed', BIT, server_default=text("((1))")),
    Column('lengthFixed', String(10, u'Chinese_PRC_CI_AS')),
    Column('updated', DateTime),
    Column('madeDate', DateTime),
    Column('createdTime', DateTime)
)


t_AA_BarCodeTermAnalysisInfo = Table(
    'AA_BarCodeTermAnalysisInfo', metadata,
    Column('code', Unicode(32)),
    Column('name', Unicode(200)),
    Column('updatedBy', Unicode(32)),
    Column('ts', TIMESTAMP, nullable=False),
    Column('Information1', Integer),
    Column('Information2', Integer),
    Column('Information3', Integer),
    Column('Information4', Integer),
    Column('Information5', Integer),
    Column('Information6', Integer),
    Column('Information7', Integer),
    Column('Information8', Integer),
    Column('Information9', Integer),
    Column('Information10', Integer),
    Column('Information11', Integer),
    Column('Information12', Integer),
    Column('Information13', Integer),
    Column('Information14', Integer),
    Column('Information15', Integer),
    Column('Information16', Integer),
    Column('Information17', Integer),
    Column('Information18', Integer),
    Column('Information19', Integer),
    Column('Information20', Integer),
    Column('Information21', Integer),
    Column('Information22', Integer),
    Column('Information23', Integer),
    Column('Information24', Integer),
    Column('Information25', Integer),
    Column('Information26', Integer),
    Column('Information27', Integer),
    Column('Information28', Integer),
    Column('Information29', Integer),
    Column('Information30', Integer),
    Column('Information31', Integer),
    Column('Information32', Integer),
    Column('Information33', Integer),
    Column('Information34', Integer),
    Column('Information35', Integer),
    Column('Information36', Integer),
    Column('Information37', Integer),
    Column('Information38', Integer),
    Column('Information39', Integer),
    Column('Information40', Integer),
    Column('Information41', Integer),
    Column('Information42', Integer),
    Column('Information43', Integer),
    Column('Information44', Integer),
    Column('Information45', Integer),
    Column('Information46', Integer),
    Column('Information47', Integer),
    Column('Information48', Integer),
    Column('Information49', Integer),
    Column('Information50', Integer),
    Column('Information51', Integer),
    Column('Information52', Integer),
    Column('Information53', Integer),
    Column('Information54', Integer),
    Column('Information55', Integer),
    Column('Information56', Integer),
    Column('Information57', Integer),
    Column('Information58', Integer),
    Column('Information59', Integer),
    Column('Information60', Integer),
    Column('Information61', Integer),
    Column('Information62', Integer),
    Column('Information63', Integer),
    Column('Information64', Integer),
    Column('Information65', Integer),
    Column('Information66', Integer),
    Column('Information67', Integer),
    Column('Information68', Integer),
    Column('Information69', Integer),
    Column('Information70', Integer),
    Column('Information71', Integer),
    Column('Information72', Integer),
    Column('Information73', Integer),
    Column('Information74', Integer),
    Column('Information75', Integer),
    Column('Information76', Integer),
    Column('Information77', Integer),
    Column('Information78', Integer),
    Column('Information79', Integer),
    Column('Information80', Integer),
    Column('Information81', Integer),
    Column('Information82', Integer),
    Column('Information83', Integer),
    Column('Information84', Integer),
    Column('Information85', Integer),
    Column('Information86', Integer),
    Column('Information87', Integer),
    Column('Information88', Integer),
    Column('Information89', Integer),
    Column('Information90', Integer),
    Column('Information91', Integer),
    Column('Information92', Integer),
    Column('Information93', Integer),
    Column('Information94', Integer),
    Column('Information95', Integer),
    Column('Information96', Integer),
    Column('Information97', Integer),
    Column('Information98', Integer),
    Column('Information99', Integer),
    Column('Information100', Integer),
    Column('Information101', Integer),
    Column('Information102', Integer),
    Column('Information103', Integer),
    Column('Information104', Integer),
    Column('Information105', Integer),
    Column('Information106', Integer),
    Column('Information107', Integer),
    Column('BarCodeSolutionId', Integer),
    Column('id', Integer, nullable=False),
    Column('idVoucher', Integer),
    Column('updated', DateTime)
)


class AABizUsage(Base):
    __tablename__ = 'AA_BizUsage'

    code = Column(Unicode(30))
    name = Column(Unicode(100))
    disabled = Column(Integer)
    ispreset = Column(Integer)
    sequenceNumber = Column(Integer)
    ts = Column(TIMESTAMP, nullable=False)
    updated = Column(String(19, u'Chinese_PRC_CI_AS'))
    updatedBy = Column(Unicode(32))
    createdTime = Column(String(19, u'Chinese_PRC_CI_AS'))
    id = Column(Integer, primary_key=True)


t_AA_BomRelation = Table(
    'AA_BomRelation', metadata,
    Column('code', Unicode(30)),
    Column('name', Unicode(200)),
    Column('ts', TIMESTAMP, nullable=False),
    Column('updatedBy', Unicode(32)),
    Column('realLevel', Integer),
    Column('level', Integer),
    Column('isVirtual', Integer),
    Column('isEnd', Integer),
    Column('bomPath', Unicode(1000)),
    Column('id', Integer, nullable=False),
    Column('idBOM', Integer),
    Column('idParent', Integer),
    Column('idTop', Integer),
    Column('idChild', Integer),
    Column('idInventory', Integer),
    Column('idSku', Integer),
    Column('createdtime', DateTime),
    Column('updated', DateTime)
)


t_AA_BusiType = Table(
    'AA_BusiType', metadata,
    Column('code', Unicode(32)),
    Column('name', Unicode(200)),
    Column('disabled', Integer),
    Column('ts', TIMESTAMP),
    Column('updatedBy', Unicode(32)),
    Column('isSystem', Integer),
    Column('ExpressionName', Unicode(60)),
    Column('id', Integer, nullable=False),
    Column('idrdStyleIn', Integer),
    Column('idrdStyleOut', Integer),
    Column('businessVoucher', Integer),
    Column('madeDate', DateTime),
    Column('updated', DateTime),
    Column('createdTime', DateTime)
)


class AACashFlowItem(Base):
    __tablename__ = 'AA_CashFlowItem'

    code = Column(Unicode(30))
    name = Column(Unicode(50))
    disabled = Column(Integer)
    createdtime = Column(String(19, u'Chinese_PRC_CI_AS'))
    sequencenumber = Column(Integer)
    ts = Column(TIMESTAMP, nullable=False)
    updated = Column(String(19, u'Chinese_PRC_CI_AS'))
    updatedBy = Column(Unicode(32))
    id = Column(Integer, primary_key=True)
    idcashflowitemclass = Column(Integer)
    direction = Column(Integer)


class AACashFlowItemClass(Base):
    __tablename__ = 'AA_CashFlowItemClass'

    code = Column(Unicode(30))
    name = Column(Unicode(50))
    depth = Column(Integer)
    isendnode = Column(Integer)
    inid = Column(Unicode(1120))
    createdtime = Column(String(19, u'Chinese_PRC_CI_AS'))
    sequencenumber = Column(Integer)
    ts = Column(TIMESTAMP, nullable=False)
    updated = Column(String(19, u'Chinese_PRC_CI_AS'))
    updatedBy = Column(Unicode(32))
    disabled = Column(Integer, nullable=False, server_default=text("((0))"))
    id = Column(Integer, primary_key=True)
    idparent = Column(Integer)


t_AA_CashFlowItemClass_Ext = Table(
    'AA_CashFlowItemClass_Ext', metadata,
    Column('CashFlowItemClasscode_lev1', Unicode(32)),
    Column('CashFlowItemClassname_lev1', Unicode(200)),
    Column('CashFlowItemClasscode_lev2', Unicode(32)),
    Column('CashFlowItemClassname_lev2', Unicode(200)),
    Column('CashFlowItemClasscode_lev3', Unicode(32)),
    Column('CashFlowItemClassname_lev3', Unicode(200)),
    Column('CashFlowItemClasscode_lev4', Unicode(32)),
    Column('CashFlowItemClassname_lev4', Unicode(200)),
    Column('CashFlowItemClasscode_lev5', Unicode(32)),
    Column('CashFlowItemClassname_lev5', Unicode(200)),
    Column('CashFlowItemClasscode_lev6', Unicode(32)),
    Column('CashFlowItemClassname_lev6', Unicode(200)),
    Column('CashFlowItemClasscode_lev7', Unicode(32)),
    Column('CashFlowItemClassname_lev7', Unicode(200)),
    Column('CashFlowItemClasscode_lev8', Unicode(32)),
    Column('CashFlowItemClassname_lev8', Unicode(200)),
    Column('CashFlowItemClasscode_lev9', Unicode(32)),
    Column('CashFlowItemClassname_lev9', Unicode(200)),
    Column('CashFlowItemClasscode_lev10', Unicode(32)),
    Column('CashFlowItemClassname_lev10', Unicode(200)),
    Column('CashFlowItemClasscode_lev11', Unicode(32)),
    Column('CashFlowItemClassname_lev11', Unicode(200)),
    Column('CashFlowItemClasscode_lev12', Unicode(32)),
    Column('CashFlowItemClassname_lev12', Unicode(200)),
    Column('CashFlowItemClasscode_lev13', Unicode(32)),
    Column('CashFlowItemClassname_lev13', Unicode(200)),
    Column('CashFlowItemClasscode_lev14', Unicode(32)),
    Column('CashFlowItemClassname_lev14', Unicode(200)),
    Column('CashFlowItemClasscode_lev15', Unicode(32)),
    Column('CashFlowItemClassname_lev15', Unicode(200)),
    Column('depth', Unicode(10)),
    Column('createTime', String(19, u'Chinese_PRC_CI_AS')),
    Column('ts', TIMESTAMP),
    Column('CashFlowItemClassid_lev1', Integer),
    Column('CashFlowItemClassid_lev10', Integer),
    Column('CashFlowItemClassid_lev11', Integer),
    Column('CashFlowItemClassid_lev12', Integer),
    Column('CashFlowItemClassid_lev13', Integer),
    Column('CashFlowItemClassid_lev14', Integer),
    Column('CashFlowItemClassid_lev15', Integer),
    Column('CashFlowItemClassid_lev2', Integer),
    Column('CashFlowItemClassid_lev3', Integer),
    Column('CashFlowItemClassid_lev4', Integer),
    Column('CashFlowItemClassid_lev5', Integer),
    Column('CashFlowItemClassid_lev6', Integer),
    Column('CashFlowItemClassid_lev7', Integer),
    Column('CashFlowItemClassid_lev8', Integer),
    Column('CashFlowItemClassid_lev9', Integer),
    Column('id', Integer)
)


class AACashItemAccountDetail(Base):
    __tablename__ = 'AA_CashItemAccountDetail'

    code = Column(Unicode(30))
    name = Column(Unicode(200))
    accountcode = Column(Unicode(50))
    createdtime = Column(String(19, u'Chinese_PRC_CI_AS'))
    sequencenumber = Column(Integer)
    ts = Column(TIMESTAMP, nullable=False)
    updated = Column(String(19, u'Chinese_PRC_CI_AS'))
    updatedBy = Column(Unicode(32))
    accountType = Column(Integer)
    idaccount = Column(Integer)
    idCashFlowItemDTO = Column(Integer)
    id = Column(Integer, primary_key=True)


class AACommonSummary(Base):
    __tablename__ = 'AA_CommonSummary'

    code = Column(Unicode(30))
    name = Column(Unicode(100))
    shorthand = Column(Unicode(100))
    createdtime = Column(String(19, u'Chinese_PRC_CI_AS'))
    sequencenumber = Column(Integer)
    ts = Column(TIMESTAMP, nullable=False)
    updated = Column(String(19, u'Chinese_PRC_CI_AS'))
    updatedBy = Column(Unicode(32))
    disabled = Column(Integer, nullable=False, server_default=text("((0))"))
    id = Column(Integer, primary_key=True)
    idcommonsummaryclass = Column(Integer)


class AACommonSummaryClass(Base):
    __tablename__ = 'AA_CommonSummaryClass'

    code = Column(Unicode(30))
    name = Column(Unicode(50))
    depth = Column(Integer)
    isendnode = Column(Integer)
    inid = Column(Unicode(1120))
    createdtime = Column(String(19, u'Chinese_PRC_CI_AS'))
    sequencenumber = Column(Integer)
    ts = Column(TIMESTAMP, nullable=False)
    updated = Column(String(19, u'Chinese_PRC_CI_AS'))
    updatedBy = Column(Unicode(32))
    disabled = Column(Integer, nullable=False, server_default=text("((0))"))
    id = Column(Integer, primary_key=True)
    idparent = Column(Integer)


t_AA_CommonSummaryClass_Ext = Table(
    'AA_CommonSummaryClass_Ext', metadata,
    Column('CommonSummaryClasscode_lev1', Unicode(32)),
    Column('CommonSummaryClassname_lev1', Unicode(200)),
    Column('CommonSummaryClasscode_lev2', Unicode(32)),
    Column('CommonSummaryClassname_lev2', Unicode(200)),
    Column('CommonSummaryClasscode_lev3', Unicode(32)),
    Column('CommonSummaryClassname_lev3', Unicode(200)),
    Column('CommonSummaryClasscode_lev4', Unicode(32)),
    Column('CommonSummaryClassname_lev4', Unicode(200)),
    Column('CommonSummaryClasscode_lev5', Unicode(32)),
    Column('CommonSummaryClassname_lev5', Unicode(200)),
    Column('CommonSummaryClasscode_lev6', Unicode(32)),
    Column('CommonSummaryClassname_lev6', Unicode(200)),
    Column('CommonSummaryClasscode_lev7', Unicode(32)),
    Column('CommonSummaryClassname_lev7', Unicode(200)),
    Column('CommonSummaryClasscode_lev8', Unicode(32)),
    Column('CommonSummaryClassname_lev8', Unicode(200)),
    Column('CommonSummaryClasscode_lev9', Unicode(32)),
    Column('CommonSummaryClassname_lev9', Unicode(200)),
    Column('CommonSummaryClasscode_lev10', Unicode(32)),
    Column('CommonSummaryClassname_lev10', Unicode(200)),
    Column('CommonSummaryClasscode_lev11', Unicode(32)),
    Column('CommonSummaryClassname_lev11', Unicode(200)),
    Column('CommonSummaryClasscode_lev12', Unicode(32)),
    Column('CommonSummaryClassname_lev12', Unicode(200)),
    Column('CommonSummaryClasscode_lev13', Unicode(32)),
    Column('CommonSummaryClassname_lev13', Unicode(200)),
    Column('CommonSummaryClasscode_lev14', Unicode(32)),
    Column('CommonSummaryClassname_lev14', Unicode(200)),
    Column('CommonSummaryClasscode_lev15', Unicode(32)),
    Column('CommonSummaryClassname_lev15', Unicode(200)),
    Column('depth', Unicode(10)),
    Column('createTime', String(19, u'Chinese_PRC_CI_AS')),
    Column('ts', TIMESTAMP),
    Column('CommonSummaryClassid_lev1', Integer),
    Column('CommonSummaryClassid_lev10', Integer),
    Column('CommonSummaryClassid_lev11', Integer),
    Column('CommonSummaryClassid_lev12', Integer),
    Column('CommonSummaryClassid_lev13', Integer),
    Column('CommonSummaryClassid_lev14', Integer),
    Column('CommonSummaryClassid_lev15', Integer),
    Column('CommonSummaryClassid_lev2', Integer),
    Column('CommonSummaryClassid_lev3', Integer),
    Column('CommonSummaryClassid_lev4', Integer),
    Column('CommonSummaryClassid_lev5', Integer),
    Column('CommonSummaryClassid_lev6', Integer),
    Column('CommonSummaryClassid_lev7', Integer),
    Column('CommonSummaryClassid_lev8', Integer),
    Column('CommonSummaryClassid_lev9', Integer),
    Column('id', Integer)
)


t_AA_Currency = Table(
    'AA_Currency', metadata,
    Column('code', Unicode(32)),
    Column('name', Unicode(200)),
    Column('currencySign', Unicode(10)),
    Column('isNative', Integer),
    Column('maxError', Numeric(28, 14)),
    Column('exchangeRate', Numeric(28, 14)),
    Column('disabled', Integer),
    Column('ts', TIMESTAMP),
    Column('updatedBy', Unicode(32)),
    Column('id', Integer, nullable=False),
    Column('calDirection', Integer),
    Column('madeDate', DateTime),
    Column('updated', DateTime),
    Column('createdTime', DateTime),
    Column('ExChangeRateType', Integer),
    Column('AccountDate', Integer),
    Column('AccountYear', Integer)
)


class AACustomerInventoryPrice(Base):
    __tablename__ = 'AA_CustomerInventoryPrice'

    code = Column(Unicode(32))
    name = Column(Unicode(200))
    agreementPrice = Column(Unicode(1000))
    lowestPrice = Column(Unicode(1000))
    ts = Column(TIMESTAMP)
    updatedBy = Column(Unicode(32))
    agreementDiscount = Column(Numeric(28, 14))
    transactionPrice = Column(Unicode(1000))
    lowestPriceFormula = Column(Unicode(1000))
    increasePriceRate = Column(Numeric(28, 14))
    PriceKey = Column(Unicode(34))
    AgreementPriceFormula = Column(Unicode(1000))
    TransactionPriceFormula = Column(Unicode(1000))
    SearchFlag = Column(Integer)
    InvBarCode = Column(Unicode(128))
    id = Column(Integer, primary_key=True)
    idpricetrace = Column(Integer)
    idinventory = Column(Integer)
    idinventoryprice = Column(Integer)
    idcustomer = Column(Integer)
    idunit = Column(Integer)
    createdtime = Column(DateTime)
    updated = Column(DateTime)


t_AA_CustomerInventoryPriceTrace = Table(
    'AA_CustomerInventoryPriceTrace', metadata,
    Column('code', Unicode(32)),
    Column('name', Unicode(200)),
    Column('lastPrice', Numeric(32, 15)),
    Column('discount', Numeric(32, 15)),
    Column('unitprice', Numeric(32, 15)),
    Column('unittaxprice', Numeric(32, 15)),
    Column('ts', TIMESTAMP),
    Column('updatedBy', Unicode(32)),
    Column('id', Integer, nullable=False),
    Column('idinventory', Integer, nullable=False, server_default=text("((0))")),
    Column('idcustomer', Integer, nullable=False, server_default=text("((0))")),
    Column('idunit', Integer, nullable=False, server_default=text("((0))")),
    Column('createdtime', DateTime),
    Column('updated', DateTime)
)


class AADRMember(Base):
    __tablename__ = 'AA_DR_Member'

    code = Column(Unicode(30))
    name = Column(Unicode(200))
    cardcode = Column(Unicode(50))
    password = Column(Unicode(50))
    cardprintdate = Column(String(19, u'Chinese_PRC_CI_AS'))
    effectivedate = Column(String(19, u'Chinese_PRC_CI_AS'))
    expirationdate = Column(String(19, u'Chinese_PRC_CI_AS'))
    memo = Column(Unicode(200))
    post = Column(Unicode(50))
    occupation = Column(Unicode(50))
    birthdate = Column(String(19, u'Chinese_PRC_CI_AS'))
    identificationcode = Column(Unicode(50))
    telephone = Column(Unicode(50))
    email = Column(Unicode(100))
    qq = Column(Unicode(50))
    msn = Column(Unicode(50))
    mobilephone = Column(Unicode(50))
    address = Column(Unicode(50))
    zipcode = Column(Unicode(50))
    picture = Column(Unicode(50))
    openintegral = Column(Numeric(28, 14))
    totalintegral = Column(Numeric(28, 14))
    balanceintegral = Column(Numeric(28, 14))
    openamount = Column(Numeric(28, 14))
    totalamount = Column(Numeric(28, 14))
    openconsumtimes = Column(Numeric(28, 14))
    totalconsumtimes = Column(Numeric(28, 14))
    lastconsumdate = Column(String(19, u'Chinese_PRC_CI_AS'))
    createdtime = Column(String(19, u'Chinese_PRC_CI_AS'))
    sequencenumber = Column(Integer)
    ts = Column(TIMESTAMP, nullable=False)
    updated = Column(String(19, u'Chinese_PRC_CI_AS'))
    updatedBy = Column(Unicode(32))
    priuserdefnvc1 = Column(Unicode(500))
    priuserdefdecm1 = Column(Numeric(28, 14))
    priuserdefnvc2 = Column(Unicode(500))
    priuserdefdecm2 = Column(Numeric(28, 14))
    priuserdefnvc3 = Column(Unicode(500))
    priuserdefdecm3 = Column(Numeric(28, 14))
    priuserdefnvc4 = Column(Unicode(500))
    priuserdefdecm4 = Column(Numeric(28, 14))
    priuserdefnvc5 = Column(Unicode(500))
    priuserdefdecm5 = Column(Numeric(28, 14))
    imagefile = Column(Unicode(50))
    openstorage = Column(Numeric(28, 14))
    balancestorage = Column(String(8000, u'Chinese_PRC_CI_AS'))
    logoutbalancestorage = Column(Numeric(28, 14))
    balanceinteforstorage = Column(Numeric(28, 14))
    totalstorage = Column(Numeric(28, 14))
    balancetotalstorage = Column(Numeric(28, 14))
    storagetimes = Column(Numeric(28, 14))
    isautopartner = Column(Integer)
    iswritedcard = Column(Integer)
    Shorthand = Column(Unicode(200))
    iddistrict = Column(Integer)
    id = Column(Integer, primary_key=True)
    idmembertype = Column(Integer)
    idpartner = Column(Integer)
    idperson = Column(Integer)
    idstore = Column(Integer)
    idpartnerClass = Column(Integer)
    IdentificationType = Column(Integer)
    memberstate = Column(Integer)
    nation = Column(Integer)
    Sex = Column(Integer)
    idsourcevouchertype = Column(Integer)


t_AA_DR_MemberBatchAdd = Table(
    'AA_DR_MemberBatchAdd', metadata,
    Column('code', Unicode(30)),
    Column('name', Unicode(200)),
    Column('priuserdefnvc1', Unicode(100)),
    Column('priuserdefdecm1', Numeric(28, 14)),
    Column('priuserdefnvc2', Unicode(100)),
    Column('priuserdefdecm2', Numeric(28, 14)),
    Column('priuserdefnvc3', Unicode(100)),
    Column('priuserdefdecm3', Numeric(28, 14)),
    Column('priuserdefnvc4', Unicode(100)),
    Column('priuserdefdecm4', Numeric(28, 14)),
    Column('priuserdefnvc5', Unicode(100)),
    Column('priuserdefdecm5', Numeric(28, 14)),
    Column('id', Integer, nullable=False, server_default=text("((0))")),
    Column('idperson', Integer),
    Column('idstore', Integer),
    Column('iddistrict', Integer),
    Column('idmembertype', Integer, nullable=False, server_default=text("((0))"))
)


class AADRMemberChangeCard(Base):
    __tablename__ = 'AA_DR_MemberChangeCard'

    code = Column(Unicode(30))
    name = Column(Unicode(200))
    oldcardcode = Column(Unicode(50))
    newcardcode = Column(Unicode(50))
    memo = Column(Unicode(50))
    createdate = Column(String(19, u'Chinese_PRC_CI_AS'))
    handperson = Column(Unicode(50))
    handpersoncode = Column(Unicode(50))
    ts = Column(TIMESTAMP, nullable=False)
    updated = Column(String(19, u'Chinese_PRC_CI_AS'))
    updatedBy = Column(Unicode(32))
    newcode = Column(Unicode(50))
    oldcode = Column(Unicode(50))
    idmember = Column(Integer)
    id = Column(Integer, primary_key=True)
    idchangecardlist = Column(Integer)
    idhandperson = Column(Integer)


class AADRMemberIntegralDetails(Base):
    __tablename__ = 'AA_DR_MemberIntegralDetails'

    code = Column(Unicode(30))
    name = Column(Unicode(200))
    createdate = Column(String(19, u'Chinese_PRC_CI_AS'))
    integral = Column(Numeric(28, 14))
    ts = Column(TIMESTAMP, nullable=False)
    updated = Column(String(19, u'Chinese_PRC_CI_AS'))
    updatedBy = Column(Unicode(32))
    vouchercode = Column(Unicode(50))
    maker = Column(Unicode(50))
    integralChangeReason = Column(Unicode(50))
    idmember = Column(Integer)
    id = Column(Integer, primary_key=True)
    integraltype = Column(Integer)


class AADRMemberRetail(Base):
    __tablename__ = 'AA_DR_MemberRetail'

    code = Column(Unicode(50))
    name = Column(Unicode(200))
    voucherdate = Column(String(19, u'Chinese_PRC_CI_AS'))
    consumeamount = Column(Numeric(28, 14))
    integral = Column(Numeric(28, 14))
    memo = Column(Unicode(200))
    ts = Column(TIMESTAMP, nullable=False)
    updated = Column(String(19, u'Chinese_PRC_CI_AS'))
    updatedBy = Column(Unicode(32))
    priuserdefnvc1 = Column(Unicode(500))
    priuserdefdecm1 = Column(Numeric(28, 14))
    priuserdefnvc2 = Column(Unicode(500))
    priuserdefdecm2 = Column(Numeric(28, 14))
    priuserdefnvc3 = Column(Unicode(500))
    priuserdefdecm3 = Column(Numeric(28, 14))
    priuserdefnvc4 = Column(Unicode(500))
    priuserdefdecm4 = Column(Numeric(28, 14))
    priuserdefnvc5 = Column(Unicode(500))
    priuserdefdecm5 = Column(Numeric(28, 14))
    priuserdefnvc6 = Column(Unicode(500))
    priuserdefdecm6 = Column(Numeric(28, 14))
    pubuserdefnvc1 = Column(Unicode(500))
    pubuserdefdecm1 = Column(Numeric(28, 14))
    pubuserdefnvc2 = Column(Unicode(500))
    pubuserdefdecm2 = Column(Numeric(28, 14))
    pubuserdefnvc3 = Column(Unicode(500))
    pubuserdefdecm3 = Column(Numeric(28, 14))
    pubuserdefnvc4 = Column(Unicode(500))
    pubuserdefdecm4 = Column(Numeric(28, 14))
    pubuserdefnvc5 = Column(Unicode(500))
    pubuserdefdecm5 = Column(Numeric(28, 14))
    pubuserdefnvc6 = Column(Unicode(500))
    pubuserdefdecm6 = Column(Numeric(28, 14))
    steadCashIntegral = Column(Numeric(28, 14))
    sysId = Column(Unicode(100))
    mId = Column(Unicode(100))
    storagesettleamount = Column(Numeric(28, 14))
    steadcashamount = Column(Numeric(28, 14))
    givechangeforstorageamount = Column(Numeric(28, 14))
    maker = Column(Unicode(50))
    idbusitype = Column(Integer)
    iddepartment = Column(Integer)
    idmember = Column(Integer)
    id = Column(Integer, primary_key=True)
    idstore = Column(Integer)
    IdMarketingOrgan = Column(Integer)
    idperson = Column(Integer)
    consumetype = Column(Integer)
    makerId = Column(Integer)
    retailid = Column(Integer)


class AADRMemberRetailPayment(Base):
    __tablename__ = 'AA_DR_MemberRetail_Payment'

    code = Column(Unicode(30))
    name = Column(Unicode(200))
    origamount = Column(Numeric(28, 14))
    amount = Column(Numeric(28, 14))
    overchargesamount = Column(Numeric(28, 14))
    updated = Column(String(19, u'Chinese_PRC_CI_AS'))
    updatedBy = Column(Unicode(32))
    idMemberRetailDTO = Column(Integer)
    id = Column(Integer, primary_key=True)
    idsettlestyle = Column(Integer)


class AADRMemberRetailB(Base):
    __tablename__ = 'AA_DR_MemberRetail_b'

    code = Column(Unicode(30))
    name = Column(Unicode(200))
    quantity = Column(Numeric(28, 14))
    retailprice = Column(Numeric(28, 14))
    memberprice = Column(Numeric(28, 14))
    memberdiscountrate = Column(Numeric(28, 14))
    discountrate = Column(Numeric(28, 14))
    taxprice = Column(Numeric(28, 14))
    retailamount = Column(Numeric(28, 14))
    taxamount = Column(Numeric(28, 14))
    detailDiscountAmount = Column(Numeric(28, 14))
    ts = Column(TIMESTAMP, nullable=False)
    updated = Column(String(19, u'Chinese_PRC_CI_AS'))
    updatedBy = Column(Unicode(32))
    freeItem0 = Column(Unicode(300))
    freeItem1 = Column(Unicode(300))
    freeItem2 = Column(Unicode(300))
    freeItem3 = Column(Unicode(300))
    freeItem4 = Column(Unicode(300))
    freeItem5 = Column(Unicode(300))
    freeItem6 = Column(Unicode(300))
    freeItem7 = Column(Unicode(300))
    freeItem8 = Column(Unicode(300))
    freeItem9 = Column(Unicode(300))
    priuserdefnvc1 = Column(Unicode(500))
    priuserdefdecm1 = Column(Numeric(28, 14))
    priuserdefnvc2 = Column(Unicode(500))
    priuserdefdecm2 = Column(Numeric(28, 14))
    priuserdefnvc3 = Column(Unicode(500))
    priuserdefdecm3 = Column(Numeric(28, 14))
    priuserdefnvc4 = Column(Unicode(500))
    priuserdefdecm4 = Column(Numeric(28, 14))
    pubuserdefnvc1 = Column(Unicode(500))
    pubuserdefdecm1 = Column(Numeric(28, 14))
    pubuserdefnvc2 = Column(Unicode(500))
    pubuserdefdecm2 = Column(Numeric(28, 14))
    pubuserdefnvc3 = Column(Unicode(500))
    pubuserdefdecm3 = Column(Numeric(28, 14))
    pubuserdefnvc4 = Column(Unicode(500))
    pubuserdefdecm4 = Column(Numeric(28, 14))
    basequantity = Column(Numeric(28, 14))
    subquantity = Column(Numeric(28, 14))
    unitexchangerate = Column(Numeric(28, 14))
    CashSettleAmount = Column(Numeric(28, 14))
    VirtualSettleAmount = Column(Numeric(28, 14))
    PromotionVoucherCodes = Column(Unicode(400))
    PromotionVoucherIds = Column(Unicode(400))
    quantity2 = Column(Numeric(28, 14))
    idMemberRetailDTO = Column(Integer)
    id = Column(Integer, primary_key=True)
    idinventory = Column(Integer)
    idbaseunit = Column(Integer)
    idsubunit = Column(Integer)
    idunit = Column(Integer)
    idunit2 = Column(Integer)
    promotiontype = Column(Integer)
    retaildetailid = Column(Integer)


class AADRMemberStorageDetails(Base):
    __tablename__ = 'AA_DR_MemberStorageDetails'

    code = Column(Unicode(30))
    name = Column(Unicode(200))
    createdate = Column(String(19, u'Chinese_PRC_CI_AS'))
    storage = Column(Numeric(28, 14))
    ts = Column(TIMESTAMP, nullable=False)
    updated = Column(String(19, u'Chinese_PRC_CI_AS'))
    updatedBy = Column(Unicode(32))
    vouchercode = Column(Unicode(50))
    maker = Column(Unicode(50))
    idmember = Column(Integer)
    id = Column(Integer, primary_key=True)
    idstore = Column(Integer)
    storagetype = Column(Integer)


t_AA_DR_MemberStorageUsed = Table(
    'AA_DR_MemberStorageUsed', metadata,
    Column('key', UNIQUEIDENTIFIER, nullable=False),
    Column('storage', Numeric(28, 14)),
    Column('retailvouchercode', Unicode(50)),
    Column('maker', Unicode(50)),
    Column('storagetype', Integer),
    Column('idmember', Integer),
    Column('idstore', Integer),
    Column('createdate', DateTime)
)


class AADRMemberType(Base):
    __tablename__ = 'AA_DR_MemberType'

    code = Column(Unicode(30))
    name = Column(Unicode(200))
    initpassword = Column(Unicode(50))
    isneedpwd = Column(Integer)
    validityperiod = Column(Integer)
    isdiscount = Column(Integer)
    generaldiscountrate = Column(Numeric(28, 14))
    newprodiscountrate = Column(Numeric(28, 14))
    isintegral = Column(Integer)
    initintegral = Column(Numeric(28, 14))
    onlyinitpriceintegral = Column(Integer)
    generalamount = Column(Numeric(28, 14))
    generaiintegral = Column(Numeric(28, 14))
    newproamount = Column(Numeric(28, 14))
    newprointegral = Column(Numeric(28, 14))
    ismonday = Column(Integer)
    istuesday = Column(Integer)
    iswednesday = Column(Integer)
    isthursday = Column(Integer)
    isfriday = Column(Integer)
    issaturday = Column(Integer)
    issunday = Column(Integer)
    weekdayintemulti = Column(Numeric(28, 14))
    memberbirthdayintemulti = Column(Numeric(28, 14))
    issystem = Column(Integer)
    createdtime = Column(String(19, u'Chinese_PRC_CI_AS'))
    sequencenumber = Column(Integer)
    ts = Column(TIMESTAMP, nullable=False)
    updated = Column(String(19, u'Chinese_PRC_CI_AS'))
    updatedBy = Column(Unicode(32))
    IsEndNode = Column(Integer, server_default=text("((1))"))
    InId = Column(Unicode(100))
    idparent = Column(Unicode(100))
    priuserdefnvc1 = Column(Unicode(500))
    priuserdefdecm1 = Column(Numeric(28, 14))
    priuserdefnvc2 = Column(Unicode(500))
    priuserdefdecm2 = Column(Numeric(28, 14))
    priuserdefnvc3 = Column(Unicode(500))
    priuserdefdecm3 = Column(Numeric(28, 14))
    priuserdefnvc4 = Column(Unicode(500))
    priuserdefdecm4 = Column(Numeric(28, 14))
    priuserdefnvc5 = Column(Unicode(500))
    priuserdefdecm5 = Column(Numeric(28, 14))
    isstorage = Column(Integer, nullable=False, server_default=text("((0))"))
    canoveramount = Column(Numeric(28, 14))
    bottomamount = Column(Numeric(28, 14))
    id = Column(Integer, primary_key=True)
    cardtype = Column(Integer)
    discounttype = Column(Integer)
    integraltype = Column(Integer)
    memberbirthdaytype = Column(Integer)


class AADRMemberTypeDiscount(Base):
    __tablename__ = 'AA_DR_MemberType_Discount'

    code = Column(Unicode(30))
    name = Column(Unicode(200))
    inventoryunit = Column(Unicode(200))
    discountrate = Column(Numeric(28, 14))
    createdtime = Column(String(19, u'Chinese_PRC_CI_AS'))
    sequencenumber = Column(Integer)
    ts = Column(TIMESTAMP, nullable=False)
    updated = Column(String(19, u'Chinese_PRC_CI_AS'))
    updatedBy = Column(Unicode(32))
    idMemberTypeDTO = Column(Integer)
    id = Column(Integer, primary_key=True)
    idinventory = Column(Integer)
    idinventoryclass = Column(Integer)
    brand = Column(Integer)


class AADRMemberTypeIntegral(Base):
    __tablename__ = 'AA_DR_MemberType_Integral'

    code = Column(Unicode(30))
    name = Column(Unicode(200))
    amount = Column(Numeric(28, 14))
    integral = Column(Numeric(28, 14))
    createdtime = Column(String(19, u'Chinese_PRC_CI_AS'))
    sequencenumber = Column(Integer)
    ts = Column(TIMESTAMP, nullable=False)
    updated = Column(String(19, u'Chinese_PRC_CI_AS'))
    updatedBy = Column(Unicode(32))
    idMemberTypeDTO = Column(Integer)
    id = Column(Integer, primary_key=True)
    idinventory = Column(Integer)
    idinventoryclass = Column(Integer)
    brand = Column(Integer)


class AADRMemberTypeIntegralDouble(Base):
    __tablename__ = 'AA_DR_MemberType_IntegralDouble'

    code = Column(Unicode(30))
    name = Column(Unicode(200))
    starttime = Column(String(19, u'Chinese_PRC_CI_AS'))
    endtime = Column(String(19, u'Chinese_PRC_CI_AS'))
    integralmulti = Column(Numeric(28, 14))
    createdtime = Column(String(19, u'Chinese_PRC_CI_AS'))
    sequencenumber = Column(Integer)
    ts = Column(TIMESTAMP, nullable=False)
    updated = Column(String(19, u'Chinese_PRC_CI_AS'))
    updatedBy = Column(Unicode(32))
    idMemberTypeDTO = Column(Integer)
    id = Column(Integer, primary_key=True)


class AADRMemberTypeIntegralForStorageRule(Base):
    __tablename__ = 'AA_DR_MemberType_IntegralForStorageRule'

    code = Column(Unicode(30))
    name = Column(Unicode(200))
    fullintegral = Column(Numeric(28, 14))
    inteforstorageamount = Column(Numeric(28, 14))
    effectivedate = Column(String(19, u'Chinese_PRC_CI_AS'))
    expirationdate = Column(String(19, u'Chinese_PRC_CI_AS'))
    createdtime = Column(String(19, u'Chinese_PRC_CI_AS'))
    sequencenumber = Column(Integer)
    ts = Column(TIMESTAMP, nullable=False)
    updated = Column(String(19, u'Chinese_PRC_CI_AS'))
    updatedBy = Column(Unicode(32))
    idMemberTypeDTO = Column(Integer)
    id = Column(Integer, primary_key=True)


class AADRMemberTypeStorageRule(Base):
    __tablename__ = 'AA_DR_MemberType_StorageRule'

    code = Column(Unicode(30))
    name = Column(Unicode(200))
    fullamount = Column(Numeric(28, 14))
    presentamount = Column(Numeric(28, 14))
    effectivedate = Column(String(19, u'Chinese_PRC_CI_AS'))
    expirationdate = Column(String(19, u'Chinese_PRC_CI_AS'))
    isstorageintegral = Column(Integer)
    createdtime = Column(String(19, u'Chinese_PRC_CI_AS'))
    sequencenumber = Column(Integer)
    ts = Column(TIMESTAMP, nullable=False)
    updated = Column(String(19, u'Chinese_PRC_CI_AS'))
    updatedBy = Column(Unicode(32))
    idMemberTypeDTO = Column(Integer)
    id = Column(Integer, primary_key=True)
    storagetype = Column(Integer)


class AADRMemberUpgradeRecord(Base):
    __tablename__ = 'AA_DR_MemberUpgradeRecord'

    code = Column(Unicode(30))
    name = Column(Unicode(200))
    handpersoncode = Column(Unicode(50))
    handperson = Column(Unicode(50))
    newcardcode = Column(Unicode(50))
    oldcardcode = Column(Unicode(50))
    ts = Column(TIMESTAMP, nullable=False)
    updated = Column(String(19, u'Chinese_PRC_CI_AS'))
    updatedBy = Column(Unicode(32))
    upgradedate = Column(String(19, u'Chinese_PRC_CI_AS'))
    createdate = Column(String(19, u'Chinese_PRC_CI_AS'))
    newcode = Column(Unicode(50))
    oldcode = Column(Unicode(50))
    idmember = Column(Integer)
    idnewmembertype = Column(Integer)
    idoldmembertype = Column(Integer)
    id = Column(Integer, primary_key=True)
    idhandperson = Column(Integer)
    upgradetype = Column(Integer)


class AADRStore(Base):
    __tablename__ = 'AA_DR_Store'

    code = Column(Unicode(30))
    name = Column(Unicode(200))
    abbreviation = Column(Unicode(50))
    shorthand = Column(Unicode(50))
    address = Column(Unicode(50))
    telephone = Column(Unicode(50))
    disabled = Column(Integer)
    memo = Column(Unicode(50))
    checkaddress = Column(Unicode(200))
    cashshieldnum = Column(Integer, server_default=text("((0))"))
    createdtime = Column(String(19, u'Chinese_PRC_CI_AS'))
    sequencenumber = Column(Integer)
    ts = Column(TIMESTAMP, nullable=False)
    updated = Column(String(19, u'Chinese_PRC_CI_AS'))
    updatedBy = Column(Unicode(32))
    priuserdefnvc1 = Column(Unicode(500))
    priuserdefdecm1 = Column(Numeric(28, 14))
    priuserdefnvc2 = Column(Unicode(500))
    priuserdefdecm2 = Column(Numeric(28, 14))
    priuserdefnvc3 = Column(Unicode(500))
    priuserdefdecm3 = Column(Numeric(28, 14))
    priuserdefnvc4 = Column(Unicode(500))
    priuserdefdecm4 = Column(Numeric(28, 14))
    priuserdefnvc5 = Column(Unicode(500))
    priuserdefdecm5 = Column(Numeric(28, 14))
    autoLogistic = Column(Unicode(10))
    autoUnLock = Column(Integer)
    nonPayNumber = Column(Integer)
    paidNumber = Column(Integer)
    haveSellerRemark = Column(Integer)
    haveBuyerMessage = Column(Integer)
    applyRefund = Column(Integer)
    cashOnDeliveryOrder = Column(Integer)
    paidOrderAutoCheck = Column(Integer)
    wholesaleType = Column(Integer)
    shipmentsAutoUpType = Column(Integer)
    autoDownAddInvertory = Column(Integer)
    virtualInvertory = Column(Numeric(28, 14))
    autoDownInventory = Column(Integer)
    upInventoryNumberPerce = Column(Numeric(18, 0))
    sellerNo = Column(Unicode(50))
    shopWebset = Column(Unicode(100))
    shopFullName = Column(Unicode(50))
    correspondwarehouse = Column(Unicode(200))
    pickedUnLock = Column(Integer)
    LastUpdateTime = Column(String(19, u'Chinese_PRC_CI_AS'))
    LastRefundTime = Column(String(19, u'Chinese_PRC_CI_AS'))
    buyerAddressUpdate = Column(Integer)
    isdeductionforepost = Column(Integer)
    idbankaccount = Column(Integer)
    iddepartment = Column(Integer)
    idmembertype = Column(Integer)
    iddefalutshipments = Column(Integer)
    id = Column(Integer, primary_key=True)
    idinventoryclass = Column(Integer)
    idmarketingorgan = Column(Integer)
    idcustomer = Column(Integer)
    idsettlementcustomer = Column(Integer)
    idpartnerclass = Column(Integer)
    idperson = Column(Integer)
    idReceiveSettleStyle = Column(Integer)
    idunit = Column(Integer)
    iddistrict = Column(Integer)
    idwarehouse = Column(Integer)
    branchdistributionway = Column(Integer)
    storetype = Column(Integer)
    priceMode = Column(Integer)
    shopType = Column(Integer)


class AADRStoreCashShield(Base):
    __tablename__ = 'AA_DR_Store_CashShield'

    code = Column(Unicode(30))
    name = Column(Unicode(200))
    memo = Column(Unicode(50))
    cashshieldcode = Column(Unicode(50))
    createdtime = Column(String(19, u'Chinese_PRC_CI_AS'))
    sequencenumber = Column(Integer)
    ts = Column(TIMESTAMP, nullable=False)
    updated = Column(String(19, u'Chinese_PRC_CI_AS'))
    updatedBy = Column(Unicode(32))
    idStoreDTO = Column(Integer)
    id = Column(Integer, primary_key=True)


class AADRStorePOS(Base):
    __tablename__ = 'AA_DR_Store_POS'

    code = Column(Unicode(30))
    name = Column(Unicode(200))
    memo = Column(Unicode(50))
    isused = Column(Integer)
    poscode = Column(Unicode(50))
    posname = Column(Unicode(50))
    createdtime = Column(String(19, u'Chinese_PRC_CI_AS'))
    sequencenumber = Column(Integer)
    ts = Column(TIMESTAMP, nullable=False)
    updated = Column(String(19, u'Chinese_PRC_CI_AS'))
    updatedBy = Column(Unicode(32))
    cancel = Column(Unicode(50))
    idStoreDTO = Column(Integer)
    encryptionstate = Column(Integer)
    id = Column(Integer, primary_key=True)


class AADRStoreRound(Base):
    __tablename__ = 'AA_DR_Store_Round'

    code = Column(Unicode(30))
    name = Column(Unicode(200))
    createdtime = Column(String(19, u'Chinese_PRC_CI_AS'))
    sequencenumber = Column(Integer)
    ts = Column(TIMESTAMP, nullable=False)
    updated = Column(String(19, u'Chinese_PRC_CI_AS'))
    updatedBy = Column(Unicode(32))
    idStoreDTO = Column(Integer)
    idroundstore = Column(Integer)
    id = Column(Integer, primary_key=True)


class AADRStoreSettleStyle(Base):
    __tablename__ = 'AA_DR_Store_SettleStyle'

    code = Column(Unicode(30))
    name = Column(Unicode(200))
    createdtime = Column(String(19, u'Chinese_PRC_CI_AS'))
    sequencenumber = Column(Integer)
    ts = Column(TIMESTAMP, nullable=False)
    updated = Column(String(19, u'Chinese_PRC_CI_AS'))
    updatedBy = Column(Unicode(32))
    idbankaccount = Column(Integer)
    idStoreDTO = Column(Integer)
    id = Column(Integer, primary_key=True)
    idsettlestyle = Column(Integer)


class AADRStoreShift(Base):
    __tablename__ = 'AA_DR_Store_Shift'

    code = Column(Unicode(30))
    name = Column(Unicode(200))
    starttime = Column(String(8, u'Chinese_PRC_CI_AS'))
    memo = Column(Unicode(50))
    createdtime = Column(String(19, u'Chinese_PRC_CI_AS'))
    sequencenumber = Column(Integer)
    ts = Column(TIMESTAMP, nullable=False)
    updated = Column(String(19, u'Chinese_PRC_CI_AS'))
    updatedBy = Column(Unicode(32))
    idStoreDTO = Column(Integer)
    id = Column(Integer, primary_key=True)
    shiftname = Column(Integer)


t_AA_DR_Store_WareHouse = Table(
    'AA_DR_Store_WareHouse', metadata,
    Column('id', UNIQUEIDENTIFIER, nullable=False),
    Column('code', Unicode(30)),
    Column('name', Unicode(200)),
    Column('createdtime', String(19, u'Chinese_PRC_CI_AS')),
    Column('sequencenumber', Integer),
    Column('ts', TIMESTAMP, nullable=False),
    Column('updated', String(19, u'Chinese_PRC_CI_AS')),
    Column('updatedBy', Unicode(32)),
    Column('idwarehouse', UNIQUEIDENTIFIER),
    Column('idstore', UNIQUEIDENTIFIER)
)


t_AA_Department = Table(
    'AA_Department', metadata,
    Column('code', Unicode(32)),
    Column('name', Unicode(200)),
    Column('isEndNode', Integer),
    Column('depth', Integer),
    Column('disabled', Integer),
    Column('ts', TIMESTAMP),
    Column('updatedBy', Unicode(32)),
    Column('priuserdefnvc1', Unicode(500)),
    Column('priuserdefdecm1', Numeric(28, 14)),
    Column('priuserdefnvc2', Unicode(500)),
    Column('priuserdefdecm2', Numeric(28, 14)),
    Column('priuserdefnvc3', Unicode(500)),
    Column('priuserdefdecm3', Numeric(28, 14)),
    Column('priuserdefnvc4', Unicode(500)),
    Column('priuserdefdecm4', Numeric(28, 14)),
    Column('priuserdefnvc5', Unicode(500)),
    Column('priuserdefdecm5', Numeric(28, 14)),
    Column('inId', Unicode(560)),
    Column('id', Integer, nullable=False),
    Column('idparent', Integer),
    Column('idMarketingOrgan', Integer),
    Column('iddirector', Integer),
    Column('madeDate', DateTime),
    Column('updated', DateTime),
    Column('createdTime', DateTime)
)


t_AA_DepartmentInventoryPrice = Table(
    'AA_DepartmentInventoryPrice', metadata,
    Column('code', Unicode(32)),
    Column('name', Unicode(200)),
    Column('level1Price', Unicode(1000)),
    Column('level2Price', Unicode(1000)),
    Column('level3Price', Unicode(1000)),
    Column('level4Price', Unicode(1000)),
    Column('level5Price', Unicode(1000)),
    Column('lowestPrice', Unicode(1000)),
    Column('retailPrice', Unicode(1000)),
    Column('ts', TIMESTAMP),
    Column('updatedBy', Unicode(32)),
    Column('retailPriceFormula', Unicode(1000)),
    Column('level1PriceFormula', Unicode(1000)),
    Column('level2PriceFormula', Unicode(1000)),
    Column('level3PriceFormula', Unicode(1000)),
    Column('level4PriceFormula', Unicode(1000)),
    Column('level5PriceFormula', Unicode(1000)),
    Column('lowestPriceFormula', Unicode(1000)),
    Column('level6Price', Unicode(1000)),
    Column('level6PriceFormula', Unicode(1000)),
    Column('level7Price', Unicode(1000)),
    Column('level7PriceFormula', Unicode(1000)),
    Column('level8Price', Unicode(1000)),
    Column('level8PriceFormula', Unicode(1000)),
    Column('level9Price', Unicode(1000)),
    Column('level9PriceFormula', Unicode(1000)),
    Column('level10Price', Unicode(1000)),
    Column('level10PriceFormula', Unicode(1000)),
    Column('id', Integer, nullable=False),
    Column('iddepartment', Integer),
    Column('idpricetrace', Integer),
    Column('idinventory', Integer),
    Column('idinventoryprice', Integer),
    Column('idunit', Integer),
    Column('createdtime', DateTime),
    Column('updated', DateTime)
)


t_AA_DepartmentInventoryPriceTrace = Table(
    'AA_DepartmentInventoryPriceTrace', metadata,
    Column('code', Unicode(32)),
    Column('name', Unicode(200)),
    Column('unitprice', Numeric(32, 15)),
    Column('discount', Numeric(32, 15)),
    Column('lastPrice', Numeric(32, 15)),
    Column('unittaxprice', Numeric(32, 15)),
    Column('ts', TIMESTAMP),
    Column('updatedBy', Unicode(32)),
    Column('id', Integer, nullable=False),
    Column('iddepartment', Integer, nullable=False, server_default=text("((0))")),
    Column('idinventory', Integer, nullable=False, server_default=text("((0))")),
    Column('idunit', Integer, nullable=False, server_default=text("((0))")),
    Column('createdtime', DateTime),
    Column('updated', DateTime)
)


t_AA_Department_Ext = Table(
    'AA_Department_Ext', metadata,
    Column('departmentcode_lev1', Unicode(32)),
    Column('departmentname_lev1', Unicode(200)),
    Column('departmentcode_lev2', Unicode(32)),
    Column('departmentname_lev2', Unicode(200)),
    Column('departmentcode_lev3', Unicode(32)),
    Column('departmentname_lev3', Unicode(200)),
    Column('departmentcode_lev4', Unicode(32)),
    Column('departmentname_lev4', Unicode(200)),
    Column('departmentcode_lev5', Unicode(32)),
    Column('departmentname_lev5', Unicode(200)),
    Column('departmentcode_lev6', Unicode(32)),
    Column('departmentname_lev6', Unicode(200)),
    Column('departmentcode_lev7', Unicode(32)),
    Column('departmentname_lev7', Unicode(200)),
    Column('departmentcode_lev8', Unicode(32)),
    Column('departmentname_lev8', Unicode(200)),
    Column('departmentcode_lev9', Unicode(32)),
    Column('departmentname_lev9', Unicode(200)),
    Column('departmentcode_lev10', Unicode(32)),
    Column('departmentname_lev10', Unicode(200)),
    Column('departmentcode_lev11', Unicode(32)),
    Column('departmentname_lev11', Unicode(200)),
    Column('departmentcode_lev12', Unicode(32)),
    Column('departmentname_lev12', Unicode(200)),
    Column('departmentcode_lev13', Unicode(32)),
    Column('departmentname_lev13', Unicode(200)),
    Column('departmentcode_lev14', Unicode(32)),
    Column('departmentname_lev14', Unicode(200)),
    Column('departmentcode_lev15', Unicode(32)),
    Column('departmentname_lev15', Unicode(200)),
    Column('depth', Unicode(10)),
    Column('ts', TIMESTAMP),
    Column('departmentid_lev1', Integer),
    Column('departmentid_lev10', Integer),
    Column('departmentid_lev11', Integer),
    Column('departmentid_lev12', Integer),
    Column('departmentid_lev13', Integer),
    Column('departmentid_lev14', Integer),
    Column('departmentid_lev15', Integer),
    Column('departmentid_lev2', Integer),
    Column('departmentid_lev3', Integer),
    Column('departmentid_lev4', Integer),
    Column('departmentid_lev5', Integer),
    Column('departmentid_lev6', Integer),
    Column('departmentid_lev7', Integer),
    Column('departmentid_lev8', Integer),
    Column('departmentid_lev9', Integer),
    Column('id', Integer),
    Column('createTime', DateTime, index=True)
)


class AADeprMethod(Base):
    __tablename__ = 'AA_DeprMethod'

    code = Column(Unicode(30))
    name = Column(Unicode(100))
    depramount = Column(Unicode(500))
    deprrate = Column(Unicode(500))
    ts = Column(TIMESTAMP, nullable=False)
    sequenceNumber = Column(Integer)
    updated = Column(String(19, u'Chinese_PRC_CI_AS'))
    updatedBy = Column(Unicode(32))
    createdTime = Column(String(19, u'Chinese_PRC_CI_AS'))
    id = Column(Integer, primary_key=True)


t_AA_District = Table(
    'AA_District', metadata,
    Column('code', Unicode(32)),
    Column('name', Unicode(200)),
    Column('disabled', Integer),
    Column('isEndNode', Integer),
    Column('depth', Integer),
    Column('ts', TIMESTAMP),
    Column('updatedBy', Unicode(32)),
    Column('inId', Unicode(560)),
    Column('id', Integer, nullable=False),
    Column('idparent', Integer),
    Column('madeDate', DateTime),
    Column('updated', DateTime),
    Column('createdTime', DateTime)
)


class AADocAccountDetail(Base):
    __tablename__ = 'AA_DocAccountDetail'

    code = Column(Unicode(30))
    name = Column(Unicode(50))
    accountcode = Column(Unicode(50))
    createdtime = Column(String(19, u'Chinese_PRC_CI_AS'))
    sequencenumber = Column(Integer)
    ts = Column(TIMESTAMP, nullable=False)
    updated = Column(String(19, u'Chinese_PRC_CI_AS'))
    updatedBy = Column(Unicode(32))
    idaccount = Column(Integer)
    id = Column(Integer, primary_key=True)
    idDocTypeDTO = Column(Integer)


class AADocType(Base):
    __tablename__ = 'AA_DocType'

    code = Column(Unicode(30))
    name = Column(Unicode(200))
    docword = Column(Unicode(50))
    createdtime = Column(String(19, u'Chinese_PRC_CI_AS'))
    sequencenumber = Column(Integer)
    ts = Column(TIMESTAMP, nullable=False)
    updated = Column(String(19, u'Chinese_PRC_CI_AS'))
    updatedBy = Column(Unicode(32))
    disabled = Column(Integer, nullable=False, server_default=text("((0))"))
    id = Column(Integer, primary_key=True)
    limitedtype = Column(Integer)


class AADocumentsUsage(Base):
    __tablename__ = 'AA_DocumentsUsage'

    code = Column(Unicode(30))
    name = Column(Unicode(100))
    shorthand = Column(Unicode(100))
    createdtime = Column(String(19, u'Chinese_PRC_CI_AS'))
    sequencenumber = Column(Integer)
    ts = Column(TIMESTAMP, nullable=False)
    updated = Column(String(19, u'Chinese_PRC_CI_AS'))
    updatedBy = Column(Unicode(32))
    id = Column(Integer, primary_key=True)


t_AA_EnumFreeItemsAvailable = Table(
    'AA_EnumFreeItemsAvailable', metadata,
    Column('code', Unicode(50)),
    Column('name', Unicode(300)),
    Column('isInUse', Integer),
    Column('ts', TIMESTAMP, nullable=False),
    Column('updatedBy', Unicode(32)),
    Column('id', Integer, nullable=False),
    Column('idInventory', Integer, nullable=False, server_default=text("((0))")),
    Column('EnumID', Integer, nullable=False, server_default=text("((0))")),
    Column('idEnumitem', Integer, nullable=False, server_default=text("((0))")),
    Column('updated', DateTime)
)


t_AA_ExchangeRate = Table(
    'AA_ExchangeRate', metadata,
    Column('id', Integer, nullable=False, unique=True),
    Column('ts', TIMESTAMP, nullable=False),
    Column('updatedBy', Unicode(32)),
    Column('updated', DateTime),
    Column('name', Unicode(200)),
    Column('code', Unicode(32)),
    Column('AccountDateRange', DateTime, index=True),
    Column('ExchangeRate', Numeric(28, 14), index=True),
    Column('IDCurrency', Integer, index=True),
    Column('ExChangeRateStyle', Integer, index=True)
)


class AAExpenseItem(Base):
    __tablename__ = 'AA_ExpenseItem'

    code = Column(Unicode(32))
    name = Column(Unicode(200))
    apportionFlag = Column(Integer)
    depth = Column(Integer)
    isEndNode = Column(Integer)
    disabled = Column(Integer)
    madeDate = Column(String(19, u'Chinese_PRC_CI_AS'))
    ts = Column(TIMESTAMP)
    updated = Column(String(19, u'Chinese_PRC_CI_AS'))
    updatedBy = Column(Unicode(32))
    inId = Column(Unicode(560))
    createdTime = Column(String(19, u'Chinese_PRC_CI_AS'))
    id = Column(Integer, primary_key=True)
    idparent = Column(Integer)
    dispatchMode = Column(Integer)
    expenseType = Column(Integer)


t_AA_FixedAssetsBarCodeSectionInfo = Table(
    'AA_FixedAssetsBarCodeSectionInfo', metadata,
    Column('code', Unicode(32)),
    Column('name', Unicode(200)),
    Column('sectionNo', Integer),
    Column('length', Integer),
    Column('ts', TIMESTAMP, nullable=False),
    Column('updatedBy', Unicode(32)),
    Column('id', Integer, nullable=False),
    Column('idBarCodeSolution', Integer),
    Column('fillType', Integer),
    Column('format', Integer),
    Column('sectionInfo', Integer),
    Column('madeDate', DateTime),
    Column('updated', DateTime),
    Column('createdTime', DateTime)
)


t_AA_FixedAssetsBarCodeSolution = Table(
    'AA_FixedAssetsBarCodeSolution', metadata,
    Column('ts', TIMESTAMP, nullable=False),
    Column('updatedBy', Unicode(32)),
    Column('code', Unicode(6)),
    Column('name', Unicode(30)),
    Column('length', Integer),
    Column('memo', Unicode(560)),
    Column('id', Integer, nullable=False),
    Column('codingType', Integer),
    Column('updated', DateTime),
    Column('madeDate', DateTime),
    Column('createdTime', DateTime)
)


t_AA_FreeItemsEnum = Table(
    'AA_FreeItemsEnum', metadata,
    Column('code', Unicode(30)),
    Column('name', Unicode(200)),
    Column('sequencenumber', Integer),
    Column('ts', TIMESTAMP, nullable=False),
    Column('updatedBy', Unicode(32)),
    Column('Freeitems', Unicode(200)),
    Column('freeItem0', Unicode(300)),
    Column('freeItem1', Unicode(300)),
    Column('freeItem2', Unicode(300)),
    Column('freeItem3', Unicode(300)),
    Column('freeItem4', Unicode(300)),
    Column('freeItem5', Unicode(300)),
    Column('freeItem6', Unicode(300)),
    Column('freeItem7', Unicode(300)),
    Column('freeItem8', Unicode(300)),
    Column('freeItem9', Unicode(300)),
    Column('id', Integer, nullable=False),
    Column('idInventoryDTO', Integer),
    Column('createdtime', DateTime),
    Column('updated', DateTime)
)


class AAHandleReason(Base):
    __tablename__ = 'AA_HandleReason'

    code = Column(Unicode(30))
    name = Column(Unicode(100))
    depth = Column(Integer)
    isendnode = Column(Integer)
    ispreset = Column(Integer)
    inid = Column(Unicode(750))
    ts = Column(TIMESTAMP, nullable=False)
    updated = Column(String(19, u'Chinese_PRC_CI_AS'))
    updatedBy = Column(Unicode(32))
    createdTime = Column(String(19, u'Chinese_PRC_CI_AS'))
    id = Column(Integer, primary_key=True)
    idparent = Column(Integer)


t_AA_HandleReason_Ext = Table(
    'AA_HandleReason_Ext', metadata,
    Column('handleReasoncode_lev1', Unicode(40)),
    Column('handleReasonname_lev1', Unicode(100)),
    Column('handleReasoncode_lev2', Unicode(40)),
    Column('handleReasonname_lev2', Unicode(100)),
    Column('handleReasoncode_lev3', Unicode(40)),
    Column('handleReasonname_lev3', Unicode(100)),
    Column('handleReasoncode_lev4', Unicode(40)),
    Column('handleReasonname_lev4', Unicode(100)),
    Column('handleReasoncode_lev5', Unicode(40)),
    Column('handleReasonname_lev5', Unicode(100)),
    Column('handleReasoncode_lev6', Unicode(40)),
    Column('handleReasonname_lev6', Unicode(100)),
    Column('handleReasoncode_lev7', Unicode(40)),
    Column('handleReasonname_lev7', Unicode(100)),
    Column('handleReasoncode_lev8', Unicode(40)),
    Column('handleReasonname_lev8', Unicode(100)),
    Column('handleReasoncode_lev9', Unicode(40)),
    Column('handleReasonname_lev9', Unicode(100)),
    Column('handleReasoncode_lev10', Unicode(40)),
    Column('handleReasonname_lev10', Unicode(100)),
    Column('handleReasoncode_lev11', Unicode(40)),
    Column('handleReasonname_lev11', Unicode(100)),
    Column('handleReasoncode_lev12', Unicode(40)),
    Column('handleReasonname_lev12', Unicode(100)),
    Column('handleReasoncode_lev13', Unicode(40)),
    Column('handleReasonname_lev13', Unicode(100)),
    Column('handleReasoncode_lev14', Unicode(40)),
    Column('handleReasonname_lev14', Unicode(100)),
    Column('handleReasoncode_lev15', Unicode(40)),
    Column('handleReasonname_lev15', Unicode(100)),
    Column('depth', Unicode(10)),
    Column('createTime', String(19, u'Chinese_PRC_CI_AS')),
    Column('ts', TIMESTAMP),
    Column('id', Integer),
    Column('handleReasonid_lev1', Integer),
    Column('handleReasonid_lev10', Integer),
    Column('handleReasonid_lev11', Integer),
    Column('handleReasonid_lev12', Integer),
    Column('handleReasonid_lev13', Integer),
    Column('handleReasonid_lev14', Integer),
    Column('handleReasonid_lev15', Integer),
    Column('handleReasonid_lev2', Integer),
    Column('handleReasonid_lev3', Integer),
    Column('handleReasonid_lev4', Integer),
    Column('handleReasonid_lev5', Integer),
    Column('handleReasonid_lev6', Integer),
    Column('handleReasonid_lev7', Integer),
    Column('handleReasonid_lev8', Integer),
    Column('handleReasonid_lev9', Integer)
)


class AAIncDecWay(Base):
    __tablename__ = 'AA_IncDecWay'

    code = Column(Unicode(30))
    name = Column(Unicode(100))
    depth = Column(Integer)
    isendnode = Column(Integer)
    inid = Column(Unicode(750))
    isinc = Column(Integer)
    ispreset = Column(Integer)
    ts = Column(TIMESTAMP, nullable=False)
    updated = Column(String(19, u'Chinese_PRC_CI_AS'))
    updatedBy = Column(Unicode(32))
    createdTime = Column(String(19, u'Chinese_PRC_CI_AS'))
    id = Column(Integer, primary_key=True)
    idparent = Column(Integer)


t_AA_IncDecWay_Ext = Table(
    'AA_IncDecWay_Ext', metadata,
    Column('incDecWaycode_lev1', Unicode(40)),
    Column('incDecWayname_lev1', Unicode(100)),
    Column('incDecWaycode_lev2', Unicode(40)),
    Column('incDecWayname_lev2', Unicode(100)),
    Column('incDecWaycode_lev3', Unicode(40)),
    Column('incDecWayname_lev3', Unicode(100)),
    Column('incDecWaycode_lev4', Unicode(40)),
    Column('incDecWayname_lev4', Unicode(100)),
    Column('incDecWaycode_lev5', Unicode(40)),
    Column('incDecWayname_lev5', Unicode(100)),
    Column('incDecWaycode_lev6', Unicode(40)),
    Column('incDecWayname_lev6', Unicode(100)),
    Column('incDecWaycode_lev7', Unicode(40)),
    Column('incDecWayname_lev7', Unicode(100)),
    Column('incDecWaycode_lev8', Unicode(40)),
    Column('incDecWayname_lev8', Unicode(100)),
    Column('incDecWaycode_lev9', Unicode(40)),
    Column('incDecWayname_lev9', Unicode(100)),
    Column('incDecWaycode_lev10', Unicode(40)),
    Column('incDecWayname_lev10', Unicode(100)),
    Column('incDecWaycode_lev11', Unicode(40)),
    Column('incDecWayname_lev11', Unicode(100)),
    Column('incDecWaycode_lev12', Unicode(40)),
    Column('incDecWayname_lev12', Unicode(100)),
    Column('incDecWaycode_lev13', Unicode(40)),
    Column('incDecWayname_lev13', Unicode(100)),
    Column('incDecWaycode_lev14', Unicode(40)),
    Column('incDecWayname_lev14', Unicode(100)),
    Column('incDecWaycode_lev15', Unicode(40)),
    Column('incDecWayname_lev15', Unicode(100)),
    Column('depth', Unicode(10)),
    Column('createTime', String(19, u'Chinese_PRC_CI_AS')),
    Column('ts', TIMESTAMP),
    Column('id', Integer),
    Column('incDecWayid_lev1', Integer),
    Column('incDecWayid_lev10', Integer),
    Column('incDecWayid_lev11', Integer),
    Column('incDecWayid_lev12', Integer),
    Column('incDecWayid_lev13', Integer),
    Column('incDecWayid_lev14', Integer),
    Column('incDecWayid_lev15', Integer),
    Column('incDecWayid_lev2', Integer),
    Column('incDecWayid_lev3', Integer),
    Column('incDecWayid_lev4', Integer),
    Column('incDecWayid_lev5', Integer),
    Column('incDecWayid_lev6', Integer),
    Column('incDecWayid_lev7', Integer),
    Column('incDecWayid_lev8', Integer),
    Column('incDecWayid_lev9', Integer)
)


class AAIncome(Base):
    __tablename__ = 'AA_Income'

    code = Column(Unicode(32))
    name = Column(Unicode(200))
    isEndNode = Column(Integer)
    depth = Column(Integer)
    disabled = Column(Integer)
    madeDate = Column(String(19, u'Chinese_PRC_CI_AS'))
    ts = Column(TIMESTAMP)
    updated = Column(String(19, u'Chinese_PRC_CI_AS'))
    updatedBy = Column(Unicode(32))
    inId = Column(Unicode(560))
    createdTime = Column(String(19, u'Chinese_PRC_CI_AS'))
    id = Column(Integer, primary_key=True)
    idparent = Column(Integer)


class AAInventory(Base):
    __tablename__ = 'AA_Inventory'

    code = Column(Unicode(32))
    name = Column(Unicode(200))
    shorthand = Column(Unicode(200))
    specification = Column(Unicode(200))
    procureBatch = Column(Numeric(28, 14))
    invSCost = Column(Numeric(28, 14))
    latestCost = Column(Numeric(28, 14))
    avagCost = Column(Numeric(28, 14))
    isLimitedWithdraw = Column(Integer)
    isBatch = Column(Integer)
    isQualityPeriod = Column(Integer)
    isSale = Column(Integer)
    isMadeSelf = Column(Integer)
    isPurchase = Column(Integer)
    isMaterial = Column(Integer)
    lowQuantity = Column(Numeric(28, 14))
    topQuantity = Column(Numeric(28, 14))
    safeQuantity = Column(Numeric(28, 14))
    picture = Column(Unicode(50))
    disabled = Column(Integer)
    isQualityCheck = Column(Integer)
    isMadeRequest = Column(Integer)
    isSingleUnit = Column(Integer)
    ts = Column(TIMESTAMP)
    updatedBy = Column(Unicode(32))
    Userfreeitem7 = Column(Integer, server_default=text("(0)"))
    Userfreeitem6 = Column(Integer, server_default=text("(0)"))
    Userfreeitem2 = Column(Integer, server_default=text("(0)"))
    Userfreeitem1 = Column(Integer, server_default=text("(0)"))
    Userfreeitem9 = Column(Integer, server_default=text("(0)"))
    Userfreeitem0 = Column(Integer, server_default=text("(0)"))
    Userfreeitem8 = Column(Integer, server_default=text("(0)"))
    Userfreeitem5 = Column(Integer, server_default=text("(0)"))
    Userfreeitem4 = Column(Integer, server_default=text("(0)"))
    Userfreeitem3 = Column(Integer, server_default=text("(0)"))
    MustInputFreeitem7 = Column(Integer, server_default=text("(0)"))
    MustInputFreeitem2 = Column(Integer, server_default=text("(0)"))
    MustInputFreeitem6 = Column(Integer, server_default=text("(0)"))
    MustInputFreeitem3 = Column(Integer, server_default=text("(0)"))
    MustInputFreeitem5 = Column(Integer, server_default=text("(0)"))
    MustInputFreeitem4 = Column(Integer, server_default=text("(0)"))
    MustInputFreeitem9 = Column(Integer, server_default=text("(0)"))
    MustInputFreeitem1 = Column(Integer, server_default=text("(0)"))
    MustInputFreeitem8 = Column(Integer, server_default=text("(0)"))
    MustInputFreeitem0 = Column(Integer, server_default=text("(0)"))
    produceBatch = Column(Numeric(28, 14))
    imageFile = Column(Unicode(500))
    priuserdefnvc1 = Column(Unicode(500))
    priuserdefdecm1 = Column(Numeric(28, 14))
    priuserdefnvc2 = Column(Unicode(500))
    priuserdefdecm2 = Column(Numeric(28, 14))
    priuserdefnvc3 = Column(Unicode(500))
    priuserdefdecm3 = Column(Numeric(28, 14))
    priuserdefnvc4 = Column(Unicode(500))
    priuserdefdecm4 = Column(Numeric(28, 14))
    priuserdefnvc5 = Column(Unicode(500))
    priuserdefdecm5 = Column(Numeric(28, 14))
    standardturnoverdays = Column(Numeric(28, 14))
    HasEverChanged = Column(Unicode(32))
    pickbatch = Column(Numeric(28, 14))
    isphantom = Column(Integer)
    ControlRangeFreeitem0 = Column(Integer)
    ControlRangeFreeitem1 = Column(Integer)
    ControlRangeFreeitem2 = Column(Integer)
    ControlRangeFreeitem3 = Column(Integer)
    ControlRangeFreeitem4 = Column(Integer)
    ControlRangeFreeitem5 = Column(Integer)
    ControlRangeFreeitem6 = Column(Integer)
    ControlRangeFreeitem7 = Column(Integer)
    ControlRangeFreeitem8 = Column(Integer)
    ControlRangeFreeitem9 = Column(Integer)
    IsLaborCost = Column(Integer)
    BatchRunNumber = Column(Numeric(18, 0))
    IsNew = Column(Integer)
    MadeRecordDate = Column(DateTime)
    InventoryDescript = Column(Unicode(500))
    ReNewGoodSellDays = Column(Integer)
    ReNewGoodAheadDays = Column(Integer)
    IsSuite = Column(Integer)
    IsWeigh = Column(Integer)
    DefaultBarCode = Column(Unicode(200))
    NewProductPeriod = Column(Integer)
    Expired = Column(Integer)
    idbarcodesolution = Column(Integer)
    id = Column(Integer, primary_key=True)
    idinventoryclass = Column(Integer)
    idinvlocation = Column(Integer)
    idMarketingOrgan = Column(Integer)
    idpartner = Column(Integer)
    idunit = Column(Integer)
    idunitbymanufacture = Column(Integer)
    idUnitByPurchase = Column(Integer)
    idUnitByRetail = Column(Integer)
    idUnitBySale = Column(Integer)
    idUnitByStock = Column(Integer)
    idunitgroup = Column(Integer)
    idSubUnitByReport = Column(Integer)
    ExpiredUnit = Column(Integer)
    idwarehouse = Column(Integer)
    customerReplenishmentRule = Column(Integer)
    pickbatchmethod = Column(Integer)
    planattribute = Column(Integer)
    productInfo = Column(Integer)
    storeReplenishmentRule = Column(Integer)
    taxRate = Column(Integer)
    unittype = Column(Integer)
    valueType = Column(Integer)
    madeDate = Column(DateTime)
    updated = Column(DateTime)
    createdTime = Column(DateTime)
    Creater = Column(Unicode(200), server_default=text("(NULL)"))
    Changer = Column(Unicode(200), server_default=text("(NULL)"))
    Changedate = Column(DateTime, server_default=text("(NULL)"))


t_AA_InventoryBarCode = Table(
    'AA_InventoryBarCode', metadata,
    Column('code', Unicode(200)),
    Column('name', Unicode(200)),
    Column('barCode', Unicode(128)),
    Column('quantity', Numeric(28, 14)),
    Column('ts', TIMESTAMP),
    Column('updatedBy', Unicode(32)),
    Column('freeItem0', Unicode(300)),
    Column('freeItem1', Unicode(300)),
    Column('freeItem2', Unicode(300)),
    Column('freeItem3', Unicode(300)),
    Column('freeItem4', Unicode(300)),
    Column('freeItem5', Unicode(300)),
    Column('freeItem6', Unicode(300)),
    Column('freeItem7', Unicode(300)),
    Column('freeItem8', Unicode(300)),
    Column('freeItem9', Unicode(300)),
    Column('batchNumber', Unicode(50)),
    Column('detail_priuserdefdecm1', Numeric(28, 14)),
    Column('detail_priuserdefdecm2', Numeric(28, 14)),
    Column('detail_priuserdefdecm3', Numeric(28, 14)),
    Column('detail_priuserdefdecm4', Numeric(28, 14)),
    Column('detail_priuserdefnvc1', Unicode(60)),
    Column('detail_priuserdefnvc2', Unicode(60)),
    Column('detail_priuserdefnvc3', Unicode(60)),
    Column('detail_priuserdefnvc4', Unicode(60)),
    Column('detail_pubuserdefdecm1', Numeric(28, 14)),
    Column('detail_pubuserdefdecm2', Numeric(28, 14)),
    Column('detail_pubuserdefdecm3', Numeric(28, 14)),
    Column('detail_pubuserdefdecm4', Numeric(28, 14)),
    Column('detail_pubuserdefnvc1', Unicode(60)),
    Column('detail_pubuserdefnvc2', Unicode(60)),
    Column('detail_pubuserdefnvc3', Unicode(60)),
    Column('detail_pubuserdefnvc4', Unicode(60)),
    Column('detail_amount', Numeric(28, 14)),
    Column('detail_price', Numeric(28, 14)),
    Column('head_priuserdefdecm1', Numeric(28, 14)),
    Column('head_priuserdefdecm2', Numeric(28, 14)),
    Column('head_priuserdefdecm3', Numeric(28, 14)),
    Column('head_priuserdefdecm4', Numeric(28, 14)),
    Column('head_priuserdefdecm5', Numeric(28, 14)),
    Column('head_priuserdefdecm6', Numeric(28, 14)),
    Column('head_priuserdefnvc1', Unicode(60)),
    Column('head_priuserdefnvc2', Unicode(60)),
    Column('head_priuserdefnvc3', Unicode(60)),
    Column('head_priuserdefnvc4', Unicode(60)),
    Column('head_priuserdefnvc5', Unicode(60)),
    Column('head_priuserdefnvc6', Unicode(60)),
    Column('head_pubuserdefdecm1', Numeric(28, 14)),
    Column('head_pubuserdefdecm2', Numeric(28, 14)),
    Column('head_pubuserdefdecm3', Numeric(28, 14)),
    Column('head_pubuserdefdecm4', Numeric(28, 14)),
    Column('head_pubuserdefdecm5', Numeric(28, 14)),
    Column('head_pubuserdefdecm6', Numeric(28, 14)),
    Column('head_pubuserdefnvc1', Unicode(60)),
    Column('head_pubuserdefnvc2', Unicode(60)),
    Column('head_pubuserdefnvc3', Unicode(60)),
    Column('head_pubuserdefnvc4', Unicode(60)),
    Column('head_pubuserdefnvc5', Unicode(60)),
    Column('head_pubuserdefnvc6', Unicode(60)),
    Column('IsDefault', Integer),
    Column('iddepartment', Integer),
    Column('idinventoryDTO', Integer),
    Column('id', Integer, nullable=False),
    Column('idcustomer', Integer),
    Column('idpartner', Integer),
    Column('idperson', Integer),
    Column('idunit', Integer),
    Column('idwarehouse', Integer),
    Column('madeDate', DateTime),
    Column('updated', DateTime),
    Column('createdTime', DateTime),
    Column('failDate', DateTime),
    Column('ProductionDate', DateTime)
)


t_AA_InventoryClass = Table(
    'AA_InventoryClass', metadata,
    Column('code', Unicode(32)),
    Column('name', Unicode(200)),
    Column('isEndNode', Integer),
    Column('depth', Integer),
    Column('disabled', Integer),
    Column('ts', TIMESTAMP),
    Column('updatedBy', Unicode(32)),
    Column('inId', Unicode(560)),
    Column('id', Integer, nullable=False),
    Column('idMarketingOrgan', Integer),
    Column('idparent', Integer),
    Column('madeDate', DateTime),
    Column('updated', DateTime),
    Column('createdTime', DateTime)
)


t_AA_InventoryCountLevelPrice = Table(
    'AA_InventoryCountLevelPrice', metadata,
    Column('name', Unicode(200)),
    Column('code', Unicode(50)),
    Column('sellPrice', Numeric(18, 0)),
    Column('countLowerLimit', Numeric(28, 14)),
    Column('countUpperLimit', Numeric(28, 14)),
    Column('price', Unicode(1000)),
    Column('priceFormula', Unicode(1000)),
    Column('Updated', DateTime),
    Column('UpdatedBy', Unicode(50)),
    Column('ts', TIMESTAMP, nullable=False),
    Column('InvBarCode', Unicode(128)),
    Column('idInventory', Integer),
    Column('id', Integer, nullable=False),
    Column('idInventoryprice', Integer),
    Column('idUnit', Integer)
)


t_AA_InventoryLocation = Table(
    'AA_InventoryLocation', metadata,
    Column('code', Unicode(32)),
    Column('name', Unicode(200)),
    Column('shorthand', Unicode(50)),
    Column('isEndNode', Integer),
    Column('depth', Integer),
    Column('memo', Unicode(50)),
    Column('disabled', Integer),
    Column('ts', TIMESTAMP),
    Column('updatedBy', Unicode(32)),
    Column('inId', Unicode(560)),
    Column('id', Integer, nullable=False),
    Column('idparent', Integer),
    Column('idwarehouse', Integer),
    Column('madeDate', DateTime),
    Column('updated', DateTime),
    Column('createdTime', DateTime)
)


t_AA_InventoryMutiCode = Table(
    'AA_InventoryMutiCode', metadata,
    Column('Updated', DateTime),
    Column('UpdatedBy', Unicode(50)),
    Column('name', Unicode(300)),
    Column('code', Unicode(300)),
    Column('CusInSaleCount', Unicode(20)),
    Column('ts', TIMESTAMP, nullable=False),
    Column('idinventory', Integer),
    Column('id', Integer, nullable=False),
    Column('idcustomer', Integer),
    Column('idunit', Integer)
)


class AAInventoryPrice(Base):
    __tablename__ = 'AA_InventoryPrice'

    code = Column(Unicode(32))
    name = Column(Unicode(200))
    retailPrice = Column(Unicode(1000))
    invMPCost = Column(Unicode(1000))
    invLSPrice = Column(Unicode(1000))
    latestPPrice = Column(Numeric(32, 15))
    latestSalePrice = Column(Numeric(32, 15))
    invSCost1 = Column(Unicode(1000))
    invSCost2 = Column(Unicode(1000))
    invSCost3 = Column(Unicode(1000))
    invSCost4 = Column(Unicode(1000))
    invSCost5 = Column(Unicode(1000))
    ts = Column(TIMESTAMP)
    updatedBy = Column(Unicode(32))
    retailPriceFormula = Column(Unicode(1000))
    invSCost1Formula = Column(Unicode(1000))
    invSCost2Formula = Column(Unicode(1000))
    invSCost3Formula = Column(Unicode(1000))
    invSCost4Formula = Column(Unicode(1000))
    invSCost5Formula = Column(Unicode(1000))
    invSCost6 = Column(Unicode(1000))
    invSCost6Formula = Column(Unicode(1000))
    invSCost7 = Column(Unicode(1000))
    invSCost7Formula = Column(Unicode(1000))
    invSCost8 = Column(Unicode(1000))
    invSCost8Formula = Column(Unicode(1000))
    invSCost9 = Column(Unicode(1000))
    invSCost9Formula = Column(Unicode(1000))
    invSCost10 = Column(Unicode(1000))
    invSCost10Formula = Column(Unicode(1000))
    invLSPriceFormula = Column(Unicode(1000))
    invMPCostFormula = Column(Unicode(1000))
    latestoutsourcedprice = Column(Numeric(28, 14))
    highestoutsourcedprice = Column(Numeric(28, 14))
    Discount = Column(Numeric(32, 15))
    MarkupRate = Column(Numeric(32, 15))
    MemberPrice = Column(Numeric(32, 15))
    retailPriceNew = Column(Numeric(32, 15))
    PriceKey = Column(Unicode(34))
    InvBarCode = Column(Unicode(128))
    idinventory = Column(Integer)
    id = Column(Integer, primary_key=True)
    idpricetrace = Column(Integer)
    idunit = Column(Integer)
    updated = Column(DateTime)


t_AA_InventoryPriceForNumeric = Table(
    'AA_InventoryPriceForNumeric', metadata,
    Column('id', Integer, nullable=False),
    Column('retailPrice', Unicode(1000)),
    Column('invMPCost', Unicode(1000)),
    Column('invLSPrice', Unicode(1000)),
    Column('latestPPrice', Numeric(32, 15)),
    Column('latestSalePrice', Numeric(32, 15)),
    Column('invSCost1', Unicode(1000)),
    Column('invSCost2', Unicode(1000)),
    Column('invSCost3', Unicode(1000)),
    Column('invSCost4', Unicode(1000)),
    Column('invSCost5', Unicode(1000)),
    Column('invSCost6', Unicode(1000)),
    Column('invSCost7', Unicode(1000)),
    Column('invSCost8', Unicode(1000)),
    Column('invSCost9', Unicode(1000)),
    Column('invSCost10', Unicode(1000)),
    Column('Discount', Numeric(32, 15)),
    Column('MarkupRate', Numeric(32, 15)),
    Column('MemberPrice', Numeric(32, 15)),
    Column('retailPriceNew', Numeric(32, 15)),
    Column('idinventory', Integer),
    Column('codeinventory', Unicode(32)),
    Column('idunit', Integer),
    Column('codeunit', Unicode(32))
)


t_AA_InventoryPriceTrace = Table(
    'AA_InventoryPriceTrace', metadata,
    Column('code', Unicode(32)),
    Column('name', Unicode(200)),
    Column('LatestPPrice', Numeric(32, 15)),
    Column('LatestSalePrice', Numeric(32, 15)),
    Column('ts', TIMESTAMP),
    Column('updatedBy', Unicode(32)),
    Column('idinventory', Integer, nullable=False, server_default=text("((0))")),
    Column('id', Integer, nullable=False),
    Column('idunit', Integer, nullable=False, server_default=text("((0))")),
    Column('createdtime', DateTime),
    Column('updated', DateTime)
)


t_AA_InventoryUnitPrice = Table(
    'AA_InventoryUnitPrice', metadata,
    Column('code', Unicode(32)),
    Column('name', Unicode(200)),
    Column('invMPCost', Numeric(28, 14)),
    Column('invLSPrice', Numeric(28, 14)),
    Column('retailPrice', Numeric(28, 14)),
    Column('latestPPrice', Numeric(28, 14)),
    Column('latestSalePrice', Numeric(28, 14)),
    Column('invSCost1', Numeric(28, 14)),
    Column('invSCost2', Numeric(28, 14)),
    Column('invSCost3', Numeric(28, 14)),
    Column('invSCost4', Numeric(28, 14)),
    Column('invSCost5', Numeric(28, 14)),
    Column('ts', TIMESTAMP),
    Column('updatedBy', Unicode(32)),
    Column('latestSaleDiscount', Numeric(28, 14)),
    Column('latestUnitSalePrice', Numeric(28, 14)),
    Column('latestUnitTaxSalePrice', Numeric(28, 14)),
    Column('highestoutsourcedprice', Numeric(28, 14)),
    Column('latestoutsourcedprice', Numeric(28, 14)),
    Column('rateOfExchange', Numeric(28, 14)),
    Column('rateDescription', Unicode(200)),
    Column('MarkupRate', Numeric(28, 14)),
    Column('Discount', Numeric(28, 14)),
    Column('InvSCost6', Numeric(28, 14)),
    Column('InvSCost7', Numeric(28, 14)),
    Column('InvSCost8', Numeric(28, 14)),
    Column('InvSCost9', Numeric(28, 14)),
    Column('InvSCost10', Numeric(28, 14)),
    Column('idinventory', Integer, nullable=False, server_default=text("((0))")),
    Column('id', Integer, nullable=False),
    Column('idunit', Integer, nullable=False, server_default=text("((0))")),
    Column('idunitgroup', Integer),
    Column('madeDate', DateTime),
    Column('updated', DateTime),
    Column('createdTime', DateTime),
    Column('isGroup', Integer)
)


t_AA_Inventory_MultiUnit = Table(
    'AA_Inventory_MultiUnit', metadata,
    Column('Unit1Code', Unicode(50)),
    Column('Unit1Name', Unicode(200)),
    Column('Unit1ChangeRate', Numeric(28, 14)),
    Column('Unit2Code', Unicode(50)),
    Column('Unit2Name', Unicode(200)),
    Column('Unit2ChangeRate', Numeric(28, 14)),
    Column('Unit3Code', Unicode(50)),
    Column('Unit3Name', Unicode(200)),
    Column('Unit3ChangeRate', Numeric(28, 14)),
    Column('Unit4Code', Unicode(50)),
    Column('Unit4Name', Unicode(200)),
    Column('Unit4ChangeRate', Numeric(28, 14)),
    Column('TS', TIMESTAMP, nullable=False),
    Column('IDInventory', Integer, nullable=False, server_default=text("((0))")),
    Column('IDUnit1', Integer),
    Column('IDUnit2', Integer),
    Column('IDUnit3', Integer),
    Column('IDUnit4', Integer)
)


t_AA_MarketingOrgan = Table(
    'AA_MarketingOrgan', metadata,
    Column('Updated', DateTime),
    Column('UpdatedBy', Unicode(32)),
    Column('ts', TIMESTAMP),
    Column('Code', Unicode(60)),
    Column('Name', Unicode(100)),
    Column('InId', Unicode(1120)),
    Column('Depth', Integer),
    Column('IsEndNode', Integer),
    Column('disabled', Integer),
    Column('IsHeaderQuaters', Integer),
    Column('id', Integer, nullable=False),
    Column('idHeaderDepartment', Integer),
    Column('idParent', Integer),
    Column('madeDate', DateTime)
)


t_AA_MarketingOrgan_Ext = Table(
    'AA_MarketingOrgan_Ext', metadata,
    Column('MarketingOrgancode_lev1', Unicode(80)),
    Column('MarketingOrganname_lev1', Unicode(400)),
    Column('MarketingOrgancode_lev2', Unicode(80)),
    Column('MarketingOrganname_lev2', Unicode(400)),
    Column('MarketingOrgancode_lev3', Unicode(80)),
    Column('MarketingOrganname_lev3', Unicode(400)),
    Column('MarketingOrgancode_lev4', Unicode(80)),
    Column('MarketingOrganname_lev4', Unicode(400)),
    Column('MarketingOrgancode_lev5', Unicode(80)),
    Column('MarketingOrganname_lev5', Unicode(400)),
    Column('MarketingOrgancode_lev6', Unicode(80)),
    Column('MarketingOrganname_lev6', Unicode(400)),
    Column('MarketingOrgancode_lev7', Unicode(80)),
    Column('MarketingOrganname_lev7', Unicode(400)),
    Column('MarketingOrgancode_lev8', Unicode(80)),
    Column('MarketingOrganname_lev8', Unicode(400)),
    Column('MarketingOrgancode_lev9', Unicode(80)),
    Column('MarketingOrganname_lev9', Unicode(400)),
    Column('MarketingOrgancode_lev10', Unicode(80)),
    Column('MarketingOrganname_lev10', Unicode(400)),
    Column('MarketingOrgancode_lev11', Unicode(80)),
    Column('MarketingOrganname_lev11', Unicode(400)),
    Column('MarketingOrgancode_lev12', Unicode(80)),
    Column('MarketingOrganname_lev12', Unicode(400)),
    Column('MarketingOrgancode_lev13', Unicode(80)),
    Column('MarketingOrganname_lev13', Unicode(400)),
    Column('MarketingOrgancode_lev14', Unicode(80)),
    Column('MarketingOrganname_lev14', Unicode(400)),
    Column('MarketingOrgancode_lev15', Unicode(80)),
    Column('MarketingOrganname_lev15', Unicode(400)),
    Column('depth', Unicode(20)),
    Column('ts', TIMESTAMP),
    Column('MarketingOrganid_lev1', Integer),
    Column('MarketingOrganid_lev10', Integer),
    Column('MarketingOrganid_lev11', Integer),
    Column('MarketingOrganid_lev12', Integer),
    Column('MarketingOrganid_lev13', Integer),
    Column('MarketingOrganid_lev14', Integer),
    Column('MarketingOrganid_lev15', Integer),
    Column('MarketingOrganid_lev2', Integer),
    Column('MarketingOrganid_lev3', Integer),
    Column('MarketingOrganid_lev4', Integer),
    Column('MarketingOrganid_lev5', Integer),
    Column('MarketingOrganid_lev6', Integer),
    Column('MarketingOrganid_lev7', Integer),
    Column('MarketingOrganid_lev8', Integer),
    Column('MarketingOrganid_lev9', Integer),
    Column('id', Integer),
    Column('createTime', DateTime)
)


t_AA_OutSourcedPriceSource = Table(
    'AA_OutSourcedPriceSource', metadata,
    Column('code', Unicode(30)),
    Column('name', Unicode(200)),
    Column('priorityLevel', Integer),
    Column('isInUse', Integer),
    Column('sequencenumber', Integer),
    Column('ts', TIMESTAMP, nullable=False),
    Column('updatedBy', Unicode(32)),
    Column('id', Integer, nullable=False),
    Column('idPriceStrategyDTO', Integer),
    Column('createdtime', DateTime),
    Column('updated', DateTime)
)


t_AA_OutsourcedVendorInventoryPrice = Table(
    'AA_OutsourcedVendorInventoryPrice', metadata,
    Column('code', Unicode(30)),
    Column('name', Unicode(200)),
    Column('sequencenumber', Integer),
    Column('ts', TIMESTAMP, nullable=False),
    Column('updatedBy', Unicode(32)),
    Column('AgreementPrice', Numeric(28, 14)),
    Column('HighestOutsourcedPrice', Numeric(28, 14)),
    Column('LatestOutresourcedPrice', Numeric(28, 14)),
    Column('idinventory', Integer),
    Column('id', Integer, nullable=False),
    Column('idpricetrace', Integer),
    Column('idOutsourcedVendorPriceStrategyDTO', Integer),
    Column('idpartner', Integer),
    Column('idunit', Integer),
    Column('createdtime', DateTime),
    Column('updated', DateTime)
)


t_AA_OutsourcedVendorInventoryPriceTrace = Table(
    'AA_OutsourcedVendorInventoryPriceTrace', metadata,
    Column('code', Unicode(30)),
    Column('name', Unicode(200)),
    Column('lastprice', Numeric(28, 14)),
    Column('discount', Numeric(28, 14)),
    Column('unitprice', Numeric(28, 14)),
    Column('unittaxprice', Numeric(28, 14)),
    Column('sequencenumber', Integer),
    Column('ts', TIMESTAMP, nullable=False),
    Column('updatedBy', Unicode(32)),
    Column('idinventory', Integer),
    Column('id', Integer, nullable=False),
    Column('idOutSourcedVender', Integer),
    Column('idunit', Integer),
    Column('createdtime', DateTime),
    Column('updated', DateTime)
)


t_AA_OutsourcedVendorPriceStrategy = Table(
    'AA_OutsourcedVendorPriceStrategy', metadata,
    Column('code', Unicode(30)),
    Column('name', Unicode(200)),
    Column('sequencenumber', Integer),
    Column('ts', TIMESTAMP, nullable=False),
    Column('updatedBy', Unicode(32)),
    Column('id', Integer, nullable=False),
    Column('createdtime', DateTime),
    Column('updated', DateTime)
)


class AAParentAccount(Base):
    __tablename__ = 'AA_ParentAccount'

    ts = Column(TIMESTAMP)
    updatedBy = Column(Unicode(32))
    updated = Column(String(19, u'Chinese_PRC_CI_AS'))
    name = Column(Unicode(200))
    code = Column(Unicode(32))
    Depth = Column(Integer)
    isEndNode = Column(Integer)
    id = Column(Integer, primary_key=True)
    idParent = Column(Integer)
    idSon = Column(Integer)


t_AA_ParentAssetClass = Table(
    'AA_ParentAssetClass', metadata,
    Column('ts', TIMESTAMP),
    Column('updatedBy', Unicode(32)),
    Column('updated', String(19, u'Chinese_PRC_CI_AS')),
    Column('name', Unicode(100)),
    Column('code', Unicode(32)),
    Column('Depth', Integer),
    Column('isEndNode', Integer),
    Column('id', Integer, nullable=False),
    Column('idParent', Integer),
    Column('idSon', Integer)
)


class AAParentCashFlowItemClass(Base):
    __tablename__ = 'AA_ParentCashFlowItemClass'

    ts = Column(TIMESTAMP)
    updatedBy = Column(Unicode(32))
    updated = Column(String(19, u'Chinese_PRC_CI_AS'))
    name = Column(Unicode(200))
    code = Column(Unicode(32))
    Depth = Column(Integer)
    isEndNode = Column(Integer)
    id = Column(Integer, primary_key=True)
    idParent = Column(Integer)
    idSon = Column(Integer)


class AAParentCommonSummaryClass(Base):
    __tablename__ = 'AA_ParentCommonSummaryClass'

    ts = Column(TIMESTAMP)
    updatedBy = Column(Unicode(32))
    updated = Column(String(19, u'Chinese_PRC_CI_AS'))
    name = Column(Unicode(200))
    code = Column(Unicode(32))
    Depth = Column(Integer)
    isEndNode = Column(Integer)
    idSon = Column(Integer)
    idParent = Column(Integer)
    id = Column(Integer, primary_key=True)


t_AA_ParentDepartment = Table(
    'AA_ParentDepartment', metadata,
    Column('ts', TIMESTAMP),
    Column('Depth', Integer),
    Column('isEndNode', Integer),
    Column('idParent', Integer),
    Column('idSon', Integer),
    Column('id', Integer, nullable=False)
)


t_AA_ParentDistrict = Table(
    'AA_ParentDistrict', metadata,
    Column('ts', TIMESTAMP),
    Column('Depth', Integer),
    Column('isEndNode', Integer),
    Column('idParent', Integer),
    Column('idSon', Integer),
    Column('id', Integer, nullable=False)
)


class AAParentExpenseItem(Base):
    __tablename__ = 'AA_ParentExpenseItem'

    ts = Column(TIMESTAMP)
    updatedBy = Column(Unicode(32))
    updated = Column(String(19, u'Chinese_PRC_CI_AS'))
    name = Column(Unicode(200))
    code = Column(Unicode(32))
    Depth = Column(Integer)
    isEndNode = Column(Integer)
    idParent = Column(Integer)
    idSon = Column(Integer)
    id = Column(Integer, primary_key=True)


t_AA_ParentHandleReason = Table(
    'AA_ParentHandleReason', metadata,
    Column('ts', TIMESTAMP),
    Column('updatedBy', Unicode(32)),
    Column('updated', String(19, u'Chinese_PRC_CI_AS')),
    Column('name', Unicode(100)),
    Column('code', Unicode(32)),
    Column('Depth', Integer),
    Column('isEndNode', Integer),
    Column('idParent', Integer),
    Column('idSon', Integer),
    Column('id', Integer, nullable=False)
)


t_AA_ParentIncDecWay = Table(
    'AA_ParentIncDecWay', metadata,
    Column('ts', TIMESTAMP),
    Column('updatedBy', Unicode(32)),
    Column('updated', String(19, u'Chinese_PRC_CI_AS')),
    Column('name', Unicode(100)),
    Column('code', Unicode(32)),
    Column('Depth', Integer),
    Column('isEndNode', Integer),
    Column('idParent', Integer),
    Column('idSon', Integer),
    Column('id', Integer, nullable=False)
)


class AAParentIncome(Base):
    __tablename__ = 'AA_ParentIncome'

    ts = Column(TIMESTAMP)
    updatedBy = Column(Unicode(32))
    updated = Column(String(19, u'Chinese_PRC_CI_AS'))
    name = Column(Unicode(200))
    code = Column(Unicode(32))
    Depth = Column(Integer)
    isEndNode = Column(Integer)
    idParent = Column(Integer)
    idSon = Column(Integer)
    id = Column(Integer, primary_key=True)


t_AA_ParentInventoryClass = Table(
    'AA_ParentInventoryClass', metadata,
    Column('ts', TIMESTAMP),
    Column('Depth', Integer),
    Column('isEndNode', Integer),
    Column('id', Integer, nullable=False),
    Column('idParent', Integer),
    Column('idSon', Integer)
)


t_AA_ParentInventoryLocation = Table(
    'AA_ParentInventoryLocation', metadata,
    Column('ts', TIMESTAMP),
    Column('Depth', Integer),
    Column('isEndNode', Integer),
    Column('idParent', Integer),
    Column('idSon', Integer),
    Column('id', Integer, nullable=False)
)


t_AA_ParentMarketingOrgan = Table(
    'AA_ParentMarketingOrgan', metadata,
    Column('ts', TIMESTAMP),
    Column('Depth', Integer),
    Column('isEndNode', Integer),
    Column('idParent', Integer),
    Column('idSon', Integer),
    Column('id', Integer, nullable=False)
)


t_AA_ParentPartnerClass = Table(
    'AA_ParentPartnerClass', metadata,
    Column('ts', TIMESTAMP),
    Column('Depth', Integer),
    Column('isEndNode', Integer),
    Column('id', Integer, nullable=False),
    Column('idParent', Integer),
    Column('idSon', Integer)
)


t_AA_ParentPosition = Table(
    'AA_ParentPosition', metadata,
    Column('ts', TIMESTAMP),
    Column('updatedBy', Unicode(32)),
    Column('updated', String(19, u'Chinese_PRC_CI_AS')),
    Column('name', Unicode(100)),
    Column('code', Unicode(32)),
    Column('Depth', Integer),
    Column('isEndNode', Integer),
    Column('id', Integer, nullable=False),
    Column('idParent', Integer),
    Column('idSon', Integer)
)


t_AA_ParentProjectClass = Table(
    'AA_ParentProjectClass', metadata,
    Column('ts', TIMESTAMP),
    Column('Depth', Integer),
    Column('isEndNode', Integer),
    Column('id', Integer, nullable=False),
    Column('idParent', Integer),
    Column('idSon', Integer)
)


t_AA_ParentRDStyle = Table(
    'AA_ParentRDStyle', metadata,
    Column('ts', TIMESTAMP),
    Column('Depth', Integer),
    Column('isEndNode', Integer),
    Column('id', Integer, nullable=False),
    Column('idParent', Integer),
    Column('idSon', Integer)
)


t_AA_ParentUseStatus = Table(
    'AA_ParentUseStatus', metadata,
    Column('ts', TIMESTAMP),
    Column('updatedBy', Unicode(32)),
    Column('updated', String(19, u'Chinese_PRC_CI_AS')),
    Column('name', Unicode(100)),
    Column('code', Unicode(32)),
    Column('Depth', Integer),
    Column('isEndNode', Integer),
    Column('id', Integer, nullable=False),
    Column('idParent', Integer),
    Column('idSon', Integer)
)


class AAPartner(Base):
    __tablename__ = 'AA_Partner'

    code = Column(Unicode(32))
    name = Column(Unicode(200))
    partnerAbbName = Column(Unicode(100))
    shortHand = Column(Unicode(100))
    representative = Column(Unicode(50))
    bankAccount = Column(Unicode(50))
    taxRegcode = Column(Unicode(50))
    saleCreditLine = Column(Numeric(28, 14))
    saleCreditDays = Column(Numeric(28, 14))
    purchaseCreditDays = Column(Numeric(28, 14))
    saleSpaceMonth = Column(Integer)
    saleCheckMonth = Column(Integer)
    saleCheckDate = Column(Integer)
    purchaseSpaceMonth = Column(Integer)
    purchaseCheckMonth = Column(Integer)
    purchaseCheckDate = Column(Integer)
    customeraddressphone = Column(Unicode(250))
    aRBalance = Column(Numeric(28, 14))
    aPBalance = Column(Numeric(28, 14))
    disabled = Column(Integer)
    ts = Column(TIMESTAMP)
    updatedBy = Column(Unicode(32))
    priuserdefnvc1 = Column(Unicode(500))
    priuserdefdecm1 = Column(Numeric(28, 14))
    priuserdefnvc2 = Column(Unicode(500))
    priuserdefdecm2 = Column(Numeric(28, 14))
    priuserdefnvc3 = Column(Unicode(500))
    priuserdefdecm3 = Column(Numeric(28, 14))
    priuserdefnvc4 = Column(Unicode(500))
    priuserdefdecm4 = Column(Numeric(28, 14))
    priuserdefnvc5 = Column(Unicode(500))
    priuserdefdecm5 = Column(Numeric(28, 14))
    isContainTaxOnPurchase = Column(Integer)
    HasEverChanged = Column(Unicode(32))
    codeSettlementPartner = Column(Unicode(32))
    AdvRBalance = Column(Numeric(28, 14))
    AdvPBalance = Column(Numeric(28, 14))
    addressJC = Column(Unicode(200))
    ShipmentAddress = Column(Unicode(200))
    Contact = Column(Unicode(50))
    MobilePhone = Column(Unicode(30))
    TelephoneNo = Column(Unicode(100))
    Fax = Column(Unicode(20))
    EmailAddr = Column(Unicode(100))
    QqNo = Column(Unicode(50))
    MsnAddress = Column(Unicode(50))
    UuNo = Column(Unicode(50))
    creditBalance = Column(Numeric(28, 14))
    extendedAccounts = Column(Numeric(28, 14))
    SellCustomer = Column(Integer)
    MadeRecordDate = Column(DateTime)
    Position = Column(String(50, u'Chinese_PRC_CI_AS'))
    RunShop = Column(Integer)
    CheckAddress = Column(Unicode(200))
    CustomerAddress = Column(Unicode(200))
    Birthday = Column(DateTime)
    AutoCreateMember = Column(Integer)
    id = Column(Integer, primary_key=True)
    idsaledepartment = Column(Integer)
    iddistrict = Column(Integer)
    idMarketingOrgan = Column(Integer)
    idPmarketingOrgan = Column(Integer)
    idsettlementPartner = Column(Integer)
    idpartnerclass = Column(Integer)
    idsaleman = Column(Integer)
    idMemberType = Column(Integer)
    accbank = Column(Integer)
    customerType = Column(Integer)
    partnerType = Column(Integer)
    priceGrade = Column(Integer)
    purchaseSettleStyle = Column(Integer)
    saleSettleStyle = Column(Integer)
    taxRate = Column(Integer)
    saleStartDate = Column(DateTime)
    purchaseStartDate = Column(DateTime)
    madeDate = Column(DateTime)
    updated = Column(DateTime)
    createdTime = Column(DateTime)


t_AA_PartnerAddress = Table(
    'AA_PartnerAddress', metadata,
    Column('code', Unicode(32)),
    Column('name', Unicode(200)),
    Column('contact', Unicode(50)),
    Column('telephoneNo', Unicode(100)),
    Column('fax', Unicode(20)),
    Column('emailAddr', Unicode(100)),
    Column('mobilePhone', Unicode(30)),
    Column('qqNo', Unicode(50)),
    Column('msnAddress', Unicode(50)),
    Column('uuNo', Unicode(50)),
    Column('shipmentAddress', Unicode(200)),
    Column('isDefaultAddress', Integer),
    Column('ts', TIMESTAMP),
    Column('updatedBy', Unicode(32)),
    Column('Position', Unicode(20)),
    Column('Birthday', DateTime),
    Column('idpartner', Integer),
    Column('id', Integer, nullable=False),
    Column('deliveryMode', Integer),
    Column('madeDate', DateTime),
    Column('updated', DateTime),
    Column('createdTime', DateTime)
)


t_AA_PartnerClass = Table(
    'AA_PartnerClass', metadata,
    Column('code', Unicode(32)),
    Column('name', Unicode(200)),
    Column('isEndNode', Integer),
    Column('depth', Integer),
    Column('disabled', Integer),
    Column('ts', TIMESTAMP),
    Column('updatedBy', Unicode(32)),
    Column('inId', Unicode(560)),
    Column('id', Integer, nullable=False),
    Column('IdMarketingOrgan', Integer),
    Column('idparent', Integer),
    Column('madeDate', DateTime),
    Column('updated', DateTime),
    Column('createdTime', DateTime)
)


t_AA_PartnerClassPriceTrace = Table(
    'AA_PartnerClassPriceTrace', metadata,
    Column('code', Unicode(32)),
    Column('name', Unicode(200)),
    Column('lastprice', Numeric(32, 15)),
    Column('discount', Numeric(32, 15)),
    Column('unitprice', Numeric(32, 15)),
    Column('unittaxprice', Numeric(32, 15)),
    Column('ts', TIMESTAMP),
    Column('updatedBy', Unicode(32)),
    Column('idinventory', Integer, nullable=False, server_default=text("((0))")),
    Column('idPartnerClass', Integer, nullable=False, server_default=text("((0))")),
    Column('id', Integer, nullable=False),
    Column('idunit', Integer, nullable=False, server_default=text("((0))")),
    Column('createdtime', DateTime),
    Column('updated', DateTime)
)


t_AA_PartnerInventory = Table(
    'AA_PartnerInventory', metadata,
    Column('code', Unicode(32)),
    Column('name', Unicode(200)),
    Column('partnerInvenCode', Unicode(100)),
    Column('ts', TIMESTAMP),
    Column('updatedBy', Unicode(32)),
    Column('freeItem0', Unicode(300)),
    Column('freeItem1', Unicode(300)),
    Column('freeItem2', Unicode(300)),
    Column('freeItem3', Unicode(300)),
    Column('freeItem4', Unicode(300)),
    Column('freeItem5', Unicode(300)),
    Column('freeItem6', Unicode(300)),
    Column('freeItem7', Unicode(300)),
    Column('freeItem8', Unicode(300)),
    Column('freeItem9', Unicode(300)),
    Column('id', Integer, nullable=False),
    Column('idinventory', Integer),
    Column('idpartner', Integer),
    Column('madeDate', DateTime),
    Column('updated', DateTime)
)


t_AA_Person = Table(
    'AA_Person', metadata,
    Column('code', Unicode(32)),
    Column('name', Unicode(200)),
    Column('shorthand', Unicode(50)),
    Column('nativePlace', Unicode(30)),
    Column('identityNo', Unicode(20)),
    Column('familyPhoneNo', Unicode(100)),
    Column('officePhoneNo', Unicode(100)),
    Column('mobilePhoneNo', Unicode(20)),
    Column('emailAddr', Unicode(100)),
    Column('qqcode', Unicode(30)),
    Column('msnAddr', Unicode(30)),
    Column('uuNo', Unicode(30)),
    Column('postCode', Unicode(50)),
    Column('postAddr', Unicode(200)),
    Column('isSalesman', Integer),
    Column('creditDate', Numeric(28, 14)),
    Column('creditQuantity', Numeric(28, 14)),
    Column('aRBalance', Numeric(28, 14)),
    Column('aPBalance', Numeric(28, 14)),
    Column('disabled', Integer),
    Column('ts', TIMESTAMP),
    Column('updatedBy', Unicode(32)),
    Column('priuserdefnvc1', Unicode(500)),
    Column('priuserdefdecm1', Numeric(28, 14)),
    Column('priuserdefnvc2', Unicode(500)),
    Column('priuserdefdecm2', Numeric(28, 14)),
    Column('priuserdefnvc3', Unicode(500)),
    Column('priuserdefdecm3', Numeric(28, 14)),
    Column('priuserdefnvc4', Unicode(500)),
    Column('priuserdefdecm4', Numeric(28, 14)),
    Column('priuserdefnvc5', Unicode(500)),
    Column('priuserdefdecm5', Numeric(28, 14)),
    Column('IsNavigator', Integer),
    Column('IsOperator', Integer),
    Column('id', Integer, nullable=False),
    Column('iddepartment', Integer),
    Column('idMarketingOrgan', Integer),
    Column('education', Integer),
    Column('gender', Integer),
    Column('identificationType', Integer),
    Column('position', Integer),
    Column('birthday', DateTime),
    Column('madeDate', DateTime),
    Column('updated', DateTime),
    Column('createdTime', DateTime)
)


class AAPosition(Base):
    __tablename__ = 'AA_Position'

    code = Column(Unicode(30))
    name = Column(Unicode(100))
    depth = Column(Integer)
    isendnode = Column(Integer)
    inid = Column(Unicode(750))
    ts = Column(TIMESTAMP, nullable=False)
    updated = Column(String(19, u'Chinese_PRC_CI_AS'))
    updatedBy = Column(Unicode(32))
    createdTime = Column(String(19, u'Chinese_PRC_CI_AS'))
    id = Column(Integer, primary_key=True)
    idparent = Column(Integer)


t_AA_Position_Ext = Table(
    'AA_Position_Ext', metadata,
    Column('positioncode_lev1', Unicode(40)),
    Column('positionname_lev1', Unicode(100)),
    Column('positioncode_lev2', Unicode(40)),
    Column('positionname_lev2', Unicode(100)),
    Column('positioncode_lev3', Unicode(40)),
    Column('positionname_lev3', Unicode(100)),
    Column('positioncode_lev4', Unicode(40)),
    Column('positionname_lev4', Unicode(100)),
    Column('positioncode_lev5', Unicode(40)),
    Column('positionname_lev5', Unicode(100)),
    Column('positioncode_lev6', Unicode(40)),
    Column('positionname_lev6', Unicode(100)),
    Column('positioncode_lev7', Unicode(40)),
    Column('positionname_lev7', Unicode(100)),
    Column('positioncode_lev8', Unicode(40)),
    Column('positionname_lev8', Unicode(100)),
    Column('positioncode_lev9', Unicode(40)),
    Column('positionname_lev9', Unicode(100)),
    Column('positioncode_lev10', Unicode(40)),
    Column('positionname_lev10', Unicode(100)),
    Column('positioncode_lev11', Unicode(40)),
    Column('positionname_lev11', Unicode(100)),
    Column('positioncode_lev12', Unicode(40)),
    Column('positionname_lev12', Unicode(100)),
    Column('positioncode_lev13', Unicode(40)),
    Column('positionname_lev13', Unicode(100)),
    Column('positioncode_lev14', Unicode(40)),
    Column('positionname_lev14', Unicode(100)),
    Column('positioncode_lev15', Unicode(40)),
    Column('positionname_lev15', Unicode(100)),
    Column('depth', Unicode(10)),
    Column('createTime', String(19, u'Chinese_PRC_CI_AS')),
    Column('ts', TIMESTAMP),
    Column('id', Integer),
    Column('positionid_lev1', Integer),
    Column('positionid_lev10', Integer),
    Column('positionid_lev11', Integer),
    Column('positionid_lev12', Integer),
    Column('positionid_lev13', Integer),
    Column('positionid_lev14', Integer),
    Column('positionid_lev15', Integer),
    Column('positionid_lev2', Integer),
    Column('positionid_lev3', Integer),
    Column('positionid_lev4', Integer),
    Column('positionid_lev5', Integer),
    Column('positionid_lev6', Integer),
    Column('positionid_lev7', Integer),
    Column('positionid_lev8', Integer),
    Column('positionid_lev9', Integer)
)


t_AA_PriceStrategy = Table(
    'AA_PriceStrategy', metadata,
    Column('code', Unicode(32)),
    Column('name', Unicode(200)),
    Column('ts', TIMESTAMP),
    Column('updatedBy', Unicode(32)),
    Column('id', Integer, nullable=False),
    Column('createdtime', DateTime),
    Column('updated', DateTime)
)


t_AA_PriceTrace = Table(
    'AA_PriceTrace', metadata,
    Column('code', Unicode(32)),
    Column('name', Unicode(200)),
    Column('lastprice', Numeric(32, 15)),
    Column('discount', Numeric(32, 15)),
    Column('unitprice', Numeric(32, 15)),
    Column('unittaxprice', Numeric(32, 15)),
    Column('pricesource', Unicode(50)),
    Column('ts', TIMESTAMP),
    Column('updatedBy', Unicode(32)),
    Column('id', Integer, nullable=False),
    Column('updated', DateTime)
)


t_AA_ProductProcess = Table(
    'AA_ProductProcess', metadata,
    Column('code', Unicode(30)),
    Column('name', Unicode(200)),
    Column('memo', Unicode(200)),
    Column('disabled', Integer),
    Column('sequencenumber', Integer),
    Column('ts', TIMESTAMP, nullable=False),
    Column('updatedBy', Unicode(32)),
    Column('priuserdefnvc1', Unicode(500)),
    Column('priuserdefdecm1', Numeric(28, 14)),
    Column('priuserdefnvc2', Unicode(500)),
    Column('priuserdefdecm2', Numeric(28, 14)),
    Column('priuserdefnvc3', Unicode(500)),
    Column('priuserdefdecm3', Numeric(28, 14)),
    Column('priuserdefnvc4', Unicode(500)),
    Column('priuserdefdecm4', Numeric(28, 14)),
    Column('priuserdefnvc5', Unicode(500)),
    Column('priuserdefdecm5', Numeric(28, 14)),
    Column('idworkshop', Integer),
    Column('id', Integer, nullable=False),
    Column('createdtime', DateTime),
    Column('updated', DateTime)
)


t_AA_Project = Table(
    'AA_Project', metadata,
    Column('Updated', DateTime),
    Column('UpdatedBy', Unicode(32)),
    Column('ts', TIMESTAMP, nullable=False),
    Column('Code', Unicode(30), nullable=False),
    Column('Name', Unicode(50), nullable=False),
    Column('disabled', Integer, nullable=False),
    Column('idMarketingOrgan', Integer),
    Column('id', Integer, nullable=False),
    Column('idclass', Integer),
    Column('madeDate', DateTime)
)


t_AA_ProjectClass = Table(
    'AA_ProjectClass', metadata,
    Column('Updated', DateTime),
    Column('UpdatedBy', Unicode(32)),
    Column('ts', TIMESTAMP, nullable=False),
    Column('Code', Unicode(30), nullable=False),
    Column('Name', Unicode(50), nullable=False),
    Column('disabled', Integer, nullable=False),
    Column('InId', Unicode(560)),
    Column('IsEndNode', Integer),
    Column('depth', Integer),
    Column('id', Integer, nullable=False),
    Column('idparent', Integer),
    Column('madeDate', DateTime)
)


t_AA_ProjectClass_Ext = Table(
    'AA_ProjectClass_Ext', metadata,
    Column('ProjectClasscode_lev1', Unicode(40)),
    Column('ProjectClassname_lev1', Unicode(200)),
    Column('ProjectClasscode_lev2', Unicode(40)),
    Column('ProjectClassname_lev2', Unicode(200)),
    Column('ProjectClasscode_lev3', Unicode(40)),
    Column('ProjectClassname_lev3', Unicode(200)),
    Column('ProjectClasscode_lev4', Unicode(40)),
    Column('ProjectClassname_lev4', Unicode(200)),
    Column('ProjectClasscode_lev5', Unicode(40)),
    Column('ProjectClassname_lev5', Unicode(200)),
    Column('ProjectClasscode_lev6', Unicode(40)),
    Column('ProjectClassname_lev6', Unicode(200)),
    Column('ProjectClasscode_lev7', Unicode(40)),
    Column('ProjectClassname_lev7', Unicode(200)),
    Column('ProjectClasscode_lev8', Unicode(40)),
    Column('ProjectClassname_lev8', Unicode(200)),
    Column('ProjectClasscode_lev9', Unicode(40)),
    Column('ProjectClassname_lev9', Unicode(200)),
    Column('ProjectClasscode_lev10', Unicode(40)),
    Column('ProjectClassname_lev10', Unicode(200)),
    Column('ProjectClasscode_lev11', Unicode(40)),
    Column('ProjectClassname_lev11', Unicode(200)),
    Column('ProjectClasscode_lev12', Unicode(40)),
    Column('ProjectClassname_lev12', Unicode(200)),
    Column('ProjectClasscode_lev13', Unicode(40)),
    Column('ProjectClassname_lev13', Unicode(200)),
    Column('ProjectClasscode_lev14', Unicode(40)),
    Column('ProjectClassname_lev14', Unicode(200)),
    Column('ProjectClasscode_lev15', Unicode(40)),
    Column('ProjectClassname_lev15', Unicode(200)),
    Column('depth', Unicode(10)),
    Column('ts', TIMESTAMP),
    Column('id', Integer),
    Column('ProjectClassid_lev1', Integer),
    Column('ProjectClassid_lev10', Integer),
    Column('ProjectClassid_lev11', Integer),
    Column('ProjectClassid_lev12', Integer),
    Column('ProjectClassid_lev13', Integer),
    Column('ProjectClassid_lev14', Integer),
    Column('ProjectClassid_lev15', Integer),
    Column('ProjectClassid_lev2', Integer),
    Column('ProjectClassid_lev3', Integer),
    Column('ProjectClassid_lev4', Integer),
    Column('ProjectClassid_lev5', Integer),
    Column('ProjectClassid_lev6', Integer),
    Column('ProjectClassid_lev7', Integer),
    Column('ProjectClassid_lev8', Integer),
    Column('ProjectClassid_lev9', Integer),
    Column('createTime', DateTime, index=True)
)


t_AA_PurchasePriceSource = Table(
    'AA_PurchasePriceSource', metadata,
    Column('code', Unicode(32)),
    Column('name', Unicode(200)),
    Column('priorityLevel', Integer),
    Column('isInUse', Integer),
    Column('ts', TIMESTAMP),
    Column('updatedBy', Unicode(32)),
    Column('discount', Numeric(32, 15)),
    Column('id', Integer, nullable=False),
    Column('idpricestrategy', Integer),
    Column('createdtime', DateTime),
    Column('updated', DateTime)
)


t_AA_RDStyle = Table(
    'AA_RDStyle', metadata,
    Column('code', Unicode(32)),
    Column('name', Unicode(200)),
    Column('isEndNode', Integer),
    Column('depth', Integer),
    Column('disabled', Integer),
    Column('ts', TIMESTAMP),
    Column('updatedBy', Unicode(32)),
    Column('inId', Unicode(560)),
    Column('id', Integer, nullable=False),
    Column('idparent', Integer),
    Column('madeDate', DateTime),
    Column('updated', DateTime),
    Column('createdTime', DateTime)
)


t_AA_RdStyle_Ext = Table(
    'AA_RdStyle_Ext', metadata,
    Column('RdStylecode_lev1', Unicode(32)),
    Column('RdStylename_lev1', Unicode(200)),
    Column('RdStylecode_lev2', Unicode(32)),
    Column('RdStylename_lev2', Unicode(200)),
    Column('RdStylecode_lev3', Unicode(32)),
    Column('RdStylename_lev3', Unicode(200)),
    Column('RdStylecode_lev4', Unicode(32)),
    Column('RdStylename_lev4', Unicode(200)),
    Column('RdStylecode_lev5', Unicode(32)),
    Column('RdStylename_lev5', Unicode(200)),
    Column('RdStylecode_lev6', Unicode(32)),
    Column('RdStylename_lev6', Unicode(200)),
    Column('RdStylecode_lev7', Unicode(32)),
    Column('RdStylename_lev7', Unicode(200)),
    Column('RdStylecode_lev8', Unicode(32)),
    Column('RdStylename_lev8', Unicode(200)),
    Column('RdStylecode_lev9', Unicode(32)),
    Column('RdStylename_lev9', Unicode(200)),
    Column('RdStylecode_lev10', Unicode(32)),
    Column('RdStylename_lev10', Unicode(200)),
    Column('RdStylecode_lev11', Unicode(32)),
    Column('RdStylename_lev11', Unicode(200)),
    Column('RdStylecode_lev12', Unicode(32)),
    Column('RdStylename_lev12', Unicode(200)),
    Column('RdStylecode_lev13', Unicode(32)),
    Column('RdStylename_lev13', Unicode(200)),
    Column('RdStylecode_lev14', Unicode(32)),
    Column('RdStylename_lev14', Unicode(200)),
    Column('RdStylecode_lev15', Unicode(32)),
    Column('RdStylename_lev15', Unicode(200)),
    Column('depth', Unicode(10)),
    Column('ts', TIMESTAMP),
    Column('RdStyleid_lev1', Integer),
    Column('RdStyleid_lev10', Integer),
    Column('RdStyleid_lev11', Integer),
    Column('RdStyleid_lev12', Integer),
    Column('RdStyleid_lev13', Integer),
    Column('RdStyleid_lev14', Integer),
    Column('RdStyleid_lev15', Integer),
    Column('RdStyleid_lev2', Integer),
    Column('RdStyleid_lev3', Integer),
    Column('RdStyleid_lev4', Integer),
    Column('RdStyleid_lev5', Integer),
    Column('RdStyleid_lev6', Integer),
    Column('RdStyleid_lev7', Integer),
    Column('RdStyleid_lev8', Integer),
    Column('RdStyleid_lev9', Integer),
    Column('id', Integer),
    Column('createTime', DateTime, index=True)
)


t_AA_Routing = Table(
    'AA_Routing', metadata,
    Column('code', Unicode(30)),
    Column('name', Unicode(50)),
    Column('defaultrouting', Integer),
    Column('disabled', Integer),
    Column('sequencenumber', Integer),
    Column('ts', TIMESTAMP, nullable=False),
    Column('updatedBy', Unicode(32)),
    Column('priuserdefnvc1', Unicode(500)),
    Column('priuserdefdecm1', Numeric(28, 14)),
    Column('priuserdefnvc2', Unicode(500)),
    Column('priuserdefdecm2', Numeric(28, 14)),
    Column('priuserdefnvc3', Unicode(500)),
    Column('priuserdefdecm3', Numeric(28, 14)),
    Column('priuserdefnvc4', Unicode(500)),
    Column('priuserdefdecm4', Numeric(28, 14)),
    Column('priuserdefnvc5', Unicode(500)),
    Column('priuserdefdecm5', Numeric(28, 14)),
    Column('freeItem0', Unicode(300)),
    Column('freeItem1', Unicode(300)),
    Column('freeItem2', Unicode(300)),
    Column('freeItem3', Unicode(300)),
    Column('freeItem4', Unicode(300)),
    Column('freeItem5', Unicode(300)),
    Column('freeItem6', Unicode(300)),
    Column('freeItem7', Unicode(300)),
    Column('freeItem8', Unicode(300)),
    Column('freeItem9', Unicode(300)),
    Column('id', Integer, nullable=False),
    Column('idworkshop', Integer),
    Column('idinventory', Integer),
    Column('idunit', Integer),
    Column('idunit2', Integer),
    Column('createdtime', DateTime),
    Column('updated', DateTime)
)


t_AA_Routing_b = Table(
    'AA_Routing_b', metadata,
    Column('code', Unicode(30)),
    Column('name', Unicode(200)),
    Column('jobsequence', Integer),
    Column('workprice', Numeric(28, 14)),
    Column('timesheet', Numeric(28, 14)),
    Column('salary', Numeric(28, 14)),
    Column('rateofexchange', Numeric(28, 14)),
    Column('completepercentage', Numeric(28, 14)),
    Column('qualifiedrate', Numeric(28, 14)),
    Column('sequencenumber', Integer),
    Column('ts', TIMESTAMP, nullable=False),
    Column('updatedBy', Unicode(32)),
    Column('priuserdefnvc1', Unicode(500)),
    Column('priuserdefdecm1', Numeric(28, 14)),
    Column('priuserdefnvc2', Unicode(500)),
    Column('priuserdefdecm2', Numeric(28, 14)),
    Column('priuserdefnvc3', Unicode(500)),
    Column('priuserdefdecm3', Numeric(28, 14)),
    Column('priuserdefnvc4', Unicode(500)),
    Column('priuserdefdecm4', Numeric(28, 14)),
    Column('priuserdefnvc5', Unicode(500)),
    Column('priuserdefdecm5', Numeric(28, 14)),
    Column('idworkshop', Integer),
    Column('idproductprocess', Integer),
    Column('idRoutingDTO', Integer),
    Column('id', Integer, nullable=False),
    Column('salarycalculatemethod', Integer),
    Column('timesheetunit', Integer),
    Column('createdtime', DateTime),
    Column('updated', DateTime)
)


t_AA_SalePriceSource = Table(
    'AA_SalePriceSource', metadata,
    Column('code', Unicode(32)),
    Column('name', Unicode(200)),
    Column('priorityLevel', Integer),
    Column('isInUse', Integer),
    Column('ts', TIMESTAMP),
    Column('updatedBy', Unicode(32)),
    Column('discount', Numeric(32, 15)),
    Column('ID', Integer, nullable=False),
    Column('idpricestrategy', Integer),
    Column('createdtime', DateTime),
    Column('updated', DateTime)
)


t_AA_SettleStyle = Table(
    'AA_SettleStyle', metadata,
    Column('code', Unicode(32)),
    Column('name', Unicode(200)),
    Column('disabled', Integer),
    Column('ts', TIMESTAMP),
    Column('updatedBy', Unicode(32)),
    Column('chequeManagement', Integer),
    Column('VirtualPay', Integer),
    Column('id', Integer, nullable=False),
    Column('idbankaccount', Integer),
    Column('madeDate', DateTime),
    Column('updated', DateTime),
    Column('createdTime', DateTime)
)


t_AA_StoreInventoryPrice = Table(
    'AA_StoreInventoryPrice', metadata,
    Column('code', Unicode(32)),
    Column('name', Unicode(200)),
    Column('MemberPrice', Numeric(32, 15)),
    Column('retailPriceNew', Numeric(32, 15)),
    Column('ts', TIMESTAMP),
    Column('updatedBy', Unicode(32)),
    Column('StoreRetailPriceFormula', Unicode(1000)),
    Column('StoreRetailPrice', Unicode(1000)),
    Column('StoreMemberPrice', Unicode(1000)),
    Column('StoreMemberPriceFormula', Unicode(1000)),
    Column('PriceKey', Unicode(36)),
    Column('SearchFlag', Integer),
    Column('InvBarCode', Unicode(1000)),
    Column('idstore', Integer),
    Column('idinventory', Integer),
    Column('id', Integer, nullable=False),
    Column('idunit', Integer),
    Column('dimension', Integer),
    Column('iddepartment', Integer),
    Column('iddistrict', Integer),
    Column('StoreType', Integer),
    Column('updated', DateTime),
    Column('createdtime', DateTime)
)


t_AA_Suite = Table(
    'AA_Suite', metadata,
    Column('code', Unicode(32)),
    Column('name', Unicode(200)),
    Column('produceQuantity', Numeric(28, 14)),
    Column('disabled', Integer),
    Column('producequantity2', Numeric(28, 14)),
    Column('ts', TIMESTAMP, nullable=False),
    Column('updatedBy', Unicode(32)),
    Column('rateofexchange', Numeric(28, 14)),
    Column('priuserdefdecm1', Numeric(28, 14)),
    Column('priuserdefdecm2', Numeric(28, 14)),
    Column('priuserdefdecm3', Numeric(28, 14)),
    Column('priuserdefdecm4', Numeric(28, 14)),
    Column('priuserdefdecm5', Numeric(28, 14)),
    Column('priuserdefdecm6', Numeric(28, 14)),
    Column('priuserdefnvc1', Unicode(500)),
    Column('priuserdefnvc2', Unicode(500)),
    Column('priuserdefnvc3', Unicode(500)),
    Column('priuserdefnvc4', Unicode(500)),
    Column('priuserdefnvc5', Unicode(500)),
    Column('priuserdefnvc6', Unicode(500)),
    Column('pubuserdefdecm1', Numeric(28, 14)),
    Column('pubuserdefdecm2', Numeric(28, 14)),
    Column('pubuserdefdecm3', Numeric(28, 14)),
    Column('pubuserdefdecm4', Numeric(28, 14)),
    Column('pubuserdefdecm5', Numeric(28, 14)),
    Column('pubuserdefdecm6', Numeric(28, 14)),
    Column('pubuserdefnvc1', Unicode(500)),
    Column('pubuserdefnvc2', Unicode(500)),
    Column('pubuserdefnvc3', Unicode(500)),
    Column('pubuserdefnvc4', Unicode(500)),
    Column('pubuserdefnvc5', Unicode(500)),
    Column('pubuserdefnvc6', Unicode(500)),
    Column('idinventory', Integer),
    Column('id', Integer, nullable=False),
    Column('idunit', Integer),
    Column('idunit2', Integer),
    Column('updated', DateTime),
    Column('madeDate', DateTime),
    Column('createdtime', DateTime)
)


t_AA_SuiteChild = Table(
    'AA_SuiteChild', metadata,
    Column('code', Unicode(32)),
    Column('name', Unicode(200)),
    Column('produceQuantity', Numeric(28, 14)),
    Column('rationQuantity', Numeric(28, 14)),
    Column('ts', TIMESTAMP, nullable=False),
    Column('requiredquantity', Numeric(28, 14)),
    Column('rateofexchange', Numeric(28, 14)),
    Column('requiredquantity2', Numeric(28, 14)),
    Column('updatedBy', Unicode(32)),
    Column('BatchNumber', Unicode(100)),
    Column('failDate', DateTime),
    Column('freeItem0', Unicode(300)),
    Column('freeItem1', Unicode(300)),
    Column('freeItem2', Unicode(300)),
    Column('freeItem3', Unicode(300)),
    Column('freeItem4', Unicode(300)),
    Column('freeItem5', Unicode(300)),
    Column('freeItem6', Unicode(300)),
    Column('freeItem7', Unicode(300)),
    Column('freeItem8', Unicode(300)),
    Column('freeItem9', Unicode(300)),
    Column('memo', Unicode(200)),
    Column('priuserdefdecm1', Numeric(28, 14)),
    Column('priuserdefdecm2', Numeric(28, 14)),
    Column('priuserdefdecm3', Numeric(28, 14)),
    Column('priuserdefdecm4', Numeric(28, 14)),
    Column('priuserdefnvc1', Unicode(500)),
    Column('priuserdefnvc2', Unicode(500)),
    Column('priuserdefnvc3', Unicode(500)),
    Column('priuserdefnvc4', Unicode(500)),
    Column('pubuserdefdecm1', Numeric(28, 14)),
    Column('pubuserdefdecm2', Numeric(28, 14)),
    Column('pubuserdefdecm3', Numeric(28, 14)),
    Column('pubuserdefdecm4', Numeric(28, 14)),
    Column('pubuserdefnvc1', Unicode(500)),
    Column('pubuserdefnvc2', Unicode(500)),
    Column('pubuserdefnvc3', Unicode(500)),
    Column('pubuserdefnvc4', Unicode(500)),
    Column('idinventory', Integer),
    Column('idbom', Integer),
    Column('id', Integer, nullable=False),
    Column('idunit', Integer),
    Column('idunit2', Integer),
    Column('madeDate', DateTime),
    Column('updated', DateTime),
    Column('createdtime', DateTime)
)


class AATicketType(Base):
    __tablename__ = 'AA_TicketType'

    code = Column(Unicode(30))
    name = Column(Unicode(200))
    facevalue = Column(Unicode(50))
    amount = Column(Numeric(28, 14))
    createdtime = Column(String(19, u'Chinese_PRC_CI_AS'))
    sequencenumber = Column(Integer)
    ts = Column(TIMESTAMP, nullable=False)
    updated = Column(String(19, u'Chinese_PRC_CI_AS'))
    updatedBy = Column(Unicode(32))
    disabled = Column(Integer, nullable=False, server_default=text("((0))"))
    idcurrency = Column(Integer)
    id = Column(Integer, primary_key=True)


class AAUnit(Base):
    __tablename__ = 'AA_Unit'

    code = Column(Unicode(50))
    name = Column(Unicode(200))
    isMainUnit = Column(Integer)
    changeRate = Column(Numeric(28, 14))
    isSingleUnit = Column(Integer)
    disabled = Column(Integer)
    ts = Column(TIMESTAMP)
    updatedBy = Column(Unicode(32))
    rateDescription = Column(Unicode(200))
    isGroup = Column(Integer)
    id = Column(Integer, primary_key=True)
    idunitgroup = Column(Integer)
    changeType = Column(Integer)
    changeType1 = Column(Integer)
    madeDate = Column(DateTime)
    updated = Column(DateTime)
    createdTime = Column(DateTime)


t_AA_UnitGroup = Table(
    'AA_UnitGroup', metadata,
    Column('code', Unicode(50)),
    Column('name', Unicode(200)),
    Column('disabled', Integer),
    Column('ts', TIMESTAMP),
    Column('updatedBy', Unicode(32)),
    Column('id', Integer, nullable=False),
    Column('madeDate', DateTime),
    Column('updated', DateTime),
    Column('createdTime', DateTime)
)


class AAUseStatus(Base):
    __tablename__ = 'AA_UseStatus'

    code = Column(Unicode(30))
    name = Column(Unicode(100))
    depth = Column(Integer)
    inid = Column(Unicode(750))
    isendnode = Column(Integer)
    ispreset = Column(Integer)
    ts = Column(TIMESTAMP, nullable=False)
    updated = Column(String(19, u'Chinese_PRC_CI_AS'))
    updatedBy = Column(Unicode(32))
    createdTime = Column(String(19, u'Chinese_PRC_CI_AS'))
    isDepr = Column(Integer)
    Disabled = Column(Integer)
    id = Column(Integer, primary_key=True)
    idparent = Column(Integer)


t_AA_UseStatus_Ext = Table(
    'AA_UseStatus_Ext', metadata,
    Column('useStatuscode_lev1', Unicode(40)),
    Column('useStatusname_lev1', Unicode(100)),
    Column('useStatuscode_lev2', Unicode(40)),
    Column('useStatusname_lev2', Unicode(100)),
    Column('useStatuscode_lev3', Unicode(40)),
    Column('useStatusname_lev3', Unicode(100)),
    Column('useStatuscode_lev4', Unicode(40)),
    Column('useStatusname_lev4', Unicode(100)),
    Column('useStatuscode_lev5', Unicode(40)),
    Column('useStatusname_lev5', Unicode(100)),
    Column('useStatuscode_lev6', Unicode(40)),
    Column('useStatusname_lev6', Unicode(100)),
    Column('useStatuscode_lev7', Unicode(40)),
    Column('useStatusname_lev7', Unicode(100)),
    Column('useStatuscode_lev8', Unicode(40)),
    Column('useStatusname_lev8', Unicode(100)),
    Column('useStatuscode_lev9', Unicode(40)),
    Column('useStatusname_lev9', Unicode(100)),
    Column('useStatuscode_lev10', Unicode(40)),
    Column('useStatusname_lev10', Unicode(100)),
    Column('useStatuscode_lev11', Unicode(40)),
    Column('useStatusname_lev11', Unicode(100)),
    Column('useStatuscode_lev12', Unicode(40)),
    Column('useStatusname_lev12', Unicode(100)),
    Column('useStatuscode_lev13', Unicode(40)),
    Column('useStatusname_lev13', Unicode(100)),
    Column('useStatuscode_lev14', Unicode(40)),
    Column('useStatusname_lev14', Unicode(100)),
    Column('useStatuscode_lev15', Unicode(40)),
    Column('useStatusname_lev15', Unicode(100)),
    Column('depth', Unicode(10)),
    Column('createTime', String(19, u'Chinese_PRC_CI_AS')),
    Column('ts', TIMESTAMP),
    Column('id', Integer),
    Column('useStatusid_lev1', Integer),
    Column('useStatusid_lev10', Integer),
    Column('useStatusid_lev11', Integer),
    Column('useStatusid_lev12', Integer),
    Column('useStatusid_lev13', Integer),
    Column('useStatusid_lev14', Integer),
    Column('useStatusid_lev15', Integer),
    Column('useStatusid_lev2', Integer),
    Column('useStatusid_lev3', Integer),
    Column('useStatusid_lev4', Integer),
    Column('useStatusid_lev5', Integer),
    Column('useStatusid_lev6', Integer),
    Column('useStatusid_lev7', Integer),
    Column('useStatusid_lev8', Integer),
    Column('useStatusid_lev9', Integer)
)


t_AA_VendorInventoryPrice = Table(
    'AA_VendorInventoryPrice', metadata,
    Column('code', Unicode(32)),
    Column('name', Unicode(200)),
    Column('agreementPrice', Unicode(1000)),
    Column('highestPrice', Unicode(1000)),
    Column('ts', TIMESTAMP),
    Column('updatedBy', Unicode(32)),
    Column('EffectiveStartDate', DateTime),
    Column('EffectiveEndDate', DateTime),
    Column('agreementDiscount', Numeric(28, 14)),
    Column('transactionPrice', Unicode(1000)),
    Column('discount', Numeric(28, 14)),
    Column('highestPriceFormula', Unicode(1000)),
    Column('PriceKey', Unicode(34)),
    Column('InvBarCode', Unicode(128)),
    Column('idinventory', Integer),
    Column('idInventoryPrice', Integer),
    Column('idvendor', Integer),
    Column('idunit', Integer),
    Column('id', Integer, nullable=False),
    Column('idpricetrace', Integer),
    Column('createdtime', DateTime),
    Column('updated', DateTime)
)


t_AA_VendorInventoryPriceDetail = Table(
    'AA_VendorInventoryPriceDetail', metadata,
    Column('Code', Unicode(32)),
    Column('Name', Unicode(200)),
    Column('AgreementPrice', Unicode(1000)),
    Column('AgreementPriceFormula', Unicode(1000)),
    Column('AgreementDiscount', Numeric(28, 14)),
    Column('TransactionPrice', Unicode(1000)),
    Column('TransactionPriceFormula', Unicode(1000)),
    Column('EffectiveStartDate', DateTime),
    Column('EffectiveEndDate', DateTime),
    Column('CreatedTime', DateTime),
    Column('Updated', DateTime),
    Column('UpdatedBy', Unicode(32)),
    Column('ts', TIMESTAMP, nullable=False),
    Column('Id', Integer, nullable=False),
    Column('IdVendorInventoryPrice', Integer, nullable=False, server_default=text("((0))"))
)


t_AA_VendorInventoryPriceTrace = Table(
    'AA_VendorInventoryPriceTrace', metadata,
    Column('code', Unicode(32)),
    Column('name', Unicode(200)),
    Column('lastPrice', Numeric(32, 15)),
    Column('discount', Numeric(32, 15)),
    Column('unitprice', Numeric(32, 15)),
    Column('unittaxprice', Numeric(32, 15)),
    Column('ts', TIMESTAMP),
    Column('updatedBy', Unicode(32)),
    Column('id', Integer, nullable=False),
    Column('idinventory', Integer, nullable=False, server_default=text("((0))")),
    Column('idvendor', Integer, nullable=False, server_default=text("((0))")),
    Column('idunit', Integer, nullable=False, server_default=text("((0))")),
    Column('createdtime', DateTime),
    Column('updated', DateTime)
)


t_AA_Warehouse = Table(
    'AA_Warehouse', metadata,
    Column('code', Unicode(32)),
    Column('name', Unicode(200)),
    Column('address', Unicode(200)),
    Column('hasPosition', Integer),
    Column('memo', Unicode(50)),
    Column('disabled', Integer),
    Column('ts', TIMESTAMP),
    Column('updatedBy', Unicode(32)),
    Column('priuserdefnvc1', Unicode(500)),
    Column('priuserdefdecm1', Numeric(28, 14)),
    Column('priuserdefnvc2', Unicode(500)),
    Column('priuserdefdecm2', Numeric(28, 14)),
    Column('priuserdefnvc3', Unicode(500)),
    Column('priuserdefdecm3', Numeric(28, 14)),
    Column('priuserdefnvc4', Unicode(500)),
    Column('priuserdefdecm4', Numeric(28, 14)),
    Column('priuserdefnvc5', Unicode(500)),
    Column('priuserdefdecm5', Numeric(28, 14)),
    Column('involveatp', Integer),
    Column('floorstocks', Integer),
    Column('shorthand', Unicode(50)),
    Column('idMarketingOrgan', Integer),
    Column('idadmin', Integer),
    Column('id', Integer, nullable=False),
    Column('DistributionWay', Integer),
    Column('madeDate', DateTime),
    Column('updated', DateTime),
    Column('createdTime', DateTime)
)


t_AA_district_Ext = Table(
    'AA_district_Ext', metadata,
    Column('districtcode_lev1', Unicode(32)),
    Column('districtname_lev1', Unicode(200)),
    Column('districtcode_lev2', Unicode(32)),
    Column('districtname_lev2', Unicode(200)),
    Column('districtcode_lev3', Unicode(32)),
    Column('districtname_lev3', Unicode(200)),
    Column('districtcode_lev4', Unicode(32)),
    Column('districtname_lev4', Unicode(200)),
    Column('districtcode_lev5', Unicode(32)),
    Column('districtname_lev5', Unicode(200)),
    Column('districtcode_lev6', Unicode(32)),
    Column('districtname_lev6', Unicode(200)),
    Column('districtcode_lev7', Unicode(32)),
    Column('districtname_lev7', Unicode(200)),
    Column('districtcode_lev8', Unicode(32)),
    Column('districtname_lev8', Unicode(200)),
    Column('districtcode_lev9', Unicode(32)),
    Column('districtname_lev9', Unicode(200)),
    Column('districtcode_lev10', Unicode(32)),
    Column('districtname_lev10', Unicode(200)),
    Column('districtcode_lev11', Unicode(32)),
    Column('districtname_lev11', Unicode(200)),
    Column('districtcode_lev12', Unicode(32)),
    Column('districtname_lev12', Unicode(200)),
    Column('districtcode_lev13', Unicode(32)),
    Column('districtname_lev13', Unicode(200)),
    Column('districtcode_lev14', Unicode(32)),
    Column('districtname_lev14', Unicode(200)),
    Column('districtcode_lev15', Unicode(32)),
    Column('districtname_lev15', Unicode(200)),
    Column('depth', Unicode(10)),
    Column('ts', TIMESTAMP),
    Column('id', Integer),
    Column('districtid_lev1', Integer),
    Column('districtid_lev10', Integer),
    Column('districtid_lev11', Integer),
    Column('districtid_lev12', Integer),
    Column('districtid_lev13', Integer),
    Column('districtid_lev14', Integer),
    Column('districtid_lev15', Integer),
    Column('districtid_lev2', Integer),
    Column('districtid_lev3', Integer),
    Column('districtid_lev4', Integer),
    Column('districtid_lev5', Integer),
    Column('districtid_lev6', Integer),
    Column('districtid_lev7', Integer),
    Column('districtid_lev8', Integer),
    Column('districtid_lev9', Integer),
    Column('createTime', DateTime, index=True)
)


t_AA_expenseitem_Ext = Table(
    'AA_expenseitem_Ext', metadata,
    Column('expenseitemcode_lev1', Unicode(32)),
    Column('expenseitemname_lev1', Unicode(200)),
    Column('expenseitemcode_lev2', Unicode(32)),
    Column('expenseitemname_lev2', Unicode(200)),
    Column('expenseitemcode_lev3', Unicode(32)),
    Column('expenseitemname_lev3', Unicode(200)),
    Column('expenseitemcode_lev4', Unicode(32)),
    Column('expenseitemname_lev4', Unicode(200)),
    Column('expenseitemcode_lev5', Unicode(32)),
    Column('expenseitemname_lev5', Unicode(200)),
    Column('expenseitemcode_lev6', Unicode(32)),
    Column('expenseitemname_lev6', Unicode(200)),
    Column('expenseitemcode_lev7', Unicode(32)),
    Column('expenseitemname_lev7', Unicode(200)),
    Column('expenseitemcode_lev8', Unicode(32)),
    Column('expenseitemname_lev8', Unicode(200)),
    Column('expenseitemcode_lev9', Unicode(32)),
    Column('expenseitemname_lev9', Unicode(200)),
    Column('expenseitemcode_lev10', Unicode(32)),
    Column('expenseitemname_lev10', Unicode(200)),
    Column('expenseitemcode_lev11', Unicode(32)),
    Column('expenseitemname_lev11', Unicode(200)),
    Column('expenseitemcode_lev12', Unicode(32)),
    Column('expenseitemname_lev12', Unicode(200)),
    Column('expenseitemcode_lev13', Unicode(32)),
    Column('expenseitemname_lev13', Unicode(200)),
    Column('expenseitemcode_lev14', Unicode(32)),
    Column('expenseitemname_lev14', Unicode(200)),
    Column('expenseitemcode_lev15', Unicode(32)),
    Column('expenseitemname_lev15', Unicode(200)),
    Column('depth', Unicode(10)),
    Column('createTime', String(19, u'Chinese_PRC_CI_AS')),
    Column('ts', TIMESTAMP),
    Column('id', Integer),
    Column('expenseitemid_lev1', Integer),
    Column('expenseitemid_lev10', Integer),
    Column('expenseitemid_lev11', Integer),
    Column('expenseitemid_lev12', Integer),
    Column('expenseitemid_lev13', Integer),
    Column('expenseitemid_lev14', Integer),
    Column('expenseitemid_lev15', Integer),
    Column('expenseitemid_lev2', Integer),
    Column('expenseitemid_lev3', Integer),
    Column('expenseitemid_lev4', Integer),
    Column('expenseitemid_lev5', Integer),
    Column('expenseitemid_lev6', Integer),
    Column('expenseitemid_lev7', Integer),
    Column('expenseitemid_lev8', Integer),
    Column('expenseitemid_lev9', Integer)
)


t_AA_income_Ext = Table(
    'AA_income_Ext', metadata,
    Column('incomecode_lev1', Unicode(32)),
    Column('incomename_lev1', Unicode(200)),
    Column('incomecode_lev2', Unicode(32)),
    Column('incomename_lev2', Unicode(200)),
    Column('incomecode_lev3', Unicode(32)),
    Column('incomename_lev3', Unicode(200)),
    Column('incomecode_lev4', Unicode(32)),
    Column('incomename_lev4', Unicode(200)),
    Column('incomecode_lev5', Unicode(32)),
    Column('incomename_lev5', Unicode(200)),
    Column('incomecode_lev6', Unicode(32)),
    Column('incomename_lev6', Unicode(200)),
    Column('incomecode_lev7', Unicode(32)),
    Column('incomename_lev7', Unicode(200)),
    Column('incomecode_lev8', Unicode(32)),
    Column('incomename_lev8', Unicode(200)),
    Column('incomecode_lev9', Unicode(32)),
    Column('incomename_lev9', Unicode(200)),
    Column('incomecode_lev10', Unicode(32)),
    Column('incomename_lev10', Unicode(200)),
    Column('incomecode_lev11', Unicode(32)),
    Column('incomename_lev11', Unicode(200)),
    Column('incomecode_lev12', Unicode(32)),
    Column('incomename_lev12', Unicode(200)),
    Column('incomecode_lev13', Unicode(32)),
    Column('incomename_lev13', Unicode(200)),
    Column('incomecode_lev14', Unicode(32)),
    Column('incomename_lev14', Unicode(200)),
    Column('incomecode_lev15', Unicode(32)),
    Column('incomename_lev15', Unicode(200)),
    Column('depth', Unicode(10)),
    Column('createTime', String(19, u'Chinese_PRC_CI_AS')),
    Column('ts', TIMESTAMP),
    Column('id', Integer),
    Column('incomeid_lev1', Integer),
    Column('incomeid_lev10', Integer),
    Column('incomeid_lev11', Integer),
    Column('incomeid_lev12', Integer),
    Column('incomeid_lev13', Integer),
    Column('incomeid_lev14', Integer),
    Column('incomeid_lev15', Integer),
    Column('incomeid_lev2', Integer),
    Column('incomeid_lev3', Integer),
    Column('incomeid_lev4', Integer),
    Column('incomeid_lev5', Integer),
    Column('incomeid_lev6', Integer),
    Column('incomeid_lev7', Integer),
    Column('incomeid_lev8', Integer),
    Column('incomeid_lev9', Integer)
)


t_AA_inventoryClass_Ext = Table(
    'AA_inventoryClass_Ext', metadata,
    Column('inventoryClasscode_lev1', Unicode(32)),
    Column('inventoryClassname_lev1', Unicode(200)),
    Column('inventoryClasscode_lev2', Unicode(32)),
    Column('inventoryClassname_lev2', Unicode(200)),
    Column('inventoryClasscode_lev3', Unicode(32)),
    Column('inventoryClassname_lev3', Unicode(200)),
    Column('inventoryClasscode_lev4', Unicode(32)),
    Column('inventoryClassname_lev4', Unicode(200)),
    Column('inventoryClasscode_lev5', Unicode(32)),
    Column('inventoryClassname_lev5', Unicode(200)),
    Column('inventoryClasscode_lev6', Unicode(32)),
    Column('inventoryClassname_lev6', Unicode(200)),
    Column('inventoryClasscode_lev7', Unicode(32)),
    Column('inventoryClassname_lev7', Unicode(200)),
    Column('inventoryClasscode_lev8', Unicode(32)),
    Column('inventoryClassname_lev8', Unicode(200)),
    Column('inventoryClasscode_lev9', Unicode(32)),
    Column('inventoryClassname_lev9', Unicode(200)),
    Column('inventoryClasscode_lev10', Unicode(32)),
    Column('inventoryClassname_lev10', Unicode(200)),
    Column('inventoryClasscode_lev11', Unicode(32)),
    Column('inventoryClassname_lev11', Unicode(200)),
    Column('inventoryClasscode_lev12', Unicode(32)),
    Column('inventoryClassname_lev12', Unicode(200)),
    Column('inventoryClasscode_lev13', Unicode(32)),
    Column('inventoryClassname_lev13', Unicode(200)),
    Column('inventoryClasscode_lev14', Unicode(32)),
    Column('inventoryClassname_lev14', Unicode(200)),
    Column('inventoryClasscode_lev15', Unicode(32)),
    Column('inventoryClassname_lev15', Unicode(200)),
    Column('depth', Unicode(10)),
    Column('ts', TIMESTAMP),
    Column('id', Integer),
    Column('inventoryClassid_lev1', Integer),
    Column('inventoryClassid_lev10', Integer),
    Column('inventoryClassid_lev11', Integer),
    Column('inventoryClassid_lev12', Integer),
    Column('inventoryClassid_lev13', Integer),
    Column('inventoryClassid_lev14', Integer),
    Column('inventoryClassid_lev15', Integer),
    Column('inventoryClassid_lev2', Integer),
    Column('inventoryClassid_lev3', Integer),
    Column('inventoryClassid_lev4', Integer),
    Column('inventoryClassid_lev5', Integer),
    Column('inventoryClassid_lev6', Integer),
    Column('inventoryClassid_lev7', Integer),
    Column('inventoryClassid_lev8', Integer),
    Column('inventoryClassid_lev9', Integer),
    Column('createTime', DateTime, index=True)
)


t_AA_inventoryLocation_Ext = Table(
    'AA_inventoryLocation_Ext', metadata,
    Column('inventoryLocationcode_lev1', Unicode(32)),
    Column('inventoryLocationname_lev1', Unicode(200)),
    Column('inventoryLocationcode_lev2', Unicode(32)),
    Column('inventoryLocationname_lev2', Unicode(200)),
    Column('inventoryLocationcode_lev3', Unicode(32)),
    Column('inventoryLocationname_lev3', Unicode(200)),
    Column('inventoryLocationcode_lev4', Unicode(32)),
    Column('inventoryLocationname_lev4', Unicode(200)),
    Column('inventoryLocationcode_lev5', Unicode(32)),
    Column('inventoryLocationname_lev5', Unicode(200)),
    Column('inventoryLocationcode_lev6', Unicode(32)),
    Column('inventoryLocationname_lev6', Unicode(200)),
    Column('inventoryLocationcode_lev7', Unicode(32)),
    Column('inventoryLocationname_lev7', Unicode(200)),
    Column('inventoryLocationcode_lev8', Unicode(32)),
    Column('inventoryLocationname_lev8', Unicode(200)),
    Column('inventoryLocationcode_lev9', Unicode(32)),
    Column('inventoryLocationname_lev9', Unicode(200)),
    Column('inventoryLocationcode_lev10', Unicode(32)),
    Column('inventoryLocationname_lev10', Unicode(200)),
    Column('inventoryLocationcode_lev11', Unicode(32)),
    Column('inventoryLocationname_lev11', Unicode(200)),
    Column('inventoryLocationcode_lev12', Unicode(32)),
    Column('inventoryLocationname_lev12', Unicode(200)),
    Column('inventoryLocationcode_lev13', Unicode(32)),
    Column('inventoryLocationname_lev13', Unicode(200)),
    Column('inventoryLocationcode_lev14', Unicode(32)),
    Column('inventoryLocationname_lev14', Unicode(200)),
    Column('inventoryLocationcode_lev15', Unicode(32)),
    Column('inventoryLocationname_lev15', Unicode(200)),
    Column('depth', Unicode(10)),
    Column('ts', TIMESTAMP),
    Column('inventoryLocationid_lev1', Integer),
    Column('inventoryLocationid_lev10', Integer),
    Column('inventoryLocationid_lev11', Integer),
    Column('inventoryLocationid_lev12', Integer),
    Column('inventoryLocationid_lev13', Integer),
    Column('inventoryLocationid_lev14', Integer),
    Column('inventoryLocationid_lev15', Integer),
    Column('inventoryLocationid_lev2', Integer),
    Column('inventoryLocationid_lev3', Integer),
    Column('inventoryLocationid_lev4', Integer),
    Column('inventoryLocationid_lev5', Integer),
    Column('inventoryLocationid_lev6', Integer),
    Column('inventoryLocationid_lev7', Integer),
    Column('inventoryLocationid_lev8', Integer),
    Column('inventoryLocationid_lev9', Integer),
    Column('id', Integer),
    Column('createTime', DateTime, index=True)
)


t_AA_partnerClass_Ext = Table(
    'AA_partnerClass_Ext', metadata,
    Column('partnerClasscode_lev1', Unicode(32)),
    Column('partnerClassname_lev1', Unicode(200)),
    Column('partnerClasscode_lev2', Unicode(32)),
    Column('partnerClassname_lev2', Unicode(200)),
    Column('partnerClasscode_lev3', Unicode(32)),
    Column('partnerClassname_lev3', Unicode(200)),
    Column('partnerClasscode_lev4', Unicode(32)),
    Column('partnerClassname_lev4', Unicode(200)),
    Column('partnerClasscode_lev5', Unicode(32)),
    Column('partnerClassname_lev5', Unicode(200)),
    Column('partnerClasscode_lev6', Unicode(32)),
    Column('partnerClassname_lev6', Unicode(200)),
    Column('partnerClasscode_lev7', Unicode(32)),
    Column('partnerClassname_lev7', Unicode(200)),
    Column('partnerClasscode_lev8', Unicode(32)),
    Column('partnerClassname_lev8', Unicode(200)),
    Column('partnerClasscode_lev9', Unicode(32)),
    Column('partnerClassname_lev9', Unicode(200)),
    Column('partnerClasscode_lev10', Unicode(32)),
    Column('partnerClassname_lev10', Unicode(200)),
    Column('partnerClasscode_lev11', Unicode(32)),
    Column('partnerClassname_lev11', Unicode(200)),
    Column('partnerClasscode_lev12', Unicode(32)),
    Column('partnerClassname_lev12', Unicode(200)),
    Column('partnerClasscode_lev13', Unicode(32)),
    Column('partnerClassname_lev13', Unicode(200)),
    Column('partnerClasscode_lev14', Unicode(32)),
    Column('partnerClassname_lev14', Unicode(200)),
    Column('partnerClasscode_lev15', Unicode(32)),
    Column('partnerClassname_lev15', Unicode(200)),
    Column('depth', Unicode(10)),
    Column('ts', TIMESTAMP),
    Column('id', Integer),
    Column('partnerClassid_lev1', Integer),
    Column('partnerClassid_lev10', Integer),
    Column('partnerClassid_lev11', Integer),
    Column('partnerClassid_lev12', Integer),
    Column('partnerClassid_lev13', Integer),
    Column('partnerClassid_lev14', Integer),
    Column('partnerClassid_lev15', Integer),
    Column('partnerClassid_lev2', Integer),
    Column('partnerClassid_lev3', Integer),
    Column('partnerClassid_lev4', Integer),
    Column('partnerClassid_lev5', Integer),
    Column('partnerClassid_lev6', Integer),
    Column('partnerClassid_lev7', Integer),
    Column('partnerClassid_lev8', Integer),
    Column('partnerClassid_lev9', Integer),
    Column('createTime', DateTime, index=True)
)


class AMAsset(Base):
    __tablename__ = 'AM_Asset'

    code = Column(Unicode(30))
    name = Column(Unicode(200))
    ver = Column(Integer)
    isactive = Column(Integer)
    spec = Column(Unicode(60))
    qty = Column(Integer, server_default=text("((0))"))
    ismultidept = Column(Integer)
    deptver = Column(Integer)
    bookdate = Column(String(19, u'Chinese_PRC_CI_AS'))
    expyears = Column(Integer)
    expmonths = Column(Integer)
    expduedate = Column(String(19, u'Chinese_PRC_CI_AS'))
    usedyears = Column(Integer, server_default=text("((0))"))
    usedmonths = Column(Integer, server_default=text("((0))"))
    leftyears = Column(Integer, server_default=text("((0))"))
    leftmonths = Column(Integer, server_default=text("((0))"))
    expuop = Column(Numeric(28, 14), server_default=text("((0))"))
    useduop = Column(Numeric(28, 14), server_default=text("((0))"))
    curuop = Column(Numeric(28, 14), server_default=text("((0))"))
    leftuop = Column(Numeric(28, 14), server_default=text("((0))"))
    amount = Column(Numeric(28, 14), server_default=text("((0))"))
    taxfee = Column(Numeric(28, 14), server_default=text("((0))"))
    fixfee = Column(Numeric(28, 14), server_default=text("((0))"))
    discardfee = Column(Numeric(28, 14), server_default=text("((0))"))
    otherfee = Column(Numeric(28, 14), server_default=text("((0))"))
    estvalue = Column(Numeric(28, 14), server_default=text("((0))"))
    origvalue = Column(Numeric(28, 14), server_default=text("((0))"))
    functionorigvalue = Column(Numeric(28, 14), server_default=text("((0))"))
    exchangerate = Column(Numeric(28, 14), server_default=text("((1))"))
    isoffsetinputtax = Column(Integer, server_default=text("((0))"))
    inputtaxrate = Column(Numeric(28, 14), server_default=text("((0))"))
    inputtax = Column(Numeric(28, 14), server_default=text("((0))"))
    totaldepr = Column(Numeric(28, 14), server_default=text("((0))"))
    netamount = Column(Numeric(28, 14), server_default=text("((0))"))
    bookvalue = Column(Numeric(28, 14), server_default=text("((0))"))
    expnrvrate = Column(Numeric(28, 14), server_default=text("((0))"))
    expnrv = Column(Numeric(28, 14), server_default=text("((0))"))
    isdepr = Column(Integer)
    monthdeprrate = Column(Numeric(28, 14), server_default=text("((0))"))
    monthdepramount = Column(Numeric(28, 14), server_default=text("((0))"))
    YearTotalProvision = Column(Numeric(28, 14), server_default=text("((0))"))
    unitdepr = Column(Numeric(28, 14), server_default=text("((0))"))
    leftprovision = Column(Numeric(28, 14), server_default=text("((0))"))
    clearincome = Column(Numeric(28, 14), server_default=text("((0))"))
    clearfee = Column(Numeric(28, 14), server_default=text("((0))"))
    saletax = Column(Numeric(28, 14), server_default=text("((0))"))
    biztax = Column(Numeric(28, 14), server_default=text("((0))"))
    impairment = Column(Numeric(28, 14), server_default=text("((0))"))
    barcode = Column(Unicode(50))
    serialnum = Column(Unicode(50))
    producedate = Column(String(19, u'Chinese_PRC_CI_AS'))
    wtydate = Column(String(19, u'Chinese_PRC_CI_AS'))
    suitnum = Column(Unicode(50))
    fundsrc = Column(Unicode(50))
    landlevel = Column(Unicode(50))
    landarea = Column(Numeric(28, 14))
    buildingarea = Column(Numeric(28, 14))
    rooms = Column(Integer)
    empower = Column(Numeric(28, 14))
    emnum = Column(Integer)
    license = Column(Unicode(50))
    nettons = Column(Numeric(28, 14))
    isbegin = Column(Integer)
    issealed = Column(Integer)
    srcvoucherid = Column(Unicode(50))
    srcvouchernum = Column(Unicode(50))
    srcvoucherdate = Column(String(19, u'Chinese_PRC_CI_AS'))
    docno = Column(Unicode(36))
    docclass = Column(Unicode(36))
    accountingperiod = Column(Integer)
    docid = Column(Unicode(36))
    accountingyear = Column(Integer)
    memo = Column(Unicode(200))
    voucherdate = Column(String(19, u'Chinese_PRC_CI_AS'))
    madedate = Column(String(19, u'Chinese_PRC_CI_AS'))
    maker = Column(Unicode(50))
    auditor = Column(Unicode(50))
    auditeddate = Column(String(19, u'Chinese_PRC_CI_AS'))
    reviser = Column(Unicode(50))
    iscarriedforwardout = Column(Integer)
    iscarriedforwardin = Column(Integer)
    ismodifiedcode = Column(Integer)
    createdtime = Column(String(19, u'Chinese_PRC_CI_AS'))
    sequencenumber = Column(Integer)
    mutidept = Column(Unicode(510))
    ts = Column(TIMESTAMP, nullable=False)
    updated = Column(String(19, u'Chinese_PRC_CI_AS'))
    updatedBy = Column(Unicode(32))
    priuserdefnvc1 = Column(Unicode(500))
    priuserdefdecm1 = Column(Numeric(28, 14))
    priuserdefnvc2 = Column(Unicode(500))
    priuserdefdecm2 = Column(Numeric(28, 14))
    priuserdefnvc3 = Column(Unicode(500))
    priuserdefdecm3 = Column(Numeric(28, 14))
    priuserdefnvc4 = Column(Unicode(500))
    priuserdefdecm4 = Column(Numeric(28, 14))
    priuserdefnvc5 = Column(Unicode(500))
    priuserdefdecm5 = Column(Numeric(28, 14))
    priuserdefnvc6 = Column(Unicode(500))
    priuserdefdecm6 = Column(Numeric(28, 14))
    pubuserdefnvc1 = Column(Unicode(500))
    pubuserdefdecm1 = Column(Numeric(28, 14))
    pubuserdefnvc2 = Column(Unicode(500))
    pubuserdefdecm2 = Column(Numeric(28, 14))
    pubuserdefnvc3 = Column(Unicode(500))
    pubuserdefdecm3 = Column(Numeric(28, 14))
    pubuserdefnvc4 = Column(Unicode(500))
    pubuserdefdecm4 = Column(Numeric(28, 14))
    pubuserdefnvc5 = Column(Unicode(500))
    pubuserdefdecm5 = Column(Numeric(28, 14))
    pubuserdefnvc6 = Column(Unicode(500))
    pubuserdefdecm6 = Column(Numeric(28, 14))
    CheckDate = Column(String(19, u'Chinese_PRC_CI_AS'))
    AssetOrderNum = Column(Unicode(50))
    IsActualDepr = Column(Integer)
    ActualDeprMethod = Column(Unicode(200))
    DeprCycle = Column(Integer, server_default=text("((0))"))
    SourceVoucherNum = Column(Unicode(200))
    SourceVoucherDate = Column(String(19, u'Chinese_PRC_CI_AS'))
    BeginDeprMonth = Column(String(19, u'Chinese_PRC_CI_AS'))
    EndDeprMonth = Column(String(19, u'Chinese_PRC_CI_AS'))
    ImageFile = Column(Unicode(200))
    UsedYearAndMonth = Column(Unicode(200))
    LeftYearAndMonth = Column(Unicode(200))
    ExpYearAndMonth = Column(Unicode(200))
    ExpTotalMonth = Column(Integer)
    UsedTotalMonth = Column(Integer)
    LeftTotalMonth = Column(Integer)
    disabled = Column(Integer)
    SumYears = Column(Integer)
    PrintCount = Column(Integer, nullable=False, server_default=text("((0))"))
    CardDate = Column(String(19, u'Chinese_PRC_CI_AS'))
    idassetclass = Column(Integer)
    idAssetProp = Column(Integer)
    idbizusage = Column(Integer)
    idcurrency = Column(Integer)
    idadmindept = Column(Integer)
    idusedept = Column(Integer)
    iddeprmethod = Column(Integer)
    idhandlereason = Column(Integer)
    idincdecway = Column(Integer)
    idpartner = Column(Integer)
    idproducer = Column(Integer)
    idperson = Column(Integer)
    idposition = Column(Integer)
    idproject = Column(Integer)
    idunit = Column(Integer)
    iduopunit = Column(Integer)
    idusestatus = Column(Integer)
    id = Column(Integer, primary_key=True)
    idPrevCardID = Column(Integer)
    cardid = Column(Integer)
    copyfrom = Column(Integer)
    SourceVoucherID = Column(Integer)
    cardstate = Column(Integer)
    IsGenDoc = Column(Integer)
    voucherstate = Column(Integer)
    auditorid = Column(Integer)
    makerid = Column(Integer)
    idbookperiod = Column(Integer)
    IDSourceVoucherPeriod = Column(Integer)
    idsrcvoucherperiod = Column(Integer)
    idprocesstype = Column(Integer)
    IDSourceVoucherType = Column(Integer)
    idSrcVoucherType = Column(Integer)


class AMAttachment(Base):
    __tablename__ = 'AM_Attachment'

    code = Column(Unicode(30))
    name = Column(Unicode(200))
    spec = Column(Unicode(60))
    qty = Column(Numeric(28, 14))
    amount = Column(Numeric(28, 14))
    memo = Column(Unicode(50))
    ts = Column(TIMESTAMP, nullable=False)
    updated = Column(String(19, u'Chinese_PRC_CI_AS'))
    updatedBy = Column(Unicode(32))
    priuserdefnvc1 = Column(Unicode(500))
    priuserdefdecm1 = Column(Numeric(28, 14))
    priuserdefnvc2 = Column(Unicode(500))
    priuserdefdecm2 = Column(Numeric(28, 14))
    priuserdefnvc3 = Column(Unicode(500))
    priuserdefdecm3 = Column(Numeric(28, 14))
    priuserdefnvc4 = Column(Unicode(500))
    priuserdefdecm4 = Column(Numeric(28, 14))
    priuserdefnvc5 = Column(Unicode(500))
    priuserdefdecm5 = Column(Numeric(28, 14))
    priuserdefnvc6 = Column(Unicode(500))
    priuserdefdecm6 = Column(Numeric(28, 14))
    pubuserdefnvc1 = Column(Unicode(500))
    pubuserdefdecm1 = Column(Numeric(28, 14))
    pubuserdefnvc2 = Column(Unicode(500))
    pubuserdefdecm2 = Column(Numeric(28, 14))
    pubuserdefnvc3 = Column(Unicode(500))
    pubuserdefdecm3 = Column(Numeric(28, 14))
    pubuserdefnvc4 = Column(Unicode(500))
    pubuserdefdecm4 = Column(Numeric(28, 14))
    pubuserdefnvc5 = Column(Unicode(500))
    pubuserdefdecm5 = Column(Numeric(28, 14))
    pubuserdefnvc6 = Column(Unicode(500))
    pubuserdefdecm6 = Column(Numeric(28, 14))
    idUnit = Column(Integer)
    idAssetDTO = Column(Integer)
    id = Column(Integer, primary_key=True)


class AMCheckDetail(Base):
    __tablename__ = 'AM_CheckDetail'

    code = Column(Unicode(30))
    name = Column(Unicode(200))
    createdtime = Column(String(19, u'Chinese_PRC_CI_AS'))
    sequencenumber = Column(Integer)
    qty = Column(Integer)
    ts = Column(TIMESTAMP, nullable=False)
    updated = Column(String(19, u'Chinese_PRC_CI_AS'))
    updatedBy = Column(Unicode(32))
    MutiDept = Column(Unicode(1024))
    OldBarCode = Column(Unicode(50))
    OldCode = Column(Unicode(30))
    OldName = Column(Unicode(200))
    OldSpec = Column(Unicode(60))
    OldQty = Column(Integer)
    OldMutiDept = Column(Unicode(1024))
    idadmindept = Column(Integer)
    idOldAdminDept = Column(Integer)
    idOldUsePerson = Column(Integer)
    iduseperson = Column(Integer)
    idOldPosition = Column(Integer)
    idposition = Column(Integer)
    idOldUseStatus = Column(Integer)
    iduseStatus = Column(Integer)
    idasset = Column(Integer)
    id = Column(Integer, primary_key=True)
    idAMCheckVoucherDTO = Column(Integer)
    admindeptcheckresult = Column(Integer)
    positioncheckresult = Column(Integer)
    qtycheckresult = Column(Integer)
    usedeptcheckresult = Column(Integer)
    usepersoncheckresult = Column(Integer)
    UseStatusCheckResult = Column(Integer)


class AMCheckRangeDetail(Base):
    __tablename__ = 'AM_CheckRangeDetail'

    ts = Column(TIMESTAMP, nullable=False)
    updatedBy = Column(Unicode(32))
    updated = Column(String(19, u'Chinese_PRC_CI_AS'))
    name = Column(Unicode(200))
    code = Column(Unicode(50))
    idAssetClass = Column(Integer)
    idAssetProp = Column(Integer)
    idAdminDept = Column(Integer)
    idUseDept = Column(Integer)
    idUsePerson = Column(Integer)
    idPosition = Column(Integer)
    idUseStatus = Column(Integer)
    id = Column(Integer, primary_key=True)
    idAMCheckVoucherDTO = Column(Integer)


t_AM_CheckUseDept = Table(
    'AM_CheckUseDept', metadata,
    Column('code', Unicode(30)),
    Column('name', Unicode(200)),
    Column('rate', Numeric(28, 14)),
    Column('ismain', Integer),
    Column('createdtime', String(19, u'Chinese_PRC_CI_AS')),
    Column('sequencenumber', Integer),
    Column('ts', TIMESTAMP, nullable=False),
    Column('updated', String(19, u'Chinese_PRC_CI_AS')),
    Column('updatedBy', Unicode(32)),
    Column('idusedept', Integer),
    Column('idAMCheckDetailDTO', Integer),
    Column('id', Integer, nullable=False)
)


class AMCheckVoucher(Base):
    __tablename__ = 'AM_CheckVoucher'

    code = Column(Unicode(30))
    name = Column(Unicode(200))
    docno = Column(Unicode(36))
    docclass = Column(Unicode(36))
    accountingperiod = Column(Integer)
    docid = Column(Unicode(36))
    accountingyear = Column(Integer)
    memo = Column(Unicode(200))
    voucherdate = Column(String(19, u'Chinese_PRC_CI_AS'))
    madedate = Column(String(19, u'Chinese_PRC_CI_AS'))
    maker = Column(Unicode(50))
    auditor = Column(Unicode(50))
    auditeddate = Column(String(19, u'Chinese_PRC_CI_AS'))
    reviser = Column(Unicode(50))
    iscarriedforwardout = Column(Integer)
    iscarriedforwardin = Column(Integer)
    ismodifiedcode = Column(Integer)
    createdtime = Column(String(19, u'Chinese_PRC_CI_AS'))
    sequencenumber = Column(Integer)
    ts = Column(TIMESTAMP, nullable=False)
    updated = Column(String(19, u'Chinese_PRC_CI_AS'))
    updatedBy = Column(Unicode(32))
    checkrange = Column(Unicode(1024))
    CheckDate = Column(String(19, u'Chinese_PRC_CI_AS'))
    PrintCount = Column(Integer, nullable=False, server_default=text("((0))"))
    idcheckdept = Column(Integer)
    idsupervisiondept = Column(Integer)
    idchecker = Column(Integer)
    idsupervision = Column(Integer)
    id = Column(Integer, primary_key=True)
    CheckResult = Column(Integer)
    CheckType = Column(Integer)
    voucherstate = Column(Integer)
    auditorid = Column(Integer)
    makerid = Column(Integer)
    idcheckperiod = Column(Integer)


t_AM_DeprSummary = Table(
    'AM_DeprSummary', metadata,
    Column('ts', TIMESTAMP, nullable=False),
    Column('Amount', Numeric(28, 14), server_default=text("((0))")),
    Column('idAssetClass', Integer),
    Column('idAssetProp', Integer),
    Column('idDepartment', Integer),
    Column('idRootDept', Integer),
    Column('idProject', Integer),
    Column('id', Integer, nullable=False),
    Column('idHandleVoucherDTO', Integer, nullable=False, server_default=text("((0))"))
)


class AMHandleVoucher(Base):
    __tablename__ = 'AM_HandleVoucher'

    code = Column(Unicode(30))
    name = Column(Unicode(200))
    changetype = Column(Unicode(50))
    docno = Column(Unicode(36))
    docclass = Column(Unicode(36))
    accountingperiod = Column(Integer)
    docid = Column(Unicode(36))
    accountingyear = Column(Integer)
    memo = Column(Unicode(200))
    voucherdate = Column(String(19, u'Chinese_PRC_CI_AS'))
    madedate = Column(String(19, u'Chinese_PRC_CI_AS'))
    maker = Column(Unicode(50))
    auditor = Column(Unicode(50))
    auditeddate = Column(String(19, u'Chinese_PRC_CI_AS'))
    reviser = Column(Unicode(50))
    iscarriedforwardout = Column(Integer)
    iscarriedforwardin = Column(Integer)
    ismodifiedcode = Column(Integer)
    createdtime = Column(String(19, u'Chinese_PRC_CI_AS'))
    sequencenumber = Column(Integer)
    ts = Column(TIMESTAMP, nullable=False)
    updated = Column(String(19, u'Chinese_PRC_CI_AS'))
    updatedBy = Column(Unicode(32))
    CheckDate = Column(String(19, u'Chinese_PRC_CI_AS'))
    SumOrgiValue = Column(Numeric(28, 14), server_default=text("((0))"))
    PrintCount = Column(Integer, nullable=False, server_default=text("((0))"))
    idprocessreason = Column(Integer)
    idincdecway = Column(Integer)
    id = Column(Integer, primary_key=True)
    isGenDoc = Column(Integer)
    voucherstate = Column(Integer)
    auditorid = Column(Integer)
    makerid = Column(Integer)
    idperiod = Column(Integer)
    idvouchertype = Column(Integer)


t_AM_HandleVoucherChangeType = Table(
    'AM_HandleVoucherChangeType', metadata,
    Column('code', Unicode(30)),
    Column('name', Unicode(200)),
    Column('createdtime', String(19, u'Chinese_PRC_CI_AS')),
    Column('sequencenumber', Integer),
    Column('ts', TIMESTAMP, nullable=False),
    Column('updated', String(19, u'Chinese_PRC_CI_AS')),
    Column('updatedBy', Unicode(32)),
    Column('idHandleVoucherDTO', Integer),
    Column('id', Integer, nullable=False),
    Column('changeType', Integer)
)


t_AM_HandleVoucherDept = Table(
    'AM_HandleVoucherDept', metadata,
    Column('Code', Unicode(200)),
    Column('name', Unicode(200)),
    Column('DeptVer', Integer),
    Column('Rate', Numeric(28, 14)),
    Column('IsMain', Integer),
    Column('CreatedTime', String(19, u'Chinese_PRC_CI_AS')),
    Column('SequenceNumber', Integer),
    Column('ts', TIMESTAMP, nullable=False),
    Column('updated', String(19, u'Chinese_PRC_CI_AS')),
    Column('updatedBy', Unicode(32)),
    Column('iduseDept', Integer),
    Column('IDHandleVoucherDetailDTO', Integer),
    Column('id', Integer, nullable=False)
)


class AMHandleVoucherB(Base):
    __tablename__ = 'AM_HandleVoucher_b'

    code = Column(Unicode(30))
    name = Column(Unicode(200))
    createdtime = Column(String(19, u'Chinese_PRC_CI_AS'))
    sequencenumber = Column(Integer)
    ts = Column(TIMESTAMP, nullable=False)
    updated = Column(String(19, u'Chinese_PRC_CI_AS'))
    updatedBy = Column(Unicode(32))
    DiffOrgiValue = Column(Numeric(28, 14), server_default=text("((0))"))
    DiffTotalDeprValue = Column(Numeric(28, 14), server_default=text("((0))"))
    DiffExpNetValue = Column(Numeric(28, 14), server_default=text("((0))"))
    AssetCardID = Column(Unicode(200))
    isdepr = Column(Integer)
    idprocessreason = Column(Integer)
    idincdecway = Column(Integer)
    idpartner = Column(Integer)
    idusestatus = Column(Integer)
    CurrentMonthUsed = Column(Integer)
    idasset = Column(Integer)
    idoldasset = Column(Integer)
    idHandleVoucherDTO = Column(Integer)
    id = Column(Integer, primary_key=True)


class AMMaintain(Base):
    __tablename__ = 'AM_Maintain'

    code = Column(Unicode(30))
    name = Column(Unicode(200))
    digest = Column(Unicode(50))
    amount = Column(Numeric(28, 14))
    memo = Column(Unicode(50))
    createdtime = Column(String(19, u'Chinese_PRC_CI_AS'))
    sequencenumber = Column(Integer)
    maintaindate = Column(String(19, u'Chinese_PRC_CI_AS'))
    fee = Column(Unicode(50))
    ts = Column(TIMESTAMP, nullable=False)
    updated = Column(String(19, u'Chinese_PRC_CI_AS'))
    updatedBy = Column(Unicode(32))
    priuserdefnvc1 = Column(Unicode(500))
    priuserdefdecm1 = Column(Numeric(28, 14))
    priuserdefnvc2 = Column(Unicode(500))
    priuserdefdecm2 = Column(Numeric(28, 14))
    priuserdefnvc3 = Column(Unicode(500))
    priuserdefdecm3 = Column(Numeric(28, 14))
    priuserdefnvc4 = Column(Unicode(500))
    priuserdefdecm4 = Column(Numeric(28, 14))
    priuserdefnvc5 = Column(Unicode(500))
    priuserdefdecm5 = Column(Numeric(28, 14))
    priuserdefnvc6 = Column(Unicode(500))
    priuserdefdecm6 = Column(Numeric(28, 14))
    pubuserdefnvc1 = Column(Unicode(500))
    pubuserdefdecm1 = Column(Numeric(28, 14))
    pubuserdefnvc2 = Column(Unicode(500))
    pubuserdefdecm2 = Column(Numeric(28, 14))
    pubuserdefnvc3 = Column(Unicode(500))
    pubuserdefdecm3 = Column(Numeric(28, 14))
    pubuserdefnvc4 = Column(Unicode(500))
    pubuserdefdecm4 = Column(Numeric(28, 14))
    pubuserdefnvc5 = Column(Unicode(500))
    pubuserdefdecm5 = Column(Numeric(28, 14))
    pubuserdefnvc6 = Column(Unicode(500))
    pubuserdefdecm6 = Column(Numeric(28, 14))
    idAssetDTO = Column(Integer)
    id = Column(Integer, primary_key=True)
    idmaintainperiod = Column(Integer)


class AMOldCheckUseDept(Base):
    __tablename__ = 'AM_OldCheckUseDept'

    name = Column(Unicode(200))
    code = Column(Unicode(50))
    Rate = Column(Numeric(28, 14))
    IsMain = Column(Integer)
    CreateTime = Column(String(19, u'Chinese_PRC_CI_AS'))
    SequenceNumber = Column(Integer)
    ts = Column(TIMESTAMP, nullable=False)
    updated = Column(String(19, u'Chinese_PRC_CI_AS'))
    updatedBy = Column(Unicode(32))
    idUseDept = Column(Integer)
    idAMCheckDetailDTO = Column(Integer)
    id = Column(Integer, primary_key=True)


class AMSplitDetail(Base):
    __tablename__ = 'AM_SplitDetail'

    code = Column(Unicode(30))
    name = Column(Unicode(200))
    createdtime = Column(String(19, u'Chinese_PRC_CI_AS'))
    sequencenumber = Column(Integer)
    ts = Column(TIMESTAMP, nullable=False)
    updated = Column(String(19, u'Chinese_PRC_CI_AS'))
    updatedBy = Column(Unicode(32))
    idasset = Column(Unicode(50))
    idsplitVoucherDTO = Column(Unicode(50))
    id = Column(Integer, primary_key=True)


class AMSplitVoucher(Base):
    __tablename__ = 'AM_SplitVoucher'

    code = Column(Unicode(30))
    name = Column(Unicode(200))
    docno = Column(Unicode(36))
    docclass = Column(Unicode(36))
    accountingperiod = Column(Integer)
    docid = Column(Unicode(36))
    accountingyear = Column(Integer)
    memo = Column(Unicode(200))
    voucherdate = Column(String(19, u'Chinese_PRC_CI_AS'))
    madedate = Column(String(19, u'Chinese_PRC_CI_AS'))
    maker = Column(Unicode(50))
    auditor = Column(Unicode(50))
    auditeddate = Column(String(19, u'Chinese_PRC_CI_AS'))
    reviser = Column(Unicode(50))
    iscarriedforwardout = Column(Integer)
    iscarriedforwardin = Column(Integer)
    ismodifiedcode = Column(Integer)
    createdtime = Column(String(19, u'Chinese_PRC_CI_AS'))
    CheckDate = Column(String(19, u'Chinese_PRC_CI_AS'))
    sequencenumber = Column(Integer)
    issplitbyqty = Column(Integer)
    ts = Column(TIMESTAMP, nullable=False)
    updated = Column(String(19, u'Chinese_PRC_CI_AS'))
    updatedBy = Column(Unicode(32))
    PrintCount = Column(Integer, nullable=False, server_default=text("((0))"))
    idhandlereason = Column(Integer)
    idasset = Column(Integer)
    id = Column(Integer, primary_key=True)
    voucherstate = Column(Integer)
    auditorid = Column(Integer)
    makerid = Column(Integer)
    idsplitperiod = Column(Integer)


class AMUseDept(Base):
    __tablename__ = 'AM_UseDept'

    code = Column(Unicode(30))
    name = Column(Unicode(200))
    deptver = Column(Integer)
    rate = Column(Numeric(28, 14))
    ismain = Column(Integer)
    createdtime = Column(String(19, u'Chinese_PRC_CI_AS'))
    sequencenumber = Column(Integer)
    ts = Column(TIMESTAMP, nullable=False)
    updated = Column(String(19, u'Chinese_PRC_CI_AS'))
    updatedBy = Column(Unicode(32))
    DeprRate = Column(Integer, server_default=text("((0))"))
    DeprValue = Column(Numeric(28, 14), server_default=text("((0))"))
    idusedept = Column(Integer)
    idAssetDTO = Column(Integer)
    id = Column(Integer, primary_key=True)


t_ARAP_AgeAnalysisRptSet = Table(
    'ARAP_AgeAnalysisRptSet', metadata,
    Column('days', Integer),
    Column('isArFlag', Integer),
    Column('userId', Integer)
)


class ARAPDetail(Base):
    __tablename__ = 'ARAP_Detail'

    code = Column(Unicode(30))
    name = Column(Unicode(200))
    year = Column(Integer)
    period = Column(Integer)
    voucherCode = Column(Unicode(30))
    voucherDate = Column(String(19, u'Chinese_PRC_CI_AS'))
    detailCode = Column(Unicode(50))
    detailName = Column(Unicode(200))
    businessCode = Column(Unicode(50))
    registerDate = Column(String(19, u'Chinese_PRC_CI_AS'))
    exchangeRate = Column(Numeric(28, 14))
    origCashAmount = Column(Numeric(28, 14))
    cashAmount = Column(Numeric(28, 14))
    origAmount = Column(Numeric(28, 14))
    origSettleAmount = Column(Numeric(28, 14))
    amount = Column(Numeric(28, 14))
    settleAmount = Column(Numeric(28, 14))
    origInAllowances = Column(Numeric(28, 14))
    inAllowances = Column(Numeric(28, 14))
    auditFlag = Column(Integer)
    auditBussinessFlag = Column(Integer)
    prepayFlag = Column(Integer)
    isArFlag = Column(Integer)
    bussinessFlag = Column(Unicode(50))
    flag = Column(Integer)
    arrivalDate = Column(String(19, u'Chinese_PRC_CI_AS'))
    memo = Column(Unicode(200))
    extendFlag = Column(Integer)
    accountingYear = Column(Integer)
    accountingPeriod = Column(Integer)
    docId = Column(Unicode(36))
    docClass = Column(Unicode(36))
    docNo = Column(Unicode(36))
    isCarriedForwardOut = Column(Integer)
    isCarriedForwardIn = Column(Integer)
    createdTime = Column(String(19, u'Chinese_PRC_CI_AS'))
    sequenceNumber = Column(Integer)
    ts = Column(TIMESTAMP)
    updated = Column(String(19, u'Chinese_PRC_CI_AS'))
    updatedBy = Column(Unicode(32))
    vouchersettleState = Column(Integer)
    saleordercode = Column(Unicode(30))
    sourceordercode = Column(Unicode(30))
    detailtype = Column(Unicode(50))
    vouchertimestamp = Column(Unicode(64))
    yearperiod = Column(Unicode(50))
    cancelassociationcodes = Column(Unicode(100))
    headPriuserdefnvc1 = Column(Unicode(500))
    headPriuserdefnvc2 = Column(Unicode(500))
    headPriuserdefnvc3 = Column(Unicode(500))
    headPriuserdefnvc4 = Column(Unicode(500))
    headPriuserdefnvc5 = Column(Unicode(500))
    headPriuserdefnvc6 = Column(Unicode(500))
    headPriuserdefdecm1 = Column(Numeric(28, 14))
    headPriuserdefdecm2 = Column(Numeric(28, 14))
    headPriuserdefdecm3 = Column(Numeric(28, 14))
    headPriuserdefdecm4 = Column(Numeric(28, 14))
    headPriuserdefdecm5 = Column(Numeric(28, 14))
    headPriuserdefdecm6 = Column(Numeric(28, 14))
    headPubuserdefnvc1 = Column(Unicode(500))
    headPubuserdefnvc2 = Column(Unicode(500))
    headPubuserdefnvc3 = Column(Unicode(500))
    headPubuserdefnvc4 = Column(Unicode(500))
    headPubuserdefnvc5 = Column(Unicode(500))
    headPubuserdefnvc6 = Column(Unicode(500))
    headPubuserdefdecm1 = Column(Numeric(28, 14))
    headPubuserdefdecm2 = Column(Numeric(28, 14))
    headPubuserdefdecm3 = Column(Numeric(28, 14))
    headPubuserdefdecm4 = Column(Numeric(28, 14))
    headPubuserdefdecm5 = Column(Numeric(28, 14))
    headPubuserdefdecm6 = Column(Numeric(28, 14))
    detailPriuserdefnvc1 = Column(Unicode(500))
    detailPriuserdefnvc2 = Column(Unicode(500))
    detailPriuserdefnvc3 = Column(Unicode(500))
    detailPriuserdefnvc4 = Column(Unicode(500))
    detailPriuserdefdecm1 = Column(Numeric(28, 14))
    detailPriuserdefdecm2 = Column(Numeric(28, 14))
    detailPriuserdefdecm3 = Column(Numeric(28, 14))
    detailPriuserdefdecm4 = Column(Numeric(28, 14))
    detailPubuserdefnvc1 = Column(Unicode(500))
    detailPubuserdefnvc2 = Column(Unicode(500))
    detailPubuserdefnvc3 = Column(Unicode(500))
    detailPubuserdefnvc4 = Column(Unicode(500))
    detailPubuserdefdecm1 = Column(Numeric(28, 14))
    detailPubuserdefdecm2 = Column(Numeric(28, 14))
    detailPubuserdefdecm3 = Column(Numeric(28, 14))
    detailPubuserdefdecm4 = Column(Numeric(28, 14))
    isRollInFlag = Column(Integer, server_default=text("((0))"))
    sourceVoucherCode = Column(Unicode(50))
    PurchaseOrderCode = Column(Unicode(50))
    SaleAllowance = Column(Numeric(28, 14))
    origSaleAllowance = Column(Numeric(28, 14))
    sourcevouchermemo = Column(Unicode(200))
    idbusitype = Column(Integer)
    idcurrency = Column(Integer)
    iddepartment = Column(Integer)
    IdMember = Column(Integer)
    detailID = Column(Integer)
    IdMarketingOrgan = Column(Integer)
    idnosettlepartner = Column(Integer)
    idpartner = Column(Integer)
    idperson = Column(Integer)
    IdDetailProject = Column(Integer)
    idproject = Column(Integer)
    BookFlag = Column(Integer)
    id = Column(Integer, primary_key=True)
    voucherDetailID = Column(Integer)
    voucherID = Column(Integer)
    businessID = Column(Integer)
    sourceVoucherID = Column(Integer)
    sourceorderid = Column(Integer)
    PurchaseOrderID = Column(Integer)
    saleorderid = Column(Integer)
    idarapvouchertype = Column(Integer)
    idsourceordertype = Column(Integer)
    idvouchertype = Column(Integer)


class ARAPDetailSecond(Base):
    __tablename__ = 'ARAP_DetailSecond'

    code = Column(Unicode(30))
    name = Column(Unicode(30))
    vouchertimestamp = Column(Unicode(50))
    registerDate = Column(String(19, u'Chinese_PRC_CI_AS'))
    year = Column(Integer)
    period = Column(Integer)
    voucherCode = Column(Unicode(30))
    voucherDate = Column(String(19, u'Chinese_PRC_CI_AS'))
    detailCode = Column(Unicode(50))
    detailName = Column(Unicode(200))
    businessCode = Column(Unicode(50))
    exchangeRate = Column(Numeric(28, 14))
    origCashAmount = Column(Numeric(28, 14))
    cashAmount = Column(Numeric(28, 14))
    origAmount = Column(Numeric(28, 14))
    origSettleAmount = Column(Numeric(28, 14))
    amount = Column(Numeric(28, 14))
    settleAmount = Column(Numeric(28, 14))
    origInAllowances = Column(Numeric(28, 14))
    inAllowances = Column(Numeric(28, 14))
    auditFlag = Column(Integer)
    auditBussinessFlag = Column(Integer)
    prepayFlag = Column(Integer)
    isArFlag = Column(Integer)
    bussinessFlag = Column(Unicode(50))
    flag = Column(Integer)
    arrivalDate = Column(String(19, u'Chinese_PRC_CI_AS'))
    memo = Column(Unicode(200))
    extendFlag = Column(Integer)
    accountingYear = Column(Integer)
    accountingPeriod = Column(Integer)
    docId = Column(Unicode(36))
    docClass = Column(Unicode(36))
    docNo = Column(Unicode(36))
    isCarriedForwardOut = Column(Integer)
    isCarriedForwardIn = Column(Integer)
    saleordercode = Column(Unicode(50))
    sourceordercode = Column(Unicode(50))
    cancelassociationcodes = Column(Unicode(100))
    detailtype = Column(Unicode(50))
    yearperiod = Column(Unicode(50))
    headPriuserdefnvc1 = Column(Unicode(500))
    headPriuserdefdecm1 = Column(Numeric(28, 14))
    headPriuserdefnvc2 = Column(Unicode(500))
    headPriuserdefdecm2 = Column(Numeric(28, 14))
    headPriuserdefnvc3 = Column(Unicode(500))
    headPriuserdefdecm3 = Column(Numeric(28, 14))
    headPriuserdefnvc4 = Column(Unicode(500))
    headPriuserdefdecm4 = Column(Numeric(28, 14))
    headPriuserdefnvc5 = Column(Unicode(500))
    headPriuserdefdecm5 = Column(Numeric(28, 14))
    headPriuserdefnvc6 = Column(Unicode(500))
    headPriuserdefdecm6 = Column(Numeric(28, 14))
    headPubuserdefnvc1 = Column(Unicode(500))
    headPubuserdefdecm1 = Column(Numeric(28, 14))
    headPubuserdefdecm2 = Column(Numeric(28, 14))
    headPubuserdefnvc2 = Column(Unicode(500))
    headPubuserdefdecm3 = Column(Numeric(28, 14))
    headPubuserdefnvc3 = Column(Unicode(500))
    headPubuserdefdecm4 = Column(Numeric(28, 14))
    headPubuserdefnvc4 = Column(Unicode(500))
    headPubuserdefdecm5 = Column(Numeric(28, 14))
    headPubuserdefnvc5 = Column(Unicode(500))
    headPubuserdefdecm6 = Column(Numeric(28, 14))
    headPubuserdefnvc6 = Column(Unicode(500))
    detailPriuserdefnvc1 = Column(Unicode(500))
    detailPriuserdefdecm1 = Column(Numeric(28, 14))
    detailPriuserdefnvc2 = Column(Unicode(500))
    detailPriuserdefdecm2 = Column(Numeric(28, 14))
    detailPriuserdefnvc3 = Column(Unicode(500))
    detailPriuserdefdecm3 = Column(Numeric(28, 14))
    detailPriuserdefnvc4 = Column(Unicode(500))
    detailPriuserdefdecm4 = Column(Numeric(28, 14))
    detailPubuserdefnvc1 = Column(Unicode(500))
    detailPubuserdefdecm1 = Column(Numeric(28, 14))
    detailPubuserdefnvc2 = Column(Unicode(500))
    detailPubuserdefdecm2 = Column(Numeric(28, 14))
    detailPubuserdefnvc3 = Column(Unicode(500))
    detailPubuserdefdecm3 = Column(Numeric(28, 14))
    detailPubuserdefnvc4 = Column(Unicode(500))
    detailPubuserdefdecm4 = Column(Numeric(28, 14))
    createdtime = Column(String(19, u'Chinese_PRC_CI_AS'))
    sequencenumber = Column(Integer)
    ts = Column(TIMESTAMP, nullable=False)
    updated = Column(String(19, u'Chinese_PRC_CI_AS'))
    updatedBy = Column(Unicode(32))
    SaleAllowance = Column(Numeric(28, 14))
    origSaleAllowance = Column(Numeric(28, 14))
    idbusitype = Column(Integer)
    idcurrency = Column(Integer)
    iddepartment = Column(Integer)
    IdMember = Column(Integer)
    detailID = Column(Integer)
    IdMarketingOrgan = Column(Integer)
    idnosettlepartner = Column(Integer)
    idpartner = Column(Integer)
    idperson = Column(Integer)
    IdDetailProject = Column(Integer)
    idproject = Column(Integer)
    id = Column(Integer, primary_key=True)
    sourceorderid = Column(Integer)
    businessID = Column(Integer)
    voucherID = Column(Integer)
    voucherDetailID = Column(Integer)
    saleorderid = Column(Integer)
    idarapvouchertype = Column(Integer)
    idsourceordertype = Column(Integer)
    idvouchertype = Column(Integer)


class ARAPExchangeAdjust(Base):
    __tablename__ = 'ARAP_ExchangeAdjust'

    code = Column(Unicode(30))
    name = Column(Unicode(200))
    exchangeRate = Column(Numeric(28, 14))
    arDifferentAmount = Column(Numeric(28, 14))
    apDifferentAmount = Column(Numeric(28, 14))
    memo = Column(Unicode(200))
    voucherDate = Column(String(19, u'Chinese_PRC_CI_AS'))
    maker = Column(Unicode(50))
    madeDate = Column(String(19, u'Chinese_PRC_CI_AS'))
    auditor = Column(Unicode(50))
    reviser = Column(Unicode(50))
    auditedDate = Column(String(19, u'Chinese_PRC_CI_AS'))
    isCarriedForwardOut = Column(Integer)
    isCarriedForwardIn = Column(Integer)
    isModifiedCode = Column(Integer)
    docNo = Column(Unicode(36))
    docClass = Column(Unicode(36))
    accountingPeriod = Column(Integer)
    docId = Column(Unicode(36))
    accountingYear = Column(Integer)
    createdTime = Column(String(19, u'Chinese_PRC_CI_AS'))
    sequenceNumber = Column(Integer)
    ts = Column(TIMESTAMP)
    updated = Column(String(19, u'Chinese_PRC_CI_AS'))
    updatedBy = Column(Unicode(32))
    priuserdefnvc1 = Column(Unicode(500))
    priuserdefdecm1 = Column(Numeric(28, 14))
    priuserdefnvc2 = Column(Unicode(500))
    priuserdefdecm2 = Column(Numeric(28, 14))
    priuserdefnvc3 = Column(Unicode(500))
    priuserdefdecm3 = Column(Numeric(28, 14))
    priuserdefnvc4 = Column(Unicode(500))
    priuserdefdecm4 = Column(Numeric(28, 14))
    priuserdefnvc5 = Column(Unicode(500))
    priuserdefdecm5 = Column(Numeric(28, 14))
    priuserdefnvc6 = Column(Unicode(500))
    priuserdefdecm6 = Column(Numeric(28, 14))
    pubuserdefnvc1 = Column(Unicode(500))
    pubuserdefdecm1 = Column(Numeric(28, 14))
    pubuserdefnvc2 = Column(Unicode(500))
    pubuserdefdecm2 = Column(Numeric(28, 14))
    pubuserdefnvc3 = Column(Unicode(500))
    pubuserdefdecm3 = Column(Numeric(28, 14))
    pubuserdefnvc4 = Column(Unicode(500))
    pubuserdefdecm4 = Column(Numeric(28, 14))
    pubuserdefnvc5 = Column(Unicode(500))
    pubuserdefdecm5 = Column(Numeric(28, 14))
    pubuserdefnvc6 = Column(Unicode(500))
    pubuserdefdecm6 = Column(Numeric(28, 14))
    PrintCount = Column(Integer, nullable=False, server_default=text("((0))"))
    idcurrency = Column(Integer)
    IdMarketingOrgan = Column(Integer)
    id = Column(Integer, primary_key=True)
    voucherstate = Column(Integer)
    auditorId = Column(Integer)
    makerId = Column(Integer)


class ARAPExchangeAdjustApDetail(Base):
    __tablename__ = 'ARAP_ExchangeAdjust_ApDetail'

    code = Column(Unicode(30))
    name = Column(Unicode(200))
    voucherDate = Column(String(19, u'Chinese_PRC_CI_AS'))
    voucherCode = Column(Unicode(30))
    detailCode = Column(Unicode(50))
    detailName = Column(Unicode(50))
    origAmount = Column(Numeric(28, 14))
    amount = Column(Numeric(28, 14))
    adjustAmount = Column(Numeric(28, 14))
    differentAmount = Column(Numeric(28, 14))
    prepayFlag = Column(Integer)
    createdTime = Column(String(19, u'Chinese_PRC_CI_AS'))
    sequenceNumber = Column(Integer)
    ts = Column(TIMESTAMP)
    updated = Column(String(19, u'Chinese_PRC_CI_AS'))
    updatedBy = Column(Unicode(32))
    vouchertimestamp = Column(Unicode(64))
    sourcevouchermemo = Column(Unicode(200))
    saleordercode = Column(Unicode(30))
    sourceordercode = Column(Unicode(30))
    arrivalDate = Column(String(19, u'Chinese_PRC_CI_AS'))
    iddepartment = Column(Integer)
    IdMember = Column(Integer)
    detailID = Column(Integer)
    idpartner = Column(Integer)
    idperson = Column(Integer)
    IdDetailProject = Column(Integer)
    idproject = Column(Integer)
    idArapExchangeAdjustDTO = Column(Integer)
    id = Column(Integer, primary_key=True)
    voucherDetailID = Column(Integer)
    voucherID = Column(Integer)
    sourceorderid = Column(Integer)
    saleorderid = Column(Integer)
    idsourceordertype = Column(Integer)
    idvouchertype = Column(Integer)


class ARAPExchangeAdjustArDetail(Base):
    __tablename__ = 'ARAP_ExchangeAdjust_ArDetail'

    code = Column(Unicode(30))
    name = Column(Unicode(200))
    detailName = Column(Unicode(50))
    voucherDate = Column(String(19, u'Chinese_PRC_CI_AS'))
    adjustAmount = Column(Numeric(28, 14))
    origAmount = Column(Numeric(28, 14))
    detailCode = Column(Unicode(50))
    voucherCode = Column(Unicode(30))
    amount = Column(Numeric(28, 14))
    differentAmount = Column(Numeric(28, 14))
    prepayFlag = Column(Integer)
    createdTime = Column(String(19, u'Chinese_PRC_CI_AS'))
    sequenceNumber = Column(Integer)
    ts = Column(TIMESTAMP)
    updated = Column(String(19, u'Chinese_PRC_CI_AS'))
    updatedBy = Column(Unicode(32))
    vouchertimestamp = Column(Unicode(64))
    sourcevouchermemo = Column(Unicode(200))
    saleordercode = Column(Unicode(30))
    sourceordercode = Column(Unicode(30))
    arrivalDate = Column(String(19, u'Chinese_PRC_CI_AS'))
    iddepartment = Column(Integer)
    IdMember = Column(Integer)
    detailID = Column(Integer)
    idnosettlepartner = Column(Integer)
    idpartner = Column(Integer)
    idperson = Column(Integer)
    IdDetailProject = Column(Integer)
    idproject = Column(Integer)
    idArapExchangeAdjustDTO = Column(Integer)
    id = Column(Integer, primary_key=True)
    voucherDetailID = Column(Integer)
    voucherID = Column(Integer)
    sourceorderid = Column(Integer)
    saleorderid = Column(Integer)
    idsourceordertype = Column(Integer)
    idvouchertype = Column(Integer)


class ARAPOriginalAmount(Base):
    __tablename__ = 'ARAP_OriginalAmount'

    code = Column(Unicode(30))
    name = Column(Unicode(200))
    voucherDate = Column(String(19, u'Chinese_PRC_CI_AS'))
    maker = Column(Unicode(50))
    madeDate = Column(String(19, u'Chinese_PRC_CI_AS'))
    auditor = Column(Unicode(50))
    reviser = Column(Unicode(50))
    auditedDate = Column(String(19, u'Chinese_PRC_CI_AS'))
    isCarriedForwardOut = Column(Integer)
    isCarriedForwardIn = Column(Integer)
    isModifiedCode = Column(Integer)
    docNo = Column(Unicode(36))
    docClass = Column(Unicode(36))
    accountingPeriod = Column(Integer)
    docId = Column(Unicode(36))
    accountingYear = Column(Integer)
    createdTime = Column(String(19, u'Chinese_PRC_CI_AS'))
    sequenceNumber = Column(Integer)
    ts = Column(TIMESTAMP)
    updated = Column(String(19, u'Chinese_PRC_CI_AS'))
    updatedBy = Column(Unicode(32))
    id = Column(Integer, primary_key=True)
    auditorId = Column(Integer)
    makerId = Column(Integer)


class ARAPOriginalAmountApDetail(Base):
    __tablename__ = 'ARAP_OriginalAmount_ApDetail'

    code = Column(Unicode(30))
    name = Column(Unicode(200))
    origDate = Column(String(19, u'Chinese_PRC_CI_AS'))
    origPrepayAmount = Column(Numeric(28, 14))
    prepayAmount = Column(Numeric(28, 14))
    origAmount = Column(Numeric(28, 14))
    amount = Column(Numeric(28, 14))
    origBalanceAmount = Column(Numeric(28, 14))
    balanceAmount = Column(Numeric(28, 14))
    origTotalPrepayAmount = Column(Numeric(28, 14))
    totalPrepayAmount = Column(Numeric(28, 14))
    origTotalAmount = Column(Numeric(28, 14))
    totalAmount = Column(Numeric(28, 14))
    createdTime = Column(String(19, u'Chinese_PRC_CI_AS'))
    sequenceNumber = Column(Integer)
    ts = Column(TIMESTAMP)
    updated = Column(String(19, u'Chinese_PRC_CI_AS'))
    updatedBy = Column(Unicode(32))
    IsCarriedForwardOut = Column(Integer)
    isCarriedForwardIn = Column(Integer)
    arrivaldate = Column(String(19, u'Chinese_PRC_CI_AS'))
    OrigOtherAmount = Column(Numeric(28, 14), server_default=text("((0))"))
    OtherAmount = Column(Numeric(28, 14), server_default=text("((0))"))
    memo = Column(Unicode(200))
    ID = Column(Integer, primary_key=True)
    idcurrency = Column(Integer)
    iddepartment = Column(Integer)
    idpartner = Column(Integer)
    idperson = Column(Integer)
    idproject = Column(Integer)
    idArapOriginalAmountDTO = Column(Integer)


class ARAPOriginalAmountArDetail(Base):
    __tablename__ = 'ARAP_OriginalAmount_ArDetail'

    code = Column(Unicode(30))
    name = Column(Unicode(200))
    origDate = Column(String(19, u'Chinese_PRC_CI_AS'))
    origPrepayAmount = Column(Numeric(28, 14))
    prepayAmount = Column(Numeric(28, 14))
    origAmount = Column(Numeric(28, 14))
    amount = Column(Numeric(28, 14))
    origBalanceAmount = Column(Numeric(28, 14))
    balanceAmount = Column(Numeric(28, 14))
    origTotalPrepayAmount = Column(Numeric(28, 14))
    totalPrepayAmount = Column(Numeric(28, 14))
    origTotalAmount = Column(Numeric(28, 14))
    totalAmount = Column(Numeric(28, 14))
    createdTime = Column(String(19, u'Chinese_PRC_CI_AS'))
    sequenceNumber = Column(Integer)
    ts = Column(TIMESTAMP)
    updated = Column(String(19, u'Chinese_PRC_CI_AS'))
    updatedBy = Column(Unicode(32))
    IsCarriedForwardOut = Column(Integer)
    isCarriedForwardIn = Column(Integer)
    arrivaldate = Column(String(19, u'Chinese_PRC_CI_AS'))
    OrigOtherAmount = Column(Numeric(28, 14), server_default=text("((0))"))
    OtherAmount = Column(Numeric(28, 14), server_default=text("((0))"))
    memo = Column(Unicode(200))
    ID = Column(Integer, primary_key=True)
    idcurrency = Column(Integer)
    iddepartment = Column(Integer)
    idpartner = Column(Integer)
    idperson = Column(Integer)
    idproject = Column(Integer)
    idnosettlepartner = Column(Integer)
    idArapOriginalAmountDTO = Column(Integer)


class ARAPReceivePayment(Base):
    __tablename__ = 'ARAP_ReceivePayment'

    code = Column(Unicode(30))
    name = Column(Unicode(200))
    exchangeRate = Column(Numeric(28, 14))
    origAllowances = Column(Numeric(28, 14))
    allowances = Column(Numeric(28, 14))
    error = Column(Numeric(28, 14))
    memo = Column(Unicode(200))
    sourceVoucherCode = Column(Unicode(50))
    cancelOrigAmount = Column(Numeric(28, 14))
    cancelAmount = Column(Numeric(28, 14))
    isAuto = Column(Integer)
    origAmount = Column(Numeric(28, 14))
    amount = Column(Numeric(28, 14))
    origPaymentAmount = Column(Numeric(28, 14))
    paymentAmount = Column(Numeric(28, 14))
    isReceiveFlag = Column(Integer)
    voucherDate = Column(String(19, u'Chinese_PRC_CI_AS'))
    maker = Column(Unicode(50))
    madeDate = Column(String(19, u'Chinese_PRC_CI_AS'))
    auditor = Column(Unicode(50))
    reviser = Column(Unicode(50))
    auditedDate = Column(String(19, u'Chinese_PRC_CI_AS'))
    isCarriedForwardOut = Column(Integer)
    isCarriedForwardIn = Column(Integer)
    isModifiedCode = Column(Integer)
    docNo = Column(Unicode(36))
    docClass = Column(Unicode(36))
    accountingPeriod = Column(Integer)
    docId = Column(Unicode(36))
    accountingYear = Column(Integer)
    createdTime = Column(String(19, u'Chinese_PRC_CI_AS'))
    sequenceNumber = Column(Integer)
    ts = Column(TIMESTAMP)
    updated = Column(String(19, u'Chinese_PRC_CI_AS'))
    updatedBy = Column(Unicode(32))
    priuserdefnvc1 = Column(Unicode(500))
    priuserdefdecm1 = Column(Numeric(28, 14))
    priuserdefnvc2 = Column(Unicode(500))
    priuserdefdecm2 = Column(Numeric(28, 14))
    priuserdefnvc3 = Column(Unicode(500))
    priuserdefdecm3 = Column(Numeric(28, 14))
    priuserdefnvc4 = Column(Unicode(500))
    priuserdefdecm4 = Column(Numeric(28, 14))
    priuserdefnvc5 = Column(Unicode(500))
    priuserdefdecm5 = Column(Numeric(28, 14))
    priuserdefnvc6 = Column(Unicode(500))
    priuserdefdecm6 = Column(Numeric(28, 14))
    pubuserdefnvc1 = Column(Unicode(500))
    pubuserdefdecm1 = Column(Numeric(28, 14))
    pubuserdefnvc2 = Column(Unicode(500))
    pubuserdefdecm2 = Column(Numeric(28, 14))
    pubuserdefnvc3 = Column(Unicode(500))
    pubuserdefdecm3 = Column(Numeric(28, 14))
    pubuserdefnvc4 = Column(Unicode(500))
    pubuserdefdecm4 = Column(Numeric(28, 14))
    pubuserdefnvc5 = Column(Unicode(500))
    pubuserdefdecm5 = Column(Numeric(28, 14))
    pubuserdefnvc6 = Column(Unicode(500))
    pubuserdefdecm6 = Column(Numeric(28, 14))
    origoverPayment = Column(Numeric(28, 14))
    overPayment = Column(Numeric(28, 14))
    SaleOrderCode = Column(Unicode(50))
    PurchaseOrderCode = Column(Unicode(50))
    PrintCount = Column(Integer, nullable=False, server_default=text("((0))"))
    ID = Column(Integer, primary_key=True)
    idbusitype = Column(Integer)
    idcurrency = Column(Integer)
    iddepartment = Column(Integer)
    IdStore = Column(Integer)
    IdMarketingOrgan = Column(Integer)
    idpartner = Column(Integer)
    idperson = Column(Integer)
    idproject = Column(Integer)
    IdSettleStyle = Column(Integer)
    IdBankAccount = Column(Integer)
    sourceVoucherID = Column(Integer)
    cancelState = Column(Integer)
    settleTime = Column(Integer)
    voucherstate = Column(Integer)
    auditorId = Column(Integer)
    makerId = Column(Integer)
    PurchaseOrderID = Column(Integer)
    SaleOrderID = Column(Integer)
    idvouchertype = Column(Integer)


class ARAPReceivePaymentMultiPayment(Base):
    __tablename__ = 'ARAP_ReceivePayment_MultiPayment'

    code = Column(Unicode(30))
    name = Column(Unicode(200))
    voucherDate = Column(String(19, u'Chinese_PRC_CI_AS'))
    voucherCode = Column(Unicode(30))
    origAmount = Column(Numeric(28, 14))
    origNoCancelAmount = Column(Numeric(28, 14))
    origCancelAmount = Column(Numeric(28, 14))
    cancelAmount = Column(Numeric(28, 14))
    createdTime = Column(String(19, u'Chinese_PRC_CI_AS'))
    sequenceNumber = Column(Integer)
    ts = Column(TIMESTAMP)
    updated = Column(String(19, u'Chinese_PRC_CI_AS'))
    updatedBy = Column(Unicode(32))
    saleOrderCode = Column(Unicode(50))
    memo = Column(Unicode(200))
    id = Column(Integer, primary_key=True)
    iddepartment = Column(Integer)
    idperson = Column(Integer)
    idproject = Column(Integer)
    idArapReceivePaymentDTO = Column(Integer)
    voucherID = Column(Integer)
    saleOrderID = Column(Integer)
    idvouchertype = Column(Integer)


class ARAPReceivePaymentMultiSettle(Base):
    __tablename__ = 'ARAP_ReceivePayment_MultiSettle'

    code = Column(Unicode(30))
    name = Column(Unicode(200))
    documentCode = Column(Unicode(30))
    origAmount = Column(Numeric(28, 14))
    amount = Column(Numeric(28, 14))
    createdTime = Column(String(19, u'Chinese_PRC_CI_AS'))
    sequenceNumber = Column(Integer)
    ts = Column(TIMESTAMP)
    updated = Column(String(19, u'Chinese_PRC_CI_AS'))
    updatedBy = Column(Unicode(32))
    ID = Column(Integer, primary_key=True)
    idbankaccount = Column(Integer)
    idsettlestyle = Column(Integer)
    idArapReceivePaymentDTO = Column(Integer)


class ARAPReceivePaymentB(Base):
    __tablename__ = 'ARAP_ReceivePayment_b'

    code = Column(Unicode(30))
    name = Column(Unicode(200))
    voucherDate = Column(String(19, u'Chinese_PRC_CI_AS'))
    voucherCode = Column(Unicode(30))
    detailCode = Column(Unicode(50))
    detailName = Column(Unicode(200))
    exchangeRate = Column(Numeric(28, 14))
    origVoucherAmount = Column(Numeric(28, 14))
    origVoucherNoSettleAmount = Column(Numeric(28, 14))
    origAmount = Column(Numeric(28, 14))
    origNoSettleAmount = Column(Numeric(28, 14))
    origCurrentAmount = Column(Numeric(28, 14))
    currentAmount = Column(Numeric(28, 14))
    origAllowancesAmount = Column(Numeric(28, 14))
    allowancesAmount = Column(Numeric(28, 14))
    arrivalDate = Column(String(19, u'Chinese_PRC_CI_AS'))
    createdTime = Column(String(19, u'Chinese_PRC_CI_AS'))
    sequenceNumber = Column(Integer)
    ts = Column(TIMESTAMP)
    updated = Column(String(19, u'Chinese_PRC_CI_AS'))
    updatedBy = Column(Unicode(32))
    saleordercode = Column(Unicode(30))
    sourceordercode = Column(Unicode(30))
    vouchertimestamp = Column(Unicode(64))
    sourcevouchermemo = Column(Unicode(200))
    id = Column(Integer, primary_key=True)
    IdBusiType = Column(Integer)
    idcurrency = Column(Integer)
    iddepartment = Column(Integer)
    IdMember = Column(Integer)
    detailID = Column(Integer)
    idnosettlepartner = Column(Integer)
    idpartner = Column(Integer)
    idperson = Column(Integer)
    IdDetailProject = Column(Integer)
    idproject = Column(Integer)
    voucherDetailID = Column(Integer)
    idArapReceivePaymentDTO = Column(Integer)
    voucherID = Column(Integer)
    sourceorderid = Column(Integer)
    saleorderid = Column(Integer)
    idsourceordertype = Column(Integer)
    idvouchertype = Column(Integer)


class ARAPStrikeBalance(Base):
    __tablename__ = 'ARAP_StrikeBalance'

    code = Column(Unicode(30))
    name = Column(Unicode(200))
    origCurrentTotalAmount = Column(Numeric(28, 14))
    currentTotalAmount = Column(Numeric(28, 14))
    exchangeRate = Column(Numeric(28, 14))
    memo = Column(Unicode(200))
    voucherDate = Column(String(19, u'Chinese_PRC_CI_AS'))
    maker = Column(Unicode(50))
    madeDate = Column(String(19, u'Chinese_PRC_CI_AS'))
    auditor = Column(Unicode(50))
    reviser = Column(Unicode(50))
    auditedDate = Column(String(19, u'Chinese_PRC_CI_AS'))
    isCarriedForwardOut = Column(Integer)
    isCarriedForwardIn = Column(Integer)
    isModifiedCode = Column(Integer)
    docNo = Column(Unicode(36))
    docClass = Column(Unicode(36))
    accountingPeriod = Column(Integer)
    docId = Column(Unicode(36))
    accountingYear = Column(Integer)
    createdTime = Column(String(19, u'Chinese_PRC_CI_AS'))
    sequenceNumber = Column(Integer)
    ts = Column(TIMESTAMP)
    updated = Column(String(19, u'Chinese_PRC_CI_AS'))
    updatedBy = Column(Unicode(32))
    priuserdefnvc1 = Column(Unicode(500))
    priuserdefdecm1 = Column(Numeric(28, 14))
    priuserdefnvc2 = Column(Unicode(500))
    priuserdefdecm2 = Column(Numeric(28, 14))
    priuserdefnvc3 = Column(Unicode(500))
    priuserdefdecm3 = Column(Numeric(28, 14))
    priuserdefnvc4 = Column(Unicode(500))
    priuserdefdecm4 = Column(Numeric(28, 14))
    priuserdefnvc5 = Column(Unicode(500))
    priuserdefdecm5 = Column(Numeric(28, 14))
    priuserdefnvc6 = Column(Unicode(500))
    priuserdefdecm6 = Column(Numeric(28, 14))
    pubuserdefnvc1 = Column(Unicode(500))
    pubuserdefdecm1 = Column(Numeric(28, 14))
    pubuserdefnvc2 = Column(Unicode(500))
    pubuserdefdecm2 = Column(Numeric(28, 14))
    pubuserdefnvc3 = Column(Unicode(500))
    pubuserdefdecm3 = Column(Numeric(28, 14))
    pubuserdefnvc4 = Column(Unicode(500))
    pubuserdefdecm4 = Column(Numeric(28, 14))
    pubuserdefnvc5 = Column(Unicode(500))
    pubuserdefdecm5 = Column(Numeric(28, 14))
    pubuserdefnvc6 = Column(Unicode(500))
    pubuserdefdecm6 = Column(Numeric(28, 14))
    sourcevouchercode = Column(Unicode(30))
    isauto = Column(Integer)
    PrintCount = Column(Integer, nullable=False, server_default=text("((0))"))
    batchNo = Column(Unicode(20))
    ID = Column(Integer, primary_key=True)
    idbusitype = Column(Integer)
    idcurrency = Column(Integer)
    IdMarketingOrgan = Column(Integer)
    idfirstpartner = Column(Integer)
    idsecondpartner = Column(Integer)
    IdDepartment = Column(Integer)
    IdPerson = Column(Integer)
    IdProject = Column(Integer)
    sourcevoucherid = Column(Integer)
    voucherstate = Column(Integer)
    auditorId = Column(Integer)
    makerId = Column(Integer)
    idsourcevouchertype = Column(Integer)


class ARAPStrikeBalanceFirstDetail(Base):
    __tablename__ = 'ARAP_StrikeBalance_FirstDetail'

    code = Column(Unicode(30))
    name = Column(Unicode(200))
    voucherDate = Column(String(19, u'Chinese_PRC_CI_AS'))
    voucherCode = Column(Unicode(30))
    detailCode = Column(Unicode(50))
    detailName = Column(Unicode(200))
    exchangeRate = Column(Numeric(28, 14))
    origVoucherAmount = Column(Numeric(28, 14))
    origVoucherNoSettleAmount = Column(Numeric(28, 14))
    origAmount = Column(Numeric(28, 14))
    origNoSettleAmount = Column(Numeric(28, 14))
    origCurrentAmount = Column(Numeric(28, 14))
    currentAmount = Column(Numeric(28, 14))
    arrivalDate = Column(String(19, u'Chinese_PRC_CI_AS'))
    createdTime = Column(String(19, u'Chinese_PRC_CI_AS'))
    sequenceNumber = Column(Integer)
    ts = Column(TIMESTAMP)
    updated = Column(String(19, u'Chinese_PRC_CI_AS'))
    updatedBy = Column(Unicode(32))
    saleordercode = Column(Unicode(30))
    sourceordercode = Column(Unicode(30))
    vouchertimestamp = Column(Unicode(64))
    sourcevouchermemo = Column(Unicode(200))
    id = Column(Integer, primary_key=True)
    IdBusiType = Column(Integer)
    idcurrency = Column(Integer)
    iddepartment = Column(Integer)
    IdMember = Column(Integer)
    detailID = Column(Integer)
    idnosettlepartner = Column(Integer)
    idperson = Column(Integer)
    IdDetailProject = Column(Integer)
    idproject = Column(Integer)
    voucherDetailID = Column(Integer)
    voucherID = Column(Integer)
    idArapStrikeBalanceDTO = Column(Integer)
    sourceorderid = Column(Integer)
    saleorderid = Column(Integer)
    idsourceordertype = Column(Integer)
    idvouchertype = Column(Integer)


class ARAPStrikeBalanceRetailSettle(Base):
    __tablename__ = 'ARAP_StrikeBalance_RetailSettle'

    ts = Column(TIMESTAMP, nullable=False)
    updatedBy = Column(Unicode(32))
    updated = Column(String(19, u'Chinese_PRC_CI_AS'))
    id = Column(Integer, primary_key=True)
    idArapStrikeBalanceDTO = Column(Integer, nullable=False, server_default=text("((0))"))
    idRetailSettleDTO = Column(Integer, nullable=False, server_default=text("((0))"))


class ARAPStrikeBalanceSecondDetail(Base):
    __tablename__ = 'ARAP_StrikeBalance_SecondDetail'

    code = Column(Unicode(30))
    name = Column(Unicode(200))
    voucherDate = Column(String(19, u'Chinese_PRC_CI_AS'))
    voucherCode = Column(Unicode(30))
    detailCode = Column(Unicode(50))
    detailName = Column(Unicode(200))
    exchangeRate = Column(Numeric(28, 14))
    origVoucherAmount = Column(Numeric(28, 14))
    origVoucherNoSettleAmount = Column(Numeric(28, 14))
    origAmount = Column(Numeric(28, 14))
    origNoSettleAmount = Column(Numeric(28, 14))
    origCurrentAmount = Column(Numeric(28, 14))
    currentAmount = Column(Numeric(28, 14))
    arrivalDate = Column(String(19, u'Chinese_PRC_CI_AS'))
    createdTime = Column(String(19, u'Chinese_PRC_CI_AS'))
    sequenceNumber = Column(Integer)
    ts = Column(TIMESTAMP)
    updated = Column(String(19, u'Chinese_PRC_CI_AS'))
    updatedBy = Column(Unicode(32))
    saleordercode = Column(Unicode(30))
    sourceordercode = Column(Unicode(30))
    vouchertimestamp = Column(Unicode(64))
    sourcevouchermemo = Column(Unicode(200))
    id = Column(Integer, primary_key=True)
    IdBusiType = Column(Integer)
    idcurrency = Column(Integer)
    iddepartment = Column(Integer)
    IdMember = Column(Integer)
    detailID = Column(Integer)
    idnosettlepartner = Column(Integer)
    idperson = Column(Integer)
    IdDetailProject = Column(Integer)
    idproject = Column(Integer)
    voucherDetailID = Column(Integer)
    voucherID = Column(Integer)
    idArapStrikeBalanceDTO = Column(Integer)
    sourceorderid = Column(Integer)
    saleorderid = Column(Integer)
    idsourceordertype = Column(Integer)
    idvouchertype = Column(Integer)


t_B2B_InventoryClassUploadLog = Table(
    'B2B_InventoryClassUploadLog', metadata,
    Column('id', Integer, nullable=False),
    Column('idInventoryClass', Integer),
    Column('B2BInventoryClassCode', Unicode(50)),
    Column('inventoryClassTS', LargeBinary(8)),
    Column('uploadDate', DateTime)
)


t_B2B_InventoryUploadLog = Table(
    'B2B_InventoryUploadLog', metadata,
    Column('id', Integer, nullable=False),
    Column('idInventory', Integer),
    Column('B2BInventoryCode', Unicode(50)),
    Column('inventoryTS', LargeBinary(8)),
    Column('uploadDate', DateTime)
)


t_B2B_PartnerClassUploadLog = Table(
    'B2B_PartnerClassUploadLog', metadata,
    Column('id', Integer, nullable=False),
    Column('idPartnerClass', Integer),
    Column('B2BPartnerClassCode', Unicode(50)),
    Column('partnerClassTS', LargeBinary(8)),
    Column('uploadDate', DateTime)
)


t_B2B_PartnerUploadLog = Table(
    'B2B_PartnerUploadLog', metadata,
    Column('id', Integer, nullable=False),
    Column('idPartner', Integer),
    Column('B2BPartnerCode', Unicode(50)),
    Column('partnerTS', LargeBinary(8)),
    Column('uploadDate', DateTime)
)


class BAPDelLogTable(Base):
    __tablename__ = 'BAP_DelLogTable'

    TableName = Column(Unicode(100))
    ts = Column(TIMESTAMP)
    id = Column(Integer, primary_key=True)
    DelID = Column(Integer)


class CSBankCashAccessVoucher(Base):
    __tablename__ = 'CS_BankCashAccessVoucher'

    code = Column(Unicode(30))
    name = Column(Unicode(200))
    memo = Column(Unicode(200))
    origInAmount = Column(Numeric(28, 14))
    origOutAmount = Column(Numeric(28, 14))
    documentCode = Column(Unicode(30))
    inAmount = Column(Numeric(28, 14))
    outAmount = Column(Numeric(28, 14))
    inExchangeRate = Column(Numeric(28, 14))
    outExchangeRate = Column(Numeric(28, 14))
    difference = Column(Numeric(28, 14))
    oldeVoucherDate = Column(String(19, u'Chinese_PRC_CI_AS'))
    voucherdate = Column(String(19, u'Chinese_PRC_CI_AS'))
    maker = Column(Unicode(50))
    madedate = Column(String(19, u'Chinese_PRC_CI_AS'))
    auditor = Column(Unicode(50))
    reviser = Column(Unicode(50))
    auditeddate = Column(String(19, u'Chinese_PRC_CI_AS'))
    iscarriedforwardout = Column(Integer)
    iscarriedforwardin = Column(Integer)
    ismodifiedcode = Column(Integer)
    docno = Column(Unicode(36))
    docclass = Column(Unicode(36))
    accountingperiod = Column(Integer)
    docid = Column(Unicode(36))
    accountingyear = Column(Integer)
    createdtime = Column(String(19, u'Chinese_PRC_CI_AS'))
    sequencenumber = Column(Integer)
    ts = Column(TIMESTAMP)
    updated = Column(String(19, u'Chinese_PRC_CI_AS'))
    updatedBy = Column(Unicode(32))
    priuserdefnvc1 = Column(Unicode(500))
    priuserdefdecm1 = Column(Numeric(28, 14))
    priuserdefnvc2 = Column(Unicode(500))
    priuserdefdecm2 = Column(Numeric(28, 14))
    priuserdefnvc3 = Column(Unicode(500))
    priuserdefdecm3 = Column(Numeric(28, 14))
    priuserdefnvc4 = Column(Unicode(500))
    priuserdefdecm4 = Column(Numeric(28, 14))
    priuserdefnvc5 = Column(Unicode(500))
    priuserdefdecm5 = Column(Numeric(28, 14))
    priuserdefnvc6 = Column(Unicode(500))
    priuserdefdecm6 = Column(Numeric(28, 14))
    pubuserdefnvc1 = Column(Unicode(500))
    pubuserdefdecm1 = Column(Numeric(28, 14))
    pubuserdefnvc2 = Column(Unicode(500))
    pubuserdefdecm2 = Column(Numeric(28, 14))
    pubuserdefnvc3 = Column(Unicode(500))
    pubuserdefdecm3 = Column(Numeric(28, 14))
    pubuserdefnvc4 = Column(Unicode(500))
    pubuserdefdecm4 = Column(Numeric(28, 14))
    pubuserdefnvc5 = Column(Unicode(500))
    pubuserdefdecm5 = Column(Numeric(28, 14))
    pubuserdefnvc6 = Column(Unicode(500))
    pubuserdefdecm6 = Column(Numeric(28, 14))
    PrintCount = Column(Integer, nullable=False, server_default=text("((0))"))
    ID = Column(Integer, primary_key=True)
    idinbankaccount = Column(Integer)
    idoutbankaccount = Column(Integer)
    idbusinesstype = Column(Integer)
    idoldbusinesstype = Column(Integer)
    idInDepartment = Column(Integer)
    idOutDepartment = Column(Integer)
    IdMarketingOrgan = Column(Integer)
    idhandler = Column(Integer)
    idInProject = Column(Integer)
    idOutProject = Column(Integer)
    idOutSettleStyle = Column(Integer)
    idInSettleStyle = Column(Integer)
    voucherstate = Column(Integer)
    auditorid = Column(Integer)
    makerid = Column(Integer)


class CSBankCheckAccount(Base):
    __tablename__ = 'CS_BankCheckAccount'

    code = Column(Unicode(30))
    name = Column(Unicode(200))
    sourcedate = Column(String(19, u'Chinese_PRC_CI_AS'))
    summary = Column(Unicode(1024))
    billNumber = Column(Unicode(50))
    origAmountDr = Column(Numeric(28, 14))
    origAmountCr = Column(Numeric(28, 14))
    tickcode = Column(Unicode(50))
    tickdate = Column(String(19, u'Chinese_PRC_CI_AS'))
    billdate = Column(String(19, u'Chinese_PRC_CI_AS'))
    createdtime = Column(String(19, u'Chinese_PRC_CI_AS'))
    sequencenumber = Column(Integer)
    ts = Column(TIMESTAMP, nullable=False)
    updated = Column(String(19, u'Chinese_PRC_CI_AS'))
    updatedBy = Column(Unicode(32))
    id = Column(Integer, primary_key=True)
    idbankaccount = Column(Integer)
    idsourcevoucherbusitype = Column(Integer)
    idsettlestyle = Column(Integer)
    idOtherPartner = Column(Integer)
    voucherdetailid = Column(Integer)
    voucherid = Column(Integer)
    tickstate = Column(Integer)


class CSBankCheckAccountVoucher(Base):
    __tablename__ = 'CS_BankCheckAccountVoucher'

    code = Column(Unicode(30))
    name = Column(Unicode(200))
    origPeriodBeginBalance = Column(Numeric(28, 14))
    summary = Column(Unicode(1024))
    billNumber = Column(Unicode(50))
    origAmountDr = Column(Numeric(28, 14))
    origAmountCr = Column(Numeric(28, 14))
    origBalance = Column(Numeric(28, 14))
    tickcode = Column(Unicode(50))
    tickdate = Column(String(19, u'Chinese_PRC_CI_AS'))
    docno = Column(Unicode(36))
    docclass = Column(Unicode(36))
    accountingperiod = Column(Integer)
    docid = Column(Unicode(36))
    accountingyear = Column(Integer)
    memo = Column(Unicode(50))
    voucherdate = Column(String(19, u'Chinese_PRC_CI_AS'))
    madedate = Column(String(19, u'Chinese_PRC_CI_AS'))
    maker = Column(Unicode(50))
    auditor = Column(Unicode(50))
    auditeddate = Column(String(19, u'Chinese_PRC_CI_AS'))
    reviser = Column(Unicode(50))
    iscarriedforwardout = Column(Integer)
    iscarriedforwardin = Column(Integer)
    ismodifiedcode = Column(Integer)
    createdtime = Column(String(19, u'Chinese_PRC_CI_AS'))
    sequencenumber = Column(Integer)
    ts = Column(TIMESTAMP, nullable=False)
    updated = Column(String(19, u'Chinese_PRC_CI_AS'))
    updatedBy = Column(Unicode(32))
    ID = Column(Integer, primary_key=True)
    idbankaccount = Column(Integer)
    idsettlestyle = Column(Integer)
    idOtherPartner = Column(Integer)
    tickstate = Column(Integer)
    voucherstate = Column(Integer)
    auditorid = Column(Integer)
    makerid = Column(Integer)


class CSCashAccount(Base):
    __tablename__ = 'CS_CashAccount'

    code = Column(Unicode(30))
    name = Column(Unicode(200))
    sourceVoucherDate = Column(String(19, u'Chinese_PRC_CI_AS'))
    sourceVoucherCode = Column(Unicode(30))
    sourceVoucherMaker = Column(Unicode(50))
    sourceVoucherAuditor = Column(Unicode(50))
    sourceVoucherMemo = Column(Unicode(200))
    origInAmount = Column(Numeric(28, 14))
    origOutAmount = Column(Numeric(28, 14))
    origAmount = Column(Numeric(28, 14))
    isPeriodBeginning = Column(Integer)
    sourceVoucherCreatedTime = Column(String(19, u'Chinese_PRC_CI_AS'))
    sourceVoucherDocumentCode = Column(Unicode(30))
    accountingYear = Column(Integer)
    accountingPeriod = Column(Integer)
    docNo = Column(Unicode(36))
    docId = Column(Unicode(36))
    docClass = Column(Unicode(36))
    year = Column(Integer)
    period = Column(Integer)
    iscarriedforwardin = Column(Integer)
    iscarriedforwardout = Column(Integer)
    createdtime = Column(String(19, u'Chinese_PRC_CI_AS'))
    sequencenumber = Column(Integer)
    ts = Column(TIMESTAMP)
    updated = Column(String(19, u'Chinese_PRC_CI_AS'))
    updatedBy = Column(Unicode(32))
    inamount = Column(Numeric(28, 14))
    outamount = Column(Numeric(28, 14))
    amount = Column(Numeric(28, 14))
    ispullin = Column(Integer)
    inexchangerate = Column(Numeric(28, 14))
    outexchangerate = Column(Numeric(28, 14))
    exchangerate = Column(Numeric(28, 14))
    OrigTotalDrAmount = Column(Numeric(28, 14))
    TotalDrAmount = Column(Numeric(28, 14))
    OrigTotalCrAmount = Column(Numeric(28, 14))
    TotalCrAmount = Column(Numeric(28, 14))
    id = Column(Integer, primary_key=True)
    idbankaccount = Column(Integer)
    idsourcevoucherbusinesstype = Column(Integer)
    iddepartment = Column(Integer)
    IdMarketingOrgan = Column(Integer)
    idpartner = Column(Integer)
    idperson = Column(Integer)
    idproject = Column(Integer)
    idsettlestyle = Column(Integer)
    IdOtherBankAccount = Column(Integer)
    IdIncome = Column(Integer)
    IdExpenseItem = Column(Integer)
    sourceVoucherID = Column(Integer)
    sourceMultiSettleID = Column(Integer)
    SourceVoucherMakerId = Column(Integer)
    idsourcevouchertype = Column(Integer)


class CSCashAccountDaily(Base):
    __tablename__ = 'CS_CashAccountDaily'

    code = Column(Unicode(30))
    name = Column(Unicode(200))
    summary = Column(Unicode(1024))
    billDate = Column(String(19, u'Chinese_PRC_CI_AS'))
    billCode = Column(Unicode(50))
    account = Column(Unicode(50))
    origAmountDr = Column(Numeric(28, 14))
    exchangeDr = Column(Numeric(28, 14))
    amountDr = Column(Numeric(28, 14))
    origAmountCr = Column(Numeric(28, 14))
    exchangeCr = Column(Numeric(28, 14))
    amountCr = Column(Numeric(28, 14))
    origBalance = Column(Numeric(28, 14))
    balance = Column(Numeric(28, 14))
    isAuto = Column(Integer)
    sourceVoucherCode = Column(Unicode(50))
    sourceVoucherDate = Column(String(19, u'Chinese_PRC_CI_AS'))
    docclassno = Column(Unicode(50))
    tickcode = Column(Unicode(50))
    tickdate = Column(String(19, u'Chinese_PRC_CI_AS'))
    year = Column(Integer)
    period = Column(Numeric(28, 14))
    docno = Column(Unicode(36))
    docclass = Column(Unicode(36))
    accountingperiod = Column(Integer)
    docid = Column(Unicode(36))
    accountingyear = Column(Integer)
    memo = Column(Unicode(200))
    voucherdate = Column(String(19, u'Chinese_PRC_CI_AS'))
    madedate = Column(String(19, u'Chinese_PRC_CI_AS'))
    maker = Column(Unicode(50))
    auditor = Column(Unicode(50))
    auditeddate = Column(String(19, u'Chinese_PRC_CI_AS'))
    reviser = Column(Unicode(50))
    iscarriedforwardout = Column(Integer)
    iscarriedforwardin = Column(Integer)
    ismodifiedcode = Column(Integer)
    createdtime = Column(String(19, u'Chinese_PRC_CI_AS'))
    sequencenumber = Column(Integer)
    ts = Column(TIMESTAMP, nullable=False)
    updated = Column(String(19, u'Chinese_PRC_CI_AS'))
    updatedBy = Column(Unicode(32))
    priuserdefnvc1 = Column(Unicode(500))
    priuserdefdecm1 = Column(Numeric(28, 14))
    priuserdefnvc2 = Column(Unicode(500))
    priuserdefdecm2 = Column(Numeric(28, 14))
    priuserdefnvc3 = Column(Unicode(500))
    priuserdefdecm3 = Column(Numeric(28, 14))
    priuserdefnvc4 = Column(Unicode(500))
    priuserdefdecm4 = Column(Numeric(28, 14))
    pubuserdefnvc1 = Column(Unicode(500))
    pubuserdefdecm1 = Column(Numeric(28, 14))
    pubuserdefnvc2 = Column(Unicode(500))
    pubuserdefdecm2 = Column(Numeric(28, 14))
    pubuserdefnvc3 = Column(Unicode(500))
    pubuserdefdecm3 = Column(Numeric(28, 14))
    pubuserdefnvc4 = Column(Unicode(500))
    pubuserdefdecm4 = Column(Numeric(28, 14))
    isPushAuto = Column(Integer)
    ID = Column(Integer, primary_key=True)
    idbankaccount = Column(Integer)
    idProDepartment = Column(Integer)
    iddoctype = Column(Integer)
    IdMarketingOrgan = Column(Integer)
    idOtherPartner = Column(Integer)
    idperson = Column(Integer)
    idproject = Column(Integer)
    idsettlestyle = Column(Integer)
    IdIncome = Column(Integer)
    IdExpenseItem = Column(Integer)
    IdAccount = Column(Integer)
    IdOtherBankAccount = Column(Integer)
    IdOtherProject = Column(Integer)
    IdOtherDepartment = Column(Integer)
    sourceVoucherID = Column(Integer)
    sourceMultiSettleID = Column(Integer)
    direction = Column(Integer)
    tickstate = Column(Integer)
    voucherstate = Column(Integer)
    auditorid = Column(Integer)
    makerid = Column(Integer)
    idsourcevouchertype = Column(Integer)


class CSCashAccountPeriodBeginning(Base):
    __tablename__ = 'CS_CashAccountPeriodBeginning'

    code = Column(Unicode(30))
    name = Column(Unicode(200))
    voucherdate = Column(String(19, u'Chinese_PRC_CI_AS'))
    maker = Column(Unicode(50))
    madedate = Column(String(19, u'Chinese_PRC_CI_AS'))
    auditor = Column(Unicode(50))
    reviser = Column(Unicode(50))
    auditeddate = Column(String(19, u'Chinese_PRC_CI_AS'))
    iscarriedforwardout = Column(Integer)
    iscarriedforwardin = Column(Integer)
    ismodifiedcode = Column(Integer)
    docno = Column(Unicode(36))
    docclass = Column(Unicode(36))
    accountingperiod = Column(Integer)
    docid = Column(Unicode(36))
    accountingyear = Column(Integer)
    createdtime = Column(String(19, u'Chinese_PRC_CI_AS'))
    sequencenumber = Column(Integer)
    ts = Column(TIMESTAMP)
    updated = Column(String(19, u'Chinese_PRC_CI_AS'))
    updatedBy = Column(Unicode(32))
    memo = Column(Unicode(200))
    ID = Column(Integer, primary_key=True)
    voucherstate = Column(Integer)
    auditorid = Column(Integer)
    makerid = Column(Integer)


class CSCashAccountPeriodBeginningB(Base):
    __tablename__ = 'CS_CashAccountPeriodBeginning_b'

    code = Column(Unicode(30))
    name = Column(Unicode(200))
    origAmount = Column(Numeric(28, 14))
    createdtime = Column(String(19, u'Chinese_PRC_CI_AS'))
    sequencenumber = Column(Integer)
    ts = Column(TIMESTAMP)
    updated = Column(String(19, u'Chinese_PRC_CI_AS'))
    updatedBy = Column(Unicode(32))
    amount = Column(Numeric(28, 14))
    currency = Column(Unicode(50))
    OrigTotalDrAmount = Column(Numeric(28, 14))
    TotalDrAmount = Column(Numeric(28, 14))
    OrigTotalCrAmount = Column(Numeric(28, 14))
    TotalCrAmount = Column(Numeric(28, 14))
    ID = Column(Integer, primary_key=True)
    idbankaccount = Column(Integer)
    idCashAccountPeriodBeginningDTO = Column(Integer)


class CSCashCheckVoucher(Base):
    __tablename__ = 'CS_CashCheckVoucher'

    code = Column(Unicode(30))
    name = Column(Unicode(200))
    origRealAmount = Column(Numeric(28, 14))
    origAccountAmount = Column(Numeric(28, 14))
    origProfitLossAmount = Column(Numeric(28, 14))
    profitLossAmount = Column(Numeric(28, 14))
    exchange = Column(Numeric(28, 14))
    docno = Column(Unicode(36))
    docclass = Column(Unicode(36))
    accountingperiod = Column(Integer)
    docid = Column(Unicode(36))
    accountingyear = Column(Integer)
    memo = Column(Unicode(200))
    voucherdate = Column(String(19, u'Chinese_PRC_CI_AS'))
    madedate = Column(String(19, u'Chinese_PRC_CI_AS'))
    maker = Column(Unicode(50))
    auditor = Column(Unicode(50))
    auditeddate = Column(String(19, u'Chinese_PRC_CI_AS'))
    reviser = Column(Unicode(50))
    iscarriedforwardout = Column(Integer)
    iscarriedforwardin = Column(Integer)
    ismodifiedcode = Column(Integer)
    createdtime = Column(String(19, u'Chinese_PRC_CI_AS'))
    sequencenumber = Column(Integer)
    ts = Column(TIMESTAMP, nullable=False)
    updated = Column(String(19, u'Chinese_PRC_CI_AS'))
    updatedBy = Column(Unicode(32))
    priuserdefnvc1 = Column(Unicode(500))
    priuserdefnvc2 = Column(Unicode(500))
    priuserdefnvc3 = Column(Unicode(500))
    priuserdefnvc4 = Column(Unicode(500))
    priuserdefnvc5 = Column(Unicode(500))
    priuserdefnvc6 = Column(Unicode(500))
    priuserdefdecm1 = Column(Numeric(28, 14))
    priuserdefdecm2 = Column(Numeric(28, 14))
    priuserdefdecm3 = Column(Numeric(28, 14))
    priuserdefdecm4 = Column(Numeric(28, 14))
    priuserdefdecm5 = Column(Numeric(28, 14))
    priuserdefdecm6 = Column(Numeric(28, 14))
    pubuserdefnvc1 = Column(Unicode(500))
    pubuserdefnvc2 = Column(Unicode(500))
    pubuserdefnvc3 = Column(Unicode(500))
    pubuserdefnvc4 = Column(Unicode(500))
    pubuserdefnvc5 = Column(Unicode(500))
    pubuserdefnvc6 = Column(Unicode(500))
    pubuserdefdecm1 = Column(Numeric(28, 14))
    pubuserdefdecm2 = Column(Numeric(28, 14))
    pubuserdefdecm3 = Column(Numeric(28, 14))
    pubuserdefdecm4 = Column(Numeric(28, 14))
    pubuserdefdecm5 = Column(Numeric(28, 14))
    pubuserdefdecm6 = Column(Numeric(28, 14))
    PrintCount = Column(Integer, nullable=False, server_default=text("((0))"))
    ID = Column(Integer, primary_key=True)
    idbankaccount = Column(Integer)
    IdMarketingOrgan = Column(Integer)
    idperson = Column(Integer)
    checkState = Column(Integer)
    voucherstate = Column(Integer)
    auditorid = Column(Integer)
    makerid = Column(Integer)


class CSCashCheckVoucherDetail(Base):
    __tablename__ = 'CS_CashCheckVoucherDetail'

    code = Column(Unicode(30))
    name = Column(Unicode(200))
    quantity = Column(Integer)
    origAmount = Column(Numeric(28, 14))
    createdtime = Column(String(19, u'Chinese_PRC_CI_AS'))
    sequencenumber = Column(Integer)
    ts = Column(TIMESTAMP, nullable=False)
    updated = Column(String(19, u'Chinese_PRC_CI_AS'))
    updatedBy = Column(Unicode(32))
    id = Column(Integer, primary_key=True)
    idtickettype = Column(Integer)
    idCashCheckVoucherDTO = Column(Integer)


class CSCheque(Base):
    __tablename__ = 'CS_Cheque'

    code = Column(Unicode(30))
    name = Column(Unicode(200))
    billDate = Column(String(19, u'Chinese_PRC_CI_AS'))
    origbillamout = Column(Numeric(28, 14))
    origLimitAmount = Column(Numeric(28, 14))
    reimbursedate = Column(String(19, u'Chinese_PRC_CI_AS'))
    origreimburseamount = Column(Numeric(28, 14))
    reimbursememo = Column(Unicode(50))
    sourcevouchercode = Column(Unicode(50))
    invalidatedate = Column(String(19, u'Chinese_PRC_CI_AS'))
    invalidatememo = Column(Unicode(50))
    receiver = Column(Unicode(50))
    receiveaccount = Column(Unicode(50))
    receivebank = Column(Unicode(50))
    paymenter = Column(Unicode(50))
    isautoreimburse = Column(Integer)
    documentsusage = Column(Unicode(50))
    billcode = Column(Unicode(50))
    settledetailid = Column(Unicode(1024))
    notepwd = Column(Unicode(50))
    docno = Column(Unicode(36))
    docclass = Column(Unicode(36))
    accountingperiod = Column(Integer)
    docid = Column(Unicode(36))
    accountingyear = Column(Integer)
    memo = Column(Unicode(50))
    voucherdate = Column(String(19, u'Chinese_PRC_CI_AS'))
    madedate = Column(String(19, u'Chinese_PRC_CI_AS'))
    maker = Column(Unicode(50))
    auditor = Column(Unicode(50))
    auditeddate = Column(String(19, u'Chinese_PRC_CI_AS'))
    reviser = Column(Unicode(50))
    iscarriedforwardout = Column(Integer)
    iscarriedforwardin = Column(Integer)
    ismodifiedcode = Column(Integer)
    createdtime = Column(String(19, u'Chinese_PRC_CI_AS'))
    sequencenumber = Column(Integer)
    ts = Column(TIMESTAMP, nullable=False)
    updated = Column(String(19, u'Chinese_PRC_CI_AS'))
    updatedBy = Column(Unicode(32))
    id = Column(Integer, primary_key=True)
    idpaymentbankaccount = Column(Integer)
    idreceivebankaccount = Column(Integer)
    idreimbursedepartment = Column(Integer)
    idusedepartment = Column(Integer)
    idcancler = Column(Integer)
    idorigreimburseperson = Column(Integer)
    iduser = Column(Integer)
    iduserperson = Column(Integer)
    idwriteoffer = Column(Integer)
    sourceVoucherID = Column(Integer)
    idChequeBookDTO = Column(Integer)
    voucherstate = Column(Integer)
    voucherstatebeforeclose = Column(Integer)
    auditorid = Column(Integer)
    makerid = Column(Integer)
    idsourcevouchertype = Column(Integer)


class CSChequeBook(Base):
    __tablename__ = 'CS_ChequeBook'

    code = Column(Unicode(30))
    name = Column(Unicode(200))
    chequecodebegin = Column(Unicode(50))
    number = Column(Integer)
    chequecodeend = Column(Unicode(50))
    numbernouse = Column(Integer)
    numberuse = Column(Integer)
    numberreimburse = Column(Integer)
    numberinvalidate = Column(Integer)
    buydate = Column(String(19, u'Chinese_PRC_CI_AS'))
    buynode = Column(Unicode(50))
    printtemplate = Column(Unicode(50))
    buyoperateperson = Column(Unicode(50))
    printtemplateid = Column(Unicode(50))
    docno = Column(Unicode(36))
    docclass = Column(Unicode(36))
    accountingperiod = Column(Integer)
    docid = Column(Unicode(36))
    accountingyear = Column(Integer)
    memo = Column(Unicode(50))
    voucherdate = Column(String(19, u'Chinese_PRC_CI_AS'))
    madedate = Column(String(19, u'Chinese_PRC_CI_AS'))
    maker = Column(Unicode(50))
    auditor = Column(Unicode(50))
    auditeddate = Column(String(19, u'Chinese_PRC_CI_AS'))
    reviser = Column(Unicode(50))
    iscarriedforwardout = Column(Integer)
    iscarriedforwardin = Column(Integer)
    ismodifiedcode = Column(Integer)
    createdtime = Column(String(19, u'Chinese_PRC_CI_AS'))
    sequencenumber = Column(Integer)
    ts = Column(TIMESTAMP, nullable=False)
    updated = Column(String(19, u'Chinese_PRC_CI_AS'))
    updatedBy = Column(Unicode(32))
    id = Column(Integer, primary_key=True)
    idbankaccount = Column(Integer)
    iddepartment = Column(Integer)
    idbuyperson = Column(Integer)
    idsettlestyle = Column(Integer)
    voucherstate = Column(Integer)
    auditorid = Column(Integer)
    makerid = Column(Integer)


t_CS_DataNoteRelate = Table(
    'CS_DataNoteRelate', metadata,
    Column('ID', Integer, nullable=False),
    Column('OutSysName', Unicode(50)),
    Column('PrjCode', Unicode(20), nullable=False),
    Column('NoteID', Unicode(128), nullable=False),
    Column('RelateXml', UnicodeText(1073741823), nullable=False)
)


t_CS_DataProject = Table(
    'CS_DataProject', metadata,
    Column('ID', Integer, nullable=False),
    Column('OutSysName', Unicode(50)),
    Column('PrjCode', Unicode(20), nullable=False),
    Column('PrjName', Unicode(100), nullable=False),
    Column('PrjFormatXml', UnicodeText(1073741823), nullable=False)
)


t_CS_DefPrinterParam = Table(
    'CS_DefPrinterParam', metadata,
    Column('ID', Integer, nullable=False),
    Column('OSVer', Integer),
    Column('DriverName', Unicode(50)),
    Column('PrintOrient', Integer),
    Column('PrintType', Integer),
    Column('PaperMode', Integer, server_default=text("((0))")),
    Column('PaperSize', Integer),
    Column('PaperName', Unicode(50)),
    Column('PaperAlign', Integer),
    Column('PrintX', Float(53)),
    Column('PrintY', Float(53)),
    Column('Image1', LargeBinary),
    Column('Image2', LargeBinary),
    Column('MicroAdjust', Integer)
)


class CSExpenseVoucher(Base):
    __tablename__ = 'CS_ExpenseVoucher'

    code = Column(Unicode(30))
    name = Column(Unicode(200))
    exchangeRate = Column(Numeric(28, 14))
    sourceVoucherCode = Column(Unicode(30))
    memo = Column(Unicode(200))
    origAmount = Column(Numeric(28, 14))
    invoiceCode = Column(Unicode(30))
    origTaxAmountSum = Column(Numeric(28, 14))
    arrivalDate = Column(String(19, u'Chinese_PRC_CI_AS'))
    oldVoucherDate = Column(String(19, u'Chinese_PRC_CI_AS'))
    amount = Column(Numeric(28, 14))
    taxAmountSum = Column(Numeric(28, 14))
    voucherdate = Column(String(19, u'Chinese_PRC_CI_AS'))
    maker = Column(Unicode(50))
    madedate = Column(String(19, u'Chinese_PRC_CI_AS'))
    auditor = Column(Unicode(50))
    reviser = Column(Unicode(50))
    auditeddate = Column(String(19, u'Chinese_PRC_CI_AS'))
    iscarriedforwardout = Column(Integer)
    iscarriedforwardin = Column(Integer)
    ismodifiedcode = Column(Integer)
    docno = Column(Unicode(36))
    docclass = Column(Unicode(36))
    accountingperiod = Column(Integer)
    docid = Column(Unicode(36))
    accountingyear = Column(Integer)
    createdtime = Column(String(19, u'Chinese_PRC_CI_AS'))
    sequencenumber = Column(Integer)
    ts = Column(TIMESTAMP)
    updated = Column(String(19, u'Chinese_PRC_CI_AS'))
    updatedBy = Column(Unicode(32))
    priuserdefnvc1 = Column(Unicode(500))
    priuserdefdecm1 = Column(Numeric(28, 14))
    priuserdefnvc2 = Column(Unicode(500))
    priuserdefdecm2 = Column(Numeric(28, 14))
    priuserdefnvc3 = Column(Unicode(500))
    priuserdefdecm3 = Column(Numeric(28, 14))
    priuserdefnvc4 = Column(Unicode(500))
    priuserdefdecm4 = Column(Numeric(28, 14))
    priuserdefnvc5 = Column(Unicode(500))
    priuserdefdecm5 = Column(Numeric(28, 14))
    priuserdefnvc6 = Column(Unicode(500))
    priuserdefdecm6 = Column(Numeric(28, 14))
    pubuserdefnvc1 = Column(Unicode(500))
    pubuserdefdecm1 = Column(Numeric(28, 14))
    pubuserdefnvc2 = Column(Unicode(500))
    pubuserdefdecm2 = Column(Numeric(28, 14))
    pubuserdefnvc3 = Column(Unicode(500))
    pubuserdefdecm3 = Column(Numeric(28, 14))
    pubuserdefnvc4 = Column(Unicode(500))
    pubuserdefdecm4 = Column(Numeric(28, 14))
    pubuserdefnvc5 = Column(Unicode(500))
    pubuserdefdecm5 = Column(Numeric(28, 14))
    pubuserdefnvc6 = Column(Unicode(500))
    pubuserdefdecm6 = Column(Numeric(28, 14))
    origpaymentamount = Column(Numeric(28, 14))
    paymentamount = Column(Numeric(28, 14))
    saleordercode = Column(Unicode(50))
    backgroundCreateVoucher = Column(Integer, nullable=False, server_default=text("((0))"))
    PrintCount = Column(Integer, nullable=False, server_default=text("((0))"))
    ID = Column(Integer, primary_key=True)
    idbusinesstype = Column(Integer)
    idoldbusinesstype = Column(Integer)
    idcurrency = Column(Integer)
    iddepartment = Column(Integer)
    IdStore = Column(Integer)
    IdMarketingOrgan = Column(Integer)
    idpartner = Column(Integer)
    idclerk = Column(Integer)
    idproject = Column(Integer)
    sourceVoucherID = Column(Integer)
    IdSettleStyle = Column(Integer)
    IdBankAccount = Column(Integer)
    arapAccountDirection = Column(Integer)
    billType = Column(Integer)
    voucherSettleState = Column(Integer)
    voucherstate = Column(Integer)
    auditorid = Column(Integer)
    makerid = Column(Integer)
    saleorderid = Column(Integer)
    idsourcevouchertype = Column(Integer)


class CSExpenseVoucherMultiPayment(Base):
    __tablename__ = 'CS_ExpenseVoucher_MultiPayment'

    code = Column(Unicode(30))
    name = Column(Unicode(200))
    voucherDate = Column(String(19, u'Chinese_PRC_CI_AS'))
    voucherCode = Column(Unicode(30))
    origAmount = Column(Numeric(28, 14))
    origCancelAmount = Column(Numeric(28, 14))
    origNoCancelAmount = Column(Numeric(28, 14))
    cancelAmount = Column(Numeric(28, 14))
    createdtime = Column(String(19, u'Chinese_PRC_CI_AS'))
    sequencenumber = Column(Integer)
    ts = Column(TIMESTAMP, nullable=False)
    updated = Column(String(19, u'Chinese_PRC_CI_AS'))
    updatedBy = Column(Unicode(32))
    memo = Column(Unicode(200))
    id = Column(Integer, primary_key=True)
    iddepartment = Column(Integer)
    idperson = Column(Integer)
    idproject = Column(Integer)
    voucherID = Column(Integer)
    idExpenseVoucherDTO = Column(Integer)
    idvouchertype = Column(Integer)


class CSExpenseVoucherMultiSettle(Base):
    __tablename__ = 'CS_ExpenseVoucher_MultiSettle'

    code = Column(Unicode(30))
    name = Column(Unicode(200))
    origAmount = Column(Numeric(28, 14))
    amount = Column(Numeric(28, 14))
    documentCode = Column(Unicode(30))
    createdtime = Column(String(19, u'Chinese_PRC_CI_AS'))
    sequencenumber = Column(Integer)
    ts = Column(TIMESTAMP)
    updated = Column(String(19, u'Chinese_PRC_CI_AS'))
    updatedBy = Column(Unicode(32))
    ID = Column(Integer, primary_key=True)
    idbankaccount = Column(Integer)
    idsettlestyle = Column(Integer)
    idExpenseVoucherDTO = Column(Integer)


class CSExpenseVoucherB(Base):
    __tablename__ = 'CS_ExpenseVoucher_b'

    code = Column(Unicode(30))
    name = Column(Unicode(200))
    origamount = Column(Numeric(28, 14))
    amount = Column(Numeric(28, 14))
    origTax = Column(Numeric(28, 14))
    tax = Column(Numeric(28, 14))
    origTaxAmount = Column(Numeric(28, 14))
    taxamount = Column(Numeric(28, 14))
    origSettleAmount = Column(Numeric(28, 14))
    settleAmount = Column(Numeric(28, 14))
    taxRate = Column(Numeric(28, 14))
    isApportion = Column(Integer)
    isTax = Column(Integer)
    ismodifyorigtax = Column(Integer)
    createdtime = Column(String(19, u'Chinese_PRC_CI_AS'))
    sequencenumber = Column(Integer)
    ts = Column(TIMESTAMP)
    updated = Column(String(19, u'Chinese_PRC_CI_AS'))
    updatedBy = Column(Unicode(32))
    priuserdefnvc1 = Column(Unicode(500))
    priuserdefdecm1 = Column(Numeric(28, 14))
    priuserdefnvc2 = Column(Unicode(500))
    priuserdefdecm2 = Column(Numeric(28, 14))
    priuserdefnvc3 = Column(Unicode(500))
    priuserdefdecm3 = Column(Numeric(28, 14))
    priuserdefnvc4 = Column(Unicode(500))
    priuserdefdecm4 = Column(Numeric(28, 14))
    pubuserdefnvc1 = Column(Unicode(500))
    pubuserdefdecm1 = Column(Numeric(28, 14))
    pubuserdefnvc2 = Column(Unicode(500))
    pubuserdefdecm2 = Column(Numeric(28, 14))
    pubuserdefnvc3 = Column(Unicode(500))
    pubuserdefdecm3 = Column(Numeric(28, 14))
    pubuserdefnvc4 = Column(Unicode(500))
    pubuserdefdecm4 = Column(Numeric(28, 14))
    expenseItemUse = Column(Unicode(128))
    ID = Column(Integer, primary_key=True)
    idexpenseitem = Column(Integer)
    idproject = Column(Integer)
    idExpenseVoucherDTO = Column(Integer)
    saleOrderDetailId = Column(Integer)
    idexpenseallocationvouchertype = Column(Integer)


class CSIncomeVoucher(Base):
    __tablename__ = 'CS_IncomeVoucher'

    code = Column(Unicode(30))
    name = Column(Unicode(200))
    memo = Column(Unicode(200))
    exchangeRate = Column(Numeric(28, 14))
    origAmount = Column(Numeric(28, 14))
    invoiceCode = Column(Unicode(30))
    sourceVoucherCode = Column(Unicode(30))
    origTaxAmountSum = Column(Numeric(28, 14))
    arrivalDate = Column(String(19, u'Chinese_PRC_CI_AS'))
    oldVoucherDate = Column(String(19, u'Chinese_PRC_CI_AS'))
    amount = Column(Numeric(28, 14))
    taxAmountSum = Column(Numeric(28, 14))
    voucherdate = Column(String(19, u'Chinese_PRC_CI_AS'))
    maker = Column(Unicode(50))
    madedate = Column(String(19, u'Chinese_PRC_CI_AS'))
    auditor = Column(Unicode(50))
    reviser = Column(Unicode(50))
    auditeddate = Column(String(19, u'Chinese_PRC_CI_AS'))
    iscarriedforwardout = Column(Integer)
    iscarriedforwardin = Column(Integer)
    ismodifiedcode = Column(Integer)
    docno = Column(Unicode(36))
    docclass = Column(Unicode(36))
    accountingperiod = Column(Integer)
    docid = Column(Unicode(36))
    accountingyear = Column(Integer)
    createdtime = Column(String(19, u'Chinese_PRC_CI_AS'))
    sequencenumber = Column(Integer)
    ts = Column(TIMESTAMP)
    updated = Column(String(19, u'Chinese_PRC_CI_AS'))
    updatedBy = Column(Unicode(32))
    priuserdefnvc1 = Column(Unicode(500))
    priuserdefdecm1 = Column(Numeric(28, 14))
    priuserdefnvc2 = Column(Unicode(500))
    priuserdefdecm2 = Column(Numeric(28, 14))
    priuserdefnvc3 = Column(Unicode(500))
    priuserdefdecm3 = Column(Numeric(28, 14))
    priuserdefnvc4 = Column(Unicode(500))
    priuserdefdecm4 = Column(Numeric(28, 14))
    priuserdefnvc5 = Column(Unicode(500))
    priuserdefdecm5 = Column(Numeric(28, 14))
    priuserdefnvc6 = Column(Unicode(500))
    priuserdefdecm6 = Column(Numeric(28, 14))
    pubuserdefnvc1 = Column(Unicode(500))
    pubuserdefdecm1 = Column(Numeric(28, 14))
    pubuserdefnvc2 = Column(Unicode(500))
    pubuserdefdecm2 = Column(Numeric(28, 14))
    pubuserdefnvc3 = Column(Unicode(500))
    pubuserdefdecm3 = Column(Numeric(28, 14))
    pubuserdefnvc4 = Column(Unicode(500))
    pubuserdefdecm4 = Column(Numeric(28, 14))
    pubuserdefnvc5 = Column(Unicode(500))
    pubuserdefdecm5 = Column(Numeric(28, 14))
    pubuserdefnvc6 = Column(Unicode(500))
    pubuserdefdecm6 = Column(Numeric(28, 14))
    origpaymentamount = Column(Numeric(28, 14))
    paymentamount = Column(Numeric(28, 14))
    saleordercode = Column(Unicode(50))
    PrintCount = Column(Integer, nullable=False, server_default=text("((0))"))
    backgroundCreateVoucher = Column(Integer, nullable=False, server_default=text("((0))"))
    ID = Column(Integer, primary_key=True)
    idbusinesstype = Column(Integer)
    idoldbusinesstype = Column(Integer)
    idcurrency = Column(Integer)
    iddepartment = Column(Integer)
    IdStore = Column(Integer)
    IdMarketingOrgan = Column(Integer)
    idpartner = Column(Integer)
    idclerk = Column(Integer)
    idproject = Column(Integer)
    IdSettleStyle = Column(Integer)
    IdBankAccount = Column(Integer)
    billType = Column(Integer)
    voucherSettleState = Column(Integer)
    voucherstate = Column(Integer)
    auditorid = Column(Integer)
    makerid = Column(Integer)
    sourceVoucherID = Column(Integer)
    saleorderid = Column(Integer)
    idsourcevouchertype = Column(Integer)


class CSIncomeVoucherMultiPayment(Base):
    __tablename__ = 'CS_IncomeVoucher_MultiPayment'

    code = Column(Unicode(30))
    name = Column(Unicode(200))
    voucherDate = Column(String(19, u'Chinese_PRC_CI_AS'))
    voucherCode = Column(Unicode(30))
    origAmount = Column(Numeric(28, 14))
    origNoCancelAmount = Column(Numeric(28, 14))
    origCancelAmount = Column(Numeric(28, 14))
    cancelAmount = Column(Numeric(28, 14))
    createdtime = Column(String(19, u'Chinese_PRC_CI_AS'))
    sequencenumber = Column(Integer)
    ts = Column(TIMESTAMP, nullable=False)
    updated = Column(String(19, u'Chinese_PRC_CI_AS'))
    updatedBy = Column(Unicode(32))
    memo = Column(Unicode(200))
    id = Column(Integer, primary_key=True)
    iddepartment = Column(Integer)
    idperson = Column(Integer)
    idproject = Column(Integer)
    voucherID = Column(Integer)
    idIncomeVoucherDTO = Column(Integer)
    idvouchertype = Column(Integer)


class CSIncomeVoucherMultiSettle(Base):
    __tablename__ = 'CS_IncomeVoucher_MultiSettle'

    code = Column(Unicode(30))
    name = Column(Unicode(200))
    origAmount = Column(Numeric(28, 14))
    amount = Column(Numeric(28, 14))
    documentCode = Column(Unicode(30))
    createdtime = Column(String(19, u'Chinese_PRC_CI_AS'))
    sequencenumber = Column(Integer)
    ts = Column(TIMESTAMP)
    updated = Column(String(19, u'Chinese_PRC_CI_AS'))
    updatedBy = Column(Unicode(32))
    ID = Column(Integer, primary_key=True)
    idbankaccount = Column(Integer)
    idsettlestyle = Column(Integer)
    idIncomeVoucherDTO = Column(Integer)


class CSIncomeVoucherB(Base):
    __tablename__ = 'CS_IncomeVoucher_b'

    code = Column(Unicode(30))
    name = Column(Unicode(200))
    origTaxAmount = Column(Numeric(28, 14))
    origTax = Column(Numeric(28, 14))
    origamount = Column(Numeric(28, 14))
    taxExchange = Column(Numeric(28, 14))
    taxamount = Column(Numeric(28, 14))
    tax = Column(Numeric(28, 14))
    amount = Column(Numeric(28, 14))
    origSettleAmount = Column(Numeric(28, 14))
    settleAmount = Column(Numeric(28, 14))
    isTax = Column(Integer)
    ismodifyorigtax = Column(Integer)
    createdtime = Column(String(19, u'Chinese_PRC_CI_AS'))
    sequencenumber = Column(Integer)
    ts = Column(TIMESTAMP)
    updated = Column(String(19, u'Chinese_PRC_CI_AS'))
    updatedBy = Column(Unicode(32))
    priuserdefnvc1 = Column(Unicode(500))
    priuserdefdecm1 = Column(Numeric(28, 14))
    priuserdefnvc2 = Column(Unicode(500))
    priuserdefdecm2 = Column(Numeric(28, 14))
    priuserdefnvc3 = Column(Unicode(500))
    priuserdefdecm3 = Column(Numeric(28, 14))
    priuserdefnvc4 = Column(Unicode(500))
    priuserdefdecm4 = Column(Numeric(28, 14))
    pubuserdefnvc1 = Column(Unicode(500))
    pubuserdefdecm1 = Column(Numeric(28, 14))
    pubuserdefnvc2 = Column(Unicode(500))
    pubuserdefdecm2 = Column(Numeric(28, 14))
    pubuserdefnvc3 = Column(Unicode(500))
    pubuserdefdecm3 = Column(Numeric(28, 14))
    pubuserdefnvc4 = Column(Unicode(500))
    pubuserdefdecm4 = Column(Numeric(28, 14))
    ID = Column(Integer, primary_key=True)
    idincomeitem = Column(Integer)
    idproject = Column(Integer)
    idIncomeVoucherDTO = Column(Integer)
    saleOrderDetailId = Column(Integer)


t_CS_NNRelate = Table(
    'CS_NNRelate', metadata,
    Column('ID', Integer, nullable=False),
    Column('NoteID', Unicode(128)),
    Column('PartName', Unicode(100)),
    Column('DestNoteID', Unicode(128)),
    Column('DestPartName', Unicode(100))
)


t_CS_NoteBase = Table(
    'CS_NoteBase', metadata,
    Column('ID', Integer, nullable=False),
    Column('LevelID', Integer),
    Column('HostName', Unicode(50)),
    Column('NoteID', Unicode(128)),
    Column('NoteName', Unicode(255), nullable=False),
    Column('ImportDate', DateTime),
    Column('NoteData', LargeBinary),
    Column('LastUpdateDate', DateTime),
    Column('LastUpdateHost', Unicode(255)),
    Column('LastUpdateName', Unicode(200)),
    Column('ImgLogoID', Integer),
    Column('ImgTypeID', Integer)
)


t_CS_NoteCommonInfo = Table(
    'CS_NoteCommonInfo', metadata,
    Column('ID', Integer, nullable=False),
    Column('UserName', Unicode(50)),
    Column('NoteID', Unicode(128)),
    Column('ShortName', Unicode(50)),
    Column('ImgLogoID', Integer),
    Column('ImgTypeID', Integer),
    Column('PosIndex', Integer)
)


t_CS_NoteImage = Table(
    'CS_NoteImage', metadata,
    Column('ID', Integer, nullable=False),
    Column('Description', Unicode(50)),
    Column('Type', Integer),
    Column('Data', LargeBinary)
)


t_CS_NoteLevel = Table(
    'CS_NoteLevel', metadata,
    Column('ID', Integer, nullable=False),
    Column('LevelName', Unicode(100)),
    Column('ParentID', Integer)
)


t_CS_NotePartProperty = Table(
    'CS_NotePartProperty', metadata,
    Column('ID', Integer, nullable=False),
    Column('UserName', Unicode(50)),
    Column('NoteID', Unicode(128)),
    Column('UseRegion', Integer),
    Column('PartName', Unicode(50)),
    Column('FldName', Unicode(50)),
    Column('IsBuiltIn', Integer, server_default=text("((0))")),
    Column('DataType', Integer),
    Column('ColWidth', Integer),
    Column('ColOrder', Integer),
    Column('IsSum', Integer),
    Column('IsVisible', Integer),
    Column('FilterPosition', Integer),
    Column('SortType', Integer),
    Column('Sort', Integer),
    Column('sFilPar1', Unicode(255)),
    Column('sFilPar2', Unicode(255)),
    Column('SubTableColName', Unicode(50), server_default=text("(NULL)")),
    Column('SubTableRowNum', Integer, server_default=text("((0))")),
    Column('SubTableName', Unicode(100), server_default=text("(NULL)")),
    Column('sFilPar3', String(255, u'Chinese_PRC_CI_AS'), server_default=text("(NULL)"))
)


t_CS_NotePrintFilter = Table(
    'CS_NotePrintFilter', metadata,
    Column('ID', Integer, nullable=False),
    Column('NoteID', Unicode(128), nullable=False),
    Column('UserName', Unicode(50)),
    Column('DateType', Integer),
    Column('DateBegin', DateTime),
    Column('DateEnd', DateTime),
    Column('UserIDList', Unicode(1024)),
    Column('HostList', Unicode(1024)),
    Column('UseRegion', Integer),
    Column('HaveCancel', Integer, server_default=text("((0))")),
    Column('SubConfig', Integer, server_default=text("((-1))")),
    Column('SourceType', String(30, u'Chinese_PRC_CI_AS'), server_default=text("(NULL)"))
)


t_CS_NotePrintInfo = Table(
    'CS_NotePrintInfo', metadata,
    Column('ID', Integer, nullable=False),
    Column('UserName', Unicode(50)),
    Column('NoteID', Unicode(128)),
    Column('NoteName', Unicode(255), nullable=False),
    Column('PrintTime', DateTime),
    Column('HostName', Unicode(255)),
    Column('IsCancel', Integer),
    Column('DriverName', Unicode(100)),
    Column('PrintDevice', Unicode(100)),
    Column('PrintOrient', Integer),
    Column('PrintX', Float(53)),
    Column('PrintY', Float(53)),
    Column('PaperMode', Integer),
    Column('PaperName', Unicode(50)),
    Column('PaperSize', Integer),
    Column('PaperAlign', Integer),
    Column('PrintType', Integer, server_default=text("((0))")),
    Column('SourceType', Integer, server_default=text("((0))")),
    Column('OutSysName', Unicode(50)),
    Column('OutID', Unicode(255))
)


t_CS_NotePrintList = Table(
    'CS_NotePrintList', metadata,
    Column('ID', Integer, nullable=False),
    Column('InfoID', Integer, nullable=False),
    Column('PartName', Unicode(255), nullable=False),
    Column('DataType', Integer, nullable=False),
    Column('DataValue', Unicode(2048)),
    Column('SubTableColName', Unicode(50), server_default=text("(NULL)")),
    Column('SubTableRowNum', Integer, server_default=text("((0))")),
    Column('SubTableName', Unicode(100), server_default=text("(NULL)"))
)


t_CS_NotePrintOrder = Table(
    'CS_NotePrintOrder', metadata,
    Column('ID', Integer, nullable=False),
    Column('NoteID', Unicode(128), nullable=False),
    Column('UserName', Unicode(50)),
    Column('SubTableOrder', Integer, nullable=False, server_default=text("((0))"))
)


class CSPeriodBeginNoArrival(Base):
    __tablename__ = 'CS_PeriodBeginNoArrival'

    code = Column(Unicode(30))
    name = Column(Unicode(200))
    origDailyBanlance = Column(Numeric(28, 14))
    origbankreceivedailynoreceive = Column(Numeric(28, 14))
    origbankpaymentdailynopayment = Column(Numeric(28, 14))
    origdailyadjustdailybanlance = Column(Numeric(28, 14))
    origBankBalance = Column(Numeric(28, 14))
    origdailyreceivebanknoreceive = Column(Numeric(28, 14))
    origdailypaymentbanknopayment = Column(Numeric(28, 14))
    origbankadjustbanlance = Column(Numeric(28, 14))
    isBanlance = Column(Integer)
    docno = Column(Unicode(36))
    docclass = Column(Unicode(36))
    accountingperiod = Column(Integer)
    docid = Column(Unicode(36))
    accountingyear = Column(Integer)
    memo = Column(Unicode(50))
    voucherdate = Column(String(19, u'Chinese_PRC_CI_AS'))
    madedate = Column(String(19, u'Chinese_PRC_CI_AS'))
    maker = Column(Unicode(50))
    auditor = Column(Unicode(50))
    auditeddate = Column(String(19, u'Chinese_PRC_CI_AS'))
    reviser = Column(Unicode(50))
    iscarriedforwardout = Column(Integer)
    iscarriedforwardin = Column(Integer)
    ismodifiedcode = Column(Integer)
    createdtime = Column(String(19, u'Chinese_PRC_CI_AS'))
    sequencenumber = Column(Integer)
    ts = Column(TIMESTAMP, nullable=False)
    updated = Column(String(19, u'Chinese_PRC_CI_AS'))
    updatedBy = Column(Unicode(32))
    ID = Column(Integer, primary_key=True)
    idbankaccount = Column(Integer)
    voucherstate = Column(Integer)
    auditorid = Column(Integer)
    makerid = Column(Integer)


class CSPeriodBeginNoArrivalBank(Base):
    __tablename__ = 'CS_PeriodBeginNoArrival_Bank'

    code = Column(Unicode(30))
    name = Column(Unicode(200))
    date = Column(String(19, u'Chinese_PRC_CI_AS'))
    summary = Column(Unicode(50))
    billNumber = Column(Unicode(50))
    origAmountDr = Column(Numeric(28, 14))
    origAmountCr = Column(Numeric(28, 14))
    billdate = Column(String(19, u'Chinese_PRC_CI_AS'))
    createdtime = Column(String(19, u'Chinese_PRC_CI_AS'))
    sequencenumber = Column(Integer)
    ts = Column(TIMESTAMP, nullable=False)
    updated = Column(String(19, u'Chinese_PRC_CI_AS'))
    updatedBy = Column(Unicode(32))
    ID = Column(Integer, primary_key=True)
    idsettlestyle = Column(Integer)
    idPeriodBeginNoArrivalDTO = Column(Integer)


class CSPeriodBeginNoArrivalDaily(Base):
    __tablename__ = 'CS_PeriodBeginNoArrival_Daily'

    code = Column(Unicode(30))
    name = Column(Unicode(200))
    date = Column(String(19, u'Chinese_PRC_CI_AS'))
    summary = Column(Unicode(50))
    billdate = Column(String(19, u'Chinese_PRC_CI_AS'))
    billNumber = Column(Unicode(50))
    origAmountDr = Column(Numeric(28, 14))
    origAmountCr = Column(Numeric(28, 14))
    createdtime = Column(String(19, u'Chinese_PRC_CI_AS'))
    sequencenumber = Column(Integer)
    ts = Column(TIMESTAMP, nullable=False)
    updated = Column(String(19, u'Chinese_PRC_CI_AS'))
    updatedBy = Column(Unicode(32))
    ID = Column(Integer, primary_key=True)
    idsettlestyle = Column(Integer)
    idPeriodBeginNoArrivalDTO = Column(Integer)


t_CS_PrintJobInfo = Table(
    'CS_PrintJobInfo', metadata,
    Column('ID', Integer, nullable=False),
    Column('NoteID', Unicode(128)),
    Column('NoteName', Unicode(200)),
    Column('HostName', Unicode(50)),
    Column('PrintDate', DateTime),
    Column('PrintTime', DateTime),
    Column('UserName', Unicode(50)),
    Column('SourceType', Integer, server_default=text("((0))")),
    Column('IsCancel', Integer, server_default=text("((0))")),
    Column('OutSysName', Unicode(50)),
    Column('OutID', Unicode(255))
)


t_CS_PrintJobList = Table(
    'CS_PrintJobList', metadata,
    Column('ID', Integer, nullable=False),
    Column('InfoID', Integer, nullable=False),
    Column('PartName', Unicode(255)),
    Column('DataType', Integer),
    Column('DataValue', Unicode(2048)),
    Column('SubTableColName', Unicode(50), server_default=text("(NULL)")),
    Column('SubTableRowNum', Integer, server_default=text("((0))")),
    Column('SubTableName', Unicode(100), server_default=text("(NULL)"))
)


t_CS_PrinterParam = Table(
    'CS_PrinterParam', metadata,
    Column('ID', Integer, nullable=False),
    Column('NoteID', Unicode(128)),
    Column('PrinterName', Unicode(100)),
    Column('DriverName', Unicode(100)),
    Column('HostName', Unicode(50)),
    Column('PrintOrient', Integer),
    Column('PrintX', Float(53)),
    Column('PrintY', Float(53)),
    Column('PaperMode', Integer),
    Column('PaperName', Unicode(50)),
    Column('PaperSize', Integer),
    Column('PaperAlign', Integer),
    Column('PrintType', Integer),
    Column('MicroAdjust', Integer),
    Column('UpdateTime', DateTime)
)


t_DI_DailyCurrentStock = Table(
    'DI_DailyCurrentStock', metadata,
    Column('code', Unicode(30)),
    Column('name', Unicode(200)),
    Column('CanUseQuantity', Numeric(28, 14), nullable=False, server_default=text("((0))")),
    Column('PurchaseOrderOnWayQuantity', Numeric(28, 14), nullable=False, server_default=text("((0))")),
    Column('PurchaseArrivalQuantity', Numeric(28, 14), nullable=False, server_default=text("((0))")),
    Column('PurchaseForReceiveQuantity', Numeric(28, 14), nullable=False, server_default=text("((0))")),
    Column('OnProducingQuantity', Numeric(28, 14), nullable=False, server_default=text("((0))")),
    Column('ProductForReceiveQuantity', Numeric(28, 14), nullable=False, server_default=text("((0))")),
    Column('PurchaseRequisitionQuantity', Numeric(28, 14), nullable=False, server_default=text("((0))")),
    Column('OtherOnWayQuantity', Numeric(28, 14), nullable=False, server_default=text("((0))")),
    Column('TransOnWayQuantity', Numeric(28, 14), nullable=False, server_default=text("((0))")),
    Column('ForSaleOrderQuantity', Numeric(28, 14), nullable=False, server_default=text("((0))")),
    Column('SaleDeliveryQuantity', Numeric(28, 14), nullable=False, server_default=text("((0))")),
    Column('ForSaleDispatchQuantity', Numeric(28, 14), nullable=False, server_default=text("((0))")),
    Column('ProduceForDispatchQuantity', Numeric(28, 14), nullable=False, server_default=text("((0))")),
    Column('MaterialForSendQuantity', Numeric(28, 14), nullable=False, server_default=text("((0))")),
    Column('OtherForDispatchQuantity', Numeric(28, 14), nullable=False, server_default=text("((0))")),
    Column('TransForDispatchQuantity', Numeric(28, 14), nullable=False, server_default=text("((0))")),
    Column('ForStockOrderQuantity', Numeric(28, 14), nullable=False, server_default=text("((0))")),
    Column('SafeQuantity', Numeric(28, 14), nullable=False, server_default=text("((0))")),
    Column('LowQuantity', Numeric(28, 14), nullable=False, server_default=text("((0))")),
    Column('BaseQuantity', Numeric(28, 14), nullable=False, server_default=text("((0))")),
    Column('ts', TIMESTAMP, nullable=False),
    Column('updated', String(19, u'Chinese_PRC_CI_AS')),
    Column('updatedBy', Unicode(32)),
    Column('StockRequestQuantity', Numeric(28, 14), nullable=False, server_default=text("((0))")),
    Column('ProduceOnWayWithUnAudit', Numeric(28, 14), nullable=False, server_default=text("((0))")),
    Column('ProduceForDispatchQuantityWithUnAudit', Numeric(28, 14), nullable=False, server_default=text("((0))")),
    Column('freeItem0', Unicode(300)),
    Column('freeItem1', Unicode(300)),
    Column('freeItem2', Unicode(300)),
    Column('freeItem3', Unicode(300)),
    Column('freeItem4', Unicode(300)),
    Column('freeItem5', Unicode(300)),
    Column('freeItem6', Unicode(300)),
    Column('freeItem7', Unicode(300)),
    Column('freeItem8', Unicode(300)),
    Column('freeItem9', Unicode(300)),
    Column('ForStockRequestQuantity', Numeric(28, 14), nullable=False, server_default=text("((0))")),
    Column('DistributionForSendQuantity', Numeric(28, 14), nullable=False, server_default=text("((0))")),
    Column('id', Integer, nullable=False),
    Column('idinventory', Integer),
    Column('idwarehouse', Integer)
)


t_DI_Distribution = Table(
    'DI_Distribution', metadata,
    Column('code', Unicode(30)),
    Column('name', Unicode(200)),
    Column('estimateddeliverydate', String(19, u'Chinese_PRC_CI_AS')),
    Column('telephone', Unicode(50)),
    Column('arrivaladdress', Unicode(50)),
    Column('sourcevouchercode', Unicode(50)),
    Column('contact', Unicode(50)),
    Column('isnomodify', Unicode(500)),
    Column('exchangerate', Numeric(28, 14)),
    Column('memo', Unicode(200)),
    Column('voucherdate', String(19, u'Chinese_PRC_CI_AS')),
    Column('madedate', String(19, u'Chinese_PRC_CI_AS')),
    Column('maker', Unicode(50)),
    Column('auditor', Unicode(50)),
    Column('auditeddate', String(19, u'Chinese_PRC_CI_AS')),
    Column('reviser', Unicode(50)),
    Column('iscarriedforwardout', Integer),
    Column('iscarriedforwardin', Integer),
    Column('ismodifiedcode', Integer),
    Column('createdtime', String(19, u'Chinese_PRC_CI_AS')),
    Column('sequencenumber', Integer),
    Column('ts', TIMESTAMP, nullable=False),
    Column('updated', String(19, u'Chinese_PRC_CI_AS')),
    Column('updatedBy', Unicode(32)),
    Column('priuserdefnvc1', Unicode(500)),
    Column('priuserdefdecm1', Numeric(28, 14)),
    Column('priuserdefnvc2', Unicode(500)),
    Column('priuserdefdecm2', Numeric(28, 14)),
    Column('priuserdefnvc3', Unicode(500)),
    Column('priuserdefdecm3', Numeric(28, 14)),
    Column('priuserdefnvc4', Unicode(500)),
    Column('priuserdefdecm4', Numeric(28, 14)),
    Column('priuserdefnvc5', Unicode(500)),
    Column('priuserdefdecm5', Numeric(28, 14)),
    Column('priuserdefnvc6', Unicode(500)),
    Column('priuserdefdecm6', Numeric(28, 14)),
    Column('pubuserdefnvc1', Unicode(500)),
    Column('pubuserdefdecm1', Numeric(28, 14)),
    Column('pubuserdefnvc2', Unicode(500)),
    Column('pubuserdefdecm2', Numeric(28, 14)),
    Column('pubuserdefnvc3', Unicode(500)),
    Column('pubuserdefdecm3', Numeric(28, 14)),
    Column('pubuserdefnvc4', Unicode(500)),
    Column('pubuserdefdecm4', Numeric(28, 14)),
    Column('pubuserdefnvc5', Unicode(500)),
    Column('pubuserdefdecm5', Numeric(28, 14)),
    Column('pubuserdefnvc6', Unicode(500)),
    Column('pubuserdefdecm6', Numeric(28, 14)),
    Column('PrintCount', Integer),
    Column('ID', Integer, nullable=False),
    Column('idbusitype', Integer),
    Column('idcurrency', Integer),
    Column('idstore', Integer),
    Column('idmarketingorgan', Integer),
    Column('idcustomer', Integer),
    Column('idsettleCustomer', Integer),
    Column('idperson', Integer),
    Column('idproject', Integer),
    Column('idinWarehouse', Integer),
    Column('idoutwarehouse', Integer),
    Column('idrra', Integer),
    Column('sourcevoucherid', Integer),
    Column('completestatus', Integer),
    Column('deliverymode', Integer),
    Column('voucherstate', Integer),
    Column('auditorid', Integer),
    Column('makerid', Integer),
    Column('idsourcevouchertype', Integer)
)


t_DI_DistributionSourceRelation = Table(
    'DI_DistributionSourceRelation', metadata,
    Column('code', Unicode(30)),
    Column('name', Unicode(200)),
    Column('changerate', Numeric(28, 14)),
    Column('basequantity', Numeric(28, 14)),
    Column('subquantity', Numeric(28, 14)),
    Column('quantity', Numeric(28, 14)),
    Column('quantity2', Numeric(28, 14)),
    Column('sequencenumber', Integer),
    Column('createdtime', String(19, u'Chinese_PRC_CI_AS')),
    Column('ts', TIMESTAMP, nullable=False),
    Column('updated', String(19, u'Chinese_PRC_CI_AS')),
    Column('updatedBy', Unicode(32)),
    Column('id', Integer, nullable=False),
    Column('idbaseunit', Integer),
    Column('idsubunit', Integer),
    Column('idunit', Integer),
    Column('idunit2', Integer),
    Column('voucherid', Integer),
    Column('idDistributionDetailDTO', Integer),
    Column('sourcevoucherid', Integer),
    Column('sourcevoucherdetailid', Integer),
    Column('idsourcevouchertype', Integer)
)


t_DI_Distribution_b = Table(
    'DI_Distribution_b', metadata,
    Column('code', Unicode(30)),
    Column('name', Unicode(200)),
    Column('invbarcode', Unicode(50)),
    Column('quantity', Numeric(28, 14)),
    Column('quantity2', Numeric(28, 14)),
    Column('retailprice', Numeric(28, 14)),
    Column('retailamount', Numeric(28, 14)),
    Column('sourcevouchercode', Unicode(50)),
    Column('totalstockinquantity', Numeric(28, 14)),
    Column('totalstockinquantity2', Numeric(28, 14)),
    Column('totaltransquantity', Numeric(28, 14)),
    Column('totaltransquantity2', Numeric(28, 14)),
    Column('totalstockoutquantity', Numeric(28, 14)),
    Column('totalstockoutquantity2', Numeric(28, 14)),
    Column('differencequantity', Numeric(28, 14)),
    Column('differencequantity2', Numeric(28, 14)),
    Column('estimateddeliverydate', String(19, u'Chinese_PRC_CI_AS')),
    Column('changerate', Numeric(28, 14)),
    Column('basequantity', Numeric(28, 14)),
    Column('subquantity', Numeric(28, 14)),
    Column('onwayquantity', Numeric(28, 14)),
    Column('onwayquantity2', Numeric(28, 14)),
    Column('totalexecutedquantity', Numeric(28, 14)),
    Column('totalexecutedquantity2', Numeric(28, 14)),
    Column('isnomodify', Unicode(500)),
    Column('compositionquantity', Unicode(50)),
    Column('createdtime', String(19, u'Chinese_PRC_CI_AS')),
    Column('sequencenumber', Integer),
    Column('ts', TIMESTAMP, nullable=False),
    Column('updated', String(19, u'Chinese_PRC_CI_AS')),
    Column('updatedBy', Unicode(32)),
    Column('priuserdefnvc1', Unicode(500)),
    Column('priuserdefdecm1', Numeric(28, 14)),
    Column('priuserdefnvc2', Unicode(500)),
    Column('priuserdefdecm2', Numeric(28, 14)),
    Column('priuserdefnvc3', Unicode(500)),
    Column('priuserdefdecm3', Numeric(28, 14)),
    Column('priuserdefnvc4', Unicode(500)),
    Column('priuserdefdecm4', Numeric(28, 14)),
    Column('pubuserdefnvc1', Unicode(500)),
    Column('pubuserdefdecm1', Numeric(28, 14)),
    Column('pubuserdefnvc2', Unicode(500)),
    Column('pubuserdefdecm2', Numeric(28, 14)),
    Column('pubuserdefnvc3', Unicode(500)),
    Column('pubuserdefdecm3', Numeric(28, 14)),
    Column('pubuserdefnvc4', Unicode(500)),
    Column('pubuserdefdecm4', Numeric(28, 14)),
    Column('freeItem0', Unicode(300)),
    Column('freeItem1', Unicode(300)),
    Column('freeItem2', Unicode(300)),
    Column('freeItem3', Unicode(300)),
    Column('freeItem4', Unicode(300)),
    Column('freeItem5', Unicode(300)),
    Column('freeItem6', Unicode(300)),
    Column('freeItem7', Unicode(300)),
    Column('freeItem8', Unicode(300)),
    Column('freeItem9', Unicode(300)),
    Column('id', Integer, nullable=False),
    Column('idinventory', Integer),
    Column('idproject', Integer),
    Column('idbaseunit', Integer),
    Column('idsubunit', Integer),
    Column('idunit', Integer),
    Column('idunit2', Integer),
    Column('idoutwarehouse', Integer),
    Column('idDistributionDTO', Integer),
    Column('sourcevoucherid', Integer),
    Column('sourcevoucherdetailid', Integer),
    Column('completestatus', Integer),
    Column('idsourcevouchertype', Integer)
)


t_DI_RRABulidPurchaseOrder = Table(
    'DI_RRABulidPurchaseOrder', metadata,
    Column('code', Unicode(30)),
    Column('name', Unicode(200)),
    Column('currentquantity', Numeric(28, 14)),
    Column('purchasedate', String(19, u'Chinese_PRC_CI_AS')),
    Column('arrivalDate', String(19, u'Chinese_PRC_CI_AS')),
    Column('price', Numeric(28, 14)),
    Column('taxRate', Numeric(28, 14)),
    Column('taxPrice', Numeric(28, 14)),
    Column('unitexchangerate', Numeric(28, 14)),
    Column('exchangerate', Numeric(28, 14)),
    Column('createdtime', String(19, u'Chinese_PRC_CI_AS')),
    Column('sequencenumber', Integer),
    Column('ts', TIMESTAMP, nullable=False),
    Column('updated', String(19, u'Chinese_PRC_CI_AS')),
    Column('updatedBy', Unicode(32)),
    Column('isNoModify', Unicode(400)),
    Column('freeItem0', Unicode(300)),
    Column('freeItem1', Unicode(300)),
    Column('freeItem2', Unicode(300)),
    Column('freeItem3', Unicode(300)),
    Column('freeItem4', Unicode(300)),
    Column('freeItem5', Unicode(300)),
    Column('freeItem6', Unicode(300)),
    Column('freeItem7', Unicode(300)),
    Column('freeItem8', Unicode(300)),
    Column('freeItem9', Unicode(300)),
    Column('id', Integer, nullable=False),
    Column('idCurrency', Integer),
    Column('idDepartment', Integer),
    Column('idInventory', Integer),
    Column('idPartner', Integer),
    Column('idClerk', Integer),
    Column('idUnit', Integer),
    Column('idWarehouse', Integer)
)


t_DI_RRAGeneratePurchaseOrderRule = Table(
    'DI_RRAGeneratePurchaseOrderRule', metadata,
    Column('code', Unicode(30)),
    Column('name', Unicode(200)),
    Column('isphurchaselots', Integer),
    Column('createdtime', String(19, u'Chinese_PRC_CI_AS')),
    Column('sequencenumber', Integer),
    Column('ts', TIMESTAMP, nullable=False),
    Column('updated', String(19, u'Chinese_PRC_CI_AS')),
    Column('updatedBy', Unicode(32)),
    Column('id', Integer, nullable=False),
    Column('mergerule', Integer),
    Column('splitrule', Integer),
    Column('iduser', Integer)
)


t_DI_RRAInventory = Table(
    'DI_RRAInventory', metadata,
    Column('Code', Unicode(30)),
    Column('Name', Unicode(200)),
    Column('AvailableQuantity', Numeric(28, 14)),
    Column('ReplenishmentRuleTotalQuantity', Numeric(28, 14)),
    Column('Ts', TIMESTAMP, nullable=False),
    Column('Updated', String(19, u'Chinese_PRC_CI_AS')),
    Column('UpdatedBy', Unicode(32)),
    Column('createdtime', String(19, u'Chinese_PRC_CI_AS')),
    Column('RequestTotalQuantity', Numeric(28, 14)),
    Column('freeItem0', Unicode(300)),
    Column('freeItem1', Unicode(300)),
    Column('freeItem2', Unicode(300)),
    Column('freeItem3', Unicode(300)),
    Column('freeItem4', Unicode(300)),
    Column('freeItem5', Unicode(300)),
    Column('freeItem6', Unicode(300)),
    Column('freeItem7', Unicode(300)),
    Column('freeItem8', Unicode(300)),
    Column('freeItem9', Unicode(300)),
    Column('ReNewGoodSellDays', Integer),
    Column('ReNewGoodAheadDays', Integer),
    Column('ID', Integer, nullable=False),
    Column('idinventory', Integer),
    Column('idunit', Integer),
    Column('idoutWarehouse', Integer),
    Column('idStoreWarehouseReplenishmentRule', Integer),
    Column('idCustormerReplenishmentRule', Integer),
    Column('idRRADTO', Integer)
)


t_DI_RRAOption = Table(
    'DI_RRAOption', metadata,
    Column('Code', Unicode(30)),
    Column('Name', Unicode(200)),
    Column('PreAvailableQuantityDate', String(19, u'Chinese_PRC_CI_AS')),
    Column('ProcuremenEarlyDays', Integer),
    Column('FIDivided', Integer),
    Column('Ts', TIMESTAMP, nullable=False),
    Column('Updated', String(19, u'Chinese_PRC_CI_AS')),
    Column('UpdatedBy', Unicode(32)),
    Column('ExistedQuantity', Integer),
    Column('PurchasereQuisition', Integer),
    Column('PurchasereQuisitionWithUnAudit', Integer),
    Column('PurchaseOrderOnWay', Integer),
    Column('PurchaseOrderOnWayWithUnAudit', Integer),
    Column('PurchaseArrival', Integer),
    Column('PurchaseReceive', Integer),
    Column('TransOnWay', Integer),
    Column('OtherOnWay', Integer),
    Column('ProductReceive', Integer),
    Column('ProduceOnWay', Integer),
    Column('SafeStock', Integer),
    Column('LowStock', Integer),
    Column('SaleOrder', Integer),
    Column('SaleOrderWithUnAudit', Integer),
    Column('SaleDelivery', Integer),
    Column('SaleDispatch', Integer),
    Column('TransDIspatch', Integer),
    Column('OtherDispatch', Integer),
    Column('MaterialDispatch', Integer),
    Column('ProduceDispatch', Integer),
    Column('UseDateTimeAvailableQuantity', Integer),
    Column('ProduceOnWayWithUnAudit', Integer),
    Column('ProduceDispatchWithUnAudit', Integer),
    Column('WithEmptyWarhouse', Integer),
    Column('Store_ExistedQuantity', Integer),
    Column('Store_PurchaseArrival', Integer),
    Column('Store_PurchaseReceive', Integer),
    Column('Store_TransOnWay', Integer),
    Column('Store_OtherOnWay', Integer),
    Column('Store_SafeStock', Integer),
    Column('Store_LowStock', Integer),
    Column('Store_SaleDelivery', Integer),
    Column('Store_SaleDispatch', Integer),
    Column('Store_TransDIspatch', Integer),
    Column('Store_OtherDispatch', Integer),
    Column('Store_StockRequestQuantity', Integer),
    Column('Store_StockRequestQuantityWithNoAudit', Integer),
    Column('Store_ESStoreForDispatchQuantity', Integer),
    Column('Store_ESStoreForDispatchQuantityNoAudit', Integer),
    Column('StockRequest', Integer),
    Column('StockRequestWithUnAudit', Integer),
    Column('DistributionForSendQuantity', Integer),
    Column('DistributionForReceiveQuantity', Integer),
    Column('ID', Integer, nullable=False),
    Column('idoutWarehouse', Integer)
)


t_DI_RRAResult = Table(
    'DI_RRAResult', metadata,
    Column('Code', Unicode(30)),
    Column('Name', Unicode(200)),
    Column('Quantity', Numeric(28, 14)),
    Column('Ts', TIMESTAMP, nullable=False),
    Column('Updated', String(19, u'Chinese_PRC_CI_AS')),
    Column('UpdatedBy', Unicode(32)),
    Column('SourceVoucherCode', Unicode(200)),
    Column('freeItem0', Unicode(300)),
    Column('freeItem1', Unicode(300)),
    Column('freeItem2', Unicode(300)),
    Column('freeItem3', Unicode(300)),
    Column('freeItem4', Unicode(300)),
    Column('freeItem5', Unicode(300)),
    Column('freeItem6', Unicode(300)),
    Column('freeItem7', Unicode(300)),
    Column('freeItem8', Unicode(300)),
    Column('freeItem9', Unicode(300)),
    Column('createdtime', String(19, u'Chinese_PRC_CI_AS')),
    Column('RequestedQuantity', Numeric(28, 14)),
    Column('SourceVoucherTs', Unicode(50)),
    Column('SourceVoucherDetailTs', Unicode(50)),
    Column('VoucherDate', String(19, u'Chinese_PRC_CI_AS')),
    Column('changerate', Numeric(28, 14)),
    Column('ID', Integer, nullable=False),
    Column('idcurrency', Integer),
    Column('StoreOrCustomerID', Integer),
    Column('idstore', Integer),
    Column('idinventory', Integer),
    Column('idcustomer', Integer),
    Column('idproject', Integer),
    Column('idunit', Integer),
    Column('idwarehouse', Integer),
    Column('idInWarehouse', Integer),
    Column('idRRADTO', Integer),
    Column('SourceVoucherID', Integer),
    Column('SourceVoucherDetailID', Integer),
    Column('IdSourceVoucherType', Integer)
)


t_DI_RRAResultSum = Table(
    'DI_RRAResultSum', metadata,
    Column('Code', Unicode(30)),
    Column('freeItem0', Unicode(300)),
    Column('freeItem1', Unicode(300)),
    Column('freeItem2', Unicode(300)),
    Column('freeItem3', Unicode(300)),
    Column('freeItem4', Unicode(300)),
    Column('freeItem5', Unicode(300)),
    Column('freeItem6', Unicode(300)),
    Column('freeItem7', Unicode(300)),
    Column('freeItem8', Unicode(300)),
    Column('freeItem9', Unicode(300)),
    Column('AvailableQuantity', Numeric(28, 14)),
    Column('Quantity', Numeric(28, 14)),
    Column('LeaveAvailableQuantity', Numeric(29, 14)),
    Column('PurchaseSuggestQuantity', Numeric(29, 14)),
    Column('PurchaseQuantity', Numeric(28, 14), server_default=text("((0))")),
    Column('Status', Integer, server_default=text("((0))")),
    Column('ID', Integer, nullable=False),
    Column('IdInventory', Integer),
    Column('IdUnit', Integer),
    Column('IdWarehouse', Integer)
)


t_DI_RRARuleObj = Table(
    'DI_RRARuleObj', metadata,
    Column('ts', TIMESTAMP, nullable=False),
    Column('updatedBy', Unicode(32)),
    Column('updated', String(19, u'Chinese_PRC_CI_AS')),
    Column('name', Unicode(200), nullable=False),
    Column('id', Integer, nullable=False),
    Column('ruleTypeID', Integer),
    Column('idEnum', Integer, nullable=False, server_default=text("((0))"))
)


t_DI_RRARuleSet_Customer = Table(
    'DI_RRARuleSet_Customer', metadata,
    Column('Code', Unicode(200)),
    Column('Name', Unicode(200)),
    Column('ts', TIMESTAMP, nullable=False),
    Column('updatedBy', Unicode(32)),
    Column('updated', String(19, u'Chinese_PRC_CI_AS')),
    Column('id', Integer, nullable=False),
    Column('IdInventory', Integer),
    Column('IdInventoryClass', Integer),
    Column('CustomerReplenishmentRule', Integer),
    Column('ProductInfo', Integer)
)


t_DI_RRARuleSet_Store = Table(
    'DI_RRARuleSet_Store', metadata,
    Column('Code', Unicode(200)),
    Column('Name', Unicode(200)),
    Column('ts', TIMESTAMP, nullable=False),
    Column('updatedBy', Unicode(32)),
    Column('updated', String(19, u'Chinese_PRC_CI_AS')),
    Column('id', Integer, nullable=False),
    Column('IdInventory', Integer),
    Column('IdInventoryClass', Integer),
    Column('ProductInfo', Integer),
    Column('StoreReplenishmentRule', Integer)
)


t_DI_RRASourceRelation = Table(
    'DI_RRASourceRelation', metadata,
    Column('Code', Unicode(30)),
    Column('Name', Unicode(200)),
    Column('Quantity', Numeric(28, 14)),
    Column('Ts', TIMESTAMP, nullable=False),
    Column('Updated', String(19, u'Chinese_PRC_CI_AS')),
    Column('UpdatedBy', Unicode(32)),
    Column('Quantity2', Numeric(28, 14)),
    Column('SourceVoucherCode', Unicode(200)),
    Column('SourceVoucherTs', Unicode(50)),
    Column('SourceVoucherDetailTs', Unicode(50)),
    Column('VoucherDate', String(19, u'Chinese_PRC_CI_AS')),
    Column('changerate', Numeric(28, 14)),
    Column('ID', Integer, nullable=False),
    Column('idcurrency', Integer),
    Column('idproject', Integer),
    Column('IdUnit', Integer),
    Column('IdUnit2', Integer),
    Column('idRRAStoreCustormerDTO', Integer),
    Column('SourceVoucherID', Integer),
    Column('SourceVoucherDetailID', Integer),
    Column('idsourceVoucherType', Integer)
)


t_DI_RRAStoreCustormer = Table(
    'DI_RRAStoreCustormer', metadata,
    Column('Code', Unicode(30)),
    Column('Name', Unicode(200)),
    Column('RequestQuantity', Numeric(28, 14)),
    Column('DistributionRqeuareQuantity', Numeric(28, 14)),
    Column('DistributionQuantity', Numeric(28, 14)),
    Column('CurrentStock', Numeric(28, 14)),
    Column('SaleQuantity', Numeric(28, 14)),
    Column('NewAllocationRatio', Numeric(28, 14)),
    Column('ReplenishmentRule', Unicode(50)),
    Column('Ts', TIMESTAMP, nullable=False),
    Column('Updated', String(19, u'Chinese_PRC_CI_AS')),
    Column('UpdatedBy', Unicode(32)),
    Column('HasDistributed', Integer),
    Column('createdtime', String(19, u'Chinese_PRC_CI_AS')),
    Column('AvailableQuantity', Numeric(28, 14)),
    Column('ID', Integer, nullable=False),
    Column('idstore', Integer),
    Column('StoreOrCustomerID', Integer),
    Column('IdInventory', Integer),
    Column('idcustomer', Integer),
    Column('idInWarehouse', Integer),
    Column('idReplenishmentRule', Integer),
    Column('IdRRAInventoryDTO', Integer)
)


t_DI_ReplenishmentPriorityLevelLevel = Table(
    'DI_ReplenishmentPriorityLevelLevel', metadata,
    Column('code', Unicode(30)),
    Column('name', Unicode(200)),
    Column('PriorityLevel', Integer),
    Column('createdtime', String(19, u'Chinese_PRC_CI_AS')),
    Column('sequencenumber', Integer),
    Column('ts', TIMESTAMP, nullable=False),
    Column('updated', String(19, u'Chinese_PRC_CI_AS')),
    Column('updatedBy', Unicode(32)),
    Column('id', Integer, nullable=False),
    Column('idstore', Integer),
    Column('StoreOrCustomerID', Integer),
    Column('idcustomer', Integer),
    Column('idInWarehouse', Integer)
)


t_DI_RunShop = Table(
    'DI_RunShop', metadata,
    Column('ts', TIMESTAMP, nullable=False),
    Column('updatedBy', Unicode(32)),
    Column('updated', String(19, u'Chinese_PRC_CI_AS')),
    Column('createdTime', String(19, u'Chinese_PRC_CI_AS')),
    Column('code', Unicode(30)),
    Column('PrintCount', Integer),
    Column('id', Integer, nullable=False)
)


t_DI_RunShopLine = Table(
    'DI_RunShopLine', metadata,
    Column('ts', TIMESTAMP, nullable=False),
    Column('updatedBy', Unicode(32)),
    Column('updated', String(19, u'Chinese_PRC_CI_AS')),
    Column('isCurrent', Integer, nullable=False),
    Column('code', Unicode(30)),
    Column('name', Unicode(200)),
    Column('createdTime', String(19, u'Chinese_PRC_CI_AS')),
    Column('LineCode', Unicode(200), nullable=False),
    Column('runshopCyc', Integer),
    Column('beginDate', String(19, u'Chinese_PRC_CI_AS')),
    Column('PrintCount', Integer),
    Column('id', Integer, nullable=False),
    Column('idSalesman', Integer),
    Column('idRunShopDTO', Integer, nullable=False, server_default=text("((0))")),
    Column('RunStatus', Integer)
)


t_DI_RunShopLine_b = Table(
    'DI_RunShopLine_b', metadata,
    Column('ts', TIMESTAMP, nullable=False),
    Column('updatedBy', Unicode(32)),
    Column('updated', String(19, u'Chinese_PRC_CI_AS')),
    Column('code', Integer),
    Column('signInTime', Unicode(50)),
    Column('signOutTime', Unicode(50)),
    Column('isReportSalesQuantity', Integer),
    Column('isReportStockQuantity', Integer),
    Column('isOrderedDirect', Integer),
    Column('isSignInPhoto', Integer),
    Column('isSignOutPhoto', Integer),
    Column('isPromotionPhoto', Integer),
    Column('isCompetitionPhoto', Integer),
    Column('mapMark', Unicode(200), nullable=False),
    Column('targetType', Integer, nullable=False),
    Column('createdTime', String(19, u'Chinese_PRC_CI_AS')),
    Column('CheckAddress', Unicode(200)),
    Column('name', Unicode(200)),
    Column('effectiveTime', Integer),
    Column('effectiveRange', Integer),
    Column('id', Integer, nullable=False),
    Column('idStore', Integer),
    Column('idPartner', Integer),
    Column('LineGroupInfo', Integer),
    Column('idRunShopLineDTO', Integer, nullable=False, server_default=text("((0))")),
    Column('idRunShopRecord', Integer)
)


t_DI_RunShopMap = Table(
    'DI_RunShopMap', metadata,
    Column('ts', TIMESTAMP, nullable=False),
    Column('updatedBy', Unicode(32)),
    Column('updated', String(19, u'Chinese_PRC_CI_AS')),
    Column('code', Unicode(30)),
    Column('menuCode', Unicode(200)),
    Column('xmlValue', Unicode(1000)),
    Column('id', Integer, nullable=False),
    Column('idRunShopDTO', Integer, nullable=False, server_default=text("((0))")),
    Column('userID', Integer)
)


t_DI_RunShopMapMark = Table(
    'DI_RunShopMapMark', metadata,
    Column('ts', TIMESTAMP, nullable=False),
    Column('updatedBy', Unicode(32)),
    Column('updated', String(19, u'Chinese_PRC_CI_AS')),
    Column('code', Unicode(32), nullable=False),
    Column('isUsed', Integer, nullable=False),
    Column('id', Integer, nullable=False)
)


t_DI_RunShopNews = Table(
    'DI_RunShopNews', metadata,
    Column('recordDate', String(10, u'Chinese_PRC_CI_AS'), nullable=False),
    Column('updated', String(19, u'Chinese_PRC_CI_AS')),
    Column('newsStatus', Integer),
    Column('position', String(200, u'Chinese_PRC_CI_AS')),
    Column('id', Integer, nullable=False),
    Column('idPerson', Integer, nullable=False, server_default=text("((0))")),
    Column('idRunShopLineDetialDTO', Integer, nullable=False, server_default=text("((0))"))
)


t_DI_RunShopRecord = Table(
    'DI_RunShopRecord', metadata,
    Column('recordDate', String(10, u'Chinese_PRC_CI_AS'), nullable=False),
    Column('signInTime', Unicode(50)),
    Column('signOutTime', Unicode(50)),
    Column('lateMinuts', Integer),
    Column('overTime', Integer),
    Column('signInPhoto', Unicode(2000)),
    Column('signOutPhoto', Unicode(2000)),
    Column('promotionPhoto', Unicode(2000)),
    Column('competitionPhoto', Unicode(2000)),
    Column('idStockSalesReport', Unicode(2000)),
    Column('idSaleOrder', Unicode(2000)),
    Column('idStockRequest', Unicode(2000)),
    Column('newsStatus', Integer),
    Column('ts', TIMESTAMP, nullable=False),
    Column('updatedBy', Unicode(32)),
    Column('updated', String(19, u'Chinese_PRC_CI_AS')),
    Column('createdTime', String(19, u'Chinese_PRC_CI_AS')),
    Column('photoCount', Integer),
    Column('code', Unicode(30)),
    Column('signOutDate', String(10, u'Chinese_PRC_CI_AS')),
    Column('signInAddress', Unicode(50)),
    Column('TaskDescription', Unicode(1000)),
    Column('id', Integer, nullable=False),
    Column('idPerson', Integer),
    Column('idRunShopLineDetailDTO', Integer)
)


t_DI_RunShopTarget = Table(
    'DI_RunShopTarget', metadata,
    Column('ts', TIMESTAMP, nullable=False),
    Column('updatedBy', Unicode(32)),
    Column('updated', String(19, u'Chinese_PRC_CI_AS')),
    Column('isReportSalesQuantity', Integer),
    Column('isReportStockQuantity', Integer),
    Column('isOrderedDirect', Integer),
    Column('isSignInPhoto', Integer),
    Column('isSignOutPhoto', Integer),
    Column('isPromotionPhoto', Integer),
    Column('isCompetitionPhoto', Integer),
    Column('targetType', Integer, nullable=False),
    Column('code', Unicode(50)),
    Column('mapMark', Unicode(200)),
    Column('id', Integer, nullable=False),
    Column('idStore', Integer),
    Column('idPartner', Integer)
)


t_DI_SelectInventoryByRRA = Table(
    'DI_SelectInventoryByRRA', metadata,
    Column('ts', TIMESTAMP),
    Column('updatedBy', Unicode(32)),
    Column('updated', String(19, u'Chinese_PRC_CI_AS')),
    Column('name', Unicode(200)),
    Column('BeginDate', String(10, u'Chinese_PRC_CI_AS')),
    Column('BeginTime', Unicode(20)),
    Column('EndDate', String(10, u'Chinese_PRC_CI_AS')),
    Column('EndTime', Unicode(20)),
    Column('ReNewGoodSellDays', Integer),
    Column('AdviceReplenishQuantity', Numeric(28, 14)),
    Column('ActualReplenishQuantity', Numeric(28, 14)),
    Column('SaleQuantity', Numeric(28, 14)),
    Column('ExistingQuantity', Numeric(28, 14)),
    Column('AvailableQuantity', Numeric(28, 14)),
    Column('freeItem0', Unicode(300)),
    Column('freeItem1', Unicode(300)),
    Column('freeItem2', Unicode(300)),
    Column('freeItem3', Unicode(300)),
    Column('freeItem4', Unicode(300)),
    Column('freeItem5', Unicode(300)),
    Column('freeItem6', Unicode(300)),
    Column('freeItem7', Unicode(300)),
    Column('freeItem8', Unicode(300)),
    Column('freeItem9', Unicode(300)),
    Column('id', Integer, nullable=False),
    Column('idInventory', Integer),
    Column('idInventoryClass', Integer),
    Column('idWarehouse', Integer),
    Column('idRraruleset_store', Integer),
    Column('ProductInfo', Integer),
    Column('StoreReplenishmentRule', Integer)
)


t_DI_StockRequest = Table(
    'DI_StockRequest', metadata,
    Column('code', Unicode(30)),
    Column('name', Unicode(200)),
    Column('requirementdate', String(19, u'Chinese_PRC_CI_AS')),
    Column('telephone', Unicode(50)),
    Column('arrivaladdress', Unicode(50)),
    Column('contact', Unicode(50)),
    Column('memo', Unicode(200)),
    Column('voucherdate', String(19, u'Chinese_PRC_CI_AS')),
    Column('madedate', String(19, u'Chinese_PRC_CI_AS')),
    Column('maker', Unicode(50)),
    Column('auditor', Unicode(50)),
    Column('auditeddate', String(19, u'Chinese_PRC_CI_AS')),
    Column('reviser', Unicode(50)),
    Column('iscarriedforwardout', Integer),
    Column('iscarriedforwardin', Integer),
    Column('ismodifiedcode', Integer),
    Column('createdtime', String(19, u'Chinese_PRC_CI_AS')),
    Column('sequencenumber', Integer),
    Column('ts', TIMESTAMP, nullable=False),
    Column('updated', String(19, u'Chinese_PRC_CI_AS')),
    Column('updatedBy', Unicode(32)),
    Column('priuserdefnvc1', Unicode(500)),
    Column('priuserdefdecm1', Numeric(28, 14)),
    Column('priuserdefnvc2', Unicode(500)),
    Column('priuserdefdecm2', Numeric(28, 14)),
    Column('priuserdefnvc3', Unicode(500)),
    Column('priuserdefdecm3', Numeric(28, 14)),
    Column('priuserdefnvc4', Unicode(500)),
    Column('priuserdefdecm4', Numeric(28, 14)),
    Column('priuserdefnvc5', Unicode(500)),
    Column('priuserdefdecm5', Numeric(28, 14)),
    Column('priuserdefnvc6', Unicode(500)),
    Column('priuserdefdecm6', Numeric(28, 14)),
    Column('pubuserdefnvc1', Unicode(500)),
    Column('pubuserdefdecm1', Numeric(28, 14)),
    Column('pubuserdefnvc2', Unicode(500)),
    Column('pubuserdefdecm2', Numeric(28, 14)),
    Column('pubuserdefnvc3', Unicode(500)),
    Column('pubuserdefdecm3', Numeric(28, 14)),
    Column('pubuserdefnvc4', Unicode(500)),
    Column('pubuserdefdecm4', Numeric(28, 14)),
    Column('pubuserdefnvc5', Unicode(500)),
    Column('pubuserdefdecm5', Numeric(28, 14)),
    Column('pubuserdefnvc6', Unicode(500)),
    Column('pubuserdefdecm6', Numeric(28, 14)),
    Column('PrintCount', Integer),
    Column('id', Integer, nullable=False),
    Column('idbusitype', Integer),
    Column('iddepartment', Integer),
    Column('idstore', Integer),
    Column('idmarketingorgan', Integer),
    Column('idcustomer', Integer),
    Column('idperson', Integer),
    Column('idproject', Integer),
    Column('IdWarehouse', Integer),
    Column('IdOutWarehouse', Integer),
    Column('completestatus', Integer),
    Column('DistributionState', Integer),
    Column('voucherstate', Integer),
    Column('auditorid', Integer),
    Column('makerid', Integer)
)


t_DI_StockRequest_b = Table(
    'DI_StockRequest_b', metadata,
    Column('code', Unicode(30)),
    Column('name', Unicode(200)),
    Column('changerate', Numeric(28, 14)),
    Column('basequantity', Numeric(28, 14)),
    Column('subquantity', Numeric(28, 14)),
    Column('invbarcode', Unicode(50)),
    Column('quantity', Numeric(28, 14)),
    Column('quantity2', Numeric(28, 14)),
    Column('retailprice', Numeric(28, 14)),
    Column('retailamount', Numeric(28, 14)),
    Column('onwayquantity', Numeric(28, 14)),
    Column('onwayquantity2', Numeric(28, 14)),
    Column('totalpurchasequantity', Numeric(28, 14)),
    Column('totalpurchasequantity2', Numeric(28, 14)),
    Column('totaltransquantity', Numeric(28, 14)),
    Column('totaltransquantity2', Numeric(28, 14)),
    Column('totalstockoutquantity', Numeric(28, 14)),
    Column('totalstockoutquantity2', Numeric(28, 14)),
    Column('differencequantity', Numeric(28, 14)),
    Column('differencequantity2', Numeric(28, 14)),
    Column('RequirementDate', String(19, u'Chinese_PRC_CI_AS')),
    Column('totaldistributionquantity', Numeric(28, 14)),
    Column('totaldistributionquantity2', Numeric(28, 14)),
    Column('totalstockinquantity', Numeric(28, 14)),
    Column('totalstockinquantity2', Numeric(28, 14)),
    Column('haspra', Integer),
    Column('totalpracount', Integer),
    Column('totalexecutedquantity', Numeric(28, 14)),
    Column('totalexecutedquantity2', Numeric(28, 14)),
    Column('compositionquantity', Unicode(50)),
    Column('createdtime', String(19, u'Chinese_PRC_CI_AS')),
    Column('sequencenumber', Integer),
    Column('ts', TIMESTAMP, nullable=False),
    Column('updated', String(19, u'Chinese_PRC_CI_AS')),
    Column('updatedBy', Unicode(32)),
    Column('priuserdefnvc1', Unicode(500)),
    Column('priuserdefdecm1', Numeric(28, 14)),
    Column('priuserdefnvc2', Unicode(500)),
    Column('priuserdefdecm2', Numeric(28, 14)),
    Column('priuserdefnvc3', Unicode(500)),
    Column('priuserdefdecm3', Numeric(28, 14)),
    Column('priuserdefnvc4', Unicode(500)),
    Column('priuserdefdecm4', Numeric(28, 14)),
    Column('pubuserdefnvc1', Unicode(500)),
    Column('pubuserdefdecm1', Numeric(28, 14)),
    Column('pubuserdefnvc2', Unicode(500)),
    Column('pubuserdefdecm2', Numeric(28, 14)),
    Column('pubuserdefnvc3', Unicode(500)),
    Column('pubuserdefdecm3', Numeric(28, 14)),
    Column('pubuserdefnvc4', Unicode(500)),
    Column('pubuserdefdecm4', Numeric(28, 14)),
    Column('freeItem0', Unicode(300)),
    Column('freeItem1', Unicode(300)),
    Column('freeItem2', Unicode(300)),
    Column('freeItem3', Unicode(300)),
    Column('freeItem4', Unicode(300)),
    Column('freeItem5', Unicode(300)),
    Column('freeItem6', Unicode(300)),
    Column('freeItem7', Unicode(300)),
    Column('freeItem8', Unicode(300)),
    Column('freeItem9', Unicode(300)),
    Column('id', Integer, nullable=False),
    Column('idinventory', Integer),
    Column('idproject', Integer),
    Column('idbaseunit', Integer),
    Column('idsubunit', Integer),
    Column('idunit', Integer),
    Column('idunit2', Integer),
    Column('IdOutWarehouse', Integer),
    Column('idStockRequestDTO', Integer),
    Column('completestatus', Integer),
    Column('DistributionState', Integer)
)


t_DI_StockSalesReport = Table(
    'DI_StockSalesReport', metadata,
    Column('code', Unicode(30)),
    Column('name', Unicode(200)),
    Column('begindate', String(19, u'Chinese_PRC_CI_AS')),
    Column('enddate', String(19, u'Chinese_PRC_CI_AS')),
    Column('contact', Unicode(50)),
    Column('telephone', Unicode(50)),
    Column('memo', Unicode(200)),
    Column('voucherdate', String(19, u'Chinese_PRC_CI_AS')),
    Column('madedate', String(19, u'Chinese_PRC_CI_AS')),
    Column('maker', Unicode(50)),
    Column('auditor', Unicode(50)),
    Column('auditeddate', String(19, u'Chinese_PRC_CI_AS')),
    Column('reviser', Unicode(50)),
    Column('iscarriedforwardout', Integer),
    Column('iscarriedforwardin', Integer),
    Column('ismodifiedcode', Integer),
    Column('createdtime', String(19, u'Chinese_PRC_CI_AS')),
    Column('sequencenumber', Integer),
    Column('ts', TIMESTAMP, nullable=False),
    Column('updated', String(19, u'Chinese_PRC_CI_AS')),
    Column('updatedBy', Unicode(32)),
    Column('priuserdefnvc1', Unicode(500)),
    Column('priuserdefdecm1', Numeric(28, 14)),
    Column('priuserdefnvc2', Unicode(500)),
    Column('priuserdefdecm2', Numeric(28, 14)),
    Column('priuserdefnvc3', Unicode(500)),
    Column('priuserdefdecm3', Numeric(28, 14)),
    Column('priuserdefnvc4', Unicode(500)),
    Column('priuserdefdecm4', Numeric(28, 14)),
    Column('priuserdefnvc5', Unicode(500)),
    Column('priuserdefdecm5', Numeric(28, 14)),
    Column('priuserdefnvc6', Unicode(500)),
    Column('priuserdefdecm6', Numeric(28, 14)),
    Column('pubuserdefnvc1', Unicode(500)),
    Column('pubuserdefdecm1', Numeric(28, 14)),
    Column('pubuserdefnvc2', Unicode(500)),
    Column('pubuserdefdecm2', Numeric(28, 14)),
    Column('pubuserdefnvc3', Unicode(500)),
    Column('pubuserdefdecm3', Numeric(28, 14)),
    Column('pubuserdefnvc4', Unicode(500)),
    Column('pubuserdefdecm4', Numeric(28, 14)),
    Column('pubuserdefnvc5', Unicode(500)),
    Column('pubuserdefdecm5', Numeric(28, 14)),
    Column('pubuserdefnvc6', Unicode(500)),
    Column('pubuserdefdecm6', Numeric(28, 14)),
    Column('PrintCount', Integer, server_default=text("((0))")),
    Column('id', Integer, nullable=False),
    Column('idmarketingorgan', Integer),
    Column('idcustomer', Integer),
    Column('idperson', Integer),
    Column('idSourceVoucherType', Integer),
    Column('StockSalesReportOrderStatus', Integer),
    Column('voucherstate', Integer),
    Column('auditorid', Integer),
    Column('makerid', Integer)
)


t_DI_StockSalesReport_b = Table(
    'DI_StockSalesReport_b', metadata,
    Column('code', Unicode(30)),
    Column('name', Unicode(200)),
    Column('quantity', Numeric(28, 14)),
    Column('dailyaveragesalesquantity', Numeric(28, 14)),
    Column('stockquantity', Numeric(28, 14)),
    Column('ReplenishQuantity', Numeric(28, 14)),
    Column('ReplenishQuantityByStockUnit', Numeric(28, 14)),
    Column('ispersist', Integer),
    Column('quantitybystockunit', Numeric(28, 14)),
    Column('dailyaveragesalesquantitybystockunit', Numeric(28, 14)),
    Column('stockquantitybystockunit', Numeric(28, 14)),
    Column('basequantity', Numeric(28, 14)),
    Column('subquantity', Numeric(28, 14)),
    Column('changerate', Numeric(28, 14)),
    Column('createdtime', String(19, u'Chinese_PRC_CI_AS')),
    Column('sequencenumber', Integer),
    Column('ts', TIMESTAMP, nullable=False),
    Column('updated', String(19, u'Chinese_PRC_CI_AS')),
    Column('updatedBy', Unicode(32)),
    Column('freeItem0', Unicode(300)),
    Column('freeItem1', Unicode(300)),
    Column('freeItem2', Unicode(300)),
    Column('freeItem3', Unicode(300)),
    Column('freeItem4', Unicode(300)),
    Column('freeItem5', Unicode(300)),
    Column('freeItem6', Unicode(300)),
    Column('freeItem7', Unicode(300)),
    Column('freeItem8', Unicode(300)),
    Column('freeItem9', Unicode(300)),
    Column('pubuserdefnvc1', Unicode(500)),
    Column('pubuserdefdecm1', Numeric(28, 14)),
    Column('pubuserdefnvc2', Unicode(500)),
    Column('pubuserdefdecm2', Numeric(28, 14)),
    Column('pubuserdefnvc3', Unicode(500)),
    Column('pubuserdefdecm3', Numeric(28, 14)),
    Column('pubuserdefnvc4', Unicode(500)),
    Column('pubuserdefdecm4', Numeric(28, 14)),
    Column('priuserdefnvc1', Unicode(500)),
    Column('priuserdefdecm1', Numeric(28, 14)),
    Column('priuserdefnvc2', Unicode(500)),
    Column('priuserdefdecm2', Numeric(28, 14)),
    Column('priuserdefnvc3', Unicode(500)),
    Column('priuserdefdecm3', Numeric(28, 14)),
    Column('priuserdefnvc4', Unicode(500)),
    Column('priuserdefdecm4', Numeric(28, 14)),
    Column('RetailPrice', Numeric(28, 14)),
    Column('RetailAmount', Numeric(28, 14)),
    Column('StockAmount', Numeric(28, 14)),
    Column('id', Integer, nullable=False),
    Column('idinventory', Integer),
    Column('idInventoryMutiCode', Integer),
    Column('idunit', Integer),
    Column('idunit2', Integer),
    Column('idStockSalesReportDTO', Integer)
)


t_DI_StoreDailyCurrentStock = Table(
    'DI_StoreDailyCurrentStock', metadata,
    Column('ts', TIMESTAMP, nullable=False),
    Column('updatedBy', Unicode(32)),
    Column('updated', String(19, u'Chinese_PRC_CI_AS')),
    Column('name', Unicode(200)),
    Column('StockRequestQuantity', Numeric(28, 14), nullable=False, server_default=text("((0))")),
    Column('BaseQuantity', Numeric(28, 14), nullable=False, server_default=text("((0))")),
    Column('CanUseQuantity', Numeric(28, 14), nullable=False, server_default=text("((0))")),
    Column('PurchaseArrivalQuantity', Numeric(28, 14), nullable=False, server_default=text("((0))")),
    Column('PurchaseForReceiveQuantity', Numeric(28, 14), nullable=False, server_default=text("((0))")),
    Column('ProductForReceiveQuantity', Numeric(28, 14), nullable=False, server_default=text("((0))")),
    Column('SaleDeliveryQuantity', Numeric(28, 14), nullable=False, server_default=text("((0))")),
    Column('SaleDispatchQuantity', Numeric(28, 14), nullable=False, server_default=text("((0))")),
    Column('OtherOnWayQuantity', Numeric(28, 14), nullable=False, server_default=text("((0))")),
    Column('TransOnWayQuantity', Numeric(28, 14), nullable=False, server_default=text("((0))")),
    Column('OtherForDispatchQuantity', Numeric(28, 14), nullable=False, server_default=text("((0))")),
    Column('TransForDispatchQuantity', Numeric(28, 14), nullable=False, server_default=text("((0))")),
    Column('SafeQuantity', Numeric(28, 14), nullable=False, server_default=text("((0))")),
    Column('LowQuantity', Numeric(28, 14), nullable=False, server_default=text("((0))")),
    Column('freeItem0', Unicode(300)),
    Column('freeItem1', Unicode(300)),
    Column('freeItem2', Unicode(300)),
    Column('freeItem3', Unicode(300)),
    Column('freeItem4', Unicode(300)),
    Column('freeItem5', Unicode(300)),
    Column('freeItem6', Unicode(300)),
    Column('freeItem7', Unicode(300)),
    Column('freeItem8', Unicode(300)),
    Column('freeItem9', Unicode(300)),
    Column('ESStoreForDispatchQuantity', Numeric(28, 14), nullable=False, server_default=text("((0))")),
    Column('DistributionForReceiveQuantity', Numeric(28, 14), nullable=False, server_default=text("((0))")),
    Column('id', Integer, nullable=False),
    Column('idinventory', Integer),
    Column('idwarehouse', Integer)
)


t_DI_TEMP_DAQ = Table(
    'DI_TEMP_DAQ', metadata,
    Column('Quantity', Numeric(28, 14)),
    Column('IdSku', Integer)
)


t_DI_VoucherSelectResult = Table(
    'DI_VoucherSelectResult', metadata,
    Column('code', Unicode(30)),
    Column('name', Unicode(200)),
    Column('VouchertypeCode', Unicode(50)),
    Column('ts', TIMESTAMP, nullable=False),
    Column('updated', String(19, u'Chinese_PRC_CI_AS')),
    Column('updatedBy', Unicode(32)),
    Column('id', Integer, nullable=False),
    Column('Voucherid', Integer),
    Column('VoucherDetailId', Integer),
    Column('userId', Integer),
    Column('idvoucherType', Integer)
)


t_EAP_AccInformation = Table(
    'EAP_AccInformation', metadata,
    Column('SysID', Unicode(4)),
    Column('InfoID', Unicode(6), nullable=False),
    Column('Name', Unicode(100), nullable=False),
    Column('Caption', Unicode(30)),
    Column('Type', Unicode(20)),
    Column('Value', Unicode(100)),
    Column('Default', Unicode(100)),
    Column('IsVisible', BIT),
    Column('IsEnable', BIT),
    Column('OptionType', Integer),
    Column('ExpressionName', Unicode(60)),
    Column('Version', Unicode(60)),
    Column('ts', TIMESTAMP, nullable=False),
    Column('idEnablePeriod', Integer)
)


class EAPAppUserAssociation(Base):
    __tablename__ = 'EAP_AppUserAssociation'

    AppUserID = Column(Unicode(64), nullable=False)
    AppUserName = Column(Unicode(64))
    ts = Column(TIMESTAMP, nullable=False)
    AccessToken = Column(Unicode(200))
    RefreshToken = Column(Unicode(200))
    ExpiredTime = Column(DateTime)
    LastUpdateTime = Column(DateTime)
    IsAdmin = Column(Integer)
    BindState = Column(Unicode(200))
    id = Column(Integer, primary_key=True)
    AppID = Column(Integer, nullable=False, server_default=text("((0))"))
    UserID = Column(Integer, nullable=False, server_default=text("((0))"))


class EAPAuthControl(Base):
    __tablename__ = 'EAP_AuthControl'

    dataauthtype = Column(Integer)
    iscontrol = Column(BIT)
    controltype = Column(Integer)
    ts = Column(TIMESTAMP)
    id = Column(Integer, primary_key=True)
    archivesid = Column(Integer)
    idactor = Column(Integer)


class EAPAuthorizedApp(Base):
    __tablename__ = 'EAP_AuthorizedApp'

    ID = Column(Integer, primary_key=True)
    Code = Column(Unicode(64), nullable=False)
    Name = Column(Unicode(128))
    Title = Column(Unicode(128))
    Description = Column(Unicode(512))
    IconUrl = Column(Unicode(256), nullable=False)
    AutoLoginUrl = Column(Unicode(256), nullable=False)
    VerifyUrl = Column(Unicode(256), nullable=False)
    InterfaceMethodUrl = Column(Unicode(256))


class EAPBusOperation(Base):
    __tablename__ = 'EAP_BusOperation'

    OperationName = Column(Unicode(50), nullable=False)
    FunctionCode = Column(Unicode(20))
    Description = Column(Unicode(100))
    Code = Column(Unicode(50), index=True)
    ViewType = Column(SmallInteger, nullable=False, server_default=text("(1)"))
    TabIndex = Column(Integer)
    IsSplit = Column(BIT, nullable=False, server_default=text("(0)"))
    SourceKey = Column(Unicode(30))
    IsAuthControl = Column(BIT, nullable=False, server_default=text("(1)"))
    Title = Column(Unicode(50), nullable=False)
    Visibility = Column(BIT, nullable=False, server_default=text("(1)"))
    ShortCut = Column(String(1, u'Chinese_PRC_CI_AS'))
    ToolTip = Column(Unicode(50))
    issystem = Column(BIT)
    IsHasAction = Column(BIT)
    IsEnd = Column(Integer, server_default=text("((1))"))
    ExpressionName = Column(Unicode(60))
    ts = Column(TIMESTAMP, nullable=False)
    CreatedTime = Column(DateTime)
    id = Column(Integer, primary_key=True)
    ParentID = Column(Integer)
    idbusoperationmain = Column(Integer)
    idfunctionauth = Column(Integer)
    viewid = Column(Integer)


class EAPBusOperationMain(Base):
    __tablename__ = 'EAP_BusOperationMain'

    code = Column(Unicode(30))
    name = Column(Unicode(200))
    ts = Column(TIMESTAMP, nullable=False)
    CreatedTime = Column(DateTime)
    TFlag = Column(Integer, server_default=text("((0))"))
    id = Column(Integer, primary_key=True)
    ViewType = Column(Integer)
    idMenu = Column(Integer)


class EAPFieldAuth(Base):
    __tablename__ = 'EAP_FieldAuth'

    menucode = Column(Unicode(30))
    name = Column(Unicode(200))
    title = Column(Unicode(50))
    orderIndex = Column(Integer)
    issystem = Column(BIT)
    isinauth = Column(BIT)
    ishasread = Column(BIT)
    ishasupdate = Column(BIT)
    ts = Column(TIMESTAMP)
    viewtype = Column(SmallInteger)
    id = Column(Integer, primary_key=True)
    ExpressionName = Column(Unicode(60))
    Category = Column(Integer)
    idparent = Column(Integer)


class EAPFunctionAuth(Base):
    __tablename__ = 'EAP_FunctionAuth'

    menucode = Column(Unicode(30))
    name = Column(Unicode(200))
    title = Column(Unicode(50))
    tabindex = Column(Integer)
    issystem = Column(BIT)
    functioncode = Column(Unicode(50))
    description = Column(Unicode(200))
    ts = Column(TIMESTAMP)
    ID = Column(Integer, primary_key=True)
    ExpressionName = Column(Unicode(60))
    Category = Column(Integer)
    ControlType = Column(Integer)
    IsHasTag = Column(Integer)
    ControlID = Column(Integer)
    idparent = Column(Integer)


class EAPGroup(Base):
    __tablename__ = 'EAP_Group'

    code = Column(Unicode(20))
    name = Column(Unicode(50))
    memo = Column(Unicode(50))
    id = Column(Integer, primary_key=True)
    IsStop = Column(BIT, server_default=text("(0)"))
    AuthState = Column(Integer, server_default=text("(0)"))
    ts = Column(TIMESTAMP)
    updated = Column(DateTime)
    updatedBy = Column(Unicode(32))
    issystem = Column(BIT, server_default=text("((0))"))
    showIndex = Column(Integer)
    IsHeadQuarters = Column(Integer)
    ExpressionName = Column(Unicode(60))
    OrderNum = Column(Integer)


class EAPHoldFieldAuth(Base):
    __tablename__ = 'EAP_HoldFieldAuth'

    menucode = Column(Unicode(30))
    name = Column(Unicode(200))
    privilegetype = Column(Integer)
    isusergroup = Column(BIT)
    ts = Column(TIMESTAMP)
    id = Column(Integer, primary_key=True)
    idfieldauth = Column(Integer)
    idactor = Column(Integer)


class EAPHoldFunctionAuth(Base):
    __tablename__ = 'EAP_HoldFunctionAuth'

    menucode = Column(Unicode(30))
    name = Column(Unicode(200))
    isusergroup = Column(BIT)
    ts = Column(TIMESTAMP)
    Tag = Column(Unicode(50))
    id = Column(Integer, primary_key=True)
    idfunctionauth = Column(Integer)
    idactor = Column(Integer)


class EAPHoldRowAuth(Base):
    __tablename__ = 'EAP_HoldRowAuth'

    isusergroup = Column(Integer)
    classtype = Column(SmallInteger)
    ts = Column(TIMESTAMP)
    id = Column(Integer, primary_key=True)
    idactor = Column(Integer)
    rowobjectid = Column(Integer)
    ArchivesId = Column(Integer)
    idarchivesauthclass = Column(Integer)


class EAPLevelBaseInfo(Base):
    __tablename__ = 'EAP_LevelBaseInfo'

    title = Column(Unicode(50))
    DTOName = Column(Unicode(200))
    TableName = Column(Unicode(50))
    MatchKeys = Column(Unicode(200))
    IsSystem = Column(Integer)
    ParentTableName = Column(Unicode(50))
    ExtTableName = Column(Unicode(50))
    IsOnlyRefEndNode = Column(Integer)
    id = Column(Integer, primary_key=True)


class EAPMenu(Base):
    __tablename__ = 'EAP_Menu'

    id = Column(Integer, primary_key=True)
    Code = Column(Unicode(50))
    Name = Column(Unicode(100))
    ShortCut = Column(String(1, u'Chinese_PRC_CI_AS'))
    Grade = Column(SmallInteger, nullable=False, server_default=text("(0)"))
    SupMenuID = Column(Unicode(12))
    EndGrade = Column(BIT, server_default=text("(0)"))
    Order = Column(Integer)
    RequestUrl = Column(Unicode(500))
    GroupFlow = Column(Unicode(20))
    IsItemGroup = Column(BIT, server_default=text("(0)"))
    IsControl = Column(BIT, nullable=False, server_default=text("(0)"))
    Version = Column(Unicode(12))
    AccountType = Column(SmallInteger, server_default=text("(0)"))
    Visibility = Column(BIT, nullable=False, server_default=text("(1)"))
    ts = Column(TIMESTAMP)
    inID = Column(Unicode(50))
    PrivilegeID = Column(Unicode(30))
    ExpressionName = Column(Unicode(60))
    InvBarCodeVoucher = Column(Integer)
    TFlag = Column(Integer, server_default=text("((0))"))
    CreatedTime = Column(DateTime)
    isCommonUse = Column(BIT, server_default=text("((0))"))
    RelationMenuCode = Column(Unicode(100))
    RelationMenuTitle = Column(Unicode(100))


class EAPMessageAddress(Base):
    __tablename__ = 'EAP_MessageAddress'

    DisplayName = Column(Unicode(100))
    Address = Column(Unicode(254), nullable=False)
    UserId = Column(Unicode(254))
    TargetId = Column(Unicode(36), nullable=False)
    Id = Column(Integer, primary_key=True)
    MessageId = Column(Integer, nullable=False, index=True, server_default=text("((0))"))


class EAPMessageAttachment(Base):
    __tablename__ = 'EAP_MessageAttachment'

    Name = Column(Unicode(100))
    Content = Column(LargeBinary)
    ContentType = Column(Unicode(100))
    Id = Column(Integer, primary_key=True)
    MessageId = Column(Integer, nullable=False, server_default=text("((0))"))


class EAPMessageBox(Base):
    __tablename__ = 'EAP_MessageBox'
    __table_args__ = (
        Index('IDX_EAP_MESSAGEBOX_MSGID_ISDEL_DIRE', 'MessageId', 'IsDelete', 'Direction'),
    )

    UserId = Column(Unicode(254), nullable=False)
    IsUnread = Column(BIT, nullable=False, server_default=text("((1))"))
    IsDelete = Column(BIT, nullable=False, server_default=text("((0))"))
    Direction = Column(Integer)
    Id = Column(Integer, primary_key=True)
    MessageId = Column(Integer, nullable=False, server_default=text("((0))"))


t_EAP_MessageRuleInfo = Table(
    'EAP_MessageRuleInfo', metadata,
    Column('Name', Unicode(50)),
    Column('Description', Unicode(100)),
    Column('BusinessCode', Unicode(50)),
    Column('Id', Integer, nullable=False, server_default=text("((0))")),
    Column('TypeId', Integer, nullable=False, server_default=text("((0))")),
    Index('IDX_EAP_MessageRuleInfo_ID_TypeID', 'Id', 'TypeId', unique=True)
)


class EAPMessageRuleTypeInfo(Base):
    __tablename__ = 'EAP_MessageRuleTypeInfo'

    Name = Column(Unicode(50), nullable=False)
    Description = Column(Unicode(100))
    RuleType = Column(Unicode(254), nullable=False)
    SettingUI = Column(Unicode(254))
    id = Column(Integer, primary_key=True)


class EAPMessageSettings(Base):
    __tablename__ = 'EAP_MessageSettings'

    Name = Column(Unicode(50), nullable=False)
    Description = Column(Unicode(100))
    Value = Column(UnicodeText(1073741823))
    Type = Column(Unicode(254))
    Id = Column(Integer, primary_key=True)


class EAPMessageTemplate(Base):
    __tablename__ = 'EAP_MessageTemplate'

    ts = Column(TIMESTAMP, nullable=False)
    Category = Column(Unicode(254))
    Title = Column(Unicode(254))
    Content = Column(Unicode(2000))
    Name = Column(Unicode(200))
    id = Column(Integer, primary_key=True)


class EAPMutexContent(Base):
    __tablename__ = 'EAP_MutexContent'

    FunctionTag = Column(Unicode(20), nullable=False)
    MutexType = Column(Integer, nullable=False)
    MutexFunction = Column(Unicode(20))
    NotMutexFunction = Column(Unicode(20))
    MutexID = Column(Integer, primary_key=True)


class EAPPortalMessage(Base):
    __tablename__ = 'EAP_PortalMessage'

    id = Column(Integer, primary_key=True)
    userId = Column(Integer, nullable=False)
    count = Column(Integer, nullable=False)
    typeId = Column(Integer, nullable=False)
    updatedDateTime = Column(DateTime)
    ts = Column(TIMESTAMP, nullable=False)


class EAPPortalMessageType(Base):
    __tablename__ = 'EAP_PortalMessageType'

    id = Column(Integer, primary_key=True)
    name = Column(Unicode(200), nullable=False)
    groupType = Column(Unicode(200), nullable=False)
    subGroupType = Column(Unicode(50), nullable=False)
    subGroupTitle = Column(Unicode(200), nullable=False)
    subGroupOrder = Column(Integer, nullable=False)
    bizCode = Column(Unicode(50))
    code = Column(Unicode(50))
    url = Column(Unicode(500), nullable=False)
    ExpressionName = Column(Unicode(60))
    IsVisible = Column(BIT)
    serviceType = Column(Unicode(500))
    AliName = Column(Unicode(100))
    ts = Column(TIMESTAMP, nullable=False)


class EAPPortalSkin(Base):
    __tablename__ = 'EAP_PortalSkin'

    id = Column(Integer, primary_key=True)
    userId = Column(Integer, nullable=False)
    skinValue = Column(Unicode(50), nullable=False)


class EAPPortalSystem(Base):
    __tablename__ = 'EAP_PortalSystem'

    ShowName = Column(Unicode(20), nullable=False)
    FirstPageStyle = Column(SmallInteger, server_default=text("((2))"))
    ID = Column(Integer, primary_key=True)
    UserId = Column(Integer, nullable=False, server_default=text("((0))"))


t_EAP_ReportBasic = Table(
    'EAP_ReportBasic', metadata,
    Column('ReportCode', Unicode(200), nullable=False, server_default=text("('')")),
    Column('SubSysId', Unicode(100), nullable=False, server_default=text("('')")),
    Column('ReportName', Unicode(200), nullable=False),
    Column('CreateDate', DateTime, nullable=False, server_default=text("(getdate())")),
    Column('Createor', Unicode(50), nullable=False),
    Column('UpdateDate', DateTime, nullable=False),
    Column('Updater', Unicode(50), nullable=False),
    Column('ReportFlag', Integer, nullable=False, server_default=text("((2))")),
    Column('Memo', Unicode(500), nullable=False, server_default=text("('')")),
    Column('TS', TIMESTAMP, nullable=False),
    Column('MenuCode', Unicode(50), nullable=False, server_default=text("('')")),
    Column('ParentMenuCode', Unicode(50), nullable=False, server_default=text("('')")),
    Column('TemplateId', Integer, nullable=False, server_default=text("((0))")),
    Column('ID', Integer, nullable=False, server_default=text("((0))")),
    Column('TypeID', Integer),
    Column('UpdateID', Integer, nullable=False, server_default=text("((0))"))
)


class EAPReportCommonSet(Base):
    __tablename__ = 'EAP_ReportCommonSet'

    ReportName = Column(Unicode(200), nullable=False)
    ItemValue = Column(Integer, nullable=False)
    ItemType = Column(Integer, nullable=False)
    sumRowDisplayName = Column(Unicode(200))
    id = Column(Integer, primary_key=True)
    ts = Column(TIMESTAMP, nullable=False)


class EAPReportCommonSetRelation(Base):
    __tablename__ = 'EAP_ReportCommonSetRelation'

    SourceTable = Column(Unicode(200), nullable=False)
    ItemValue = Column(Integer, nullable=False)
    RelationTable = Column(Unicode(200), nullable=False)
    ID = Column(Integer, primary_key=True)
    ts = Column(TIMESTAMP, nullable=False)
    SourceID = Column(Integer, nullable=False, server_default=text("((0))"))
    RelationID = Column(Integer, nullable=False, server_default=text("((0))"))


class EAPReportData(Base):
    __tablename__ = 'EAP_ReportData'

    ReportData = Column(UnicodeText(1073741823), nullable=False)
    TS = Column(TIMESTAMP, nullable=False)
    TemplateChanged = Column(Integer, nullable=False)
    Sheet = Column(Integer, nullable=False, server_default=text("((1))"))
    SheetName = Column(Unicode(50), nullable=False, server_default=text("('')"))
    Cols = Column(Integer, nullable=False, server_default=text("((1))"))
    Rows = Column(Integer, nullable=False, server_default=text("((1))"))
    ID = Column(Integer, primary_key=True)
    ReportID = Column(Integer, nullable=False, server_default=text("((0))"))
    TemplateId = Column(Integer, nullable=False, server_default=text("((0))"))
    UpdateID = Column(Integer, nullable=False, server_default=text("((0))"))


class EAPReportFormat(Base):
    __tablename__ = 'EAP_ReportFormat'

    FormatData = Column(LargeBinary, nullable=False)
    TS = Column(TIMESTAMP, nullable=False)
    ID = Column(Integer, primary_key=True)
    ReportID = Column(Integer, nullable=False, server_default=text("((0))"))
    UpdateID = Column(Integer, nullable=False, server_default=text("((0))"))


class EAPReportFormula(Base):
    __tablename__ = 'EAP_ReportFormula'

    FormulaCode = Column(Unicode(50))
    FormulaName = Column(Unicode(50), nullable=False, server_default=text("('')"))
    FormulaTitle = Column(Unicode(50), nullable=False, server_default=text("('')"))
    FormulaFormat = Column(Unicode(1000), server_default=text("('')"))
    FormulaDescription = Column(Unicode(1000), server_default=text("('')"))
    FormulaHelp = Column(Unicode(400), nullable=False, server_default=text("('')"))
    IsHasReference = Column(BIT, nullable=False, server_default=text("((0))"))
    ReferenceUrl = Column(Unicode(100), nullable=False, server_default=text("('')"))
    ShowIndex = Column(Integer, nullable=False, server_default=text("((0))"))
    Example = Column(Unicode(1000), server_default=text("('')"))
    ID = Column(Integer, primary_key=True)
    LinkUrl = Column(Unicode(200))
    code = Column(Unicode(200))
    name = Column(Unicode(200))
    TypeID = Column(Integer, nullable=False, server_default=text("((0))"))


class EAPReportFormulaCheck(Base):
    __tablename__ = 'EAP_ReportFormulaCheck'

    Formulas = Column(Unicode(500), nullable=False, server_default=text("('')"))
    CheckName = Column(Unicode(200), server_default=text("('')"))
    ErrDescript = Column(Unicode(100), nullable=False, server_default=text("('')"))
    CheckType = Column(Integer, nullable=False, server_default=text("((1))"))
    ID = Column(Integer, primary_key=True)
    TemplateID = Column(Integer, nullable=False, server_default=text("((0))"))


class EAPReportFormulaType(Base):
    __tablename__ = 'EAP_ReportFormulaType'

    TypeName = Column(Unicode(50), nullable=False, server_default=text("('')"))
    SubSysId = Column(Unicode(20), nullable=False, server_default=text("('')"))
    Assembly = Column(Unicode(200), nullable=False, server_default=text("('')"))
    ClassName = Column(Unicode(100), nullable=False, server_default=text("('')"))
    IsVisible = Column(BIT)
    Flag = Column(Integer)
    ID = Column(Integer, primary_key=True)
    Position = Column(Integer)
    TypeLevel = Column(Integer, nullable=False, server_default=text("((1))"))
    IsEndNode = Column(Integer)
    IdParent = Column(Integer)


t_EAP_ReportFormulaValue = Table(
    'EAP_ReportFormulaValue', metadata,
    Column('ReportFormulaValue', UnicodeText(1073741823)),
    Column('Ts', TIMESTAMP, nullable=False),
    Column('Sheet', Integer),
    Column('ReportID', Integer, nullable=False, server_default=text("((0))")),
    Column('TemplateId', Integer, nullable=False, server_default=text("((0))"))
)


class EAPReportKeyWords(Base):
    __tablename__ = 'EAP_ReportKeyWords'

    KeyName = Column(Unicode(100), nullable=False, server_default=text("('')"))
    KeyText = Column(Unicode(50), server_default=text("('')"))
    KeyType = Column(Unicode(100), nullable=False, server_default=text("('0')"))
    SubSysId = Column(Unicode(50), server_default=text("('')"))
    ID = Column(Integer, primary_key=True)
    FieldType = Column(Unicode(400))
    RefDTOName = Column(Unicode(100))
    RefDTOProperty = Column(Unicode(100))
    EnumName = Column(Unicode(100))
    ControlType = Column(Unicode(100))
    SortId = Column(Integer)
    idEnum = Column(Integer)
    USAGE = Column(Integer)


class EAPReportKeyWordsData(Base):
    __tablename__ = 'EAP_ReportKeyWordsData'

    KeyName = Column(Unicode(50), primary_key=True, nullable=False, server_default=text("('')"))
    KeyValue = Column(Unicode(50))
    KeyDataType = Column(Integer, nullable=False, server_default=text("((-1))"))
    TS = Column(TIMESTAMP)
    SortId = Column(Integer, nullable=False, server_default=text("((0))"))
    ID = Column(Integer, primary_key=True, nullable=False)
    ReportID = Column(Integer, server_default=text("((0))"))


class EAPReportReject(Base):
    __tablename__ = 'EAP_ReportReject'

    Factor = Column(Integer, nullable=False, server_default=text("((1))"))
    Symbol = Column(Unicode(10), nullable=False, server_default=text("('')"))
    Digits = Column(Integer, nullable=False, server_default=text("((0))"))
    FormulaArea = Column(Unicode(20), nullable=False, server_default=text("('')"))
    Expression = Column(Unicode(1000), nullable=False, server_default=text("('')"))
    ID = Column(Integer, primary_key=True)
    ReportID = Column(Integer, server_default=text("((0))"))


class EAPReportRelationEntity(Base):
    __tablename__ = 'EAP_ReportRelationEntity'

    ts = Column(TIMESTAMP, nullable=False)
    ReportName = Column(Unicode(50), nullable=False)
    EntityName = Column(Unicode(400))
    JoinType = Column(Unicode(20))
    JoinWhere = Column(Unicode(400))
    IsMainEntity = Column(Integer)
    TableName = Column(Unicode)
    EntityTitle = Column(Unicode(50))
    RelationEntity = Column(Unicode(400))
    RelationOption = Column(Unicode(50))
    OptionValue = Column(Unicode(50))
    IsMainVoucher = Column(Integer)
    UnionSection = Column(Integer)
    DTOName = Column(Unicode(50))
    BusinessType = Column(Integer)
    IsEndNode = Column(Integer)
    id = Column(Integer, primary_key=True)
    EntityType = Column(Integer)
    idparent = Column(Integer)
    ideap_reporttemplate = Column(Integer)
    CreatedTime = Column(DateTime)


class EAPReportSection(Base):
    __tablename__ = 'EAP_ReportSection'

    ts = Column(TIMESTAMP, nullable=False)
    Updated = Column(DateTime)
    UpdatedBy = Column(Unicode(32))
    name = Column(Unicode(200), nullable=False)
    Height = Column(Integer)
    Width = Column(Integer)
    LeftSize = Column(Integer)
    TopSize = Column(Integer)
    IsRollUp = Column(Integer)
    id = Column(Integer, primary_key=True)
    SectionType = Column(Integer)
    ideap_reporttemplate = Column(Integer)


class EAPReportTemplateBasic(Base):
    __tablename__ = 'EAP_ReportTemplateBasic'

    TemplateName = Column(Unicode(100), nullable=False, server_default=text("('')"))
    Code = Column(Unicode(30), nullable=False, server_default=text("('')"))
    SubSysId = Column(Unicode(100), nullable=False, server_default=text("('')"))
    Memo = Column(Unicode(500), nullable=False, server_default=text("('')"))
    Creator = Column(Unicode(50), nullable=False)
    CreateTime = Column(DateTime, nullable=False, server_default=text("(getdate())"))
    Updater = Column(Unicode(50), nullable=False, server_default=text("('')"))
    UpdateDate = Column(DateTime, nullable=False, server_default=text("(getdate())"))
    TemplateFlag = Column(Integer, server_default=text("((0))"))
    InSubSys = Column(Integer, server_default=text("((0))"))
    TS = Column(TIMESTAMP, nullable=False)
    IsVisible = Column(Integer, server_default=text("((1))"))
    MenuCode = Column(Unicode(50), nullable=False, server_default=text("('')"))
    ParentMenuCode = Column(Unicode(50), nullable=False, server_default=text("('')"))
    ID = Column(Integer, primary_key=True)
    TemplateID = Column(Integer, nullable=False, server_default=text("((0))"))
    CopyFrom = Column(Integer)
    TypeID = Column(Integer, nullable=False, server_default=text("((0))"))
    UpdateID = Column(Integer, nullable=False, server_default=text("((0))"))


class EAPReportTemplateFormat(Base):
    __tablename__ = 'EAP_ReportTemplateFormat'

    TemplateData = Column(LargeBinary, nullable=False)
    TS = Column(TIMESTAMP, nullable=False)
    ID = Column(Integer, primary_key=True)
    TemplateID = Column(Integer, nullable=False, server_default=text("((0))"))
    UpdateID = Column(Integer, nullable=False, server_default=text("((0))"))
    TemplateBilloneData = Column(LargeBinary)


class EAPReportTemplateFormulas(Base):
    __tablename__ = 'EAP_ReportTemplateFormulas'

    FormulaText = Column(UnicodeText(1073741823), nullable=False, server_default=text("('')"))
    Sheet = Column(Integer, nullable=False, server_default=text("((1))"))
    SheetName = Column(Unicode(50), nullable=False, server_default=text("('')"))
    ID = Column(Integer, primary_key=True)
    UpdateFlag = Column(Integer)
    TemplateID = Column(Integer, nullable=False, server_default=text("((0))"))
    UpdateID = Column(Integer, nullable=False, server_default=text("((0))"))


class EAPReportTemplateModel(Base):
    __tablename__ = 'EAP_ReportTemplateModel'

    TemplateStyle = Column(UnicodeText(1073741823), nullable=False, server_default=text("('')"))
    TS = Column(TIMESTAMP, nullable=False)
    Sheet = Column(Integer, nullable=False, server_default=text("((0))"))
    Rows = Column(Integer, nullable=False, server_default=text("((1))"))
    Cols = Column(Integer, nullable=False, server_default=text("((1))"))
    SheetName = Column(Unicode(50), nullable=False, server_default=text("('')"))
    ID = Column(Integer, primary_key=True)
    TemplateID = Column(Integer, nullable=False, server_default=text("((0))"))
    UpdateID = Column(Integer, nullable=False, server_default=text("((0))"))


class EAPReportType(Base):
    __tablename__ = 'EAP_ReportType'

    Name = Column(Unicode(100), nullable=False, server_default=text("('')"))
    Code = Column(Unicode(100), nullable=False, server_default=text("('')"))
    CreateDate = Column(DateTime, nullable=False, server_default=text("(getdate())"))
    IsSystem = Column(Integer, nullable=False, server_default=text("((1))"))
    TypeLevel = Column(Integer, nullable=False, server_default=text("((1))"))
    SubSysId = Column(Unicode(50), nullable=False, server_default=text("('')"))
    HasChild = Column(Integer, server_default=text("((0))"))
    ID = Column(Integer, primary_key=True)
    TypeState = Column(Integer, nullable=False, server_default=text("((2))"))
    IsEndNode = Column(Integer, nullable=False, server_default=text("((0))"))
    InId = Column(Unicode(2000), nullable=False, server_default=text("('')"))
    NumbID = Column(Integer)
    IdParent = Column(Integer)


class EAPRowAuth(Base):
    __tablename__ = 'EAP_RowAuth'

    ts = Column(TIMESTAMP, nullable=False)
    name = Column(Unicode(200), nullable=False)
    IsSystem = Column(Integer)
    Title = Column(Unicode(50))
    ShowIndex = Column(Integer)
    ModuleName = Column(Unicode(20))
    Category = Column(Integer)
    MarketingOrganFileName = Column(Unicode(60))
    id = Column(Integer, primary_key=True)


class EAPRowAuthItem(Base):
    __tablename__ = 'EAP_RowAuthItem'

    ts = Column(TIMESTAMP, nullable=False)
    name = Column(Unicode(200), nullable=False)
    DataSource = Column(Unicode(50))
    RefDataSource = Column(Unicode(50))
    Title = Column(Unicode(20))
    ShowIndex = Column(Integer)
    AuthType = Column(Integer)
    IsPublic = Column(Integer)
    DynPropertyString = Column(Unicode(2000))
    IsSystem = Column(Integer)
    id = Column(Integer, primary_key=True)
    ideap_rowauth = Column(Integer)


class EAPRowAuthMapping(Base):
    __tablename__ = 'EAP_RowAuthMapping'

    ts = Column(TIMESTAMP, nullable=False)
    name = Column(Unicode(200), nullable=False)
    SelectFields = Column(Unicode(200))
    DTOName = Column(Unicode(200))
    MenuCode = Column(Unicode(50))
    id = Column(Integer, primary_key=True)


t_EAP_SYSReportKeyWordsData = Table(
    'EAP_SYSReportKeyWordsData', metadata,
    Column('KeyName', Unicode(50), nullable=False, server_default=text("('')")),
    Column('KeyValue', Unicode(50)),
    Column('KeyDataType', Integer, nullable=False, server_default=text("((-1))")),
    Column('TS', TIMESTAMP),
    Column('SortId', Integer, nullable=False, server_default=text("((0))")),
    Column('SubSysId', Unicode(20), nullable=False, server_default=text("('')")),
    Column('ID', Integer, server_default=text("((0))"))
)


class EAPSYSReportTemplateBasic(Base):
    __tablename__ = 'EAP_SYSReportTemplateBasic'

    TemplateName = Column(Unicode(100), nullable=False, server_default=text("('')"))
    Code = Column(Unicode(30), nullable=False, server_default=text("('')"))
    Memo = Column(Unicode(500), nullable=False, server_default=text("('')"))
    Creator = Column(Unicode(50), nullable=False)
    CreateTime = Column(DateTime, nullable=False, server_default=text("(getdate())"))
    Updater = Column(Unicode(50), nullable=False, server_default=text("('')"))
    UpdateDate = Column(DateTime, nullable=False, server_default=text("(getdate())"))
    TemplateFlag = Column(Integer, server_default=text("((0))"))
    InSubSys = Column(Integer, server_default=text("((0))"))
    TS = Column(TIMESTAMP, nullable=False)
    IsVisible = Column(Integer, server_default=text("((1))"))
    SubSysId = Column(Unicode(20), nullable=False, server_default=text("('')"))
    TypeID = Column(Integer, nullable=False, server_default=text("((0))"))
    IDIndustryType = Column(Integer)
    CopyFrom = Column(Integer)
    UpdateID = Column(Integer, nullable=False, server_default=text("((0))"))
    TemplateId = Column(Integer, primary_key=True)


class EAPSYSReportTemplateFormat(Base):
    __tablename__ = 'EAP_SYSReportTemplateFormat'

    TemplateData = Column(LargeBinary, nullable=False)
    TS = Column(TIMESTAMP, nullable=False)
    SubSysId = Column(Unicode(20), nullable=False, server_default=text("('')"))
    TemplateID = Column(Integer, primary_key=True, server_default=text("((0))"))
    UpdateID = Column(Integer, nullable=False, server_default=text("((0))"))


class EAPSYSReportTemplateFormulas(Base):
    __tablename__ = 'EAP_SYSReportTemplateFormulas'

    FormulaText = Column(UnicodeText(1073741823), nullable=False, server_default=text("('')"))
    Sheet = Column(Integer, nullable=False, server_default=text("((1))"))
    SheetName = Column(Unicode(50), nullable=False, server_default=text("('')"))
    SubSysId = Column(Unicode(20), nullable=False, server_default=text("('')"))
    TemplateID = Column(Integer, primary_key=True, server_default=text("((0))"))
    UpdateID = Column(Integer, nullable=False, server_default=text("((0))"))


class EAPSYSReportTemplateModel(Base):
    __tablename__ = 'EAP_SYSReportTemplateModel'

    TemplateStyle = Column(UnicodeText(1073741823), nullable=False, server_default=text("('')"))
    TS = Column(TIMESTAMP, nullable=False)
    Sheet = Column(Integer, nullable=False, server_default=text("((0))"))
    Rows = Column(Integer, nullable=False, server_default=text("((1))"))
    Cols = Column(Integer, nullable=False, server_default=text("((1))"))
    SheetName = Column(Unicode(50), nullable=False, server_default=text("('')"))
    SubSysId = Column(Unicode(20), nullable=False, server_default=text("('')"))
    TemplateID = Column(Integer, primary_key=True, server_default=text("((0))"))
    UpdateID = Column(Integer, nullable=False, server_default=text("((0))"))


class EAPSchemaDoc(Base):
    __tablename__ = 'EAP_SchemaDoc'

    id = Column(Integer, primary_key=True)
    flag = Column(Integer, nullable=False)
    name = Column(Unicode(200), nullable=False)
    moudle = Column(Unicode(200), nullable=False)
    content = Column(Unicode(1000), nullable=False)


class EAPSchemaDocB(Base):
    __tablename__ = 'EAP_SchemaDoc_b'

    id = Column(Integer, primary_key=True)
    name = Column(Unicode(200), nullable=False)
    defineType = Column(Unicode(200), nullable=False)
    content = Column(Unicode(1000), nullable=False)
    idSchemaDoc = Column(Integer, index=True)


class EAPSearchInfoExt(Base):
    __tablename__ = 'EAP_SearchInfo_Ext'

    Code = Column(Unicode(50), nullable=False)
    Name = Column(Unicode(50), nullable=False)
    Title = Column(Unicode(100), nullable=False)
    SearchType = Column(Integer, nullable=False)
    ID = Column(Integer, primary_key=True)
    ts = Column(TIMESTAMP, nullable=False)
    CreatedTime = Column(DateTime)
    EndGrade = Column(BIT)
    TFlag = Column(Integer, server_default=text("((0))"))


class EAPSearchItemCtrlInfoExt(Base):
    __tablename__ = 'EAP_SearchItemCtrlInfo_Ext'

    DtoName = Column(Unicode(50), nullable=False)
    RefPage = Column(Unicode(100), nullable=False)
    RefAddPage = Column(Unicode(50), nullable=False, server_default=text("('')"))
    RefWhere = Column(Unicode(300), nullable=False, server_default=text("('')"))
    EnumName = Column(Unicode(50))
    Status = Column(Integer, server_default=text("((1))"))
    ValueType = Column(Unicode(50), nullable=False, server_default=text("('Code')"))
    AllowEdit = Column(BIT, server_default=text("((1))"))
    DropDownStyle = Column(Unicode(50))
    DropDownPanelID = Column(Unicode(50))
    ControlType = Column(Unicode(50), server_default=text("('TextBox')"))
    DropDownWhere = Column(Unicode(300))
    RefDataSource = Column(Unicode(50))
    Precision = Column(Integer, server_default=text("((0))"))
    MaxLength = Column(Integer, server_default=text("((20))"))
    PropTitleCanChange = Column(BIT, server_default=text("((1))"))
    SelectButtonItems = Column(Unicode(1000))
    onClientClick = Column(Unicode(100))
    PrefixCheckCtrlStyle = Column(Integer, server_default=text("((0))"))
    RefShowField = Column(Unicode(200))
    ts = Column(TIMESTAMP, nullable=False)
    ExpressionName = Column(Unicode(60))
    CreatedTime = Column(DateTime)
    PrefixCheckCtrlStylename = Column(Unicode(100))
    ItemId = Column(Integer, nullable=False, index=True, server_default=text("((0))"))
    id = Column(Integer, primary_key=True)
    MultiSelect = Column(Integer)


class EAPSearchItemExt(Base):
    __tablename__ = 'EAP_SearchItem_Ext'

    FieldName = Column(Unicode(200), nullable=False, index=True)
    ColumnName = Column(Unicode(200), nullable=False, index=True, server_default=text("('')"))
    FieldTitle = Column(Unicode(200))
    FieldType = Column(Unicode(50), server_default=text("('Nvarchars')"))
    IsBetween = Column(BIT, server_default=text("((0))"))
    LinkSign = Column(Unicode(50), nullable=False, server_default=text("('and')"))
    CompareSign = Column(Unicode(500), server_default=text("('=')"))
    CanGroupSum = Column(BIT, server_default=text("((0))"))
    BeginDefault = Column(Unicode(400))
    EndDefault = Column(Unicode(400))
    OrderNum = Column(Integer, server_default=text("((0))"))
    FieldTitle2 = Column(Unicode(50))
    BeginDefaultText = Column(Unicode(100))
    EndDefaultText = Column(Unicode(100))
    CanFilterSearch = Column(BIT, server_default=text("((1))"))
    IsSystem = Column(BIT, nullable=False, server_default=text("((0))"))
    RepelGroup = Column(Unicode(50))
    WhereOrder = Column(Integer, server_default=text("((0))"))
    whereName = Column(Unicode(50))
    RepelItems = Column(Unicode(400))
    isNotNullValue = Column(BIT, server_default=text("((0))"))
    DependItems = Column(Unicode(400))
    DTOProp = Column(Unicode(300))
    RefDtoProp = Column(Unicode(400))
    id = Column(Integer, primary_key=True)
    ts = Column(TIMESTAMP, nullable=False)
    ExpressionName = Column(Unicode(60))
    CreatedTime = Column(DateTime)
    FormatString = Column(Unicode(50))
    SearchId = Column(Integer, nullable=False, index=True, server_default=text("((0))"))


class EAPSearchPlanInfoExt(Base):
    __tablename__ = 'EAP_SearchPlanInfo_Ext'
    __table_args__ = (
        Index('EAP_SearchPlanInfo_Ext_Index_UserID_SearchName', 'UserId', 'SearchName'),
    )

    SearchName = Column(Unicode(50), nullable=False)
    SearchStyle = Column(Integer, nullable=False)
    IsDefault = Column(BIT)
    IsSystem = Column(BIT)
    PlanName = Column(Unicode(50))
    MaxItemCount = Column(Integer)
    IsDirectSearch = Column(BIT)
    IsPublicPlan = Column(BIT)
    LayoutStyle = Column(Integer, server_default=text("((2))"))
    LayoutColumnCount = Column(Integer, server_default=text("((1))"))
    id = Column(Integer, primary_key=True)
    ts = Column(TIMESTAMP, nullable=False)
    IsShowExpression = Column(BIT)
    Expression = Column(Unicode(400))
    Isdisplay = Column(BIT)
    CreatedTime = Column(DateTime)
    EndGrade = Column(BIT)
    TFlag = Column(Integer, server_default=text("((0))"))
    NoDelete = Column(Unicode(50))
    ExpressionName = Column(Unicode(60))
    SearchId = Column(Integer, nullable=False, server_default=text("((0))"))
    UserId = Column(Integer)


class EAPSearchPlanItemGroupInfoExt(Base):
    __tablename__ = 'EAP_SearchPlanItemGroupInfo_Ext'

    IsMutiLevelGroup = Column(BIT, server_default=text("((0))"))
    ParentDataField = Column(Unicode(50))
    MutiGroupLevel = Column(Integer, server_default=text("((1))"))
    mutiGroupLevelOper = Column(Integer, server_default=text("((0))"))
    GroupTitle = Column(Unicode(100))
    RowGroup = Column(BIT, server_default=text("((0))"))
    ColumnGroup = Column(BIT, server_default=text("((0))"))
    CanRowGroup = Column(BIT, server_default=text("((0))"))
    CanColumnGroup = Column(BIT, server_default=text("((0))"))
    GroupOrderNum = Column(Integer, server_default=text("((0))"))
    IsGroup = Column(BIT, server_default=text("((0))"))
    IsSum = Column(BIT, server_default=text("((0))"))
    MaxGroupLevel = Column(Integer, server_default=text("((15))"))
    BeginGroupLevel = Column(Integer, server_default=text("((1))"))
    EndGroupLevel = Column(Integer, server_default=text("((1))"))
    IsHorizontalLayout = Column(BIT, server_default=text("((0))"))
    LastLevelIndetifyField = Column(Unicode(100))
    FieldName = Column(Unicode(200), index=True)
    IsSystem = Column(BIT, server_default=text("((0))"))
    IsStaticGroup = Column(BIT, server_default=text("((0))"))
    ColumnName = Column(Unicode(200))
    DTOProp = Column(Unicode(300))
    RefDtoProp = Column(Unicode(400))
    GrpFieldType = Column(Unicode(100), nullable=False, server_default=text("('string')"))
    DateFieldGrpStyle = Column(Unicode(100))
    IsFixed = Column(BIT, server_default=text("((0))"))
    ts = Column(TIMESTAMP, nullable=False)
    IsHeaderItem = Column(Integer)
    ExpressionName = Column(Unicode(60))
    CreatedTime = Column(DateTime)
    IsHorizontal = Column(BIT)
    ideap_reportsolution = Column(Integer)
    ItemId = Column(Integer)
    PlanId = Column(Integer, nullable=False, index=True, server_default=text("((0))"))
    id = Column(Integer, primary_key=True)


class EAPSearchPlanItemExt(Base):
    __tablename__ = 'EAP_SearchPlanItem_Ext'

    OrderNum = Column(Integer, server_default=text("((0))"))
    BeginValue = Column(Unicode)
    EndValue = Column(Unicode)
    BeginText = Column(Unicode)
    EndText = Column(Unicode)
    IsControlPermission = Column(BIT, server_default=text("((0))"))
    IsControlFieldPermission = Column(BIT, server_default=text("((0))"))
    Selected = Column(BIT, server_default=text("((0))"))
    ts = Column(TIMESTAMP, nullable=False)
    CompareSign = Column(Unicode(300))
    ExpressionName = Column(Unicode(60))
    CreatedTime = Column(DateTime)
    SearchItemId = Column(Integer, nullable=False, server_default=text("((0))"))
    planid = Column(Integer, nullable=False, index=True, server_default=text("((0))"))
    id = Column(Integer, primary_key=True)


class EAPSetupApp(Base):
    __tablename__ = 'EAP_SetupApp'

    ts = Column(TIMESTAMP, nullable=False)
    AppID = Column(Unicode(50))
    Version = Column(Unicode(64))
    id = Column(Integer, primary_key=True)
    SetupDateTime = Column(DateTime)


class EAPTemplate(Base):
    __tablename__ = 'EAP_Template'

    GroupName = Column(Unicode(20), nullable=False)
    voucherInfoName = Column(Unicode(50), nullable=False)
    Title = Column(Unicode(50), nullable=False)
    DisposalType = Column(Integer, nullable=False)
    IndexOrder = Column(Integer, nullable=False)
    IsExport = Column(BIT, nullable=False, server_default=text("((1))"))
    IsImport = Column(BIT, nullable=False, server_default=text("((1))"))
    IsSearch = Column(BIT, nullable=False, server_default=text("((0))"))
    IsSystem = Column(BIT, nullable=False, server_default=text("((0))"))
    Description = Column(Unicode(255))
    ExpressionName = Column(Unicode(60))
    id = Column(Integer, primary_key=True)
    voucherInfoID = Column(Integer, nullable=False, server_default=text("((0))"))


class EAPTemplateGroup(Base):
    __tablename__ = 'EAP_TemplateGroup'

    GroupName = Column(Unicode(200), nullable=False)
    GroupTitle = Column(Unicode(200), nullable=False)
    ShowIndex = Column(Integer, nullable=False)
    IsSystem = Column(BIT, nullable=False)
    CreatedDate = Column(DateTime)
    CreatedBy = Column(Unicode(50))
    Description = Column(Unicode(1000))
    TS = Column(TIMESTAMP, nullable=False)
    id = Column(Integer, primary_key=True)


class EAPUFMessage(Base):
    __tablename__ = 'EAP_UFMessage'

    To = Column(Unicode(36), nullable=False)
    From = Column(Unicode(36), nullable=False)
    CC = Column(Unicode(36))
    Bcc = Column(Unicode(36))
    Subject = Column(Unicode(1000))
    Body = Column(UnicodeText(1073741823), nullable=False)
    IsBodyHtml = Column(BIT, server_default=text("((0))"))
    SendedDateTime = Column(DateTime, index=True)
    Priority = Column(Integer, server_default=text("((0))"))
    Type = Column(Integer, nullable=False)
    Category = Column(Unicode(50))
    Tag = Column(Unicode(200))
    AdditionalInfo = Column(Unicode(1000))
    id = Column(Integer, primary_key=True)
    DsName = Column(Unicode(100))
    IsNeedReplay = Column(BIT, server_default=text("((0))"))


class EAPUser(Base):
    __tablename__ = 'EAP_User'

    Code = Column(Unicode(50), index=True)
    name = Column(Unicode(50))
    email = Column(Unicode(200))
    IsUsed = Column(BIT, server_default=text("(0)"))
    password = Column(Unicode(50))
    isAdmin = Column(BIT, server_default=text("(0)"))
    isStoped = Column(BIT, server_default=text("(0)"))
    mobile = Column(Unicode(20))
    AuthState = Column(Integer, server_default=text("(0)"))
    PersonName = Column(Unicode(50))
    ts = Column(TIMESTAMP)
    Memo = Column(Unicode(50))
    issystem = Column(BIT)
    ShowNewFuncIntro = Column(Integer, nullable=False, server_default=text("((1))"))
    OrderNum = Column(Integer)
    id = Column(Integer, primary_key=True)
    IdMarketingOrgan = Column(Integer)
    IdPerson = Column(Integer)
    ActorType = Column(Integer, server_default=text("((0))"))
    IsHeadQuarters = Column(BIT)
    ExpressionName = Column(Unicode(200))
    CloudUserId = Column(Unicode(128))
    UpgradePwdState = Column(Integer, server_default=text("((0))"))
    lastLoginDate = Column(DateTime)
    createdDate = Column(DateTime)


class EAPUserGroupRelation(Base):
    __tablename__ = 'EAP_UserGroupRelation'

    ts = Column(TIMESTAMP, nullable=False)
    groupid = Column(Integer)
    UserId = Column(Integer)
    id = Column(Integer, primary_key=True)


class EAPVoucherDraft(Base):
    __tablename__ = 'EAP_VoucherDraft'

    ts = Column(TIMESTAMP, nullable=False)
    name = Column(Unicode(200), nullable=False)
    Json = Column(UnicodeText(1073741823), nullable=False)
    IsHandMade = Column(Integer, nullable=False)
    Code = Column(Unicode(200))
    VoucherName = Column(Unicode(200))
    DraftType = Column(Integer)
    UserId = Column(Integer)
    id = Column(Integer, primary_key=True)
    CreatedTime = Column(DateTime)


class EapAuxiliaryAccounting(Base):
    __tablename__ = 'Eap_AuxiliaryAccounting'

    Name = Column(Unicode(50))
    Title = Column(Unicode(200))
    DTOName = Column(Unicode(50))
    isApply = Column(BIT, nullable=False)
    AAType = Column(Integer)
    isSystem = Column(BIT, nullable=False, server_default=text("((0))"))
    Description = Column(Unicode(200))
    IndexOrder = Column(Integer)
    ts = Column(TIMESTAMP)
    Visible = Column(BIT, nullable=False, server_default=text("((1))"))
    ExpressionName = Column(Unicode(100))
    id = Column(Integer, primary_key=True)
    DTOID = Column(Integer, nullable=False, server_default=text("((0))"))
    CompareSign = Column(Unicode(1000))


class EapCloudUserApp(Base):
    __tablename__ = 'Eap_CloudUserApp'
    __table_args__ = (
        Index('IDX_Eap_CloudUserApp_AppID_UserID', 'AppID', 'UserID'),
    )

    Id = Column(Integer, primary_key=True)
    UserID = Column(Integer)
    BindState = Column(Integer)
    AppID = Column(Integer)
    UserType = Column(Integer)
    AppUserID = Column(Unicode(200))
    AppUserName = Column(Unicode(200))
    EncryToken = Column(Unicode(500))
    ts = Column(TIMESTAMP, nullable=False)
    Updated = Column(DateTime)
    UpdatedBy = Column(Unicode(32))


class EapColumnSet(Base):
    __tablename__ = 'Eap_ColumnSet'
    __table_args__ = (
        Index('IDX_EAP_ColumnSet_SolutionIDField', 'SolutionID', 'Field'),
    )

    Field = Column(Unicode(200), index=True)
    QryField = Column(Unicode(50))
    ColPos = Column(Integer)
    Caption = Column(Unicode(100))
    Fixed = Column(BIT)
    Display = Column(BIT)
    Width = Column(Integer)
    Align = Column(Integer)
    OrderMode = Column(Unicode(30))
    MustSelect = Column(BIT)
    NeedSum = Column(BIT)
    IsSystem = Column(BIT, nullable=False, server_default=text("(0)"))
    DecimalDigits = Column(SmallInteger, server_default=text("(2)"))
    NeedReSetBooleanTxt = Column(BIT, nullable=False, server_default=text("(0)"))
    BooleanTxt = Column(Unicode(30), nullable=False, server_default=text("('是|否')"))
    Precision = Column(Integer)
    FieldExpression = Column(Unicode(1000))
    ColumnFormatString = Column(Unicode(50))
    NegativeFormatMode = Column(Integer)
    DTOProp = Column(Unicode(200))
    RefDtoProp = Column(Unicode(200))
    PropTitleCanChange = Column(BIT, nullable=False, server_default=text("(1)"))
    IsAsSearchCategoryField = Column(BIT, nullable=False, server_default=text("(1)"))
    FieldType = Column(Unicode(30), nullable=False, server_default=text("('string')"))
    IsDevField = Column(BIT, nullable=False, server_default=text("(0)"))
    IsMergeColumn = Column(BIT)
    DisplayOld = Column(BIT)
    id = Column(Integer, primary_key=True)
    ExpressionName = Column(Unicode(60))
    ts = Column(TIMESTAMP, nullable=False)
    IsShowTotal = Column(BIT)
    IsTotal = Column(BIT)
    CreatedTime = Column(DateTime)
    idparent = Column(Integer)
    SolutionID = Column(Integer, index=True)
    NegativeShowFormat = Column(Integer)


class EapColumnSetSolutionUser(Base):
    __tablename__ = 'Eap_ColumnSetSolution_User'

    Name = Column(Unicode(50), index=True)
    ClassFullName = Column(Unicode(80))
    Title = Column(Unicode(100))
    UserId = Column(Unicode(100), nullable=False)
    IsShowDetail = Column(BIT)
    IsFirstShowDetail = Column(BIT)
    Width = Column(Integer)
    IsDefault = Column(Integer, server_default=text("((0))"))
    DtoName = Column(Unicode(100))
    IsTotal = Column(BIT)
    SolutionID = Column(Integer, nullable=False, server_default=text("((0))"))
    id = Column(Integer, primary_key=True)


class EapColumnSetUser(Base):
    __tablename__ = 'Eap_ColumnSet_User'
    __table_args__ = (
        Index('IDX_EAP_ColumnSetUser_SolutionIDField', 'SolutionID', 'Field'),
    )

    UserId = Column(Unicode(100), nullable=False)
    Field = Column(Unicode(200), index=True)
    QryField = Column(Unicode(50))
    ColPos = Column(Integer)
    Caption = Column(Unicode(100))
    Fixed = Column(BIT)
    Display = Column(BIT)
    Width = Column(Integer)
    Align = Column(Integer)
    OrderMode = Column(Unicode(30))
    MustSelect = Column(BIT)
    NeedSum = Column(BIT)
    IsSystem = Column(BIT, nullable=False, server_default=text("(0)"))
    DecimalDigits = Column(SmallInteger, server_default=text("(2)"))
    NeedReSetBooleanTxt = Column(BIT, nullable=False, server_default=text("(0)"))
    BooleanTxt = Column(Unicode(30), nullable=False, server_default=text("('是|否')"))
    Precision = Column(Integer)
    FieldExpression = Column(Unicode(1000))
    DTOProp = Column(Unicode(200))
    RefDtoProp = Column(Unicode(200))
    PropTitleCanChange = Column(BIT, nullable=False, server_default=text("(1)"))
    IsMergeColumn = Column(BIT)
    DisplayOld = Column(BIT)
    ExpressionName = Column(Unicode(60))
    IsShowTotal = Column(BIT)
    IsTotal = Column(BIT)
    Ts = Column(TIMESTAMP, nullable=False)
    id = Column(Integer, primary_key=True)
    idparent = Column(Integer)
    SolutionID = Column(Integer, nullable=False, index=True, server_default=text("((0))"))


class EapFreeItems(Base):
    __tablename__ = 'Eap_FreeItems'

    Name = Column(Unicode(50), nullable=False)
    Title = Column(Unicode(50), nullable=False)
    beUsed = Column(BIT, nullable=False)
    FieldType = Column(Unicode(50), nullable=False)
    EnumName = Column(Unicode(50), nullable=False)
    RefObject = Column(Unicode(50), nullable=False)
    ValueFrom = Column(Unicode(50), nullable=False)
    ValueConcrete = Column(Unicode(50), nullable=False)
    MaxLength = Column(Integer, nullable=False)
    AllowNull = Column(BIT, nullable=False)
    AllowEdit = Column(BIT, nullable=False)
    DefaultValue = Column(Unicode(50), nullable=False)
    Width = Column(Integer, nullable=False)
    Visible = Column(BIT, nullable=False)
    Vouchers = Column(Unicode(800), nullable=False)
    Apply = Column(BIT, nullable=False)
    AutoAdd = Column(BIT, nullable=False, server_default=text("((1))"))
    ID = Column(Integer, primary_key=True)


class EapGridParams(Base):
    __tablename__ = 'Eap_GridParams'

    UserID = Column(Unicode(200))
    DtoName = Column(Unicode(50))
    PageSize = Column(Integer)
    ID = Column(Integer, primary_key=True)


t_Eap_MenuDefaultOption = Table(
    'Eap_MenuDefaultOption', metadata,
    Column('Code', Unicode(50), nullable=False),
    Column('OrderIndex', Integer, nullable=False),
    Column('isSystem', BIT, nullable=False, server_default=text("((0))"))
)


class EapMenuIndividuation(Base):
    __tablename__ = 'Eap_MenuIndividuation'

    UserID = Column(Unicode(100), nullable=False)
    Code = Column(Unicode(50), nullable=False)
    OrderIndex = Column(Integer, nullable=False)
    isSystem = Column(BIT, nullable=False, server_default=text("((0))"))
    ID = Column(Integer, primary_key=True)


class EapMenuTree(Base):
    __tablename__ = 'Eap_MenuTree'

    Title = Column(Unicode(50), nullable=False)
    ShowIndex = Column(Integer)
    isSystem = Column(BIT)
    inId = Column(Unicode(1120))
    Category = Column(Integer)
    TFlag = Column(Integer, server_default=text("((0))"))
    IsEndNode = Column(Integer)
    id = Column(Integer, primary_key=True)
    parentID = Column(Integer)
    ExpressionName = Column(Unicode(200))


class EapMenuTreeRelation(Base):
    __tablename__ = 'Eap_MenuTreeRelation'

    MenuCode = Column(Unicode(50), nullable=False)
    Name = Column(Unicode(100))
    isSystem = Column(BIT, server_default=text("((0))"))
    showIndex = Column(Integer)
    Category = Column(Integer)
    IsControlShowNum = Column(Integer)
    ControlNum = Column(Integer)
    ControlPage = Column(Unicode(200))
    ControlJS = Column(Unicode(200))
    ExpressionName = Column(Unicode(60))
    TFlag = Column(Integer, server_default=text("((0))"))
    id = Column(Integer, primary_key=True)
    TreeID = Column(Integer)


class EapMenuUserEverUsed(Base):
    __tablename__ = 'Eap_MenuUserEverUsed'

    UserID = Column(Unicode(100), nullable=False)
    ID = Column(Integer, primary_key=True)


class EapOperationLog(Base):
    __tablename__ = 'Eap_OperationLog'

    OperateType = Column(Integer, nullable=False)
    AccountID = Column(Unicode(50), nullable=False)
    AccountName = Column(Unicode(50))
    Operate = Column(Unicode(50))
    UserID = Column(Unicode(100), nullable=False)
    UserName = Column(Unicode(100))
    MachineName = Column(Unicode(50))
    Time = Column(DateTime, nullable=False)
    DocNo = Column(Unicode(50), nullable=False)
    Description = Column(UnicodeText(1073741823))
    Status = Column(Integer, nullable=False)
    ModuleCode = Column(Unicode(50))
    FunctionCode = Column(Unicode(50))
    FunctionName = Column(Unicode(50))
    ProductName = Column(Unicode(50))
    ID = Column(BigInteger, primary_key=True)
    FunctionDate = Column(DateTime)


class EapOperationLogBakPara(Base):
    __tablename__ = 'Eap_OperationLogBakPara'

    ClearMode = Column(Unicode(50), nullable=False)
    BakPath = Column(Unicode(300), nullable=False)
    KeepDays = Column(Integer, nullable=False)
    ID = Column(Integer, primary_key=True)


class EapOperationLogFileName(Base):
    __tablename__ = 'Eap_OperationLogFileName'

    AccountID = Column(Unicode(50), nullable=False)
    LogFileName = Column(Unicode(100))
    ID = Column(Integer, primary_key=True)


class EapPrintCountSet(Base):
    __tablename__ = 'Eap_PrintCountSet'

    isControl = Column(BIT, nullable=False, server_default=text("((0))"))
    maxPrintNum = Column(Integer)
    password = Column(Unicode(50))
    isSystem = Column(BIT, nullable=False, server_default=text("((0))"))
    description = Column(Unicode(50))
    OrderIndex = Column(Integer)
    ID = Column(Integer, primary_key=True)
    PrintOccasion = Column(Integer, nullable=False, server_default=text("((0))"))
    voucherInfoID = Column(Integer, nullable=False, server_default=text("((0))"))
    ExpressionName = Column(Unicode(200))


t_Eap_PrintDataColumn = Table(
    'Eap_PrintDataColumn', metadata,
    Column('ts', TIMESTAMP, nullable=False),
    Column('name', Unicode(200), nullable=False),
    Column('Title', Unicode(4000)),
    Column('DataType', Unicode(30)),
    Column('DynPropertyString', Unicode(1000)),
    Column('PosLeft', Integer),
    Column('id', Integer, nullable=False),
    Column('IdPrintDataTable', Integer)
)


t_Eap_PrintDataField = Table(
    'Eap_PrintDataField', metadata,
    Column('ts', TIMESTAMP, nullable=False),
    Column('name', Unicode(200), nullable=False),
    Column('Title', Unicode(200)),
    Column('DataType', Unicode(30)),
    Column('DynPropertyString', Unicode(1000)),
    Column('PosTop', Integer),
    Column('PosLeft', Integer),
    Column('PosTitleTop', Integer),
    Column('PosTitleLeft', Integer),
    Column('id', Integer, nullable=False),
    Column('SourceType', Integer),
    Column('IdPrintTemplate', Integer),
    Column('updated', DateTime)
)


t_Eap_PrintDataTable = Table(
    'Eap_PrintDataTable', metadata,
    Column('ts', TIMESTAMP, nullable=False),
    Column('name', Unicode(200), nullable=False),
    Column('DetailType', Unicode(30)),
    Column('ParentDetail', Unicode(200)),
    Column('FixRows', Integer),
    Column('PrintPageTotal', Integer),
    Column('FillBlankRows', Integer),
    Column('RowsAdaptive', Integer),
    Column('PrintTotal', Integer),
    Column('PrintPageSubTotal', Integer),
    Column('DynPropertyString', Unicode(1000)),
    Column('PosTop', Integer),
    Column('PosBottom', Integer),
    Column('id', Integer, nullable=False),
    Column('IdPrintTemplate', Integer)
)


class EapPrintDesignField(Base):
    __tablename__ = 'Eap_PrintDesignField'

    ts = Column(TIMESTAMP, nullable=False)
    name = Column(Unicode(200), nullable=False)
    IsDetailField = Column(Integer)
    DetailName = Column(Unicode(100))
    SourceFieldAttr = Column(Unicode(100))
    SourceFieldName = Column(Unicode(100))
    SourceFieldTtitle = Column(Unicode(100))
    SourceFieldType = Column(Unicode(30))
    WhereSql = Column(Unicode(1000))
    Visible = Column(Integer)
    DynPropertyString = Column(Unicode(1000))
    id = Column(Integer, primary_key=True)
    IdPrintDir = Column(Integer)


class EapPrintOption(Base):
    __tablename__ = 'Eap_PrintOption'

    ts = Column(TIMESTAMP, nullable=False)
    name = Column(Unicode(200), nullable=False)
    AddBlankPage = Column(Integer)
    DefaultTemplateName = Column(Unicode(200))
    PrePageSum = Column(Integer)
    CurPageSum = Column(Integer)
    PrintLeftPage = Column(Integer, server_default=text("((1))"))
    PrintPageSubTotal = Column(Integer)
    FixRows = Column(Integer)
    PrintRightPage = Column(Integer, server_default=text("((1))"))
    RowsAdaptive = Column(Integer)
    PrintPageTotal = Column(Integer)
    FillBlankRows = Column(Integer)
    DynPropertyString = Column(Unicode(1000))
    PrintCurrTwoFilter = Column(Integer)
    id = Column(Integer, primary_key=True)
    PageGroupSet = Column(Integer)
    PrintType = Column(Integer)


class EapPrintSetting(Base):
    __tablename__ = 'Eap_PrintSetting'

    ts = Column(TIMESTAMP, nullable=False)
    name = Column(Unicode(200), nullable=False)
    PrintAllPage = Column(Integer)
    PrintPageRange = Column(Unicode(200))
    PageCopies = Column(Integer)
    PageVouchers = Column(Integer)
    PrintSeparator = Column(Integer)
    CopiesSpacing = Column(Integer)
    Collated = Column(Integer)
    DynPropertyString = Column(Unicode(1000))
    id = Column(Integer, primary_key=True)


class EapRefSet(Base):
    __tablename__ = 'Eap_RefSet'

    DataSourceKey = Column(Unicode(50), nullable=False)
    DataSourceName = Column(Unicode(100))
    SolutionName = Column(Unicode(50))
    CategoryData = Column(Unicode(30))
    CategoryTree = Column(Unicode(30))
    RelationCodeField = Column(Unicode(200))
    TreeLevelIdField = Column(Unicode(30))
    TreeLevelNameField = Column(Unicode(30))
    TreeLevelGradeField = Column(Unicode(30))
    TreeTitle = Column(Unicode(100))
    TreeDisplayMode = Column(Unicode(30))
    DisplayType = Column(Integer, nullable=False)
    ClassType = Column(Integer)
    BaseArchiveUrl = Column(Unicode(200))
    TreeOneOrderByClause = Column(Unicode(200))
    TreeTwoOrderByClause = Column(Unicode(100))
    ID = Column(Integer, primary_key=True)
    RightColumnDisplayStyle = Column(Integer)
    columnset = Column(Integer)
    FirstMatchOrder = Column(Integer)
    QueryWhereSet = Column(Integer)
    QuerySolutionName = Column(Unicode(100))
    IsFieldAuth = Column(Integer)
    IsDataAuth = Column(Integer)
    ReturnFieldNames = Column(Unicode(3998))
    TFlag = Column(Integer, server_default=text("((0))"))
    ts = Column(TIMESTAMP, nullable=False)
    CreatedTime = Column(DateTime)


class EapRefSetExtControls(Base):
    __tablename__ = 'Eap_RefSet_ExtControls'

    id = Column(Integer, primary_key=True)
    RefDTOName = Column(Unicode(100), nullable=False)
    RefType = Column(Integer)
    AllowRecord = Column(Integer)
    RecordRule = Column(Unicode(100), nullable=False)
    RecordRuleValue = Column(Unicode(400), nullable=False)
    RecordValue = Column(Unicode(1000))
    DefaultValue = Column(Unicode(1000), nullable=False)
    IsSystem = Column(Integer, server_default=text("((0))"))
    Visible = Column(Integer)
    FieldName = Column(Unicode(400), nullable=False)
    Condition = Column(Unicode(400), nullable=False)
    LabelID = Column(Unicode(100))
    LabelTitle = Column(Unicode(100), nullable=False)
    ControlID = Column(Unicode(100))
    ControlType = Column(Unicode(50), nullable=False)
    ts = Column(TIMESTAMP)


class EapReportCarriedItem(Base):
    __tablename__ = 'Eap_ReportCarriedItem'

    ReportName = Column(Unicode(100), nullable=False)
    ItemType = Column(Integer, nullable=False)
    ItemKey = Column(Unicode(100))
    Position = Column(Integer, nullable=False, server_default=text("((0))"))
    IsSystem = Column(BIT, nullable=False, server_default=text("((0))"))
    MustDisplay = Column(BIT, nullable=False, server_default=text("((0))"))
    Display = Column(BIT, server_default=text("((1))"))
    DisplayName = Column(Unicode(200))
    DisplayValue = Column(Unicode(200))
    ShowIndex = Column(Integer, server_default=text("((1))"))
    ColumnName = Column(Unicode(200))
    id = Column(Integer, primary_key=True)
    ts = Column(TIMESTAMP, nullable=False)
    ExpressionName = Column(Unicode(60))
    FilterItemID = Column(Integer)
    ideap_reportsolution = Column(Integer)
    Width = Column(Integer, server_default=text("((250))"))
    CreatedTime = Column(DateTime)


class EapReportCommonData(Base):
    __tablename__ = 'Eap_ReportCommonData'

    ReportName = Column(Unicode(100), nullable=False)
    DisplayStyle = Column(Integer, nullable=False, server_default=text("((0))"))
    IsShowFontPage = Column(BIT, nullable=False, server_default=text("((1))"))
    IsShowOtherPage = Column(BIT, nullable=False, server_default=text("((1))"))
    ShowPageHeaderPage = Column(BIT, nullable=False, server_default=text("((1))"))
    ShowPageFooterPage = Column(BIT, nullable=False, server_default=text("((1))"))
    columnConfigFlag = Column(Unicode(100), nullable=False, server_default=text("('')"))
    ItemID = Column(Integer, primary_key=True)


class EapReportFilterItem(Base):
    __tablename__ = 'Eap_ReportFilterItem'

    FieldName = Column(Unicode(200))
    ColumnID = Column(Unicode(200))
    ColumnName = Column(Unicode(200))
    id = Column(Integer, primary_key=True)
    SearchName = Column(Unicode(200), nullable=False, server_default=text("('')"))
    ItemType = Column(Integer, nullable=False, server_default=text("((1))"))
    IsSystem = Column(BIT, nullable=False, server_default=text("((0))"))
    MustDisplay = Column(BIT, nullable=False, server_default=text("((1))"))
    Display = Column(BIT)
    DisplayName = Column(Unicode(200))
    ShowIndex = Column(Integer)
    ExpressionName = Column(Unicode(60))
    ts = Column(TIMESTAMP, nullable=False)
    CreatedTime = Column(DateTime)
    ideap_reportsolution = Column(Integer)
    Width = Column(Integer, server_default=text("((250))"))


class EapReportMatrixItem(Base):
    __tablename__ = 'Eap_ReportMatrixItem'

    SearchName = Column(Unicode(200), nullable=False)
    IsSystem = Column(BIT, nullable=False, server_default=text("((0))"))
    MustDisplay = Column(BIT, nullable=False, server_default=text("((0))"))
    Display = Column(BIT, server_default=text("((1))"))
    DisplayName = Column(Unicode(200))
    ShowIndex = Column(Integer, server_default=text("((1))"))
    FieldName = Column(Unicode(200))
    ItemType = Column(Integer, nullable=False, server_default=text("((1))"))
    id = Column(Integer, primary_key=True)
    ts = Column(TIMESTAMP, nullable=False)
    ExpressionName = Column(Unicode(60))
    DTOProp = Column(Unicode(200))
    RefDTOProp = Column(Unicode(400))
    CreatedTime = Column(DateTime)
    ideap_reportsolution = Column(Integer)


class EapReportPageSet(Base):
    __tablename__ = 'Eap_ReportPageSet'

    ts = Column(TIMESTAMP, nullable=False)
    DataItems = Column(Unicode(200))
    SectionType = Column(Integer)
    OtherInfos = Column(Unicode(1020))
    Styles = Column(Unicode(200))
    CreatedTime = Column(DateTime)
    id = Column(Integer, primary_key=True)
    ideap_reportsolution = Column(Integer)


class EapReportUserCarriedItem(Base):
    __tablename__ = 'Eap_ReportUserCarriedItem'

    Display = Column(BIT, nullable=False, server_default=text("((1))"))
    DisplayName = Column(Unicode(200))
    DisplayValue = Column(Unicode(200))
    ShowIndex = Column(Integer, server_default=text("((1))"))
    NameAlign = Column(Integer, server_default=text("((2))"))
    ValueAlign = Column(Integer, server_default=text("((0))"))
    id = Column(Integer, primary_key=True)
    ts = Column(TIMESTAMP, nullable=False)
    CarriedItemID = Column(Integer, nullable=False, server_default=text("((0))"))
    SolutionID = Column(Integer, nullable=False, server_default=text("((0))"))
    Width = Column(Integer, server_default=text("((250))"))
    CreatedTime = Column(DateTime)


class EapReportUserFilterItem(Base):
    __tablename__ = 'Eap_ReportUserFilterItem'

    Display = Column(BIT, nullable=False, server_default=text("((1))"))
    DisplayName = Column(Unicode(200))
    ShowIndex = Column(Integer, nullable=False, server_default=text("((1))"))
    ItemType = Column(Integer, nullable=False, server_default=text("((1))"))
    id = Column(Integer, primary_key=True)
    ts = Column(TIMESTAMP, nullable=False)
    FilterItemID = Column(Integer, nullable=False, server_default=text("((0))"))
    PlanID = Column(Integer, nullable=False, server_default=text("((0))"))
    Width = Column(Integer, server_default=text("((250))"))


class EapUserDefineArticleColumn(Base):
    __tablename__ = 'Eap_UserDefineArticleColumn'

    ts = Column(TIMESTAMP, nullable=False)
    name = Column(Unicode(50), nullable=False)
    Title = Column(Unicode(100), nullable=False)
    FieldType = Column(Unicode(200), nullable=False)
    Length = Column(Integer)
    ColPrecision = Column(Integer)
    FormatString = Column(Unicode(100))
    IsNotNull = Column(Integer)
    IsAllowEdit = Column(Integer)
    IsDisplayInData = Column(Integer)
    IsDisplayInSet = Column(Integer)
    IsDefault = Column(Integer)
    IsSystem = Column(Integer)
    IsDisabled = Column(Integer)
    IsPrimaryKey = Column(Integer)
    DefaultValue = Column(Unicode(200))
    RefDTOName = Column(Unicode(50))
    RefDTOProperty = Column(Unicode(50))
    EnumName = Column(Unicode(50))
    RefTitle = Column(Unicode(100))
    RePage = Column(Unicode(100))
    ColPos = Column(Integer)
    ValueFrom = Column(Unicode(50))
    ControlType = Column(Unicode(50))
    id = Column(Integer, primary_key=True)
    FieldName = Column(Unicode(100))
    RefWhere = Column(Unicode(500))
    ExpressionName = Column(Unicode(60))
    idEnum = Column(Integer)
    ArticleDictId = Column(Integer, nullable=False, server_default=text("((0))"))
    MadeDate = Column(DateTime)
    ModifiedDate = Column(DateTime)


class EapUserDefineItemRefSet(Base):
    __tablename__ = 'Eap_UserDefineItemRefSet'

    Title = Column(Unicode(100))
    AADtoName = Column(Unicode(100))
    Visible = Column(Integer, nullable=False, server_default=text("((1))"))
    OrderIndex = Column(Integer, nullable=False)
    ExpressionName = Column(Unicode(60))
    EditTableID = Column(Integer)
    id = Column(Integer, primary_key=True)
    VoucherID = Column(Integer)


class EapUserDefineItems(Base):
    __tablename__ = 'Eap_UserDefineItems'

    FieldName = Column(Unicode(50), nullable=False, server_default=text("('')"))
    Type = Column(Integer, nullable=False, server_default=text("(1)"))
    Title = Column(Unicode(50), nullable=False, server_default=text("('')"))
    Expression = Column(Unicode(100), nullable=False, server_default=text("('')"))
    EnumName = Column(Unicode(50), nullable=False, server_default=text("('')"))
    MaxLength = Column(Integer, nullable=False, server_default=text("(50)"))
    RefDTOName = Column(Unicode(50), nullable=False, server_default=text("('')"))
    FieldType = Column(Unicode(50), nullable=False, server_default=text("('String')"))
    RefLinkField = Column(Unicode(50), nullable=False, server_default=text("('')"))
    AllowNone = Column(BIT, nullable=False, server_default=text("(1)"))
    EditReadOnly = Column(BIT, nullable=False, server_default=text("(1)"))
    Visible = Column(BIT, nullable=False, server_default=text("(1)"))
    beUsed = Column(BIT, nullable=False, server_default=text("(0)"))
    UserPrompt = Column(Unicode(100), nullable=False, server_default=text("('')"))
    VoucherIDs = Column(Unicode(2000), nullable=False, server_default=text("('')"))
    VoucherNames = Column(Unicode(2000), nullable=False, server_default=text("('')"))
    OrderNum = Column(Integer, nullable=False)
    Precision = Column(SmallInteger)
    ID = Column(Integer, primary_key=True)


class EapViewModule(Base):
    __tablename__ = 'Eap_ViewModule'

    ViewURL = Column(Unicode(255))
    ViewController = Column(Unicode(50))
    Ts = Column(TIMESTAMP, nullable=False)
    Code = Column(Unicode(50), nullable=False)
    Name = Column(Unicode(50), nullable=False)
    TFlag = Column(Integer, server_default=text("((0))"))
    ID = Column(Integer, primary_key=True)
    CreatedTime = Column(DateTime)


class EapViewParameter(Base):
    __tablename__ = 'Eap_ViewParameter'

    id = Column(Integer, primary_key=True)
    Code = Column(Unicode(200))
    Name = Column(Unicode(200), nullable=False)
    IsNeed = Column(Integer, nullable=False, server_default=text("((0))"))
    Memo = Column(Unicode(200))
    ParameterCode = Column(Integer, nullable=False, server_default=text("((0))"))
    ParentID = Column(Integer)
    CreatedTime = Column(DateTime)
    Ts = Column(TIMESTAMP, nullable=False)


class EapViewSet(Base):
    __tablename__ = 'Eap_ViewSet'

    Name = Column(Unicode(200), nullable=False)
    Title = Column(Unicode(200), nullable=False)
    ViewURL = Column(Unicode(200))
    ViewController = Column(Unicode(200))
    Ts = Column(TIMESTAMP, nullable=False)
    TFlag = Column(Integer, server_default=text("((0))"))
    ID = Column(Integer, primary_key=True)
    SubsystemCode = Column(Integer)
    IDMenu = Column(Integer)
    IDDTOPackage = Column(Integer)
    IDViewModule = Column(Integer, nullable=False, server_default=text("((0))"))
    RFlag = Column(Integer, server_default=text("((0))"))
    MenuCode = Column(Unicode(50))
    CreatedTime = Column(DateTime)


class EapViewSetItem(Base):
    __tablename__ = 'Eap_ViewSetItem'

    Name = Column(Unicode(200))
    ParameterValue = Column(Unicode(200), nullable=False)
    Memo = Column(Unicode(200))
    Ts = Column(TIMESTAMP, nullable=False)
    ID = Column(Integer, primary_key=True)
    ParameterCode = Column(Integer, nullable=False, server_default=text("((0))"))
    IDViewSet = Column(Integer, nullable=False, server_default=text("((0))"))
    RFlag = Column(Integer, server_default=text("((0))"))
    CreatedTime = Column(DateTime)


class EapWorkPlanFormSettingSolution(Base):
    __tablename__ = 'Eap_WorkPlanFormSettingSolution'

    Name = Column(Unicode(100), nullable=False)
    Title = Column(Unicode(100))
    DefaultCardIndex = Column(Integer)
    ID = Column(Integer, primary_key=True)


class EapWorkPlanFormDefault(Base):
    __tablename__ = 'Eap_WorkPlanForm_Default'

    Code = Column(Unicode(50), nullable=False)
    OrderIndex = Column(Integer, nullable=False)
    Type = Column(Unicode(50), nullable=False)
    SolutionName = Column(Unicode(100), nullable=False)
    MustSelect = Column(BIT)
    Visible = Column(BIT, nullable=False)
    isSystem = Column(BIT, nullable=False, server_default=text("((0))"))
    ID = Column(Integer, primary_key=True)
    ExpressionName = Column(Unicode(200))


class EapWorkPlanFormUser(Base):
    __tablename__ = 'Eap_WorkPlanForm_User'

    Code = Column(Unicode(50), nullable=False)
    OrderIndex = Column(Integer, nullable=False)
    Type = Column(Unicode(50), nullable=False)
    SolutionName = Column(Unicode(100), nullable=False)
    MustSelect = Column(BIT)
    Visible = Column(BIT, nullable=False)
    UserID = Column(Unicode(100), nullable=False)
    isSystem = Column(BIT, nullable=False, server_default=text("((0))"))
    ID = Column(Integer, primary_key=True)


class EapHistory(Base):
    __tablename__ = 'Eap_history'

    Name = Column(Unicode(50), nullable=False)
    URL = Column(Unicode(1000))
    Code = Column(Unicode(100))
    RecordTime = Column(DateTime, nullable=False)
    historyID = Column(Integer, primary_key=True, unique=True)
    UserID = Column(Integer, nullable=False, server_default=text("((0))"))


class EapSyncfileinfo(Base):
    __tablename__ = 'Eap_syncfileinfo'

    posmaxts = Column(String(16, u'Chinese_PRC_CI_AS'), nullable=False)
    maxts = Column(String(16, u'Chinese_PRC_CI_AS'))
    posOtherMaxts = Column(String(16, u'Chinese_PRC_CI_AS'))
    maxOtherts = Column(String(16, u'Chinese_PRC_CI_AS'))
    filepath = Column(Unicode(200), nullable=False)
    reqpos = Column(Unicode(400))
    datatype = Column(Integer, nullable=False)
    ts = Column(TIMESTAMP, nullable=False)
    filename = Column(Unicode(200), nullable=False)
    accnum = Column(Unicode(20))
    BapType = Column(Unicode(50), nullable=False, server_default=text("((5))"))
    id = Column(Integer, primary_key=True)
    makedate = Column(DateTime)


t_GLAuxDetailReturnTempTable13671904217 = Table(
    'GLAuxDetailReturnTempTable13671904217', metadata,
    Column('eap_reportrowtype', Integer, nullable=False),
    Column('accountID', UNIQUEIDENTIFIER),
    Column('accountCode', Unicode(40)),
    Column('accountName', Unicode(50)),
    Column('accountDcdirection', UNIQUEIDENTIFIER),
    Column('AuxAccCustomerName', Unicode(200)),
    Column('AuxAccCustomerID', UNIQUEIDENTIFIER),
    Column('AuxAccCustomerCode', Unicode(40)),
    Column('madeDate', String(19, u'Chinese_PRC_CI_AS')),
    Column('period', String(34, u'Chinese_PRC_CI_AS')),
    Column('docwordCode', Unicode(34)),
    Column('docTypeNo', Unicode(34)),
    Column('docID', UNIQUEIDENTIFIER),
    Column('docNo', Unicode(34)),
    Column('entryNo', Unicode(34)),
    Column('summary', Unicode(4000), nullable=False),
    Column('currencyID', UNIQUEIDENTIFIER),
    Column('currencyCode', Unicode(32)),
    Column('currencyName', Unicode(200)),
    Column('calDirection', UNIQUEIDENTIFIER),
    Column('exchangeRate', Numeric(38, 14)),
    Column('price', Numeric(38, 14)),
    Column('quantityDr', Numeric(38, 14)),
    Column('origAmountDr', Numeric(38, 14)),
    Column('amountDr', Numeric(38, 14)),
    Column('priceDr', Numeric(28, 14)),
    Column('quantityCr', Numeric(38, 14)),
    Column('origAmountCr', Numeric(38, 14)),
    Column('amountCr', Numeric(38, 14)),
    Column('priceCr', Numeric(28, 14)),
    Column('dCDirection', UNIQUEIDENTIFIER),
    Column('priceBalance', Numeric(38, 14)),
    Column('quantityBalance', Numeric(38, 14)),
    Column('origAmountBalance', Numeric(38, 14)),
    Column('exchangeRateBalance', Numeric(38, 14)),
    Column('amountBalance', Numeric(38, 14))
)


t_GLAuxDetailReturnTempTable13917156705 = Table(
    'GLAuxDetailReturnTempTable13917156705', metadata,
    Column('eap_reportrowtype', Integer, nullable=False),
    Column('accountID', UNIQUEIDENTIFIER),
    Column('accountCode', Unicode(40)),
    Column('accountName', Unicode(50)),
    Column('accountDcdirection', UNIQUEIDENTIFIER),
    Column('AuxAccPersonName', Unicode(200)),
    Column('AuxAccPersonID', UNIQUEIDENTIFIER),
    Column('AuxAccPersonCode', Unicode(40)),
    Column('madeDate', String(19, u'Chinese_PRC_CI_AS')),
    Column('period', String(34, u'Chinese_PRC_CI_AS')),
    Column('docwordCode', Unicode(34)),
    Column('docTypeNo', Unicode(34)),
    Column('docID', UNIQUEIDENTIFIER),
    Column('docNo', Unicode(34)),
    Column('entryNo', Unicode(34)),
    Column('summary', Unicode(4000), nullable=False),
    Column('currencyID', UNIQUEIDENTIFIER),
    Column('currencyCode', Unicode(32)),
    Column('currencyName', Unicode(200)),
    Column('calDirection', UNIQUEIDENTIFIER),
    Column('exchangeRate', Numeric(38, 14)),
    Column('price', Numeric(38, 14)),
    Column('quantityDr', Numeric(38, 14)),
    Column('origAmountDr', Numeric(38, 14)),
    Column('amountDr', Numeric(38, 14)),
    Column('priceDr', Numeric(28, 14)),
    Column('quantityCr', Numeric(38, 14)),
    Column('origAmountCr', Numeric(38, 14)),
    Column('amountCr', Numeric(38, 14)),
    Column('priceCr', Numeric(28, 14)),
    Column('dCDirection', UNIQUEIDENTIFIER),
    Column('priceBalance', Numeric(38, 14)),
    Column('quantityBalance', Numeric(38, 14)),
    Column('origAmountBalance', Numeric(38, 14)),
    Column('exchangeRateBalance', Numeric(38, 14)),
    Column('amountBalance', Numeric(38, 14))
)


t_GLAuxDetailReturnTempTabledemo = Table(
    'GLAuxDetailReturnTempTabledemo', metadata,
    Column('eap_reportrowtype', Integer, nullable=False),
    Column('accountID', UNIQUEIDENTIFIER),
    Column('accountCode', Unicode(40)),
    Column('accountName', Unicode(50)),
    Column('accountDcdirection', UNIQUEIDENTIFIER),
    Column('AuxAccCustomerName', Unicode(200)),
    Column('AuxAccCustomerID', UNIQUEIDENTIFIER),
    Column('AuxAccCustomerCode', Unicode(40)),
    Column('madeDate', String(19, u'Chinese_PRC_CI_AS')),
    Column('period', String(34, u'Chinese_PRC_CI_AS')),
    Column('docwordCode', Unicode(34)),
    Column('docTypeNo', Unicode(34)),
    Column('docID', UNIQUEIDENTIFIER),
    Column('docNo', Unicode(34)),
    Column('entryNo', Unicode(34)),
    Column('summary', Unicode(4000), nullable=False),
    Column('currencyID', UNIQUEIDENTIFIER),
    Column('currencyCode', Unicode(32)),
    Column('currencyName', Unicode(200)),
    Column('calDirection', UNIQUEIDENTIFIER),
    Column('exchangeRate', Numeric(38, 14)),
    Column('price', Numeric(38, 14)),
    Column('quantityDr', Numeric(38, 14)),
    Column('origAmountDr', Numeric(38, 14)),
    Column('amountDr', Numeric(38, 14)),
    Column('priceDr', Numeric(28, 14)),
    Column('quantityCr', Numeric(38, 14)),
    Column('origAmountCr', Numeric(38, 14)),
    Column('amountCr', Numeric(38, 14)),
    Column('priceCr', Numeric(28, 14)),
    Column('dCDirection', UNIQUEIDENTIFIER),
    Column('priceBalance', Numeric(38, 14)),
    Column('quantityBalance', Numeric(38, 14)),
    Column('origAmountBalance', Numeric(38, 14)),
    Column('exchangeRateBalance', Numeric(38, 14)),
    Column('amountBalance', Numeric(38, 14))
)


t_GLAuxSumReturnTempTable13671904217 = Table(
    'GLAuxSumReturnTempTable13671904217', metadata,
    Column('CurrentYear', Integer),
    Column('eap_reportrowtype', Integer, nullable=False),
    Column('accountID', UNIQUEIDENTIFIER),
    Column('accountCode', Unicode(40)),
    Column('accountName', Unicode(50)),
    Column('accountDcdirection', UNIQUEIDENTIFIER),
    Column('AuxAccCustomerName', Unicode(200)),
    Column('AuxAccCustomerID', UNIQUEIDENTIFIER),
    Column('AuxAccCustomerCode', Unicode(40)),
    Column('currencyID', UNIQUEIDENTIFIER),
    Column('currencyCode', Unicode(32)),
    Column('currencyName', Unicode(200)),
    Column('calDirection', UNIQUEIDENTIFIER),
    Column('exchangeRate', Integer),
    Column('period', String(34, u'Chinese_PRC_CI_AS')),
    Column('summary', Unicode(8), nullable=False),
    Column('quantityDr', Numeric(38, 14)),
    Column('origAmountDr', Numeric(38, 14)),
    Column('amountDr', Numeric(38, 14)),
    Column('quantityCr', Numeric(38, 14)),
    Column('origAmountCr', Numeric(38, 14)),
    Column('amountCr', Numeric(38, 14)),
    Column('dCDirection', UNIQUEIDENTIFIER),
    Column('quantityBalance', Numeric(38, 14)),
    Column('origAmountBalance', Numeric(38, 14)),
    Column('amountBalance', Numeric(38, 14))
)


t_GLAuxSumReturnTempTable13917156705 = Table(
    'GLAuxSumReturnTempTable13917156705', metadata,
    Column('CurrentYear', Integer),
    Column('eap_reportrowtype', Integer, nullable=False),
    Column('accountID', UNIQUEIDENTIFIER),
    Column('accountCode', Unicode(40)),
    Column('accountName', Unicode(50)),
    Column('accountDcdirection', UNIQUEIDENTIFIER),
    Column('AuxAccCustomerName', Unicode(200)),
    Column('AuxAccCustomerID', UNIQUEIDENTIFIER),
    Column('AuxAccCustomerCode', Unicode(40)),
    Column('currencyID', UNIQUEIDENTIFIER),
    Column('currencyCode', Unicode(32)),
    Column('currencyName', Unicode(200)),
    Column('calDirection', UNIQUEIDENTIFIER),
    Column('exchangeRate', Integer),
    Column('period', String(34, u'Chinese_PRC_CI_AS')),
    Column('summary', Unicode(8), nullable=False),
    Column('quantityDr', Numeric(38, 14)),
    Column('origAmountDr', Numeric(38, 14)),
    Column('amountDr', Numeric(38, 14)),
    Column('quantityCr', Numeric(38, 14)),
    Column('origAmountCr', Numeric(38, 14)),
    Column('amountCr', Numeric(38, 14)),
    Column('dCDirection', UNIQUEIDENTIFIER),
    Column('quantityBalance', Numeric(38, 14)),
    Column('origAmountBalance', Numeric(38, 14)),
    Column('amountBalance', Numeric(38, 14))
)


t_GLBalanceSumTempTable13671904217 = Table(
    'GLBalanceSumTempTable13671904217', metadata,
    Column('eap_reportrowtype', Integer, nullable=False),
    Column('accountTypeID', UNIQUEIDENTIFIER),
    Column('accountTypeCode', Unicode(40)),
    Column('accountTypeName', Unicode(50)),
    Column('accountID', UNIQUEIDENTIFIER),
    Column('accountCode', Unicode(40)),
    Column('accountName', Unicode(500)),
    Column('accountDcdirection', UNIQUEIDENTIFIER),
    Column('accountUnit', Unicode(50)),
    Column('currencyID', UNIQUEIDENTIFIER),
    Column('currencyCode', Unicode(32)),
    Column('currencyName', Unicode(200)),
    Column('calDirection', UNIQUEIDENTIFIER),
    Column('quantityBalance', Numeric(28, 14)),
    Column('origAmountBalance', Numeric(28, 14)),
    Column('amountBalance', Numeric(28, 14)),
    Column('periodBeginBalanceQuantityDr', Numeric(28, 14)),
    Column('periodBeginBalanceOrigAmountDr', Numeric(28, 14)),
    Column('periodBeginBalanceAmountDr', Numeric(28, 14)),
    Column('periodBeginBalanceQuantityCr', Numeric(28, 14)),
    Column('periodBeginBalanceOrigAmountCr', Numeric(28, 14)),
    Column('periodBeginBalanceAmountCr', Numeric(28, 14)),
    Column('quantityDr', Numeric(28, 14)),
    Column('origAmountDr', Numeric(28, 14)),
    Column('amountDr', Numeric(28, 14)),
    Column('quantityCr', Numeric(28, 14)),
    Column('origAmountCr', Numeric(28, 14)),
    Column('amountCr', Numeric(28, 14)),
    Column('cumQuantityDr', Numeric(28, 14)),
    Column('cumOrigAmountDr', Numeric(28, 14)),
    Column('cumAmountDr', Numeric(28, 14)),
    Column('cumQuantityCr', Numeric(28, 14)),
    Column('cumOrigAmountCr', Numeric(28, 14)),
    Column('cumAmountCr', Numeric(28, 14)),
    Column('periodEndBalanceQuantityDr', Numeric(28, 14)),
    Column('periodEndBalanceOrigAmountDr', Numeric(28, 14)),
    Column('periodEndBalanceAmountDr', Numeric(28, 14)),
    Column('periodEndBalanceQuantityCr', Numeric(28, 14)),
    Column('periodEndBalanceOrigAmountCr', Numeric(28, 14)),
    Column('periodEndBalanceAmountCr', Numeric(28, 14)),
    Column('auxAccAuxSelfDef', Unicode(10))
)


t_GLBalanceSumTempTable13726451076 = Table(
    'GLBalanceSumTempTable13726451076', metadata,
    Column('eap_reportrowtype', Integer, nullable=False),
    Column('accountTypeID', UNIQUEIDENTIFIER),
    Column('accountTypeCode', Unicode(40)),
    Column('accountTypeName', Unicode(50)),
    Column('accountID', UNIQUEIDENTIFIER),
    Column('accountCode', Unicode(40)),
    Column('accountName', Unicode(500)),
    Column('accountDcdirection', UNIQUEIDENTIFIER),
    Column('accountUnit', Unicode(50)),
    Column('currencyID', UNIQUEIDENTIFIER),
    Column('currencyCode', Unicode(32)),
    Column('currencyName', Unicode(200)),
    Column('calDirection', UNIQUEIDENTIFIER),
    Column('quantityBalance', Numeric(28, 14)),
    Column('origAmountBalance', Numeric(28, 14)),
    Column('amountBalance', Numeric(28, 14)),
    Column('periodBeginBalanceQuantityDr', Numeric(28, 14)),
    Column('periodBeginBalanceOrigAmountDr', Numeric(28, 14)),
    Column('periodBeginBalanceAmountDr', Numeric(28, 14)),
    Column('periodBeginBalanceQuantityCr', Numeric(28, 14)),
    Column('periodBeginBalanceOrigAmountCr', Numeric(28, 14)),
    Column('periodBeginBalanceAmountCr', Numeric(28, 14)),
    Column('quantityDr', Numeric(28, 14)),
    Column('origAmountDr', Numeric(28, 14)),
    Column('amountDr', Numeric(28, 14)),
    Column('quantityCr', Numeric(28, 14)),
    Column('origAmountCr', Numeric(28, 14)),
    Column('amountCr', Numeric(28, 14)),
    Column('cumQuantityDr', Numeric(28, 14)),
    Column('cumOrigAmountDr', Numeric(28, 14)),
    Column('cumAmountDr', Numeric(28, 14)),
    Column('cumQuantityCr', Numeric(28, 14)),
    Column('cumOrigAmountCr', Numeric(28, 14)),
    Column('cumAmountCr', Numeric(28, 14)),
    Column('periodEndBalanceQuantityDr', Numeric(28, 14)),
    Column('periodEndBalanceOrigAmountDr', Numeric(28, 14)),
    Column('periodEndBalanceAmountDr', Numeric(28, 14)),
    Column('periodEndBalanceQuantityCr', Numeric(28, 14)),
    Column('periodEndBalanceOrigAmountCr', Numeric(28, 14)),
    Column('periodEndBalanceAmountCr', Numeric(28, 14)),
    Column('auxAccAuxSelfDef', Unicode(10))
)


t_GLBalanceSumTempTabledemo = Table(
    'GLBalanceSumTempTabledemo', metadata,
    Column('eap_reportrowtype', Integer, nullable=False),
    Column('accountTypeID', UNIQUEIDENTIFIER),
    Column('accountTypeCode', Unicode(40)),
    Column('accountTypeName', Unicode(50)),
    Column('accountID', UNIQUEIDENTIFIER),
    Column('accountCode', Unicode(40)),
    Column('accountName', Unicode(500)),
    Column('accountDcdirection', UNIQUEIDENTIFIER),
    Column('accountUnit', Unicode(50)),
    Column('currencyID', UNIQUEIDENTIFIER),
    Column('currencyCode', Unicode(32)),
    Column('currencyName', Unicode(200)),
    Column('calDirection', UNIQUEIDENTIFIER),
    Column('quantityBalance', Numeric(28, 14)),
    Column('origAmountBalance', Numeric(28, 14)),
    Column('amountBalance', Numeric(28, 14)),
    Column('periodBeginBalanceQuantityDr', Numeric(28, 14)),
    Column('periodBeginBalanceOrigAmountDr', Numeric(28, 14)),
    Column('periodBeginBalanceAmountDr', Numeric(28, 14)),
    Column('periodBeginBalanceQuantityCr', Numeric(28, 14)),
    Column('periodBeginBalanceOrigAmountCr', Numeric(28, 14)),
    Column('periodBeginBalanceAmountCr', Numeric(28, 14)),
    Column('quantityDr', Numeric(28, 14)),
    Column('origAmountDr', Numeric(28, 14)),
    Column('amountDr', Numeric(28, 14)),
    Column('quantityCr', Numeric(28, 14)),
    Column('origAmountCr', Numeric(28, 14)),
    Column('amountCr', Numeric(28, 14)),
    Column('cumQuantityDr', Numeric(28, 14)),
    Column('cumOrigAmountDr', Numeric(28, 14)),
    Column('cumAmountDr', Numeric(28, 14)),
    Column('cumQuantityCr', Numeric(28, 14)),
    Column('cumOrigAmountCr', Numeric(28, 14)),
    Column('cumAmountCr', Numeric(28, 14)),
    Column('periodEndBalanceQuantityDr', Numeric(28, 14)),
    Column('periodEndBalanceOrigAmountDr', Numeric(28, 14)),
    Column('periodEndBalanceAmountDr', Numeric(28, 14)),
    Column('periodEndBalanceQuantityCr', Numeric(28, 14)),
    Column('periodEndBalanceOrigAmountCr', Numeric(28, 14)),
    Column('periodEndBalanceAmountCr', Numeric(28, 14)),
    Column('auxAccAuxSelfDef', Unicode(10))
)


t_GLDetailReturnTempTable13671904217 = Table(
    'GLDetailReturnTempTable13671904217', metadata,
    Column('isIncludeUnPost', Integer, nullable=False),
    Column('eap_reportrowtype', Integer, nullable=False),
    Column('accountID', UNIQUEIDENTIFIER),
    Column('accountCode', Unicode(40)),
    Column('accountName', Unicode(50)),
    Column('accountDcdirection', UNIQUEIDENTIFIER),
    Column('madeDate', Unicode(34)),
    Column('period', Unicode(34)),
    Column('docwordCode', Unicode(100)),
    Column('docTypeNo', Unicode(30)),
    Column('docID', UNIQUEIDENTIFIER),
    Column('docNo', Unicode(50)),
    Column('entryNo', Unicode(50)),
    Column('summary', Unicode(4000)),
    Column('currencyID', UNIQUEIDENTIFIER),
    Column('currencyCode', Unicode(32)),
    Column('currencyName', Unicode(200)),
    Column('calDirection', UNIQUEIDENTIFIER),
    Column('oppositeAccount', Unicode(4000)),
    Column('price', Numeric(28, 14)),
    Column('exchangeRate', Numeric(28, 14)),
    Column('quantityDr', Numeric(28, 14)),
    Column('origAmountDr', Numeric(28, 14)),
    Column('amountDr', Numeric(28, 14)),
    Column('priceDr', Numeric(28, 14)),
    Column('quantityCr', Numeric(28, 14)),
    Column('origAmountCr', Numeric(28, 14)),
    Column('amountCr', Numeric(28, 14)),
    Column('priceCr', Numeric(28, 14)),
    Column('dCDirection', Integer),
    Column('priceBalance', Numeric(28, 14)),
    Column('quantityBalance', Numeric(28, 14)),
    Column('origAmountBalance', Numeric(28, 14)),
    Column('exchangeRateBalance', Numeric(28, 14)),
    Column('amountBalance', Numeric(28, 14)),
    Column('tempQuantityCr', Numeric(28, 14)),
    Column('tempQuantityDr', Numeric(28, 14)),
    Column('temporigAmountDr', Numeric(28, 14)),
    Column('temporigAmountCr', Numeric(28, 14)),
    Column('DocDrCrType', Integer)
)


t_GLDetailReturnTempTable13917156705 = Table(
    'GLDetailReturnTempTable13917156705', metadata,
    Column('isIncludeUnPost', Integer, nullable=False),
    Column('eap_reportrowtype', Integer, nullable=False),
    Column('accountID', UNIQUEIDENTIFIER),
    Column('accountCode', Unicode(40)),
    Column('accountName', Unicode(50)),
    Column('accountDcdirection', UNIQUEIDENTIFIER),
    Column('madeDate', Unicode(34)),
    Column('period', Unicode(34)),
    Column('docwordCode', Unicode(100)),
    Column('docTypeNo', Unicode(30)),
    Column('docID', UNIQUEIDENTIFIER),
    Column('docNo', Unicode(50)),
    Column('entryNo', Unicode(50)),
    Column('summary', Unicode(4000)),
    Column('currencyID', UNIQUEIDENTIFIER),
    Column('currencyCode', Unicode(32)),
    Column('currencyName', Unicode(200)),
    Column('calDirection', UNIQUEIDENTIFIER),
    Column('oppositeAccount', Unicode(4000)),
    Column('price', Numeric(28, 14)),
    Column('exchangeRate', Numeric(28, 14)),
    Column('quantityDr', Numeric(28, 14)),
    Column('origAmountDr', Numeric(28, 14)),
    Column('amountDr', Numeric(28, 14)),
    Column('priceDr', Numeric(28, 14)),
    Column('quantityCr', Numeric(28, 14)),
    Column('origAmountCr', Numeric(28, 14)),
    Column('amountCr', Numeric(28, 14)),
    Column('priceCr', Numeric(28, 14)),
    Column('dCDirection', Integer),
    Column('priceBalance', Numeric(28, 14)),
    Column('quantityBalance', Numeric(28, 14)),
    Column('origAmountBalance', Numeric(28, 14)),
    Column('exchangeRateBalance', Numeric(28, 14)),
    Column('amountBalance', Numeric(28, 14)),
    Column('tempQuantityCr', Numeric(28, 14)),
    Column('tempQuantityDr', Numeric(28, 14)),
    Column('temporigAmountDr', Numeric(28, 14)),
    Column('temporigAmountCr', Numeric(28, 14)),
    Column('DocDrCrType', Integer)
)


t_GLSumReturnTempTable13671904217 = Table(
    'GLSumReturnTempTable13671904217', metadata,
    Column('CurrentYear', Integer),
    Column('eap_reportrowtype', Integer, nullable=False),
    Column('accountID', UNIQUEIDENTIFIER),
    Column('accountCode', Unicode(400)),
    Column('accountName', Unicode(1000)),
    Column('accountDcdirection', UNIQUEIDENTIFIER),
    Column('madeDate', Unicode(34)),
    Column('period', Unicode(34)),
    Column('summary', Unicode(8), nullable=False),
    Column('currencyID', UNIQUEIDENTIFIER),
    Column('currencyCode', Unicode(32)),
    Column('currencyName', Unicode(200)),
    Column('quantityDr', Numeric(38, 14)),
    Column('origAmountDr', Numeric(38, 14)),
    Column('amountDr', Numeric(38, 14)),
    Column('quantityCr', Numeric(38, 14)),
    Column('origAmountCr', Numeric(38, 14)),
    Column('amountCr', Numeric(38, 14)),
    Column('dCDirection', Integer),
    Column('quantityBalance', Numeric(38, 14)),
    Column('origAmountBalance', Numeric(38, 14)),
    Column('amountBalance', Numeric(38, 14)),
    Column('auxAccAuxSelfDef', Unicode(200)),
    Column('auxAccCustomerID', UNIQUEIDENTIFIER),
    Column('auxAccCustomerCode', Unicode(32)),
    Column('auxAccCustomerName', Unicode(200)),
    Column('auxAccPersonID', UNIQUEIDENTIFIER),
    Column('auxAccPersonCode', Unicode(32)),
    Column('auxAccPersonName', Unicode(200)),
    Column('auxAccDepartmentID', UNIQUEIDENTIFIER),
    Column('auxAccDepartmentCode', Unicode(32)),
    Column('auxAccDepartmentName', Unicode(200)),
    Column('auxAccProjectID', UNIQUEIDENTIFIER),
    Column('auxAccProjectCode', Unicode(32)),
    Column('auxAccProjectName', Unicode(200)),
    Column('auxAccInventoryID', UNIQUEIDENTIFIER),
    Column('auxAccInventoryCode', Unicode(32)),
    Column('auxAccInventoryName', Unicode(200)),
    Column('ExAuxAcc1ID', UNIQUEIDENTIFIER),
    Column('ExAuxAcc1Code', Unicode(50)),
    Column('ExAuxAcc1Name', Unicode(200)),
    Column('ExAuxAcc2ID', UNIQUEIDENTIFIER),
    Column('ExAuxAcc2Code', Unicode(50)),
    Column('ExAuxAcc2Name', Unicode(200)),
    Column('ExAuxAcc3ID', UNIQUEIDENTIFIER),
    Column('ExAuxAcc3Code', Unicode(50)),
    Column('ExAuxAcc3Name', Unicode(200)),
    Column('ExAuxAcc4ID', UNIQUEIDENTIFIER),
    Column('ExAuxAcc4Code', Unicode(50)),
    Column('ExAuxAcc4Name', Unicode(200)),
    Column('ExAuxAcc5ID', UNIQUEIDENTIFIER),
    Column('ExAuxAcc5Code', Unicode(50)),
    Column('ExAuxAcc5Name', Unicode(200)),
    Column('ExAuxAcc6ID', UNIQUEIDENTIFIER),
    Column('ExAuxAcc6Code', Unicode(50)),
    Column('ExAuxAcc6Name', Unicode(200)),
    Column('ExAuxAcc7ID', UNIQUEIDENTIFIER),
    Column('ExAuxAcc7Code', Unicode(50)),
    Column('ExAuxAcc7Name', Unicode(200)),
    Column('ExAuxAcc8ID', UNIQUEIDENTIFIER),
    Column('ExAuxAcc8Code', Unicode(50)),
    Column('ExAuxAcc8Name', Unicode(200)),
    Column('ExAuxAcc9ID', UNIQUEIDENTIFIER),
    Column('ExAuxAcc9Code', Unicode(50)),
    Column('ExAuxAcc9Name', Unicode(200)),
    Column('ExAuxAcc10ID', UNIQUEIDENTIFIER),
    Column('ExAuxAcc10Code', Unicode(50)),
    Column('ExAuxAcc10Name', Unicode(200))
)


t_GLSumReturnTempTabledemo = Table(
    'GLSumReturnTempTabledemo', metadata,
    Column('CurrentYear', Integer),
    Column('eap_reportrowtype', Integer, nullable=False),
    Column('accountID', UNIQUEIDENTIFIER),
    Column('accountCode', Unicode(400)),
    Column('accountName', Unicode(1000)),
    Column('accountDcdirection', UNIQUEIDENTIFIER),
    Column('madeDate', Unicode(34)),
    Column('period', Unicode(34)),
    Column('summary', Unicode(8), nullable=False),
    Column('currencyID', UNIQUEIDENTIFIER),
    Column('currencyCode', Unicode(32)),
    Column('currencyName', Unicode(200)),
    Column('quantityDr', Numeric(38, 14)),
    Column('origAmountDr', Numeric(38, 14)),
    Column('amountDr', Numeric(38, 14)),
    Column('quantityCr', Numeric(38, 14)),
    Column('origAmountCr', Numeric(38, 14)),
    Column('amountCr', Numeric(38, 14)),
    Column('dCDirection', Integer),
    Column('quantityBalance', Numeric(38, 14)),
    Column('origAmountBalance', Numeric(38, 14)),
    Column('amountBalance', Numeric(38, 14)),
    Column('auxAccAuxSelfDef', Unicode(200)),
    Column('auxAccCustomerID', UNIQUEIDENTIFIER),
    Column('auxAccCustomerCode', Unicode(32)),
    Column('auxAccCustomerName', Unicode(200)),
    Column('auxAccPersonID', UNIQUEIDENTIFIER),
    Column('auxAccPersonCode', Unicode(32)),
    Column('auxAccPersonName', Unicode(200)),
    Column('auxAccDepartmentID', UNIQUEIDENTIFIER),
    Column('auxAccDepartmentCode', Unicode(32)),
    Column('auxAccDepartmentName', Unicode(200)),
    Column('auxAccProjectID', UNIQUEIDENTIFIER),
    Column('auxAccProjectCode', Unicode(32)),
    Column('auxAccProjectName', Unicode(200)),
    Column('auxAccInventoryID', UNIQUEIDENTIFIER),
    Column('auxAccInventoryCode', Unicode(32)),
    Column('auxAccInventoryName', Unicode(200)),
    Column('ExAuxAcc1ID', UNIQUEIDENTIFIER),
    Column('ExAuxAcc1Code', Unicode(50)),
    Column('ExAuxAcc1Name', Unicode(200)),
    Column('ExAuxAcc2ID', UNIQUEIDENTIFIER),
    Column('ExAuxAcc2Code', Unicode(50)),
    Column('ExAuxAcc2Name', Unicode(200)),
    Column('ExAuxAcc3ID', UNIQUEIDENTIFIER),
    Column('ExAuxAcc3Code', Unicode(50)),
    Column('ExAuxAcc3Name', Unicode(200)),
    Column('ExAuxAcc4ID', UNIQUEIDENTIFIER),
    Column('ExAuxAcc4Code', Unicode(50)),
    Column('ExAuxAcc4Name', Unicode(200)),
    Column('ExAuxAcc5ID', UNIQUEIDENTIFIER),
    Column('ExAuxAcc5Code', Unicode(50)),
    Column('ExAuxAcc5Name', Unicode(200)),
    Column('ExAuxAcc6ID', UNIQUEIDENTIFIER),
    Column('ExAuxAcc6Code', Unicode(50)),
    Column('ExAuxAcc6Name', Unicode(200)),
    Column('ExAuxAcc7ID', UNIQUEIDENTIFIER),
    Column('ExAuxAcc7Code', Unicode(50)),
    Column('ExAuxAcc7Name', Unicode(200)),
    Column('ExAuxAcc8ID', UNIQUEIDENTIFIER),
    Column('ExAuxAcc8Code', Unicode(50)),
    Column('ExAuxAcc8Name', Unicode(200)),
    Column('ExAuxAcc9ID', UNIQUEIDENTIFIER),
    Column('ExAuxAcc9Code', Unicode(50)),
    Column('ExAuxAcc9Name', Unicode(200)),
    Column('ExAuxAcc10ID', UNIQUEIDENTIFIER),
    Column('ExAuxAcc10Code', Unicode(50)),
    Column('ExAuxAcc10Name', Unicode(200))
)


class GLAccountAuxPeriodBeginDetail(Base):
    __tablename__ = 'GL_AccountAuxPeriodBeginDetail'

    code = Column(Unicode(30))
    name = Column(Unicode(200))
    docdate = Column(String(19, u'Chinese_PRC_CI_AS'))
    docno = Column(Unicode(200))
    summarry = Column(Unicode(100))
    quantity = Column(Numeric(28, 14))
    origamount = Column(Numeric(28, 14))
    amount = Column(Numeric(28, 14))
    vouchercode = Column(Unicode(50))
    voucherdate = Column(String(19, u'Chinese_PRC_CI_AS'))
    duedate = Column(String(19, u'Chinese_PRC_CI_AS'))
    isfrompreyear = Column(Integer)
    createdtime = Column(String(19, u'Chinese_PRC_CI_AS'))
    sequencenumber = Column(Integer)
    ts = Column(TIMESTAMP, nullable=False)
    updated = Column(String(19, u'Chinese_PRC_CI_AS'))
    updatedBy = Column(Unicode(32))
    id = Column(Integer, primary_key=True)
    idaccountDTO = Column(Integer)
    idcurrencyDTO = Column(Integer, nullable=False, server_default=text("((0))"))
    idauxaccdepartment = Column(Integer)
    idauxaccinventory = Column(Integer)
    idauxacccustomer = Column(Integer)
    idauxaccsupplier = Column(Integer)
    idauxaccperson = Column(Integer)
    idclerk = Column(Integer)
    idauxaccproject = Column(Integer)
    dcdirection = Column(Integer)
    idAccountAuxPeriodBeginDTO = Column(Integer)
    idexauxacc1 = Column(Integer)
    idexauxacc10 = Column(Integer)
    idexauxacc2 = Column(Integer)
    idexauxacc3 = Column(Integer)
    idexauxacc4 = Column(Integer)
    idexauxacc5 = Column(Integer)
    idexauxacc6 = Column(Integer)
    idexauxacc7 = Column(Integer)
    idexauxacc8 = Column(Integer)
    idexauxacc9 = Column(Integer)


class GLAccountPeriodBegin(Base):
    __tablename__ = 'GL_AccountPeriodBegin'

    code = Column(Unicode(30))
    name = Column(Unicode(200))
    accountingyear = Column(Integer)
    accountingperiod = Column(Integer)
    currency = Column(Unicode(50))
    yearbeginbalancequantity = Column(Numeric(28, 14))
    yearbeginbalanceorigamount = Column(Numeric(28, 14))
    yearbeginbalanceamount = Column(Numeric(28, 14))
    cumquantitydr = Column(Numeric(28, 14))
    cumorigamountdr = Column(Numeric(28, 14))
    cumamountdr = Column(Numeric(28, 14))
    cumquantitycr = Column(Numeric(28, 14))
    cumorigamountcr = Column(Numeric(28, 14))
    cumamountcr = Column(Numeric(28, 14))
    periodbeginbalancequantity = Column(Numeric(28, 14))
    periodbeginbalanceorigamount = Column(Numeric(28, 14))
    periodbeginbalanceamount = Column(Numeric(28, 14))
    createdtime = Column(String(19, u'Chinese_PRC_CI_AS'))
    sequencenumber = Column(Integer)
    ts = Column(TIMESTAMP, nullable=False)
    updated = Column(String(19, u'Chinese_PRC_CI_AS'))
    updatedBy = Column(Unicode(32))
    SourceType = Column(String(200, u'Chinese_PRC_CI_AS'))
    SourceContent = Column(String(200, u'Chinese_PRC_CI_AS'))
    id = Column(Integer, primary_key=True)
    idaccountDTO = Column(Integer)


class GLAccountPeriodBeginDetail(Base):
    __tablename__ = 'GL_AccountPeriodBeginDetail'

    code = Column(Unicode(30))
    name = Column(Unicode(200))
    yearbeginbalancequantity = Column(Numeric(28, 14))
    yearbeginbalanceorigamount = Column(Numeric(28, 14))
    yearbeginbalanceamount = Column(Numeric(28, 14))
    cumquantitydr = Column(Numeric(28, 14))
    cumorigamountdr = Column(Numeric(28, 14))
    cumamountdr = Column(Numeric(28, 14))
    cumquantitycr = Column(Numeric(28, 14))
    cumorigamountcr = Column(Numeric(28, 14))
    cumamountcr = Column(Numeric(28, 14))
    periodbeginbalancequantity = Column(Numeric(28, 14))
    periodbeginbalanceorigamount = Column(Numeric(28, 14))
    periodbeginbalanceamount = Column(Numeric(28, 14))
    createdtime = Column(String(19, u'Chinese_PRC_CI_AS'))
    sequencenumber = Column(Integer)
    ts = Column(TIMESTAMP, nullable=False)
    updated = Column(String(19, u'Chinese_PRC_CI_AS'))
    updatedBy = Column(Unicode(32))
    id = Column(Integer, primary_key=True)
    idaccountDTO = Column(Integer)
    idcurrencyDTO = Column(Integer)
    idauxaccdepartment = Column(Integer)
    idauxaccinventory = Column(Integer)
    idauxacccustomer = Column(Integer)
    idauxaccsupplier = Column(Integer)
    idauxaccperson = Column(Integer)
    idauxaccproject = Column(Integer)
    idAccountPeriodBeginDTO = Column(Integer)
    idexauxacc1 = Column(Integer)
    idexauxacc10 = Column(Integer)
    idexauxacc2 = Column(Integer)
    idexauxacc3 = Column(Integer)
    idexauxacc4 = Column(Integer)
    idexauxacc5 = Column(Integer)
    idexauxacc6 = Column(Integer)
    idexauxacc7 = Column(Integer)
    idexauxacc8 = Column(Integer)
    idexauxacc9 = Column(Integer)


t_GL_AgeAnalysisRptSet = Table(
    'GL_AgeAnalysisRptSet', metadata,
    Column('days', Integer),
    Column('flag', Integer),
    Column('userId', Integer)
)


class GLAuxiliaryInfo(Base):
    __tablename__ = 'GL_AuxiliaryInfo'

    code = Column(Unicode(30))
    name = Column(Unicode(200))
    billno = Column(Unicode(50))
    billdate = Column(String(19, u'Chinese_PRC_CI_AS'))
    bizdate = Column(String(19, u'Chinese_PRC_CI_AS'))
    bizno = Column(Unicode(50))
    duedate = Column(String(19, u'Chinese_PRC_CI_AS'))
    origamount = Column(Numeric(28, 14))
    amount = Column(Numeric(28, 14))
    quantity = Column(Numeric(28, 14))
    price = Column(Numeric(28, 14))
    createdtime = Column(String(19, u'Chinese_PRC_CI_AS'))
    sequencenumber = Column(Integer)
    ts = Column(TIMESTAMP, nullable=False)
    updated = Column(String(19, u'Chinese_PRC_CI_AS'))
    updatedBy = Column(Unicode(32))
    unit = Column(Unicode(200))
    exchangerate = Column(Numeric(28, 14))
    ID = Column(Integer, primary_key=True)
    idaccount = Column(Integer)
    idbankAccount = Column(Integer)
    idcurrency = Column(Integer)
    idauxAccDepartment = Column(Integer)
    idauxAccInventory = Column(Integer)
    idauxAccCustomer = Column(Integer)
    idauxAccSupplier = Column(Integer)
    idauxAccPerson = Column(Integer)
    idclerk = Column(Integer)
    idauxAccProject = Column(Integer)
    idsettlestyle = Column(Integer)
    dcdirection = Column(Integer)
    DocId = Column(Integer)
    idEntryDTO = Column(Integer)
    idexauxacc1 = Column(Integer)
    idexauxacc10 = Column(Integer)
    idexauxacc2 = Column(Integer)
    idexauxacc3 = Column(Integer)
    idexauxacc4 = Column(Integer)
    idexauxacc5 = Column(Integer)
    idexauxacc6 = Column(Integer)
    idexauxacc7 = Column(Integer)
    idexauxacc8 = Column(Integer)
    idexauxacc9 = Column(Integer)


class GLCashFlowInfo(Base):
    __tablename__ = 'GL_CashFlowInfo'

    code = Column(Unicode(30))
    name = Column(Unicode(200))
    amount = Column(Numeric(28, 14))
    createdtime = Column(String(19, u'Chinese_PRC_CI_AS'))
    sequencenumber = Column(Integer)
    ts = Column(TIMESTAMP, nullable=False)
    updated = Column(String(19, u'Chinese_PRC_CI_AS'))
    updatedBy = Column(Unicode(32))
    ownerEntryNo = Column(Integer)
    mapEntryNo = Column(Integer)
    id = Column(Integer, primary_key=True)
    idaccount = Column(Integer)
    idcashflowitem = Column(Integer)
    idcurrency = Column(Integer)
    idDocDTO = Column(Integer)


class GLCashFlowPeriodBegin(Base):
    __tablename__ = 'GL_CashFlowPeriodBegin'

    code = Column(Unicode(30))
    name = Column(Unicode(200))
    periodbeginamount = Column(Numeric(28, 14))
    createdtime = Column(String(19, u'Chinese_PRC_CI_AS'))
    sequencenumber = Column(Integer)
    ts = Column(TIMESTAMP, nullable=False)
    updated = Column(String(19, u'Chinese_PRC_CI_AS'))
    updatedBy = Column(Unicode(32))
    id = Column(Integer, primary_key=True)
    idcashflowitem = Column(Integer)


class GLDoc(Base):
    __tablename__ = 'GL_Doc'

    code = Column(Unicode(30))
    name = Column(Unicode(200))
    accuorigamountdr = Column(Numeric(28, 14))
    accuorigamountcr = Column(Numeric(28, 14))
    accuamountdr = Column(Numeric(28, 14))
    accuamountcr = Column(Numeric(28, 14))
    issupervisoraudit = Column(Integer)
    supervisorname = Column(Unicode(50))
    supervisorauditdate = Column(String(19, u'Chinese_PRC_CI_AS'))
    iscashieraudit = Column(Integer)
    cashiername = Column(Unicode(50))
    cashierauditdate = Column(String(19, u'Chinese_PRC_CI_AS'))
    ispost = Column(Integer)
    bookkeepername = Column(Unicode(50))
    postdate = Column(String(19, u'Chinese_PRC_CI_AS'))
    iserror = Column(Integer)
    errormessage = Column(Unicode(50))
    isinvalidate = Column(Integer)
    invalidatorname = Column(Unicode(50))
    invalidatedate = Column(String(19, u'Chinese_PRC_CI_AS'))
    istaxed = Column(Integer)
    iscashflowed = Column(Integer)
    isquantitydoc = Column(Integer)
    isforeigncurrencydoc = Column(Integer)
    attachedvouchernum = Column(Integer)
    docno = Column(Unicode(50))
    docclass = Column(Unicode(50))
    accountingperiod = Column(Integer)
    docid = Column(Unicode(50))
    accountingyear = Column(Integer)
    memo = Column(Unicode(50))
    voucherdate = Column(String(19, u'Chinese_PRC_CI_AS'))
    madedate = Column(String(19, u'Chinese_PRC_CI_AS'))
    maker = Column(Unicode(50))
    auditor = Column(Unicode(50))
    auditeddate = Column(String(19, u'Chinese_PRC_CI_AS'))
    reviser = Column(Unicode(50))
    iscarriedforwardout = Column(Integer)
    iscarriedforwardin = Column(Integer)
    ismodifiedcode = Column(Integer)
    createdtime = Column(String(19, u'Chinese_PRC_CI_AS'))
    sequencenumber = Column(Integer)
    ts = Column(TIMESTAMP, nullable=False)
    updated = Column(String(19, u'Chinese_PRC_CI_AS'))
    updatedBy = Column(Unicode(32))
    priuserdefnvc1 = Column(Unicode(500))
    priuserdefdecm1 = Column(Numeric(28, 14))
    priuserdefdecm2 = Column(Numeric(28, 14))
    priuserdefnvc2 = Column(Unicode(500))
    priuserdefnvc3 = Column(Unicode(500))
    priuserdefdecm3 = Column(Numeric(28, 14))
    priuserdefnvc4 = Column(Unicode(500))
    priuserdefdecm4 = Column(Numeric(28, 14))
    priuserdefnvc5 = Column(Unicode(500))
    priuserdefdecm5 = Column(Numeric(28, 14))
    priuserdefnvc6 = Column(Unicode(500))
    priuserdefdecm6 = Column(Numeric(28, 14))
    isCashierDoc = Column(Integer)
    DocOrderNum = Column(Unicode(200))
    SourceType = Column(String(200, u'Chinese_PRC_CI_AS'))
    SourceContent = Column(String(200, u'Chinese_PRC_CI_AS'))
    PrintCount = Column(Integer, nullable=False, server_default=text("((0))"))
    isCashflowByHand = Column(Integer)
    externalCode = Column(Unicode(50), server_default=text("(NULL)"))
    businessDocMoney = Column(Numeric(28, 14))
    batch = Column(DateTime)
    id = Column(Integer, primary_key=True)
    iddoctype = Column(Integer)
    isdefrence = Column(Integer)
    cashflowedstate = Column(Integer)
    docbusinesstype = Column(Integer)
    docsourcetype = Column(Integer)
    invalidateState = Column(Integer)
    makeErrorState = Column(Integer)
    voucherstate = Column(Integer)
    tempDocGenerate = Column(Integer)
    auditorid = Column(Integer)
    makerid = Column(Integer)
    bookkeeperid = Column(Integer)
    cashierid = Column(Integer)
    invalidatorid = Column(Integer)
    supervisorid = Column(Integer)
    idperiod = Column(Integer)
    transDocId = Column(Unicode(50))


t_GL_DocJournal = Table(
    'GL_DocJournal', metadata,
    Column('madedate', String(19, u'Chinese_PRC_CI_AS'), nullable=False),
    Column('DocType', Unicode(200), nullable=False),
    Column('docno', Unicode(50), nullable=False),
    Column('attachedvouchernum', Integer),
    Column('summary', Unicode(200), nullable=False),
    Column('period', Unicode(64), nullable=False),
    Column('accountCode', Unicode(200), nullable=False),
    Column('accountName', Unicode(200)),
    Column('currency', Unicode(200), nullable=False),
    Column('exchangerate', Numeric(28, 14)),
    Column('quantity', Numeric(28, 14)),
    Column('price', Numeric(28, 14)),
    Column('OrigAmount', Numeric(28, 14)),
    Column('Amount', Numeric(28, 14), nullable=False),
    Column('billNo', Unicode(200)),
    Column('billDate', String(19, u'Chinese_PRC_CI_AS')),
    Column('bizNo', Unicode(200)),
    Column('bizDate', String(19, u'Chinese_PRC_CI_AS')),
    Column('dueDate', String(19, u'Chinese_PRC_CI_AS')),
    Column('ClerkCode', Unicode(200)),
    Column('ClerkName', Unicode(200)),
    Column('BankAccountName', Unicode(200)),
    Column('SettlestyleName', Unicode(200)),
    Column('AuxAccCustomerCode', Unicode(200)),
    Column('AuxAccCustomerName', Unicode(200)),
    Column('AuxAccDepartmentCode', Unicode(200)),
    Column('AuxAccDepartmentName', Unicode(200)),
    Column('AuxAccInventoryCode', Unicode(200)),
    Column('AuxAccInventoryName', Unicode(200)),
    Column('AuxAccPersonCode', Unicode(200)),
    Column('AuxAccPersonName', Unicode(200)),
    Column('AuxAccProjectCode', Unicode(200)),
    Column('AuxAccProjectName', Unicode(200)),
    Column('Exauxacc1Code', Unicode(200)),
    Column('Exauxacc1Name', Unicode(200)),
    Column('Exauxacc2Code', Unicode(200)),
    Column('Exauxacc2Name', Unicode(200)),
    Column('Exauxacc3Code', Unicode(200)),
    Column('Exauxacc3Name', Unicode(200)),
    Column('Exauxacc4Code', Unicode(200)),
    Column('Exauxacc4Name', Unicode(200)),
    Column('Exauxacc5Code', Unicode(200)),
    Column('Exauxacc5Name', Unicode(200)),
    Column('Exauxacc6Code', Unicode(200)),
    Column('Exauxacc6Name', Unicode(200)),
    Column('Exauxacc7Code', Unicode(200)),
    Column('Exauxacc7Name', Unicode(200)),
    Column('Exauxacc8Code', Unicode(200)),
    Column('Exauxacc8Name', Unicode(200)),
    Column('Exauxacc9Code', Unicode(200)),
    Column('Exauxacc9Name', Unicode(200)),
    Column('Exauxacc10Code', Unicode(200)),
    Column('Exauxacc10Name', Unicode(200)),
    Column('ts', TIMESTAMP, nullable=False),
    Column('updated', String(19, u'Chinese_PRC_CI_AS')),
    Column('updatedBy', Unicode(32)),
    Column('id', Integer, nullable=False),
    Column('direction', Integer, nullable=False, server_default=text("((0))"))
)


class GLEntry(Base):
    __tablename__ = 'GL_Entry'

    code = Column(Unicode(30))
    name = Column(Unicode(200))
    summary = Column(Unicode(200))
    exchangerate = Column(Numeric(28, 14))
    origamountdr = Column(Numeric(28, 14))
    origamountcr = Column(Numeric(28, 14))
    amountdr = Column(Numeric(28, 14))
    amountcr = Column(Numeric(28, 14))
    quantitydr = Column(Numeric(28, 14))
    quantitycr = Column(Numeric(28, 14))
    price = Column(Numeric(28, 14))
    createdtime = Column(String(19, u'Chinese_PRC_CI_AS'))
    sequencenumber = Column(Integer)
    ts = Column(TIMESTAMP, nullable=False)
    updated = Column(String(19, u'Chinese_PRC_CI_AS'))
    updatedBy = Column(Unicode(32))
    priuserdefnvc1 = Column(Unicode(500))
    priuserdefdecm1 = Column(Numeric(28, 14))
    priuserdefnvc2 = Column(Unicode(500))
    priuserdefdecm2 = Column(Numeric(28, 14))
    priuserdefnvc3 = Column(Unicode(500))
    priuserdefdecm3 = Column(Numeric(28, 14))
    priuserdefnvc4 = Column(Unicode(500))
    priuserdefdecm4 = Column(Numeric(28, 14))
    AuxiliaryItems = Column(Unicode(200))
    id = Column(Integer, primary_key=True)
    idaccount = Column(Integer)
    idcurrency = Column(Integer)
    datafrom = Column(Integer)
    idDocDTO = Column(Integer)


class GLExAuxAcc(Base):
    __tablename__ = 'GL_ExAuxAcc'

    code = Column(Unicode(30))
    name = Column(Unicode(200))
    id = Column(Integer, primary_key=True)


class GLExchangeLossProfitTransform(Base):
    __tablename__ = 'GL_ExchangeLossProfitTransform'

    code = Column(Unicode(30))
    name = Column(Unicode(200))
    iscontain = Column(Integer)
    iscurrency = Column(Integer)
    accountingyear = Column(Integer)
    ts = Column(TIMESTAMP, nullable=False)
    updated = Column(String(19, u'Chinese_PRC_CI_AS'))
    updatedBy = Column(Unicode(32))
    id = Column(Integer, primary_key=True)
    idlossaccount = Column(Integer)
    idlossprofitaccount = Column(Integer)
    idprofitaccount = Column(Integer)
    iddoctype = Column(Integer)
    idperiod = Column(Integer)


class GLFindBalance(Base):
    __tablename__ = 'GL_FindBalance'

    ts = Column(TIMESTAMP, nullable=False)
    updatedBy = Column(Unicode(32))
    updated = Column(String(19, u'Chinese_PRC_CI_AS'))
    name = Column(Unicode(200), nullable=False)
    auxaccInfos = Column(Unicode(200))
    account = Column(Unicode(200))
    unit = Column(Unicode(200))
    dcDirection = Column(Unicode(200))
    id = Column(Integer, primary_key=True)
    idcurrency = Column(Integer)
    idperid = Column(Integer)


class GLFindBalanceDetail(Base):
    __tablename__ = 'GL_FindBalanceDetail'

    ts = Column(TIMESTAMP, nullable=False)
    updatedBy = Column(Unicode(32))
    updated = Column(String(19, u'Chinese_PRC_CI_AS'))
    origAmount = Column(Numeric(28, 14))
    amount = Column(Numeric(28, 14))
    quantity = Column(Numeric(28, 14))
    code = Column(Unicode(200))
    id = Column(Integer, primary_key=True)
    docDataType = Column(Integer)
    idfindBalance = Column(Integer)


class GLFuncDefinition(Base):
    __tablename__ = 'GL_FuncDefinition'

    code = Column(Unicode(30))
    name = Column(Unicode(200))
    title = Column(Unicode(50))
    function = Column(Unicode(50))
    format = Column(Unicode(300))
    description = Column(Unicode(300))
    demo = Column(Unicode(300))
    type = Column(Integer)
    isvisible = Column(Integer)
    createdtime = Column(String(19, u'Chinese_PRC_CI_AS'))
    sequencenumber = Column(Integer)
    ts = Column(TIMESTAMP, nullable=False)
    updated = Column(String(19, u'Chinese_PRC_CI_AS'))
    updatedBy = Column(Unicode(32))
    referenceurl = Column(Unicode(200))
    id = Column(Integer, primary_key=True)


class GLGLCheckAccountInfo(Base):
    __tablename__ = 'GL_GLCheckAccountInfo'

    code = Column(Unicode(30))
    name = Column(Unicode(200))
    totalvalue = Column(Numeric(28, 14))
    detailvalue = Column(Numeric(28, 14))
    createdtime = Column(String(19, u'Chinese_PRC_CI_AS'))
    sequencenumber = Column(Integer)
    ts = Column(TIMESTAMP, nullable=False)
    updated = Column(String(19, u'Chinese_PRC_CI_AS'))
    updatedBy = Column(Unicode(32))
    id = Column(Integer, primary_key=True)
    idaccount = Column(Integer)
    idcurrency = Column(Integer)
    idauxaccdepartment = Column(Integer)
    idauxaccinventory = Column(Integer)
    idauxacccustomer = Column(Integer)
    idauxaccsupplier = Column(Integer)
    idauxaccperson = Column(Integer)
    idauxaccproject = Column(Integer)
    glcheckaccounttype = Column(Integer)
    glcheckaccountvaluetype = Column(Integer)
    idexauxacc1 = Column(Integer)
    idexauxacc10 = Column(Integer)
    idexauxacc2 = Column(Integer)
    idexauxacc3 = Column(Integer)
    idexauxacc4 = Column(Integer)
    idexauxacc5 = Column(Integer)
    idexauxacc6 = Column(Integer)
    idexauxacc7 = Column(Integer)
    idexauxacc8 = Column(Integer)
    idexauxacc9 = Column(Integer)


class GLJournal(Base):
    __tablename__ = 'GL_Journal'

    code = Column(Unicode(30))
    name = Column(Unicode(200))
    docno = Column(Unicode(50))
    rowno = Column(Unicode(50))
    summary = Column(Unicode(200))
    maker = Column(Unicode(50))
    madedate = Column(String(19, u'Chinese_PRC_CI_AS'))
    auditorname = Column(Unicode(50))
    auditdate = Column(String(19, u'Chinese_PRC_CI_AS'))
    supervisorname = Column(Unicode(50))
    supervisorauditdate = Column(String(19, u'Chinese_PRC_CI_AS'))
    cashiername = Column(Unicode(50))
    cashierauditdate = Column(String(19, u'Chinese_PRC_CI_AS'))
    bookkeepername = Column(Unicode(50))
    postdate = Column(String(19, u'Chinese_PRC_CI_AS'))
    istaxed = Column(Integer)
    seqno = Column(Unicode(50))
    exchangerate = Column(Numeric(28, 14))
    price = Column(Numeric(28, 14))
    iscarriedforwardout = Column(Integer, server_default=text("((0))"))
    iscarriedforwardin = Column(Integer, server_default=text("((0))"))
    createdtime = Column(String(19, u'Chinese_PRC_CI_AS'))
    sequencenumber = Column(Integer)
    ispost = Column(Integer)
    year = Column(Integer)
    currentperiod = Column(Integer)
    ts = Column(TIMESTAMP, nullable=False)
    updated = Column(String(19, u'Chinese_PRC_CI_AS'))
    updatedBy = Column(Unicode(32))
    quantityDr = Column(Numeric(28, 14))
    quantityCr = Column(Numeric(28, 14))
    amountDr = Column(Numeric(28, 14))
    amountCr = Column(Numeric(28, 14))
    origAmountDr = Column(Numeric(28, 14))
    OrigAmountCr = Column(Numeric(28, 14))
    periodBeginOrigAmountDr = Column(Numeric(28, 14))
    periodBeginOrigAmountCr = Column(Numeric(28, 14))
    periodBeginAmountDr = Column(Numeric(28, 14))
    periodBeginAmountCr = Column(Numeric(28, 14))
    periodBeginQuantityDr = Column(Numeric(28, 14))
    periodBeginQuantityCr = Column(Numeric(28, 14))
    isPeriodBegin = Column(Integer)
    bizNo = Column(Unicode(200))
    bizDate = Column(String(19, u'Chinese_PRC_CI_AS'))
    billNo = Column(Unicode(200))
    billDate = Column(String(19, u'Chinese_PRC_CI_AS'))
    dueDate = Column(String(19, u'Chinese_PRC_CI_AS'))
    DocDrCrType = Column(Integer)
    id = Column(Integer, primary_key=True)
    idaccount = Column(Integer, nullable=False, server_default=text("((0))"))
    idcurrency = Column(Integer)
    idauxAccDepartment = Column(Integer)
    idDocType = Column(Integer)
    idauxAccInventory = Column(Integer)
    idauxAccCustomer = Column(Integer)
    idauxAccSupplier = Column(Integer)
    idauxAccPerson = Column(Integer)
    idclerk = Column(Integer)
    idauxAccProject = Column(Integer)
    idsettlestyle = Column(Integer)
    isdefrence = Column(Integer)
    datafrom = Column(Integer)
    docsourcetype = Column(Integer)
    direction = Column(Integer)
    docbusinesstype = Column(Integer)
    makerId = Column(Integer)
    docid = Column(Integer, nullable=False, server_default=text("((0))"))
    entryid = Column(Integer)
    auxiliaryinfoid = Column(Integer)
    idexauxacc1 = Column(Integer)
    idexauxacc10 = Column(Integer)
    idexauxacc2 = Column(Integer)
    idexauxacc3 = Column(Integer)
    idexauxacc4 = Column(Integer)
    idexauxacc5 = Column(Integer)
    idexauxacc6 = Column(Integer)
    idexauxacc7 = Column(Integer)
    idexauxacc8 = Column(Integer)
    idexauxacc9 = Column(Integer)
    idaccountingperiod = Column(Integer)


class GLKeyWord(Base):
    __tablename__ = 'GL_KeyWord'

    code = Column(Unicode(30))
    name = Column(Unicode(200))
    word = Column(Unicode(50))
    dtotype = Column(Unicode(50))
    isauxacc = Column(Integer)
    isused = Column(Integer)
    createdtime = Column(String(19, u'Chinese_PRC_CI_AS'))
    sequencenumber = Column(Integer)
    ts = Column(TIMESTAMP, nullable=False)
    updated = Column(String(19, u'Chinese_PRC_CI_AS'))
    updatedBy = Column(Unicode(32))
    id = Column(Integer, primary_key=True)


class GLMultiColumnSet(Base):
    __tablename__ = 'GL_MultiColumnSet'

    code = Column(Unicode(30))
    name = Column(Unicode(200))
    isBalanceMultiColumn = Column(Integer)
    createdtime = Column(String(19, u'Chinese_PRC_CI_AS'))
    sequencenumber = Column(Integer)
    ts = Column(TIMESTAMP, nullable=False)
    updated = Column(String(19, u'Chinese_PRC_CI_AS'))
    updatedBy = Column(Unicode(32))
    id = Column(Integer, primary_key=True)
    idanalysisaccount = Column(Integer)
    multicolumnsetanalysiscontent = Column(Integer)
    multicolumnsetanalysismethod = Column(Integer)
    searchplanid = Column(Integer)
    userid = Column(Integer)


class GLMultiColumnSetDetail(Base):
    __tablename__ = 'GL_MultiColumnSetDetail'

    code = Column(Unicode(30))
    name = Column(Unicode(200))
    columnName = Column(Unicode(50))
    createdtime = Column(String(19, u'Chinese_PRC_CI_AS'))
    sequencenumber = Column(Integer)
    ts = Column(TIMESTAMP, nullable=False)
    updated = Column(String(19, u'Chinese_PRC_CI_AS'))
    updatedBy = Column(Unicode(32))
    id = Column(Integer, primary_key=True)
    idcolumnaccount = Column(Integer)
    multicolumnsetanalysisdirection = Column(Integer)
    idMultiColumnSetDTO = Column(Integer)


class GLPeriodCloseBroughtInfo(Base):
    __tablename__ = 'GL_PeriodCloseBroughtInfo'

    code = Column(Unicode(30))
    name = Column(Unicode(200))
    createdtime = Column(String(19, u'Chinese_PRC_CI_AS'))
    sequencenumber = Column(Integer)
    ts = Column(TIMESTAMP, nullable=False)
    updated = Column(String(19, u'Chinese_PRC_CI_AS'))
    updatedBy = Column(Unicode(32))
    id = Column(Integer, primary_key=True)
    idaccount = Column(Integer)
    idPeriodCloseInfoDTO = Column(Integer)


class GLPeriodCloseInfo(Base):
    __tablename__ = 'GL_PeriodCloseInfo'

    code = Column(Unicode(30))
    name = Column(Unicode(200))
    doccount = Column(Integer, server_default=text("((0))"))
    entrycount = Column(Integer, server_default=text("((0))"))
    createdtime = Column(String(19, u'Chinese_PRC_CI_AS'))
    sequencenumber = Column(Integer)
    ts = Column(TIMESTAMP, nullable=False)
    updated = Column(String(19, u'Chinese_PRC_CI_AS'))
    updatedBy = Column(Unicode(32))
    id = Column(Integer, primary_key=True)


class GLPeriodCloseWorkLoadInfo(Base):
    __tablename__ = 'GL_PeriodCloseWorkLoadInfo'

    code = Column(Unicode(30))
    name = Column(Unicode(200))
    doccount = Column(Integer, server_default=text("((0))"))
    entrycount = Column(Integer, server_default=text("((0))"))
    createdtime = Column(String(19, u'Chinese_PRC_CI_AS'))
    sequencenumber = Column(Integer)
    ts = Column(TIMESTAMP, nullable=False)
    updated = Column(String(19, u'Chinese_PRC_CI_AS'))
    updatedBy = Column(Unicode(32))
    id = Column(Integer, primary_key=True)
    iddoctype = Column(Integer)
    idPeriodCloseInfoDTO = Column(Integer)


class GLPeriodLossProfitTransform(Base):
    __tablename__ = 'GL_PeriodLossProfitTransform'

    code = Column(Unicode(30))
    name = Column(Unicode(200))
    iscontain = Column(Integer)
    issingletransform = Column(Integer)
    ts = Column(TIMESTAMP, nullable=False)
    updated = Column(String(19, u'Chinese_PRC_CI_AS'))
    updatedBy = Column(Unicode(32))
    ismergeaccount = Column(Integer)
    id = Column(Integer, primary_key=True)
    idprofitaccount = Column(Integer)
    iddoctype = Column(Integer)
    iincomeexpencesetype = Column(Integer)
    settype = Column(Integer)
    idperiod = Column(Integer)


class GLPeriodLossProfitTransformDetail(Base):
    __tablename__ = 'GL_PeriodLossProfitTransformDetail'

    code = Column(Unicode(30))
    name = Column(Unicode(200))
    istransform = Column(Integer)
    ts = Column(TIMESTAMP, nullable=False)
    updated = Column(String(19, u'Chinese_PRC_CI_AS'))
    updatedBy = Column(Unicode(32))
    id = Column(Integer, primary_key=True)
    idlossaccount = Column(Integer)
    idprofitaccount = Column(Integer)
    idPeriodLossProfitTransFormDTO = Column(Integer)


class GLReferenceAuxiliaryInfo(Base):
    __tablename__ = 'GL_ReferenceAuxiliaryInfo'

    code = Column(Unicode(30))
    name = Column(Unicode(200))
    billno = Column(Unicode(50))
    billdate = Column(String(19, u'Chinese_PRC_CI_AS'))
    bizdate = Column(String(19, u'Chinese_PRC_CI_AS'))
    bizno = Column(Unicode(50))
    duedate = Column(String(19, u'Chinese_PRC_CI_AS'))
    origamount = Column(Numeric(28, 14))
    amount = Column(Numeric(28, 14))
    quantity = Column(Numeric(28, 14))
    price = Column(Numeric(28, 14))
    createdtime = Column(String(19, u'Chinese_PRC_CI_AS'))
    sequencenumber = Column(Integer)
    ts = Column(TIMESTAMP, nullable=False)
    updated = Column(String(19, u'Chinese_PRC_CI_AS'))
    updatedBy = Column(Unicode(32))
    unit = Column(Unicode(200))
    exchangerate = Column(Numeric(28, 14))
    id = Column(Integer, primary_key=True)
    idaccount = Column(Integer)
    idbankAccount = Column(Integer)
    idcurrency = Column(Integer)
    idauxAccDepartment = Column(Integer)
    idauxAccInventory = Column(Integer)
    idauxAccCustomer = Column(Integer)
    idauxAccSupplier = Column(Integer)
    idauxAccPerson = Column(Integer)
    idclerk = Column(Integer)
    idauxAccProject = Column(Integer)
    idsettlestyle = Column(Integer)
    dcdirection = Column(Integer)
    idexauxacc1 = Column(Integer)
    idexauxacc10 = Column(Integer)
    idexauxacc2 = Column(Integer)
    idexauxacc3 = Column(Integer)
    idexauxacc4 = Column(Integer)
    idexauxacc5 = Column(Integer)
    idexauxacc6 = Column(Integer)
    idexauxacc7 = Column(Integer)
    idexauxacc8 = Column(Integer)
    idexauxacc9 = Column(Integer)
    ReferenceDocId = Column(Integer)
    idReferenceEntryDTO = Column(Integer)


class GLReferenceCashFlowInfo(Base):
    __tablename__ = 'GL_ReferenceCashFlowInfo'

    code = Column(Unicode(30))
    name = Column(Unicode(200))
    amount = Column(Numeric(28, 14))
    createdtime = Column(String(19, u'Chinese_PRC_CI_AS'))
    sequencenumber = Column(Integer)
    ts = Column(TIMESTAMP, nullable=False)
    updated = Column(String(19, u'Chinese_PRC_CI_AS'))
    updatedBy = Column(Unicode(32))
    accountcode = Column(Unicode(200))
    accountname = Column(Unicode(200))
    ownerEntryNo = Column(Integer)
    mapEntryNo = Column(Integer)
    id = Column(Integer, primary_key=True)
    idaccount = Column(Integer)
    idcashflowitem = Column(Integer)
    idcurrency = Column(Integer)
    idReferenceDocDTO = Column(Integer)


class GLReferenceDoc(Base):
    __tablename__ = 'GL_ReferenceDoc'

    code = Column(Unicode(30))
    name = Column(Unicode(200))
    attachedvouchernum = Column(Integer)
    docno = Column(Unicode(50))
    docclass = Column(Unicode(50))
    accountingperiod = Column(Integer)
    docid = Column(Unicode(50))
    accountingyear = Column(Integer)
    memo = Column(Unicode(50))
    voucherdate = Column(String(19, u'Chinese_PRC_CI_AS'))
    madedate = Column(String(19, u'Chinese_PRC_CI_AS'))
    maker = Column(Unicode(50))
    auditor = Column(Unicode(50))
    auditeddate = Column(String(19, u'Chinese_PRC_CI_AS'))
    reviser = Column(Unicode(50))
    ismodifiedcode = Column(Integer)
    createdtime = Column(String(19, u'Chinese_PRC_CI_AS'))
    sequencenumber = Column(Integer)
    ts = Column(TIMESTAMP, nullable=False)
    updated = Column(String(19, u'Chinese_PRC_CI_AS'))
    updatedBy = Column(Unicode(32))
    priuserdefnvc1 = Column(Unicode(500))
    priuserdefdecm1 = Column(Numeric(28, 14))
    priuserdefnvc2 = Column(Unicode(500))
    priuserdefdecm2 = Column(Numeric(28, 14))
    priuserdefnvc3 = Column(Unicode(500))
    priuserdefdecm3 = Column(Numeric(28, 14))
    priuserdefnvc4 = Column(Unicode(500))
    priuserdefdecm4 = Column(Numeric(28, 14))
    priuserdefnvc5 = Column(Unicode(500))
    priuserdefdecm5 = Column(Numeric(28, 14))
    priuserdefnvc6 = Column(Unicode(500))
    priuserdefdecm6 = Column(Numeric(28, 14))
    IsCashFlowed = Column(Integer)
    id = Column(Integer, primary_key=True)
    iddoctype = Column(Integer)
    CashFlowedState = Column(Integer)
    referencedoctype = Column(Integer)
    voucherstate = Column(Integer)
    auditorid = Column(Integer)
    makerid = Column(Integer)
    idreferencedocclass = Column(Integer)


t_GL_ReferenceDocClass = Table(
    'GL_ReferenceDocClass', metadata,
    Column('ts', TIMESTAMP, nullable=False),
    Column('Updated', DateTime),
    Column('UpdatedBy', Unicode(32)),
    Column('name', Unicode(50)),
    Column('code', Unicode(32), unique=True),
    Column('madeDate', String(19, u'Chinese_PRC_CI_AS')),
    Column('createdTime', String(19, u'Chinese_PRC_CI_AS')),
    Column('id', Integer, nullable=False)
)


class GLReferenceEntry(Base):
    __tablename__ = 'GL_ReferenceEntry'

    code = Column(Unicode(30))
    name = Column(Unicode(200))
    summary = Column(Unicode(200))
    exchangerate = Column(Numeric(28, 14))
    origamountdr = Column(Numeric(28, 14))
    origamountcr = Column(Numeric(28, 14))
    amountdr = Column(Numeric(28, 14))
    amountcr = Column(Numeric(28, 14))
    quantitydr = Column(Numeric(28, 14))
    quantitycr = Column(Numeric(28, 14))
    price = Column(Numeric(28, 14))
    createdtime = Column(String(19, u'Chinese_PRC_CI_AS'))
    sequencenumber = Column(Integer)
    ts = Column(TIMESTAMP, nullable=False)
    updated = Column(String(19, u'Chinese_PRC_CI_AS'))
    updatedBy = Column(Unicode(32))
    priuserdefnvc1 = Column(Unicode(500))
    priuserdefdecm1 = Column(Numeric(28, 14))
    priuserdefnvc2 = Column(Unicode(500))
    priuserdefdecm2 = Column(Numeric(28, 14))
    priuserdefnvc3 = Column(Unicode(500))
    priuserdefdecm3 = Column(Numeric(28, 14))
    priuserdefnvc4 = Column(Unicode(500))
    priuserdefdecm4 = Column(Numeric(28, 14))
    accountcode = Column(Unicode(200))
    accountname = Column(Unicode(200))
    AuxiliaryItems = Column(Unicode(200))
    id = Column(Integer, primary_key=True)
    idaccount = Column(Integer)
    idcurrency = Column(Integer)
    idReferenceDocDTO = Column(Integer)


class GLSrcVoucherInfo(Base):
    __tablename__ = 'GL_SrcVoucherInfo'

    code = Column(Unicode(30))
    name = Column(Unicode(200))
    createdtime = Column(String(19, u'Chinese_PRC_CI_AS'))
    sequencenumber = Column(Integer)
    ts = Column(TIMESTAMP, nullable=False)
    updated = Column(String(19, u'Chinese_PRC_CI_AS'))
    updatedBy = Column(Unicode(32))
    srcVoucherTimeStamp = Column(Unicode(200))
    srcVoucherNo = Column(Unicode(200))
    srcVoucherDate = Column(String(19, u'Chinese_PRC_CI_AS'))
    id = Column(Integer, primary_key=True)
    idSrcBusiType = Column(Integer)
    srcvoucherid = Column(Integer)
    carryforwardtype = Column(Integer)
    idDocDTO = Column(Integer)
    idSrcVoucherType = Column(Integer)
    idTransactionDocDTO = Column(Integer)


class GLSummarySet(Base):
    __tablename__ = 'GL_SummarySet'

    ts = Column(TIMESTAMP, nullable=False)
    updatedBy = Column(Unicode(32))
    updated = Column(String(19, u'Chinese_PRC_CI_AS'))
    name = Column(Unicode(200), nullable=False)
    code = Column(Unicode(32))
    isVisible = Column(Integer)
    orderIndex = Column(Integer)
    defaultOrderIndex = Column(Integer)
    summarySetType = Column(Unicode(50))
    id = Column(Integer, primary_key=True)
    summarySet = Column(Integer)


class GLUserdefinedtransform(Base):
    __tablename__ = 'GL_Userdefinedtransform'

    code = Column(Unicode(30))
    name = Column(Unicode(200))
    createdtime = Column(String(19, u'Chinese_PRC_CI_AS'))
    sequencenumber = Column(Integer)
    ts = Column(TIMESTAMP, nullable=False)
    updated = Column(String(19, u'Chinese_PRC_CI_AS'))
    updatedBy = Column(Unicode(32))
    id = Column(Integer, primary_key=True)
    iddoctype = Column(Integer)
    transformType = Column(Integer)
    voucherstate = Column(Integer)


class GLUserdefinedtransformdetail(Base):
    __tablename__ = 'GL_Userdefinedtransformdetail'

    summary = Column(Unicode(200))
    accountcode = Column(Unicode(50))
    formula = Column(Unicode(1000))
    amountformula = Column(Unicode(1000))
    origformula = Column(Unicode(1000))
    rate = Column(Numeric(28, 14))
    createdtime = Column(String(19, u'Chinese_PRC_CI_AS'))
    sequencenumber = Column(Integer)
    ts = Column(TIMESTAMP, nullable=False)
    updated = Column(String(19, u'Chinese_PRC_CI_AS'))
    updatedBy = Column(Unicode(32))
    exAuxAccCollection = Column(Unicode(500))
    FormulaAuxAccType = Column(Integer)
    AuxXMLHideValue = Column(Unicode(2000))
    code = Column(Unicode(30))
    id = Column(Integer, primary_key=True)
    idcurrency = Column(Integer)
    idauxAccDepartment = Column(Integer)
    idauxAccInventory = Column(Integer)
    idauxAccCustomer = Column(Integer)
    idauxAccSupplier = Column(Integer)
    idauxAccPerson = Column(Integer)
    idauxAccProject = Column(Integer)
    direction = Column(Integer)
    Method = Column(Integer)
    idexauxacc1 = Column(Integer)
    idexauxacc10 = Column(Integer)
    idexauxacc2 = Column(Integer)
    idexauxacc3 = Column(Integer)
    idexauxacc4 = Column(Integer)
    idexauxacc5 = Column(Integer)
    idexauxacc6 = Column(Integer)
    idexauxacc7 = Column(Integer)
    idexauxacc8 = Column(Integer)
    idexauxacc9 = Column(Integer)
    idUserDefinedTransformDTO = Column(Integer)


class GLWriteOffHistory(Base):
    __tablename__ = 'GL_WriteOffHistory'

    code = Column(Unicode(30))
    name = Column(Unicode(200))
    writeoffbatch = Column(Integer)
    writeoffno = Column(Integer)
    writeoffdate = Column(String(19, u'Chinese_PRC_CI_AS'))
    writeofforigamount = Column(Numeric(28, 14))
    writeoffamount = Column(Numeric(28, 14))
    writeoffer = Column(Unicode(50))
    createdtime = Column(String(19, u'Chinese_PRC_CI_AS'))
    sequencenumber = Column(Integer)
    ts = Column(TIMESTAMP, nullable=False)
    updated = Column(String(19, u'Chinese_PRC_CI_AS'))
    updatedBy = Column(Unicode(32))
    iscarriedforwardout = Column(Integer, server_default=text("((0))"))
    iscarriedforwardin = Column(Integer, server_default=text("((0))"))
    id = Column(Integer, primary_key=True)
    writeofftype = Column(Integer)
    idwriteoff = Column(Integer)
    idwriteoffed = Column(Integer)


class GLWriteOffHistoryCache(Base):
    __tablename__ = 'GL_WriteOffHistoryCache'

    code = Column(Unicode(30))
    ts = Column(TIMESTAMP, nullable=False)
    updatedBy = Column(Unicode(32))
    updated = Column(String(19, u'Chinese_PRC_CI_AS'))
    name = Column(Unicode(200), nullable=False)
    writeOffBatch = Column(Unicode(200))
    writeOffNo = Column(Unicode(200))
    writeOffDate = Column(String(19, u'Chinese_PRC_CI_AS'))
    docMadeDate = Column(String(19, u'Chinese_PRC_CI_AS'))
    bizDate = Column(String(19, u'Chinese_PRC_CI_AS'))
    bizNo = Column(Unicode(200))
    summary = Column(Unicode(200))
    writeOffOrigAmountDr = Column(Numeric(28, 14))
    writeOffAmountDr = Column(Numeric(28, 14))
    writeOffOrigAmountCr = Column(Numeric(28, 14))
    writeOffAmountCr = Column(Numeric(28, 14))
    writeOffer = Column(Unicode(200))
    docSignNo = Column(Unicode(200))
    id = Column(Integer, primary_key=True)
    idCurrency = Column(Integer)
    idauxAccDepartment = Column(Integer)
    idauxAccInventory = Column(Integer)
    idauxAccCustomer = Column(Integer)
    idauxAccSupplier = Column(Integer)
    idauxAccPerson = Column(Integer)
    idauxAccProject = Column(Integer)
    idExAuxAcc1 = Column(Integer)
    idExAuxAcc10 = Column(Integer)
    idExAuxAcc2 = Column(Integer)
    idExAuxAcc3 = Column(Integer)
    idExAuxAcc4 = Column(Integer)
    idExAuxAcc5 = Column(Integer)
    idExAuxAcc6 = Column(Integer)
    idExAuxAcc7 = Column(Integer)
    idExAuxAcc8 = Column(Integer)
    idExAuxAcc9 = Column(Integer)
    idWriteOffHistory = Column(Integer)


class GLWriteOffJournal(Base):
    __tablename__ = 'GL_WriteOffJournal'

    code = Column(Unicode(30))
    name = Column(Unicode(200))
    docmadedate = Column(String(19, u'Chinese_PRC_CI_AS'))
    bizno = Column(Unicode(50))
    bizdate = Column(String(19, u'Chinese_PRC_CI_AS'))
    origamount = Column(Numeric(28, 14))
    amount = Column(Numeric(28, 14))
    quantity = Column(Numeric(28, 14))
    writeoffedorigamount = Column(Numeric(28, 14))
    price = Column(Numeric(28, 14))
    writeoffedamount = Column(Numeric(28, 14))
    writeoffableorigamount = Column(Numeric(28, 14))
    writeoffableamount = Column(Numeric(28, 14))
    iscarriedforwardout = Column(Integer, server_default=text("((0))"))
    iscarriedforwardin = Column(Integer, server_default=text("((0))"))
    ts = Column(TIMESTAMP, nullable=False)
    updated = Column(String(19, u'Chinese_PRC_CI_AS'))
    updatedBy = Column(Unicode(32))
    summary = Column(Unicode(200))
    docno = Column(Unicode(200))
    billNo = Column(Unicode(200))
    billDate = Column(String(19, u'Chinese_PRC_CI_AS'))
    dueDate = Column(String(19, u'Chinese_PRC_CI_AS'))
    id = Column(Integer, primary_key=True)
    idaccount = Column(Integer)
    idcurrency = Column(Integer, nullable=False, server_default=text("((0))"))
    idauxAccDepartment = Column(Integer)
    iddocType = Column(Integer)
    idauxAccInventory = Column(Integer)
    idauxAccCustomer = Column(Integer)
    idauxAccSupplier = Column(Integer)
    idauxAccPerson = Column(Integer)
    idclerk = Column(Integer)
    idauxaccproject = Column(Integer)
    dcdirection = Column(Integer)
    writeoffjournaltype = Column(Integer)
    idauxperiodbegindetail = Column(Integer)
    idexauxacc1 = Column(Integer)
    idexauxacc10 = Column(Integer)
    idexauxacc2 = Column(Integer)
    idexauxacc3 = Column(Integer)
    idexauxacc4 = Column(Integer)
    idexauxacc5 = Column(Integer)
    idexauxacc6 = Column(Integer)
    idexauxacc7 = Column(Integer)
    idexauxacc8 = Column(Integer)
    idexauxacc9 = Column(Integer)
    idjournal = Column(Integer)


t_MB_EntInfo = Table(
    'MB_EntInfo', metadata,
    Column('entId', String(50, u'Chinese_PRC_CI_AS'), nullable=False),
    Column('manager', String(50, u'Chinese_PRC_CI_AS'), nullable=False),
    Column('adminPwd', String(50, u'Chinese_PRC_CI_AS'), nullable=False)
)


t_MB_SyncPartnerAddress = Table(
    'MB_SyncPartnerAddress', metadata,
    Column('partnerTs', BINARY(8), nullable=False),
    Column('partnerAddressId', Integer, nullable=False, server_default=text("((0))")),
    Column('partnerId', Integer, nullable=False, server_default=text("((0))")),
    Column('userId', Integer, nullable=False, server_default=text("((0))"))
)


class MEIntegralAdjust(Base):
    __tablename__ = 'ME_IntegralAdjust'

    code = Column(Unicode(30))
    name = Column(Unicode(200))
    adjustintegral = Column(Integer)
    adjustreason = Column(Unicode(50))
    adjustdate = Column(String(19, u'Chinese_PRC_CI_AS'))
    ts = Column(TIMESTAMP, nullable=False)
    updated = Column(String(19, u'Chinese_PRC_CI_AS'))
    updatedBy = Column(Unicode(32))
    id = Column(Integer, primary_key=True)
    idmember = Column(Integer)
    adjustreasonid = Column(Integer)


class MEIntegralClear(Base):
    __tablename__ = 'ME_IntegralClear'

    code = Column(Unicode(30))
    name = Column(Unicode(200))
    opratedate = Column(String(19, u'Chinese_PRC_CI_AS'))
    cleardate = Column(String(19, u'Chinese_PRC_CI_AS'))
    clearreason = Column(String(50, u'Chinese_PRC_CI_AS'))
    integralbalancecleardate = Column(Numeric(28, 14))
    clearintegral = Column(Numeric(28, 14))
    useintegralcurdate = Column(Numeric(28, 14))
    handperson = Column(Unicode(50))
    handpersoncode = Column(Unicode(50))
    ts = Column(TIMESTAMP, nullable=False)
    updated = Column(String(19, u'Chinese_PRC_CI_AS'))
    updatedBy = Column(Unicode(32))
    id = Column(Integer, primary_key=True)
    idmember = Column(Integer)
    idhandperson = Column(Integer)


class MEIntegralForGift(Base):
    __tablename__ = 'ME_IntegralForGift'

    code = Column(Unicode(30))
    name = Column(Unicode(200))
    memberintegral = Column(Numeric(28, 14))
    thistotalintegral = Column(Numeric(28, 14))
    integralbalance = Column(Numeric(28, 14))
    autooutstock = Column(Integer)
    docno = Column(Unicode(36))
    docclass = Column(Unicode(36))
    accountingperiod = Column(Integer)
    docid = Column(Unicode(36))
    accountingyear = Column(Integer)
    memo = Column(Unicode(200))
    voucherdate = Column(String(19, u'Chinese_PRC_CI_AS'))
    madedate = Column(String(19, u'Chinese_PRC_CI_AS'))
    maker = Column(Unicode(50))
    auditor = Column(Unicode(50))
    auditeddate = Column(String(19, u'Chinese_PRC_CI_AS'))
    reviser = Column(Unicode(50))
    iscarriedforwardout = Column(Integer)
    iscarriedforwardin = Column(Integer)
    ismodifiedcode = Column(Integer)
    createdtime = Column(String(19, u'Chinese_PRC_CI_AS'))
    sequencenumber = Column(Integer)
    ts = Column(TIMESTAMP, nullable=False)
    updated = Column(String(19, u'Chinese_PRC_CI_AS'))
    updatedBy = Column(Unicode(32))
    PrintCount = Column(Integer)
    id = Column(Integer, primary_key=True)
    idmember = Column(Integer)
    idmemberType = Column(Integer)
    idstore = Column(Integer)
    idmarketingOrgan = Column(Integer)
    idpartner = Column(Integer)
    idwarehouse = Column(Integer)
    outstockstate = Column(Integer)
    voucherstate = Column(Integer)
    auditorid = Column(Integer)
    makerid = Column(Integer)


class MEIntegralForGiftSetting(Base):
    __tablename__ = 'ME_IntegralForGiftSetting'

    code = Column(Unicode(30))
    name = Column(Unicode(200))
    exchangeintegral = Column(Integer)
    exchangebegindate = Column(String(19, u'Chinese_PRC_CI_AS'))
    exchangeenddate = Column(String(19, u'Chinese_PRC_CI_AS'))
    iscarriedforwardout = Column(Integer)
    iscarriedforwardin = Column(Integer)
    ts = Column(TIMESTAMP, nullable=False)
    updated = Column(String(19, u'Chinese_PRC_CI_AS'))
    updatedBy = Column(Unicode(32))
    sequencenumber = Column(Integer)
    id = Column(Integer, primary_key=True)
    idinventory = Column(Integer)
    idinventoryprice = Column(Integer)
    idunit = Column(Integer)
    idwarehouse = Column(Integer)


class MEIntegralForGiftB(Base):
    __tablename__ = 'ME_IntegralForGift_b'

    code = Column(Unicode(30))
    name = Column(Unicode(200))
    inventorybarcode = Column(Unicode(200))
    quantity = Column(Numeric(28, 14))
    needintegral = Column(Numeric(28, 14))
    needtotalintegral = Column(Numeric(28, 14))
    price = Column(Numeric(28, 14))
    amount = Column(Numeric(28, 14))
    existingquantity = Column(Numeric(28, 14))
    createdtime = Column(String(19, u'Chinese_PRC_CI_AS'))
    sequencenumber = Column(Integer)
    ts = Column(TIMESTAMP, nullable=False)
    updated = Column(String(19, u'Chinese_PRC_CI_AS'))
    updatedBy = Column(Unicode(32))
    freeItem0 = Column(Unicode(300))
    freeItem1 = Column(Unicode(300))
    freeItem2 = Column(Unicode(300))
    freeItem3 = Column(Unicode(300))
    freeItem4 = Column(Unicode(300))
    freeItem5 = Column(Unicode(300))
    freeItem6 = Column(Unicode(300))
    freeItem7 = Column(Unicode(300))
    freeItem8 = Column(Unicode(300))
    freeItem9 = Column(Unicode(300))
    id = Column(Integer, primary_key=True)
    idinventory = Column(Integer)
    idunit = Column(Integer)
    idwarehouse = Column(Integer)
    idIntegralForGiftDTO = Column(Integer)


class MEIntegralForStorage(Base):
    __tablename__ = 'ME_IntegralForStorage'

    code = Column(Unicode(30))
    name = Column(Unicode(200))
    docno = Column(Unicode(36))
    docclass = Column(Unicode(36))
    accountingperiod = Column(Integer)
    docid = Column(Unicode(36))
    accountingyear = Column(Integer)
    memo = Column(Unicode(200))
    voucherdate = Column(String(19, u'Chinese_PRC_CI_AS'))
    madedate = Column(String(19, u'Chinese_PRC_CI_AS'))
    maker = Column(Unicode(50))
    auditor = Column(Unicode(50))
    auditeddate = Column(String(19, u'Chinese_PRC_CI_AS'))
    reviser = Column(Unicode(50))
    iscarriedforwardout = Column(Integer)
    iscarriedforwardin = Column(Integer)
    ismodifiedcode = Column(Integer)
    createdtime = Column(String(19, u'Chinese_PRC_CI_AS'))
    sequencenumber = Column(Integer)
    ts = Column(TIMESTAMP, nullable=False)
    updated = Column(String(19, u'Chinese_PRC_CI_AS'))
    updatedBy = Column(Unicode(32))
    PrintCount = Column(Integer)
    priuserdefnvc1 = Column(Unicode(100))
    priuserdefdecm1 = Column(Numeric(28, 14))
    priuserdefnvc2 = Column(Unicode(100))
    priuserdefdecm2 = Column(Numeric(28, 14))
    priuserdefnvc3 = Column(Unicode(100))
    priuserdefdecm3 = Column(Numeric(28, 14))
    priuserdefnvc4 = Column(Unicode(100))
    priuserdefdecm4 = Column(Numeric(28, 14))
    priuserdefnvc5 = Column(Unicode(100))
    priuserdefdecm5 = Column(Numeric(28, 14))
    priuserdefnvc6 = Column(Unicode(100))
    priuserdefdecm6 = Column(Numeric(28, 14))
    pubuserdefnvc1 = Column(Unicode(100))
    pubuserdefdecm1 = Column(Numeric(28, 14))
    pubuserdefnvc2 = Column(Unicode(100))
    pubuserdefdecm2 = Column(Numeric(28, 14))
    pubuserdefnvc3 = Column(Unicode(100))
    pubuserdefdecm3 = Column(Numeric(28, 14))
    pubuserdefnvc4 = Column(Unicode(100))
    pubuserdefdecm4 = Column(Numeric(28, 14))
    pubuserdefnvc5 = Column(Unicode(100))
    pubuserdefdecm5 = Column(Numeric(28, 14))
    pubuserdefnvc6 = Column(Unicode(100))
    pubuserdefdecm6 = Column(Numeric(28, 14))
    id = Column(Integer, primary_key=True)
    idstore = Column(Integer)
    idcustomer = Column(Integer)
    poststate = Column(Integer)
    voucherstate = Column(Integer)
    auditorid = Column(Integer)
    makerid = Column(Integer)


class MEIntegralForStorageB(Base):
    __tablename__ = 'ME_IntegralForStorage_b'

    code = Column(Unicode(30))
    name = Column(Unicode(200))
    balanceintegralbefore = Column(Numeric(28, 14))
    balancestoragebefore = Column(Numeric(28, 14))
    balanceinteforstoragebefore = Column(Numeric(28, 14))
    forstorageintegral = Column(Numeric(28, 14))
    forstorageamount = Column(Numeric(28, 14))
    balanceintegralafter = Column(Numeric(28, 14))
    balancestorageafter = Column(Numeric(28, 14))
    balanceinteforstorageafter = Column(Numeric(28, 14))
    createdtime = Column(String(19, u'Chinese_PRC_CI_AS'))
    sequencenumber = Column(Integer)
    ts = Column(TIMESTAMP, nullable=False)
    updated = Column(String(19, u'Chinese_PRC_CI_AS'))
    updatedBy = Column(Unicode(32))
    priuserdefnvc1 = Column(Unicode(100))
    priuserdefdecm1 = Column(Numeric(28, 14))
    priuserdefnvc2 = Column(Unicode(100))
    priuserdefdecm2 = Column(Numeric(28, 14))
    priuserdefnvc3 = Column(Unicode(100))
    priuserdefdecm3 = Column(Numeric(28, 14))
    priuserdefnvc4 = Column(Unicode(100))
    priuserdefdecm4 = Column(Numeric(28, 14))
    pubuserdefnvc1 = Column(Unicode(100))
    pubuserdefdecm1 = Column(Numeric(28, 14))
    pubuserdefnvc2 = Column(Unicode(100))
    pubuserdefdecm2 = Column(Numeric(28, 14))
    pubuserdefnvc3 = Column(Unicode(100))
    pubuserdefdecm3 = Column(Numeric(28, 14))
    pubuserdefnvc4 = Column(Unicode(100))
    pubuserdefdecm4 = Column(Numeric(28, 14))
    id = Column(Integer, primary_key=True)
    idmember = Column(Integer)
    idIntegralForStorageDTO = Column(Integer)


class MEIntegralSteadCashSetting(Base):
    __tablename__ = 'ME_IntegralSteadCashSetting'

    code = Column(Unicode(30))
    name = Column(Unicode(200))
    permintegral = Column(Integer)
    steadnyuan = Column(Numeric(28, 14))
    membertype = Column(String(5000, u'Chinese_PRC_CI_AS'))
    minsteadcashintegral = Column(Integer)
    topsteadcashscale = Column(Numeric(28, 14))
    steadcashbegindate = Column(String(19, u'Chinese_PRC_CI_AS'))
    steadcashenddate = Column(String(19, u'Chinese_PRC_CI_AS'))
    iscarriedforwardout = Column(Integer)
    iscarriedforwardin = Column(Integer)
    ts = Column(TIMESTAMP, nullable=False)
    updated = Column(String(19, u'Chinese_PRC_CI_AS'))
    updatedBy = Column(Unicode(32))
    sequencenumber = Column(Integer)
    id = Column(Integer, primary_key=True)


class MEIntegralSteadCashSettingMemberType(Base):
    __tablename__ = 'ME_IntegralSteadCashSetting_MemberType'

    code = Column(Unicode(30))
    name = Column(Unicode(200))
    createdtime = Column(String(19, u'Chinese_PRC_CI_AS'))
    sequencenumber = Column(Integer)
    ts = Column(TIMESTAMP, nullable=False)
    updated = Column(String(19, u'Chinese_PRC_CI_AS'))
    updatedBy = Column(Unicode(32))
    id = Column(Integer, primary_key=True)
    idmembertype = Column(Integer)
    idIntegralSteadCashSettingDTO = Column(Integer)


t_ME_MemberStorage = Table(
    'ME_MemberStorage', metadata,
    Column('code', Unicode(30)),
    Column('name', Unicode(200)),
    Column('cardcode', Unicode(50)),
    Column('memberquantity', Numeric(28, 14)),
    Column('storageamount', Numeric(28, 14)),
    Column('singlestorageamount', Numeric(28, 14)),
    Column('docno', Unicode(36)),
    Column('docclass', Unicode(36)),
    Column('accountingperiod', Integer),
    Column('docid', Unicode(36)),
    Column('accountingyear', Integer),
    Column('memo', Unicode(200)),
    Column('voucherdate', String(19, u'Chinese_PRC_CI_AS')),
    Column('madedate', String(19, u'Chinese_PRC_CI_AS')),
    Column('maker', Unicode(50)),
    Column('auditor', Unicode(50)),
    Column('auditeddate', String(19, u'Chinese_PRC_CI_AS')),
    Column('reviser', Unicode(50)),
    Column('iscarriedforwardout', Integer),
    Column('iscarriedforwardin', Integer),
    Column('ismodifiedcode', Integer),
    Column('createdtime', String(19, u'Chinese_PRC_CI_AS')),
    Column('sequencenumber', Integer),
    Column('ts', TIMESTAMP, nullable=False),
    Column('updated', String(19, u'Chinese_PRC_CI_AS')),
    Column('updatedBy', Unicode(32)),
    Column('integral', Numeric(28, 14)),
    Column('PrintCount', Integer),
    Column('ExternalCode', Unicode(50)),
    Column('id', Integer, nullable=False),
    Column('idintegralmember', Integer),
    Column('idmember', Integer),
    Column('idstore', Integer),
    Column('idcustomer', Integer),
    Column('idsettlecustomer', Integer),
    Column('poststate', Integer),
    Column('voucherstate', Integer),
    Column('auditorid', Integer),
    Column('makerid', Integer)
)


t_ME_MemberStorageDetail_b = Table(
    'ME_MemberStorageDetail_b', metadata,
    Column('code', Unicode(30)),
    Column('name', Unicode(200)),
    Column('totalstorageamount', Numeric(28, 14)),
    Column('balancetotalstorage', Numeric(28, 14)),
    Column('thisstorageamount', Numeric(28, 14)),
    Column('thispresentamount', Numeric(28, 14)),
    Column('thisvalidstorageamount', Numeric(28, 14)),
    Column('fullamount', Numeric(28, 14)),
    Column('storagedetails', Unicode(200)),
    Column('createdtime', String(19, u'Chinese_PRC_CI_AS')),
    Column('sequencenumber', Integer),
    Column('ts', TIMESTAMP, nullable=False),
    Column('updated', String(19, u'Chinese_PRC_CI_AS')),
    Column('updatedBy', Unicode(32)),
    Column('AfterBalanceStorage', Numeric(28, 14)),
    Column('id', Integer, nullable=False),
    Column('idmember', Integer),
    Column('idmembertype', Integer),
    Column('idmembertypebefore', Integer),
    Column('storagetype', Integer),
    Column('idMemberStorageDTO', Integer)
)


t_ME_MemberStorage_Logs = Table(
    'ME_MemberStorage_Logs', metadata,
    Column('ExternalCode', Unicode(50)),
    Column('logtiming', Unicode(50)),
    Column('recorddate', DateTime),
    Column('storageamount', Numeric(28, 14)),
    Column('integralmember', Unicode(200)),
    Column('integral', Numeric(28, 14)),
    Column('maker', Unicode(50)),
    Column('details', Unicode(2000))
)


t_ME_MemberStorage_MutiSettle = Table(
    'ME_MemberStorage_MutiSettle', metadata,
    Column('code', Unicode(30)),
    Column('name', Unicode(200)),
    Column('storageamount', Numeric(28, 14)),
    Column('balancebankaccount', Numeric(28, 14)),
    Column('createdtime', String(19, u'Chinese_PRC_CI_AS')),
    Column('sequencenumber', Integer),
    Column('ts', TIMESTAMP, nullable=False),
    Column('updated', String(19, u'Chinese_PRC_CI_AS')),
    Column('updatedBy', Unicode(32)),
    Column('id', Integer, nullable=False),
    Column('idbankaccount', Integer),
    Column('idsettlestyle', Integer),
    Column('idMemberStorageDTO', Integer)
)


class MEMemberUpgrade(Base):
    __tablename__ = 'ME_MemberUpgrade'

    code = Column(Unicode(30))
    name = Column(Unicode(200))
    newcardcode = Column(Unicode(50))
    handperson = Column(Unicode(50))
    handpersoncode = Column(Unicode(50))
    ts = Column(TIMESTAMP, nullable=False)
    updated = Column(String(19, u'Chinese_PRC_CI_AS'))
    updatedBy = Column(Unicode(32))
    memberts = Column(LargeBinary(8))
    newcode = Column(Unicode(50))
    id = Column(Integer, primary_key=True)
    idmember = Column(Integer)
    idnewmembertype = Column(Integer)
    idhandperson = Column(Integer)
    upgradetype = Column(Integer)


class MEMemberUpgradeSetting(Base):
    __tablename__ = 'ME_MemberUpgradeSetting'

    code = Column(Unicode(30))
    name = Column(Unicode(200))
    upgradecondition = Column(Integer)
    ts = Column(TIMESTAMP, nullable=False)
    updated = Column(String(19, u'Chinese_PRC_CI_AS'))
    updatedBy = Column(Unicode(32))
    LowestTotalConsumAmount = Column(Numeric(28, 14))
    LowestStorageAmount = Column(Numeric(28, 14))
    id = Column(Integer, primary_key=True)
    idaftermemtype = Column(Integer)
    idbeforememtype = Column(Integer)


class MPAvailable(Base):
    __tablename__ = 'MP_Available'

    PurchaseOrderOnWayQuantity = Column(Numeric(28, 14), server_default=text("((0))"))
    PurchaseArrivalQuantity = Column(Numeric(28, 14), server_default=text("((0))"))
    PurchaseForReceiveQuantity = Column(Numeric(28, 14), server_default=text("((0))"))
    OnProducingQuantity = Column(Numeric(28, 14), server_default=text("((0))"))
    ProductForReceiveQuantity = Column(Numeric(28, 14), server_default=text("((0))"))
    ExistingQuantity = Column(Numeric(28, 14), server_default=text("((0))"))
    PurchaseRequisitionQuantity = Column(Numeric(28, 14), server_default=text("((0))"))
    OtherOnWayQuantity = Column(Numeric(28, 14), server_default=text("((0))"))
    TransOnWayQuantity = Column(Numeric(28, 14), server_default=text("((0))"))
    ForSaleOrderQuantity = Column(Numeric(28, 14), server_default=text("((0))"))
    SaleDeliveryQuantity = Column(Numeric(28, 14), server_default=text("((0))"))
    ForSaleDispatchQuantity = Column(Numeric(28, 14), server_default=text("((0))"))
    ProduceForDispatchQuantity = Column(Numeric(28, 14), server_default=text("((0))"))
    MaterialForSendQuantity = Column(Numeric(28, 14), server_default=text("((0))"))
    SafeLowQuantity = Column(Numeric(28, 14), server_default=text("((0))"))
    OtherForDispatchQuantity = Column(Numeric(28, 14), server_default=text("((0))"))
    TransForDispatchQuantity = Column(Numeric(28, 14), server_default=text("((0))"))
    ForStockOrderQuantity = Column(Numeric(28, 14), server_default=text("((0))"))
    IdSku = Column(Integer, primary_key=True, server_default=text("((0))"))


class MPBomRelation(Base):
    __tablename__ = 'MP_BomRelation'

    code = Column(Unicode(30))
    name = Column(Unicode(200))
    createdtime = Column(String(19, u'Chinese_PRC_CI_AS'))
    sequencenumber = Column(Integer)
    ts = Column(TIMESTAMP, nullable=False)
    updated = Column(String(19, u'Chinese_PRC_CI_AS'))
    updatedBy = Column(Unicode(32))
    Level = Column(Integer)
    bomPath = Column(String(1000, u'Chinese_PRC_CI_AS'))
    realLevel = Column(Integer)
    isEnd = Column(Integer)
    id = Column(Integer, primary_key=True)
    IdRealParent = Column(Integer)
    idTop = Column(Integer)
    idBom = Column(Integer)
    idChild = Column(Integer)
    IdInventory = Column(Integer)
    idSku = Column(Integer)


class MPCostAllocationDirectMaterialSumOrder(Base):
    __tablename__ = 'MP_CostAllocationDirectMaterialSumOrder'

    code = Column(Unicode(30))
    name = Column(Unicode(200))
    isnomodify = Column(Unicode(50))
    docno = Column(Unicode(36))
    docclass = Column(Unicode(36))
    docid = Column(Unicode(36))
    accountingperiod = Column(Integer)
    accountingyear = Column(Integer)
    voucherdate = Column(String(19, u'Chinese_PRC_CI_AS'))
    madedate = Column(String(19, u'Chinese_PRC_CI_AS'))
    maker = Column(Unicode(50))
    memo = Column(Unicode(50))
    auditor = Column(Unicode(50))
    auditeddate = Column(String(19, u'Chinese_PRC_CI_AS'))
    reviser = Column(Unicode(50))
    iscarriedforwardout = Column(Integer)
    iscarriedforwardin = Column(Integer)
    ismodifiedcode = Column(Integer)
    createdtime = Column(String(19, u'Chinese_PRC_CI_AS'))
    sequencenumber = Column(Integer)
    rkdcode = Column(Unicode(50))
    jgdcode = Column(Unicode(50))
    ts = Column(TIMESTAMP, nullable=False)
    updated = Column(String(19, u'Chinese_PRC_CI_AS'))
    updatedBy = Column(Unicode(32))
    quantity = Column(Numeric(28, 14))
    id = Column(Integer, primary_key=True)
    idinventory = Column(Integer)
    voucherstate = Column(Integer)
    auditorid = Column(Integer)
    makerid = Column(Integer)
    costallocationorderdetailid = Column(Integer)
    jgdid = Column(Integer)
    rkdid = Column(Integer)


class MPCostAllocationDirectMaterialSumOrderB(Base):
    __tablename__ = 'MP_CostAllocationDirectMaterialSumOrder_b'

    code = Column(Unicode(30))
    name = Column(Unicode(200))
    quantity = Column(Numeric(28, 14))
    nassignedquantity = Column(Numeric(28, 14))
    nassignedcost = Column(Numeric(28, 14))
    assignedquantity = Column(Numeric(28, 14))
    assignedcost = Column(Numeric(28, 14))
    balancequantity = Column(Numeric(28, 14))
    balancecost = Column(Numeric(28, 14))
    origassignedquantity = Column(Numeric(28, 14))
    totalassignedquantity = Column(Numeric(28, 14))
    createdtime = Column(String(19, u'Chinese_PRC_CI_AS'))
    sequencenumber = Column(Integer)
    ckcost = Column(Numeric(28, 14))
    ts = Column(TIMESTAMP, nullable=False)
    updated = Column(String(19, u'Chinese_PRC_CI_AS'))
    updatedBy = Column(Unicode(32))
    priuserdefnvc1 = Column(Unicode(100))
    priuserdefdecm1 = Column(Numeric(28, 14))
    priuserdefnvc2 = Column(Unicode(100))
    priuserdefdecm2 = Column(Numeric(28, 14))
    priuserdefnvc3 = Column(Unicode(100))
    priuserdefdecm3 = Column(Numeric(28, 14))
    priuserdefnvc4 = Column(Unicode(100))
    priuserdefdecm4 = Column(Numeric(28, 14))
    pubuserdefnvc1 = Column(Unicode(100))
    pubuserdefdecm1 = Column(Numeric(28, 14))
    pubuserdefnvc2 = Column(Unicode(100))
    pubuserdefdecm2 = Column(Numeric(28, 14))
    pubuserdefnvc3 = Column(Unicode(100))
    pubuserdefdecm3 = Column(Numeric(28, 14))
    pubuserdefnvc4 = Column(Unicode(100))
    pubuserdefdecm4 = Column(Numeric(28, 14))
    id = Column(Integer, primary_key=True)
    idinventory = Column(Integer)
    idbaseunit = Column(Integer)
    idCostAllocationDirectMaterialSumOrderDTO = Column(Integer)
    ManufactureOrderMaterialDetailId = Column(Integer)


t_MP_CostAllocationDirectMaterialSumOrder_b_tmp = Table(
    'MP_CostAllocationDirectMaterialSumOrder_b_tmp', metadata,
    Column('code', Unicode(30)),
    Column('name', Unicode(200)),
    Column('quantity', Numeric(28, 14)),
    Column('nassignedquantity', Numeric(28, 14)),
    Column('nassignedcost', Numeric(28, 14)),
    Column('assignedquantity', Numeric(28, 14)),
    Column('assignedcost', Numeric(28, 14)),
    Column('balancequantity', Numeric(28, 14)),
    Column('balancecost', Numeric(28, 14)),
    Column('origassignedquantity', Numeric(28, 14)),
    Column('totalassignedquantity', Numeric(28, 14)),
    Column('createdtime', String(19, u'Chinese_PRC_CI_AS')),
    Column('sequencenumber', Integer),
    Column('ckcost', Numeric(28, 14)),
    Column('ts', TIMESTAMP, nullable=False),
    Column('updated', String(19, u'Chinese_PRC_CI_AS')),
    Column('updatedBy', Unicode(32)),
    Column('priuserdefnvc1', Unicode(100)),
    Column('priuserdefdecm1', Numeric(28, 14)),
    Column('priuserdefnvc2', Unicode(100)),
    Column('priuserdefdecm2', Numeric(28, 14)),
    Column('priuserdefnvc3', Unicode(100)),
    Column('priuserdefdecm3', Numeric(28, 14)),
    Column('priuserdefnvc4', Unicode(100)),
    Column('priuserdefdecm4', Numeric(28, 14)),
    Column('pubuserdefnvc1', Unicode(100)),
    Column('pubuserdefdecm1', Numeric(28, 14)),
    Column('pubuserdefnvc2', Unicode(100)),
    Column('pubuserdefdecm2', Numeric(28, 14)),
    Column('pubuserdefnvc3', Unicode(100)),
    Column('pubuserdefdecm3', Numeric(28, 14)),
    Column('pubuserdefnvc4', Unicode(100)),
    Column('pubuserdefdecm4', Numeric(28, 14)),
    Column('isupdated', Integer, server_default=text("((0))")),
    Column('id', Integer, nullable=False),
    Column('idinventory', Integer),
    Column('idbaseunit', Integer),
    Column('CurrUserID', Integer),
    Column('idCostAllocationDirectMaterialSumOrderDTO', Integer),
    Column('ManufactureOrderMaterialDetailId', Integer)
)


class MPCostAllocationDirectMaterialSumOrderS(Base):
    __tablename__ = 'MP_CostAllocationDirectMaterialSumOrder_s'

    code = Column(Unicode(30))
    name = Column(Unicode(200))
    quantity = Column(Numeric(28, 14))
    price = Column(Numeric(28, 14))
    amount = Column(Numeric(28, 14))
    nassignedquantity = Column(Numeric(28, 14))
    nassignedcost = Column(Numeric(28, 14))
    assignedquantity = Column(Numeric(28, 14))
    assignedcost = Column(Numeric(28, 14))
    balancequantity = Column(Numeric(28, 14))
    balancecost = Column(Numeric(28, 14))
    origassignedquantity = Column(Numeric(28, 14))
    totalrdrecordassignedquantity = Column(Numeric(28, 14))
    totalinventoryassignedquantity = Column(Numeric(28, 14))
    createdtime = Column(String(19, u'Chinese_PRC_CI_AS'))
    sequencenumber = Column(Integer)
    ckcost = Column(Numeric(28, 14))
    sourceVoucherCode = Column(Unicode(50))
    sourcevoucherdetailts = Column(LargeBinary(1))
    sourcevoucherts = Column(LargeBinary(1))
    sourcevoucherdate = Column(String(19, u'Chinese_PRC_CI_AS'))
    ts = Column(TIMESTAMP, nullable=False)
    updated = Column(String(19, u'Chinese_PRC_CI_AS'))
    updatedBy = Column(Unicode(32))
    priuserdefnvc1 = Column(Unicode(100))
    priuserdefdecm1 = Column(Numeric(28, 14))
    priuserdefnvc2 = Column(Unicode(100))
    priuserdefdecm2 = Column(Numeric(28, 14))
    priuserdefnvc3 = Column(Unicode(100))
    priuserdefdecm3 = Column(Numeric(28, 14))
    priuserdefnvc4 = Column(Unicode(100))
    priuserdefdecm4 = Column(Numeric(28, 14))
    pubuserdefnvc1 = Column(Unicode(100))
    pubuserdefdecm1 = Column(Numeric(28, 14))
    pubuserdefnvc2 = Column(Unicode(100))
    pubuserdefdecm2 = Column(Numeric(28, 14))
    pubuserdefnvc3 = Column(Unicode(100))
    pubuserdefdecm3 = Column(Numeric(28, 14))
    pubuserdefnvc4 = Column(Unicode(100))
    pubuserdefdecm4 = Column(Numeric(28, 14))
    id = Column(Integer, primary_key=True)
    idinventory = Column(Integer)
    idbaseunit = Column(Integer)
    voucherId = Column(Integer)
    idCostAllocationDirectMaterialSumDetailDTO = Column(Integer)
    sourceVoucherId = Column(Integer)
    sourceVoucherDetailId = Column(Integer)


t_MP_CostAllocationDirectMaterialSumOrder_s_tmp = Table(
    'MP_CostAllocationDirectMaterialSumOrder_s_tmp', metadata,
    Column('code', Unicode(30)),
    Column('name', Unicode(200)),
    Column('quantity', Numeric(28, 14)),
    Column('price', Numeric(28, 14)),
    Column('amount', Numeric(28, 14)),
    Column('nassignedquantity', Numeric(28, 14)),
    Column('nassignedcost', Numeric(28, 14)),
    Column('assignedquantity', Numeric(28, 14)),
    Column('assignedcost', Numeric(28, 14)),
    Column('balancequantity', Numeric(28, 14)),
    Column('balancecost', Numeric(28, 14)),
    Column('origassignedquantity', Numeric(28, 14)),
    Column('totalrdrecordassignedquantity', Numeric(28, 14)),
    Column('totalinventoryassignedquantity', Numeric(28, 14)),
    Column('createdtime', String(19, u'Chinese_PRC_CI_AS')),
    Column('sequencenumber', Integer),
    Column('ckcost', Numeric(28, 14)),
    Column('sourceVoucherCode', Unicode(50)),
    Column('sourcevoucherdetailts', LargeBinary(1)),
    Column('sourcevoucherts', LargeBinary(1)),
    Column('sourcevoucherdate', String(19, u'Chinese_PRC_CI_AS')),
    Column('ts', TIMESTAMP, nullable=False),
    Column('updated', String(19, u'Chinese_PRC_CI_AS')),
    Column('updatedBy', Unicode(32)),
    Column('priuserdefnvc1', Unicode(100)),
    Column('priuserdefdecm1', Numeric(28, 14)),
    Column('priuserdefnvc2', Unicode(100)),
    Column('priuserdefdecm2', Numeric(28, 14)),
    Column('priuserdefnvc3', Unicode(100)),
    Column('priuserdefdecm3', Numeric(28, 14)),
    Column('priuserdefnvc4', Unicode(100)),
    Column('priuserdefdecm4', Numeric(28, 14)),
    Column('pubuserdefnvc1', Unicode(100)),
    Column('pubuserdefdecm1', Numeric(28, 14)),
    Column('pubuserdefnvc2', Unicode(100)),
    Column('pubuserdefdecm2', Numeric(28, 14)),
    Column('pubuserdefnvc3', Unicode(100)),
    Column('pubuserdefdecm3', Numeric(28, 14)),
    Column('pubuserdefnvc4', Unicode(100)),
    Column('pubuserdefdecm4', Numeric(28, 14)),
    Column('isupdated', Integer, server_default=text("((0))")),
    Column('id', Integer, nullable=False),
    Column('idinventory', Integer),
    Column('idbaseunit', Integer),
    Column('CurrUserID', Integer),
    Column('voucherId', Integer),
    Column('idCostAllocationDirectMaterialSumDetailDTO', Integer),
    Column('sourceVoucherId', Integer),
    Column('sourceVoucherDetailId', Integer)
)


t_MP_CostAllocationDirectMaterialSumOrder_tmp = Table(
    'MP_CostAllocationDirectMaterialSumOrder_tmp', metadata,
    Column('code', Unicode(30)),
    Column('name', Unicode(200)),
    Column('isnomodify', Unicode(50)),
    Column('docno', Unicode(36)),
    Column('docclass', Unicode(36)),
    Column('docid', Unicode(36)),
    Column('accountingperiod', Integer),
    Column('accountingyear', Integer),
    Column('voucherdate', String(19, u'Chinese_PRC_CI_AS')),
    Column('madedate', String(19, u'Chinese_PRC_CI_AS')),
    Column('maker', Unicode(50)),
    Column('memo', Unicode(50)),
    Column('auditor', Unicode(50)),
    Column('auditeddate', String(19, u'Chinese_PRC_CI_AS')),
    Column('reviser', Unicode(50)),
    Column('iscarriedforwardout', Integer),
    Column('iscarriedforwardin', Integer),
    Column('ismodifiedcode', Integer),
    Column('createdtime', String(19, u'Chinese_PRC_CI_AS')),
    Column('sequencenumber', Integer),
    Column('rkdcode', Unicode(50)),
    Column('jgdcode', Unicode(50)),
    Column('ts', TIMESTAMP, nullable=False),
    Column('updated', String(19, u'Chinese_PRC_CI_AS')),
    Column('updatedBy', Unicode(32)),
    Column('quantity', Numeric(28, 14)),
    Column('id', Integer, nullable=False),
    Column('idinventory', Integer),
    Column('voucherstate', Integer),
    Column('auditorid', Integer),
    Column('CurrUserID', Integer),
    Column('makerid', Integer),
    Column('costallocationorderdetailid', Integer),
    Column('jgdid', Integer),
    Column('rkdid', Integer)
)


class MPCostAllocationOrder(Base):
    __tablename__ = 'MP_CostAllocationOrder'

    code = Column(Unicode(30))
    isNoModify = Column(Unicode(50))
    docno = Column(Unicode(36))
    docclass = Column(Unicode(36))
    accountingperiod = Column(Integer)
    docid = Column(Unicode(36))
    accountingyear = Column(Integer)
    memo = Column(Unicode(50))
    voucherdate = Column(String(19, u'Chinese_PRC_CI_AS'))
    madedate = Column(String(19, u'Chinese_PRC_CI_AS'))
    maker = Column(Unicode(50))
    auditor = Column(Unicode(50))
    auditeddate = Column(String(19, u'Chinese_PRC_CI_AS'))
    reviser = Column(Unicode(50))
    iscarriedforwardout = Column(Integer)
    iscarriedforwardin = Column(Integer)
    ismodifiedcode = Column(Integer)
    createdtime = Column(String(19, u'Chinese_PRC_CI_AS'))
    directmaterialcost = Column(Numeric(28, 14))
    indirectmaterialcost = Column(Numeric(28, 14))
    manufacturcost = Column(Numeric(28, 14))
    mancost = Column(Numeric(28, 14))
    consignationcost = Column(Numeric(28, 14))
    othercost = Column(Numeric(28, 14))
    othercost1 = Column(Numeric(28, 14))
    othercost2 = Column(Numeric(28, 14))
    ts = Column(TIMESTAMP, nullable=False)
    updated = Column(String(19, u'Chinese_PRC_CI_AS'))
    updatedBy = Column(Unicode(32))
    priuserdefnvc1 = Column(Unicode(100))
    priuserdefdecm1 = Column(Numeric(28, 14))
    priuserdefnvc2 = Column(Unicode(100))
    priuserdefdecm2 = Column(Numeric(28, 14))
    priuserdefnvc3 = Column(Unicode(100))
    priuserdefdecm3 = Column(Numeric(28, 14))
    priuserdefnvc4 = Column(Unicode(100))
    priuserdefdecm4 = Column(Numeric(28, 14))
    priuserdefnvc5 = Column(Unicode(100))
    priuserdefdecm5 = Column(Numeric(28, 14))
    priuserdefnvc6 = Column(Unicode(100))
    priuserdefdecm6 = Column(Numeric(28, 14))
    pubuserdefnvc1 = Column(Unicode(100))
    pubuserdefdecm1 = Column(Numeric(28, 14))
    pubuserdefnvc2 = Column(Unicode(100))
    pubuserdefdecm2 = Column(Numeric(28, 14))
    pubuserdefnvc3 = Column(Unicode(100))
    pubuserdefdecm3 = Column(Numeric(28, 14))
    pubuserdefnvc4 = Column(Unicode(100))
    pubuserdefdecm4 = Column(Numeric(28, 14))
    pubuserdefnvc5 = Column(Unicode(100))
    pubuserdefdecm5 = Column(Numeric(28, 14))
    pubuserdefnvc6 = Column(Unicode(100))
    pubuserdefdecm6 = Column(Numeric(28, 14))
    PrintCount = Column(Integer)
    id = Column(Integer, primary_key=True)
    idmarketingorgan = Column(Integer)
    idperson = Column(Integer)
    idproject = Column(Integer)
    allocationbasis = Column(Integer)
    costcollectorobject = Column(Integer)
    voucherstate = Column(Integer)
    auditorid = Column(Integer)
    makerid = Column(Integer)


class MPCostAllocationOrderB(Base):
    __tablename__ = 'MP_CostAllocationOrder_b'

    code = Column(Unicode(30))
    sourceVoucherCode = Column(Unicode(50))
    sourcevoucherdetailts = Column(LargeBinary(1))
    sourcevoucherts = Column(LargeBinary(1))
    batch = Column(Unicode(50))
    createdtime = Column(String(19, u'Chinese_PRC_CI_AS'))
    refcost = Column(Numeric(28, 14))
    totalrefcost = Column(Numeric(28, 14))
    quantity = Column(Numeric(28, 14))
    directmaterials = Column(Numeric(28, 14))
    indirectmaterials = Column(Numeric(28, 14))
    manufacturecost = Column(Numeric(28, 14))
    mancost = Column(Numeric(28, 14))
    outsourcingcost = Column(Numeric(28, 14))
    othercost = Column(Numeric(28, 14))
    othercost1 = Column(Numeric(28, 14))
    othercost2 = Column(Numeric(28, 14))
    totalcost = Column(Numeric(28, 14))
    unitcost = Column(Numeric(28, 14))
    jgdcode = Column(Unicode(50))
    rkdcode = Column(Unicode(50))
    ts = Column(TIMESTAMP, nullable=False)
    priuserdefnvc1 = Column(Unicode(100))
    priuserdefdecm1 = Column(Numeric(28, 14))
    priuserdefnvc2 = Column(Unicode(100))
    priuserdefdecm2 = Column(Numeric(28, 14))
    priuserdefnvc3 = Column(Unicode(100))
    priuserdefdecm3 = Column(Numeric(28, 14))
    priuserdefnvc4 = Column(Unicode(100))
    priuserdefdecm4 = Column(Numeric(28, 14))
    pubuserdefnvc1 = Column(Unicode(100))
    pubuserdefdecm1 = Column(Numeric(28, 14))
    pubuserdefnvc2 = Column(Unicode(100))
    pubuserdefdecm2 = Column(Numeric(28, 14))
    pubuserdefnvc3 = Column(Unicode(100))
    pubuserdefdecm3 = Column(Numeric(28, 14))
    pubuserdefnvc4 = Column(Unicode(100))
    pubuserdefdecm4 = Column(Numeric(28, 14))
    id = Column(Integer, primary_key=True)
    idinventory = Column(Integer)
    idproject = Column(Integer)
    idbaseunit = Column(Integer)
    idWarehouse = Column(Integer)
    idCostAllocationOrderDTO = Column(Integer)
    jgdid = Column(Integer)
    jgdDetailId = Column(Integer)
    rkdid = Column(Integer)
    sourceVoucherId = Column(Integer)
    rkdDetailId = Column(Integer)
    sourceVoucherDetailId = Column(Integer)


t_MP_CostAllocationOrder_b_tmp = Table(
    'MP_CostAllocationOrder_b_tmp', metadata,
    Column('id', Integer, nullable=False),
    Column('code', Unicode(30)),
    Column('name', Unicode(200)),
    Column('sourceVoucherCode', Unicode(50)),
    Column('sourcevoucherdetailts', LargeBinary(1)),
    Column('sourcevoucherts', LargeBinary(1)),
    Column('batch', Unicode(50)),
    Column('createdtime', String(19, u'Chinese_PRC_CI_AS')),
    Column('sequencenumber', Integer),
    Column('refcost', Numeric(28, 14)),
    Column('totalrefcost', Numeric(28, 14)),
    Column('quantity', Numeric(28, 14)),
    Column('directmaterials', Numeric(28, 14)),
    Column('indirectmaterials', Numeric(28, 14)),
    Column('manufacturecost', Numeric(28, 14)),
    Column('mancost', Numeric(28, 14)),
    Column('outsourcingcost', Numeric(28, 14)),
    Column('othercost', Numeric(28, 14)),
    Column('othercost1', Numeric(28, 14)),
    Column('othercost2', Numeric(28, 14)),
    Column('totalcost', Numeric(28, 14)),
    Column('unitcost', Numeric(28, 14)),
    Column('jgdcode', Unicode(50)),
    Column('rkdcode', Unicode(50)),
    Column('ts', TIMESTAMP, nullable=False),
    Column('updated', String(19, u'Chinese_PRC_CI_AS')),
    Column('updatedBy', Unicode(32)),
    Column('priuserdefnvc1', Unicode(100)),
    Column('priuserdefdecm1', Numeric(28, 14)),
    Column('priuserdefnvc2', Unicode(100)),
    Column('priuserdefdecm2', Numeric(28, 14)),
    Column('priuserdefnvc3', Unicode(100)),
    Column('priuserdefdecm3', Numeric(28, 14)),
    Column('priuserdefnvc4', Unicode(100)),
    Column('priuserdefdecm4', Numeric(28, 14)),
    Column('pubuserdefnvc1', Unicode(100)),
    Column('pubuserdefdecm1', Numeric(28, 14)),
    Column('pubuserdefnvc2', Unicode(100)),
    Column('pubuserdefdecm2', Numeric(28, 14)),
    Column('pubuserdefnvc3', Unicode(100)),
    Column('pubuserdefdecm3', Numeric(28, 14)),
    Column('pubuserdefnvc4', Unicode(100)),
    Column('pubuserdefdecm4', Numeric(28, 14)),
    Column('idinventory', Integer),
    Column('idproject', Integer),
    Column('idbaseunit', Integer),
    Column('idWarehouse', Integer),
    Column('CurrUserID', Integer),
    Column('idCostAllocationOrderDTO', Integer),
    Column('jgdid', Integer),
    Column('jgdDetailId', Integer),
    Column('rkdid', Integer),
    Column('sourceVoucherId', Integer),
    Column('rkdDetailId', Integer),
    Column('sourceVoucherDetailId', Integer)
)


class MPCostAllocationOrderSrc(Base):
    __tablename__ = 'MP_CostAllocationOrder_src'

    sourceVoucherCode = Column(Unicode(50))
    sourcevoucherdetailts = Column(LargeBinary(8))
    sourcevoucherts = Column(LargeBinary(8))
    batch = Column(Unicode(50))
    createdtime = Column(String(19, u'Chinese_PRC_CI_AS'))
    sequencenumber = Column(Integer)
    refcost = Column(Numeric(28, 14))
    totalrefcost = Column(Numeric(28, 14))
    quantity = Column(Numeric(28, 14))
    jgdcode = Column(Unicode(50))
    rkdcode = Column(Unicode(50))
    ts = Column(TIMESTAMP, nullable=False)
    updated = Column(String(19, u'Chinese_PRC_CI_AS'))
    updatedBy = Column(Unicode(32))
    priuserdefnvc1 = Column(Unicode(100))
    priuserdefdecm1 = Column(Numeric(28, 14))
    priuserdefnvc2 = Column(Unicode(100))
    priuserdefdecm2 = Column(Numeric(28, 14))
    priuserdefnvc3 = Column(Unicode(100))
    priuserdefdecm3 = Column(Numeric(28, 14))
    priuserdefnvc4 = Column(Unicode(100))
    priuserdefdecm4 = Column(Numeric(28, 14))
    pubuserdefnvc1 = Column(Unicode(100))
    pubuserdefdecm1 = Column(Numeric(28, 14))
    pubuserdefnvc2 = Column(Unicode(100))
    pubuserdefdecm2 = Column(Numeric(28, 14))
    pubuserdefnvc3 = Column(Unicode(100))
    pubuserdefdecm3 = Column(Numeric(28, 14))
    pubuserdefnvc4 = Column(Unicode(100))
    pubuserdefdecm4 = Column(Numeric(28, 14))
    id = Column(Integer, primary_key=True)
    idinventory = Column(Integer)
    idproject = Column(Integer)
    idbaseunit = Column(Integer)
    idWarehouse = Column(Integer)
    idCostAllocationOrderDTO = Column(Integer)
    voucherId = Column(Integer)
    idSum = Column(Integer)
    jgdid = Column(Integer)
    jgdDetailId = Column(Integer)
    rkdid = Column(Integer)
    sourceVoucherId = Column(Integer)
    rkdDetailId = Column(Integer)
    sourceVoucherDetailId = Column(Integer)


t_MP_CostAllocationOrder_src_tmp = Table(
    'MP_CostAllocationOrder_src_tmp', metadata,
    Column('sourceVoucherCode', Unicode(50)),
    Column('sourcevoucherdetailts', LargeBinary(8)),
    Column('sourcevoucherts', LargeBinary(8)),
    Column('batch', Unicode(50)),
    Column('createdtime', String(19, u'Chinese_PRC_CI_AS')),
    Column('sequencenumber', Integer),
    Column('refcost', Numeric(28, 14)),
    Column('totalrefcost', Numeric(28, 14)),
    Column('quantity', Numeric(28, 14)),
    Column('jgdcode', Unicode(50)),
    Column('rkdcode', Unicode(50)),
    Column('ts', TIMESTAMP, nullable=False),
    Column('updated', String(19, u'Chinese_PRC_CI_AS')),
    Column('updatedBy', Unicode(32)),
    Column('priuserdefnvc1', Unicode(100)),
    Column('priuserdefdecm1', Numeric(28, 14)),
    Column('priuserdefnvc2', Unicode(100)),
    Column('priuserdefdecm2', Numeric(28, 14)),
    Column('priuserdefnvc3', Unicode(100)),
    Column('priuserdefdecm3', Numeric(28, 14)),
    Column('priuserdefnvc4', Unicode(100)),
    Column('priuserdefdecm4', Numeric(28, 14)),
    Column('pubuserdefnvc1', Unicode(100)),
    Column('pubuserdefdecm1', Numeric(28, 14)),
    Column('pubuserdefnvc2', Unicode(100)),
    Column('pubuserdefdecm2', Numeric(28, 14)),
    Column('pubuserdefnvc3', Unicode(100)),
    Column('pubuserdefdecm3', Numeric(28, 14)),
    Column('pubuserdefnvc4', Unicode(100)),
    Column('pubuserdefdecm4', Numeric(28, 14)),
    Column('id', Integer, nullable=False),
    Column('idinventory', Integer),
    Column('idproject', Integer),
    Column('idbaseunit', Integer),
    Column('idWarehouse', Integer),
    Column('CurrUserID', Integer),
    Column('voucherId', Integer),
    Column('idCostAllocationOrderDTO', Integer),
    Column('idSum', Integer),
    Column('jgdid', Integer),
    Column('jgdDetailId', Integer),
    Column('rkdid', Integer),
    Column('sourceVoucherId', Integer),
    Column('rkdDetailId', Integer),
    Column('sourceVoucherDetailId', Integer)
)


t_MP_CostAllocationOrder_tmp = Table(
    'MP_CostAllocationOrder_tmp', metadata,
    Column('code', Unicode(30)),
    Column('name', Unicode(200)),
    Column('isNoModify', Unicode(50)),
    Column('docno', Unicode(36)),
    Column('docclass', Unicode(36)),
    Column('accountingperiod', Integer),
    Column('docid', Unicode(36)),
    Column('accountingyear', Integer),
    Column('memo', Unicode(50)),
    Column('voucherdate', String(19, u'Chinese_PRC_CI_AS')),
    Column('madedate', String(19, u'Chinese_PRC_CI_AS')),
    Column('maker', Unicode(50)),
    Column('auditor', Unicode(50)),
    Column('auditeddate', String(19, u'Chinese_PRC_CI_AS')),
    Column('reviser', Unicode(50)),
    Column('iscarriedforwardout', Integer),
    Column('iscarriedforwardin', Integer),
    Column('ismodifiedcode', Integer),
    Column('createdtime', String(19, u'Chinese_PRC_CI_AS')),
    Column('sequencenumber', Integer),
    Column('directmaterialcost', Numeric(28, 14)),
    Column('indirectmaterialcost', Numeric(28, 14)),
    Column('manufacturcost', Numeric(28, 14)),
    Column('mancost', Numeric(28, 14)),
    Column('consignationcost', Numeric(28, 14)),
    Column('othercost', Numeric(28, 14)),
    Column('othercost1', Numeric(28, 14)),
    Column('othercost2', Numeric(28, 14)),
    Column('ts', TIMESTAMP, nullable=False),
    Column('updated', String(19, u'Chinese_PRC_CI_AS')),
    Column('updatedBy', Unicode(32)),
    Column('priuserdefnvc1', Unicode(100)),
    Column('priuserdefdecm1', Numeric(28, 14)),
    Column('priuserdefnvc2', Unicode(100)),
    Column('priuserdefdecm2', Numeric(28, 14)),
    Column('priuserdefnvc3', Unicode(100)),
    Column('priuserdefdecm3', Numeric(28, 14)),
    Column('priuserdefnvc4', Unicode(100)),
    Column('priuserdefdecm4', Numeric(28, 14)),
    Column('priuserdefnvc5', Unicode(100)),
    Column('priuserdefdecm5', Numeric(28, 14)),
    Column('priuserdefnvc6', Unicode(100)),
    Column('priuserdefdecm6', Numeric(28, 14)),
    Column('pubuserdefnvc1', Unicode(100)),
    Column('pubuserdefdecm1', Numeric(28, 14)),
    Column('pubuserdefnvc2', Unicode(100)),
    Column('pubuserdefdecm2', Numeric(28, 14)),
    Column('pubuserdefnvc3', Unicode(100)),
    Column('pubuserdefdecm3', Numeric(28, 14)),
    Column('pubuserdefnvc4', Unicode(100)),
    Column('pubuserdefdecm4', Numeric(28, 14)),
    Column('pubuserdefnvc5', Unicode(100)),
    Column('pubuserdefdecm5', Numeric(28, 14)),
    Column('pubuserdefnvc6', Unicode(100)),
    Column('pubuserdefdecm6', Numeric(28, 14)),
    Column('PrintCount', Integer),
    Column('id', Integer, nullable=False),
    Column('idmarketingorgan', Integer),
    Column('idperson', Integer),
    Column('idproject', Integer),
    Column('voucherstate', Integer),
    Column('allocationbasis', Integer),
    Column('costcollectorobject', Integer),
    Column('auditorid', Integer),
    Column('CurrUserID', Integer),
    Column('makerid', Integer)
)


t_MP_Cycle_Queue = Table(
    'MP_Cycle_Queue', metadata,
    Column('parentInv', String(40, u'Chinese_PRC_CI_AS')),
    Column('sonInv', String(40, u'Chinese_PRC_CI_AS')),
    Column('SourceParent', String(40, u'Chinese_PRC_CI_AS'))
)


t_MP_Cycle_Queue_Temp = Table(
    'MP_Cycle_Queue_Temp', metadata,
    Column('parentInv', String(40, u'Chinese_PRC_CI_AS')),
    Column('sonInv', String(40, u'Chinese_PRC_CI_AS')),
    Column('SourceParent', String(40, u'Chinese_PRC_CI_AS'))
)


t_MP_Cycle_This = Table(
    'MP_Cycle_This', metadata,
    Column('parentInv', String(40, u'Chinese_PRC_CI_AS')),
    Column('sonInv', String(40, u'Chinese_PRC_CI_AS')),
    Column('SourceParent', String(40, u'Chinese_PRC_CI_AS'))
)


t_MP_DeductAq = Table(
    'MP_DeductAq', metadata,
    Column('DeductQuantity', Numeric(28, 14)),
    Column('IdSku', Integer, nullable=False, server_default=text("((0))"))
)


class MPDeductAqSum(Base):
    __tablename__ = 'MP_DeductAqSum'

    DeductQuantity = Column(Numeric(28, 14))
    IdSku = Column(Integer, primary_key=True, server_default=text("((0))"))


class MPIntendSaleOrder(Base):
    __tablename__ = 'MP_IntendSaleOrder'

    code = Column(Unicode(30))
    name = Column(Unicode(200))
    demandingDate = Column(String(19, u'Chinese_PRC_CI_AS'))
    memo = Column(Unicode(200))
    voucherDate = Column(String(19, u'Chinese_PRC_CI_AS'))
    maker = Column(Unicode(50))
    madeDate = Column(String(19, u'Chinese_PRC_CI_AS'))
    auditor = Column(Unicode(50))
    reviser = Column(Unicode(50))
    auditedDate = Column(String(19, u'Chinese_PRC_CI_AS'))
    isCarriedForwardOut = Column(Integer)
    isCarriedForwardIn = Column(Integer)
    isModifiedCode = Column(Integer)
    docNo = Column(Unicode(36))
    docClass = Column(Unicode(36))
    accountingPeriod = Column(Integer)
    docId = Column(Unicode(36))
    accountingYear = Column(Integer)
    createdTime = Column(String(19, u'Chinese_PRC_CI_AS'))
    sequenceNumber = Column(Integer)
    ts = Column(TIMESTAMP, nullable=False)
    updated = Column(String(19, u'Chinese_PRC_CI_AS'))
    updatedBy = Column(Unicode(32))
    priuserdefnvc1 = Column(Unicode(500))
    priuserdefdecm1 = Column(Numeric(28, 14))
    priuserdefnvc2 = Column(Unicode(500))
    priuserdefdecm2 = Column(Numeric(28, 14))
    priuserdefnvc3 = Column(Unicode(500))
    priuserdefdecm3 = Column(Numeric(28, 14))
    priuserdefnvc4 = Column(Unicode(500))
    priuserdefdecm4 = Column(Numeric(28, 14))
    priuserdefnvc5 = Column(Unicode(500))
    priuserdefdecm5 = Column(Numeric(28, 14))
    priuserdefnvc6 = Column(Unicode(500))
    priuserdefdecm6 = Column(Numeric(28, 14))
    pubuserdefnvc1 = Column(Unicode(500))
    pubuserdefdecm1 = Column(Numeric(28, 14))
    pubuserdefnvc2 = Column(Unicode(500))
    pubuserdefdecm2 = Column(Numeric(28, 14))
    pubuserdefnvc3 = Column(Unicode(500))
    pubuserdefdecm3 = Column(Numeric(28, 14))
    pubuserdefnvc4 = Column(Unicode(500))
    pubuserdefdecm4 = Column(Numeric(28, 14))
    pubuserdefnvc5 = Column(Unicode(500))
    pubuserdefdecm5 = Column(Numeric(28, 14))
    pubuserdefnvc6 = Column(Unicode(500))
    pubuserdefdecm6 = Column(Numeric(28, 14))
    PrintCount = Column(Integer)
    ID = Column(Integer, primary_key=True)
    idbusitype = Column(Integer)
    iddepartment = Column(Integer)
    idMarketingOrgan = Column(Integer)
    idproject = Column(Integer)
    voucherState = Column(Integer)
    auditorId = Column(Integer)
    makerId = Column(Integer)


class MPIntendSaleOrderB(Base):
    __tablename__ = 'MP_IntendSaleOrder_b'

    code = Column(Unicode(30))
    name = Column(Unicode(200))
    compositionQuantity = Column(Unicode(50))
    inventoryBarCode = Column(Unicode(128))
    quantity = Column(Numeric(28, 14))
    quantity2 = Column(Numeric(28, 14))
    baseQuantity = Column(Numeric(28, 14))
    subQuantity = Column(Numeric(28, 14))
    unitExchangeRate = Column(Numeric(28, 14))
    demandingDate = Column(String(19, u'Chinese_PRC_CI_AS'))
    bomType = Column(Unicode(50))
    bomVersion = Column(Unicode(50))
    hasMRP = Column(Integer)
    hasPRA = Column(Integer)
    totalMRPCount = Column(Integer)
    totalPRACount = Column(Integer)
    totalManufactureQuantity = Column(Numeric(28, 14))
    totalManufactureQuantity2 = Column(Numeric(28, 14))
    totalPurchaseQuantity = Column(Numeric(28, 14))
    totalPurchaseQuantity2 = Column(Numeric(28, 14))
    totalExecutedQuantity = Column(Numeric(28, 14))
    totalExecutedQuantity2 = Column(Numeric(28, 14))
    createdTime = Column(String(19, u'Chinese_PRC_CI_AS'))
    sequenceNumber = Column(Integer)
    ts = Column(TIMESTAMP, nullable=False)
    updated = Column(String(19, u'Chinese_PRC_CI_AS'))
    updatedBy = Column(Unicode(32))
    priuserdefnvc1 = Column(Unicode(500))
    priuserdefdecm1 = Column(Numeric(28, 14))
    priuserdefnvc2 = Column(Unicode(500))
    priuserdefdecm2 = Column(Numeric(28, 14))
    priuserdefnvc3 = Column(Unicode(500))
    priuserdefdecm3 = Column(Numeric(28, 14))
    priuserdefnvc4 = Column(Unicode(500))
    priuserdefdecm4 = Column(Numeric(28, 14))
    pubuserdefnvc1 = Column(Unicode(500))
    pubuserdefdecm1 = Column(Numeric(28, 14))
    pubuserdefnvc2 = Column(Unicode(500))
    pubuserdefdecm2 = Column(Numeric(28, 14))
    pubuserdefnvc3 = Column(Unicode(500))
    pubuserdefdecm3 = Column(Numeric(28, 14))
    pubuserdefnvc4 = Column(Unicode(500))
    pubuserdefdecm4 = Column(Numeric(28, 14))
    freeItem0 = Column(Unicode(300))
    freeItem1 = Column(Unicode(300))
    freeItem2 = Column(Unicode(300))
    freeItem3 = Column(Unicode(300))
    freeItem4 = Column(Unicode(300))
    freeItem5 = Column(Unicode(300))
    freeItem6 = Column(Unicode(300))
    freeItem7 = Column(Unicode(300))
    freeItem8 = Column(Unicode(300))
    freeItem9 = Column(Unicode(300))
    ID = Column(Integer, primary_key=True)
    bomId = Column(Integer)
    idbom = Column(Integer)
    idinventory = Column(Integer)
    idproject = Column(Integer)
    idbaseunit = Column(Integer)
    idsubunit = Column(Integer)
    idunit = Column(Integer)
    idunit2 = Column(Integer)
    idIntendSaleOrderDTO = Column(Integer)


class MPInventoryLine(Base):
    __tablename__ = 'MP_InventoryLine'

    Level = Column(Integer)
    InventoryCode = Column(Unicode(32))
    InventoryName = Column(Unicode(200))
    createdtime = Column(String(19, u'Chinese_PRC_CI_AS'), server_default=text("(CONVERT([char](19),getdate(),(120)))"))
    updatedtime = Column(String(19, u'Chinese_PRC_CI_AS'))
    id = Column(Integer, primary_key=True)
    idInventory = Column(Integer)


t_MP_MRPPRA_SourceVoucherDetails = Table(
    'MP_MRPPRA_SourceVoucherDetails', metadata,
    Column('sourceVoucherDetailId', Integer, nullable=False)
)


t_MP_MRPPRA_StopWatch = Table(
    'MP_MRPPRA_StopWatch', metadata,
    Column('code', Unicode(100), nullable=False),
    Column('name', Unicode(50)),
    Column('memo', Unicode(100)),
    Column('elapsed', Integer),
    Column('startTime', DateTime, server_default=text("(getdate())")),
    Column('endTime', DateTime, server_default=text("(getdate())"))
)


class MPManufactureOrder(Base):
    __tablename__ = 'MP_ManufactureOrder'

    code = Column(Unicode(30))
    name = Column(Unicode(200))
    preStartDate = Column(String(19, u'Chinese_PRC_CI_AS'))
    preFinishDate = Column(String(19, u'Chinese_PRC_CI_AS'))
    startDate = Column(String(19, u'Chinese_PRC_CI_AS'))
    finishDate = Column(String(19, u'Chinese_PRC_CI_AS'))
    haveCheckedCost = Column(Integer)
    saleOrderCode = Column(Unicode(30))
    isNoModify = Column(Unicode(200))
    docno = Column(Unicode(36))
    docclass = Column(Unicode(36))
    accountingperiod = Column(Integer)
    docid = Column(Unicode(36))
    accountingyear = Column(Integer)
    memo = Column(Unicode(200))
    voucherdate = Column(String(19, u'Chinese_PRC_CI_AS'))
    madedate = Column(String(19, u'Chinese_PRC_CI_AS'))
    maker = Column(Unicode(50))
    auditor = Column(Unicode(50))
    auditeddate = Column(String(19, u'Chinese_PRC_CI_AS'))
    reviser = Column(Unicode(50))
    iscarriedforwardout = Column(Integer)
    iscarriedforwardin = Column(Integer)
    ismodifiedcode = Column(Integer)
    createdtime = Column(String(19, u'Chinese_PRC_CI_AS'))
    sequencenumber = Column(Integer)
    ts = Column(TIMESTAMP, nullable=False)
    updated = Column(String(19, u'Chinese_PRC_CI_AS'))
    updatedBy = Column(Unicode(32))
    priuserdefnvc1 = Column(Unicode(500))
    priuserdefdecm1 = Column(Numeric(28, 14))
    priuserdefnvc2 = Column(Unicode(500))
    priuserdefdecm2 = Column(Numeric(28, 14))
    priuserdefnvc3 = Column(Unicode(500))
    priuserdefdecm3 = Column(Numeric(28, 14))
    priuserdefnvc4 = Column(Unicode(500))
    priuserdefdecm4 = Column(Numeric(28, 14))
    priuserdefnvc5 = Column(Unicode(500))
    priuserdefdecm5 = Column(Numeric(28, 14))
    priuserdefnvc6 = Column(Unicode(500))
    priuserdefdecm6 = Column(Numeric(28, 14))
    pubuserdefnvc1 = Column(Unicode(500))
    pubuserdefdecm1 = Column(Numeric(28, 14))
    pubuserdefnvc2 = Column(Unicode(500))
    pubuserdefdecm2 = Column(Numeric(28, 14))
    pubuserdefnvc3 = Column(Unicode(500))
    pubuserdefdecm3 = Column(Numeric(28, 14))
    pubuserdefnvc4 = Column(Unicode(500))
    pubuserdefdecm4 = Column(Numeric(28, 14))
    pubuserdefnvc5 = Column(Unicode(500))
    pubuserdefdecm5 = Column(Numeric(28, 14))
    pubuserdefnvc6 = Column(Unicode(500))
    pubuserdefdecm6 = Column(Numeric(28, 14))
    changedate = Column(String(19, u'Chinese_PRC_CI_AS'))
    changer = Column(Unicode(50))
    PrintCount = Column(Integer)
    ID = Column(Integer, primary_key=True)
    iddepartment = Column(Integer)
    idMarketingOrgan = Column(Integer)
    idcustomer = Column(Integer)
    idperson = Column(Integer)
    idproject = Column(Integer)
    finishState = Column(Integer)
    voucherstate = Column(Integer)
    auditorid = Column(Integer)
    makerid = Column(Integer)
    changerid = Column(Integer)
    saleOrderId = Column(Integer)


class MPManufactureOrderMaterial(Base):
    __tablename__ = 'MP_ManufactureOrder_Material'

    code = Column(Unicode(30))
    name = Column(Unicode(200))
    inventoryBarCode = Column(Unicode(128))
    parentScaleQuantity = Column(Numeric(28, 14))
    sonScaleQuantity = Column(Numeric(28, 14))
    sonScaleQuantity2 = Column(Numeric(28, 14))
    sonNeededQuantity = Column(Numeric(28, 14))
    sonLossQuantity = Column(Numeric(28, 14))
    sonLossRate = Column(Numeric(28, 14))
    quantity = Column(Numeric(28, 14))
    unitExchangeRate = Column(Numeric(28, 14))
    sonNeededQuantity2 = Column(Numeric(28, 14))
    sonLossQuantity2 = Column(Numeric(28, 14))
    quantity2 = Column(Numeric(28, 14))
    isInvertedMaterial = Column(Integer)
    batch = Column(Unicode(50))
    totalRequisitionedQuantity = Column(Numeric(28, 14))
    totalRequisitionedQuantity2 = Column(Numeric(28, 14))
    totalStockOutCost = Column(Numeric(28, 14))
    totalStockCount = Column(Integer)
    baseQuantity = Column(Numeric(28, 14))
    subQuantity = Column(Numeric(28, 14))
    SonNeededSubQuantity = Column(Numeric(28, 14))
    SonLossSubQuantity = Column(Numeric(28, 14))
    WholeSuitMaterialQuantity = Column(Numeric(28, 14))
    createdtime = Column(String(19, u'Chinese_PRC_CI_AS'))
    sequencenumber = Column(Integer)
    ts = Column(TIMESTAMP, nullable=False)
    updated = Column(String(19, u'Chinese_PRC_CI_AS'))
    updatedBy = Column(Unicode(32))
    priuserdefnvc1 = Column(Unicode(500))
    priuserdefdecm1 = Column(Numeric(28, 14))
    priuserdefnvc2 = Column(Unicode(500))
    priuserdefdecm2 = Column(Numeric(28, 14))
    priuserdefnvc3 = Column(Unicode(500))
    priuserdefdecm3 = Column(Numeric(28, 14))
    priuserdefnvc4 = Column(Unicode(500))
    priuserdefdecm4 = Column(Numeric(28, 14))
    pubuserdefnvc1 = Column(Unicode(500))
    pubuserdefdecm1 = Column(Numeric(28, 14))
    pubuserdefnvc2 = Column(Unicode(500))
    pubuserdefdecm2 = Column(Numeric(28, 14))
    pubuserdefnvc3 = Column(Unicode(500))
    pubuserdefdecm3 = Column(Numeric(28, 14))
    pubuserdefnvc4 = Column(Unicode(500))
    pubuserdefdecm4 = Column(Numeric(28, 14))
    freeItem0 = Column(Unicode(300))
    freeItem1 = Column(Unicode(300))
    freeItem2 = Column(Unicode(300))
    freeItem3 = Column(Unicode(300))
    freeItem4 = Column(Unicode(300))
    freeItem5 = Column(Unicode(300))
    freeItem6 = Column(Unicode(300))
    freeItem7 = Column(Unicode(300))
    freeItem8 = Column(Unicode(300))
    freeItem9 = Column(Unicode(300))
    id = Column(Integer, primary_key=True)
    idinventory = Column(Integer)
    idproductprocess = Column(Integer)
    idbaseunit = Column(Integer)
    idsubunit = Column(Integer)
    idunit = Column(Integer)
    idunit2 = Column(Integer)
    idwarehouse = Column(Integer)
    voucherId = Column(Integer)
    idManufactureOrderDetailDTO = Column(Integer)


class MPManufactureOrderSourceRelation(Base):
    __tablename__ = 'MP_ManufactureOrder_SourceRelation'

    code = Column(Unicode(30))
    name = Column(Unicode(200))
    quantity = Column(Numeric(28, 14))
    unitExchangeRate = Column(Numeric(28, 14))
    quantity2 = Column(Numeric(28, 14))
    baseQuantity = Column(Numeric(28, 14))
    subQuantity = Column(Numeric(28, 14))
    createdtime = Column(String(19, u'Chinese_PRC_CI_AS'))
    sequencenumber = Column(Integer)
    ts = Column(TIMESTAMP, nullable=False)
    updated = Column(String(19, u'Chinese_PRC_CI_AS'))
    updatedBy = Column(Unicode(32))
    id = Column(Integer, primary_key=True)
    idbaseunit = Column(Integer)
    idsubunit = Column(Integer)
    idunit = Column(Integer)
    idunit2 = Column(Integer)
    sourceVoucherId = Column(Integer)
    sourceVoucherDetailId = Column(Integer)
    voucherId = Column(Integer)
    idManufactureOrderDetailDTO = Column(Integer)
    idsourcevouchertype = Column(Integer)


class MPManufactureOrderTrace(Base):
    __tablename__ = 'MP_ManufactureOrder_Trace'

    code = Column(Unicode(30))
    name = Column(Unicode(200))
    sourceVoucherCode = Column(Unicode(50))
    createdtime = Column(String(19, u'Chinese_PRC_CI_AS'))
    sequencenumber = Column(Integer)
    ts = Column(TIMESTAMP, nullable=False)
    updated = Column(String(19, u'Chinese_PRC_CI_AS'))
    updatedBy = Column(Unicode(32))
    id = Column(Integer, primary_key=True)
    sourceVoucherId = Column(Integer)
    sourceVoucherDetailId = Column(Integer)
    voucherId = Column(Integer)
    idManufactureOrderDetailDTO = Column(Integer)
    idsourcevouchertype = Column(Integer)


class MPManufactureOrderB(Base):
    __tablename__ = 'MP_ManufactureOrder_b'

    code = Column(Unicode(30))
    name = Column(Unicode(200))
    inventoryBarCode = Column(Unicode(128))
    sourceVoucherCode = Column(Unicode(50))
    bomType = Column(Unicode(50))
    bomVersion = Column(Unicode(50))
    batch = Column(Unicode(50))
    quantity = Column(Numeric(28, 14))
    unitExchangeRate = Column(Numeric(28, 14))
    quantity2 = Column(Numeric(28, 14))
    preStartDate = Column(String(19, u'Chinese_PRC_CI_AS'))
    preFinishDate = Column(String(19, u'Chinese_PRC_CI_AS'))
    startDate = Column(String(19, u'Chinese_PRC_CI_AS'))
    finishDate = Column(String(19, u'Chinese_PRC_CI_AS'))
    wholeSuitMaterialQuantity = Column(Numeric(28, 14))
    totalStockInQuantity = Column(Numeric(28, 14))
    TotalStockInQuantity2 = Column(Numeric(28, 14))
    totalCheckedAccount = Column(Numeric(28, 14))
    totalCheckedQuantity = Column(Numeric(28, 14))
    hasPRA = Column(Integer)
    totalpracount = Column(Integer)
    totalStockCount = Column(Integer)
    saleOrderCode = Column(Unicode(30))
    isNoModify = Column(Unicode(200))
    baseQuantity = Column(Numeric(28, 14))
    subQuantity = Column(Numeric(28, 14))
    fulfillCostFlag = Column(Integer)
    createdtime = Column(String(19, u'Chinese_PRC_CI_AS'))
    sequencenumber = Column(Integer)
    ts = Column(TIMESTAMP, nullable=False)
    updated = Column(String(19, u'Chinese_PRC_CI_AS'))
    updatedBy = Column(Unicode(32))
    priuserdefnvc1 = Column(Unicode(500))
    priuserdefdecm1 = Column(Numeric(28, 14))
    priuserdefnvc2 = Column(Unicode(500))
    priuserdefdecm2 = Column(Numeric(28, 14))
    priuserdefnvc3 = Column(Unicode(500))
    priuserdefdecm3 = Column(Numeric(28, 14))
    priuserdefnvc4 = Column(Unicode(500))
    priuserdefdecm4 = Column(Numeric(28, 14))
    pubuserdefnvc1 = Column(Unicode(500))
    pubuserdefdecm1 = Column(Numeric(28, 14))
    pubuserdefnvc2 = Column(Unicode(500))
    pubuserdefdecm2 = Column(Numeric(28, 14))
    pubuserdefnvc3 = Column(Unicode(500))
    pubuserdefdecm3 = Column(Numeric(28, 14))
    pubuserdefnvc4 = Column(Unicode(500))
    pubuserdefdecm4 = Column(Numeric(28, 14))
    freeItem0 = Column(Unicode(300))
    freeItem1 = Column(Unicode(300))
    freeItem2 = Column(Unicode(300))
    freeItem3 = Column(Unicode(300))
    freeItem4 = Column(Unicode(300))
    freeItem5 = Column(Unicode(300))
    freeItem6 = Column(Unicode(300))
    freeItem7 = Column(Unicode(300))
    freeItem8 = Column(Unicode(300))
    freeItem9 = Column(Unicode(300))
    id = Column(Integer, primary_key=True)
    idbom = Column(Integer)
    bomId = Column(Integer)
    idinventory = Column(Integer)
    idcustomer = Column(Integer)
    idproject = Column(Integer)
    idrouting = Column(Integer)
    idbaseunit = Column(Integer)
    idsubunit = Column(Integer)
    idunit = Column(Integer)
    idunit2 = Column(Integer)
    idwarehouse = Column(Integer)
    bomExpandType = Column(Integer)
    finishState = Column(Integer)
    processState = Column(Integer)
    sourcecondition = Column(Integer)
    sourceVoucherId = Column(Integer)
    sourceVoucherDetailId = Column(Integer)
    idManufactureOrderDTO = Column(Integer)
    saleOrderId = Column(Integer)
    saleOrderDetailId = Column(Integer)
    idsourcevouchertype = Column(Integer)


class MPOperationSku(Base):
    __tablename__ = 'MP_OperationSku'

    Level = Column(Integer)
    demandingDate = Column(String(19, u'Chinese_PRC_CI_AS'))
    availableQuantity = Column(Numeric(28, 14))
    grossDemand = Column(Numeric(28, 14))
    actualDemand = Column(Numeric(28, 14))
    suggestionQuantity = Column(Numeric(28, 14))
    openingQuantity = Column(Numeric(28, 14))
    IsComputed = Column(Integer)
    ClosingQuantity = Column(Numeric(28, 14))
    UnitType = Column(Integer)
    unitExchangeRate = Column(Numeric(28, 14))
    requiredquantity = Column(Numeric(28, 14))
    produceQuantity = Column(Numeric(28, 14))
    ProcureBatch = Column(Numeric(28, 14))
    YieldRate = Column(Numeric(28, 14))
    WasteRate = Column(Numeric(28, 14))
    IsEnd = Column(Integer)
    pickbatch = Column(Numeric(28, 14))
    IsMadeSelf = Column(Integer)
    IsMadeRequest = Column(Integer)
    IsPurchase = Column(Integer)
    createdtime = Column(String(19, u'Chinese_PRC_CI_AS'), server_default=text("(CONVERT([char](19),getdate(),(120)))"))
    code = Column(Unicode(30))
    computevoucherCode = Column(Unicode(30))
    freeItem0 = Column(Unicode(300))
    freeItem1 = Column(Unicode(300))
    freeItem2 = Column(Unicode(300))
    freeItem3 = Column(Unicode(300))
    freeItem4 = Column(Unicode(300))
    freeItem5 = Column(Unicode(300))
    freeItem6 = Column(Unicode(300))
    freeItem7 = Column(Unicode(300))
    freeItem8 = Column(Unicode(300))
    freeItem9 = Column(Unicode(300))
    ID = Column(Integer, primary_key=True)
    idBom = Column(Integer)
    IdBomRelationParent = Column(Integer)
    idbomchild = Column(Integer)
    idBomRelation = Column(Integer)
    IdInventory = Column(Integer)
    idBaseUnit = Column(Integer)
    idSourceDetailId = Column(Integer)
    planattribute = Column(Integer)
    idComputeVoucher = Column(Integer)
    IdSku = Column(Integer)
    idSourceVoucherType = Column(Integer)


t_MP_PRA_FormComputerSetting = Table(
    'MP_PRA_FormComputerSetting', metadata,
    Column('code', Unicode(30)),
    Column('name', Unicode(200)),
    Column('increasevalue', Numeric(28, 14)),
    Column('increasescale', Numeric(28, 14)),
    Column('isnullitem', Integer),
    Column('ts', TIMESTAMP, nullable=False),
    Column('updated', String(19, u'Chinese_PRC_CI_AS')),
    Column('updatedBy', Unicode(32)),
    Column('id', Integer, nullable=False),
    Column('increasemode', Integer)
)


t_MP_PRA_GeneratePurchaseOrderRule = Table(
    'MP_PRA_GeneratePurchaseOrderRule', metadata,
    Column('code', Unicode(30)),
    Column('name', Unicode(200)),
    Column('isphurchaselots', Integer),
    Column('createdtime', String(19, u'Chinese_PRC_CI_AS')),
    Column('sequencenumber', Integer),
    Column('ts', TIMESTAMP, nullable=False),
    Column('updated', String(19, u'Chinese_PRC_CI_AS')),
    Column('updatedBy', Unicode(32)),
    Column('ID', Integer, nullable=False),
    Column('mergerule', Integer),
    Column('splitrule', Integer),
    Column('iduser', Integer)
)


t_MP_PRA_GeneratePurchaseOrderSetting = Table(
    'MP_PRA_GeneratePurchaseOrderSetting', metadata,
    Column('code', Unicode(30)),
    Column('name', Unicode(200)),
    Column('purchasedate', String(19, u'Chinese_PRC_CI_AS')),
    Column('arrivaldate', String(19, u'Chinese_PRC_CI_AS')),
    Column('exchangerate', Numeric(28, 14)),
    Column('isnullitem', Integer),
    Column('ts', TIMESTAMP, nullable=False),
    Column('updated', String(19, u'Chinese_PRC_CI_AS')),
    Column('updatedBy', Unicode(32)),
    Column('id', Integer, nullable=False),
    Column('idcurrency', Integer),
    Column('iddepartment', Integer),
    Column('idpartner', Integer),
    Column('idperson', Integer)
)


t_MP_PRA_GeneratePurchaseRequisitionRule = Table(
    'MP_PRA_GeneratePurchaseRequisitionRule', metadata,
    Column('code', Unicode(30)),
    Column('name', Unicode(200)),
    Column('isPhurchaseLots', Integer),
    Column('createdtime', String(19, u'Chinese_PRC_CI_AS')),
    Column('sequencenumber', Integer),
    Column('ts', TIMESTAMP, nullable=False),
    Column('updated', String(19, u'Chinese_PRC_CI_AS')),
    Column('updatedBy', Unicode(32)),
    Column('id', Integer, nullable=False),
    Column('mergeRule', Integer),
    Column('splitRule', Integer),
    Column('idUser', Integer)
)


t_MP_PRA_GeneratePurchaseRequisitionSetting = Table(
    'MP_PRA_GeneratePurchaseRequisitionSetting', metadata,
    Column('code', Unicode(30)),
    Column('name', Unicode(200)),
    Column('purchaseDate', String(19, u'Chinese_PRC_CI_AS')),
    Column('demanddate', String(19, u'Chinese_PRC_CI_AS')),
    Column('isnullitem', Integer),
    Column('ts', TIMESTAMP, nullable=False),
    Column('updated', String(19, u'Chinese_PRC_CI_AS')),
    Column('updatedBy', Unicode(32)),
    Column('id', Integer, nullable=False),
    Column('iddepartment', Integer),
    Column('idpartner', Integer),
    Column('idclerk', Integer)
)


class MPPRAPraComputeVoucher(Base):
    __tablename__ = 'MP_PRA_PraComputeVoucher'

    code = Column(Unicode(30))
    name = Column(Unicode(200))
    sourceVoucherCode = Column(Unicode(50))
    saleOrderCode = Column(Unicode(30))
    quantity = Column(Numeric(28, 14))
    quantity2 = Column(Numeric(28, 14))
    unitExchangeRate = Column(Numeric(28, 14))
    baseQuantity = Column(Numeric(28, 14))
    subQuantity = Column(Numeric(28, 14))
    increaseScale = Column(Numeric(28, 14))
    increaseQuantity = Column(Numeric(28, 14))
    operationQuantity = Column(Numeric(28, 14))
    increaseQuantity2 = Column(Numeric(28, 14))
    operationQuantity2 = Column(Numeric(28, 14))
    nextgeneratecount = Column(Numeric(28, 14))
    excutequantity = Column(Numeric(28, 14))
    excutequantity2 = Column(Numeric(28, 14))
    demandingdate = Column(String(19, u'Chinese_PRC_CI_AS'))
    watchtime = Column(String(19, u'Chinese_PRC_CI_AS'))
    createdtime = Column(String(19, u'Chinese_PRC_CI_AS'))
    sequencenumber = Column(Integer)
    ts = Column(TIMESTAMP, nullable=False)
    updated = Column(String(19, u'Chinese_PRC_CI_AS'))
    updatedBy = Column(Unicode(32))
    isNoModify = Column(Unicode(400))
    priuserdefnvc1 = Column(Unicode(500))
    priuserdefdecm1 = Column(Numeric(28, 14))
    priuserdefnvc2 = Column(Unicode(500))
    priuserdefdecm2 = Column(Numeric(28, 14))
    priuserdefnvc3 = Column(Unicode(500))
    priuserdefdecm3 = Column(Numeric(28, 14))
    priuserdefnvc4 = Column(Unicode(500))
    priuserdefdecm4 = Column(Numeric(28, 14))
    priuserdefnvc5 = Column(Unicode(500))
    priuserdefdecm5 = Column(Numeric(28, 14))
    priuserdefnvc6 = Column(Unicode(500))
    priuserdefdecm6 = Column(Numeric(28, 14))
    priuserdefnvc7 = Column(Unicode(500))
    priuserdefdecm7 = Column(Numeric(28, 14))
    priuserdefnvc8 = Column(Unicode(500))
    priuserdefdecm8 = Column(Numeric(28, 14))
    priuserdefnvc9 = Column(Unicode(500))
    priuserdefdecm9 = Column(Numeric(28, 14))
    priuserdefnvc10 = Column(Unicode(500))
    priuserdefdecm10 = Column(Numeric(28, 14))
    pubuserdefnvc1 = Column(Unicode(500))
    pubuserdefdecm1 = Column(Numeric(28, 14))
    pubuserdefnvc2 = Column(Unicode(500))
    pubuserdefdecm2 = Column(Numeric(28, 14))
    pubuserdefnvc3 = Column(Unicode(500))
    pubuserdefdecm3 = Column(Numeric(28, 14))
    pubuserdefnvc4 = Column(Unicode(500))
    pubuserdefdecm4 = Column(Numeric(28, 14))
    pubuserdefnvc5 = Column(Unicode(500))
    pubuserdefdecm5 = Column(Numeric(28, 14))
    pubuserdefnvc6 = Column(Unicode(500))
    pubuserdefdecm6 = Column(Numeric(28, 14))
    pubuserdefnvc7 = Column(Unicode(500))
    pubuserdefdecm7 = Column(Numeric(28, 14))
    pubuserdefnvc8 = Column(Unicode(500))
    pubuserdefdecm8 = Column(Numeric(28, 14))
    pubuserdefnvc9 = Column(Unicode(500))
    pubuserdefdecm9 = Column(Numeric(28, 14))
    pubuserdefnvc10 = Column(Unicode(500))
    pubuserdefdecm10 = Column(Numeric(28, 14))
    freeItem0 = Column(Unicode(300))
    freeItem1 = Column(Unicode(300))
    freeItem2 = Column(Unicode(300))
    freeItem3 = Column(Unicode(300))
    freeItem4 = Column(Unicode(300))
    freeItem5 = Column(Unicode(300))
    freeItem6 = Column(Unicode(300))
    freeItem7 = Column(Unicode(300))
    freeItem8 = Column(Unicode(300))
    freeItem9 = Column(Unicode(300))
    SourceVoucherTs = Column(DateTime)
    SourceVoucherDetailTs = Column(DateTime)
    ID = Column(Integer, primary_key=True)
    idbom = Column(Integer)
    idinventory = Column(Integer)
    idcustomer = Column(Integer)
    idproject = Column(Integer)
    idbaseunit = Column(Integer)
    idsubunit = Column(Integer)
    idunit = Column(Integer)
    idunit2 = Column(Integer)
    idWarehouse = Column(Integer)
    sourceVoucherId = Column(Integer)
    sourceVoucherDetailId = Column(Integer)
    idPraVoucherDTO = Column(Integer)
    saleOrderId = Column(Integer)
    saleorderdetailid = Column(Integer)
    idsourcevouchertype = Column(Integer)


class MPPRAPraComputeVoucherTemp(Base):
    __tablename__ = 'MP_PRA_PraComputeVoucher_Temp'

    code = Column(Unicode(30))
    name = Column(Unicode(200))
    sourceVoucherCode = Column(Unicode(50))
    saleOrderCode = Column(Unicode(30))
    quantity = Column(Numeric(28, 14))
    quantity2 = Column(Numeric(28, 14))
    unitExchangeRate = Column(Numeric(28, 14))
    baseQuantity = Column(Numeric(28, 14))
    subQuantity = Column(Numeric(28, 14))
    increaseScale = Column(Numeric(28, 14))
    increaseQuantity = Column(Numeric(28, 14))
    operationQuantity = Column(Numeric(28, 14))
    increaseQuantity2 = Column(Numeric(28, 14))
    operationQuantity2 = Column(Numeric(28, 14))
    nextgeneratecount = Column(Numeric(28, 14))
    excutequantity = Column(Numeric(28, 14))
    excutequantity2 = Column(Numeric(28, 14))
    demandingdate = Column(String(19, u'Chinese_PRC_CI_AS'))
    watchtime = Column(String(19, u'Chinese_PRC_CI_AS'))
    createdtime = Column(String(19, u'Chinese_PRC_CI_AS'))
    sequencenumber = Column(Integer)
    ts = Column(TIMESTAMP, nullable=False)
    updated = Column(String(19, u'Chinese_PRC_CI_AS'))
    updatedBy = Column(Unicode(32))
    isNoModify = Column(Unicode(400))
    priuserdefnvc1 = Column(Unicode(500))
    priuserdefdecm1 = Column(Numeric(28, 14))
    priuserdefnvc2 = Column(Unicode(500))
    priuserdefdecm2 = Column(Numeric(28, 14))
    priuserdefnvc3 = Column(Unicode(500))
    priuserdefdecm3 = Column(Numeric(28, 14))
    priuserdefnvc4 = Column(Unicode(500))
    priuserdefdecm4 = Column(Numeric(28, 14))
    priuserdefnvc5 = Column(Unicode(500))
    priuserdefdecm5 = Column(Numeric(28, 14))
    priuserdefnvc6 = Column(Unicode(500))
    priuserdefdecm6 = Column(Numeric(28, 14))
    priuserdefnvc7 = Column(Unicode(500))
    priuserdefdecm7 = Column(Numeric(28, 14))
    priuserdefnvc8 = Column(Unicode(500))
    priuserdefdecm8 = Column(Numeric(28, 14))
    priuserdefnvc9 = Column(Unicode(500))
    priuserdefdecm9 = Column(Numeric(28, 14))
    priuserdefnvc10 = Column(Unicode(500))
    priuserdefdecm10 = Column(Numeric(28, 14))
    pubuserdefnvc1 = Column(Unicode(500))
    pubuserdefdecm1 = Column(Numeric(28, 14))
    pubuserdefnvc2 = Column(Unicode(500))
    pubuserdefdecm2 = Column(Numeric(28, 14))
    pubuserdefnvc3 = Column(Unicode(500))
    pubuserdefdecm3 = Column(Numeric(28, 14))
    pubuserdefnvc4 = Column(Unicode(500))
    pubuserdefdecm4 = Column(Numeric(28, 14))
    pubuserdefnvc5 = Column(Unicode(500))
    pubuserdefdecm5 = Column(Numeric(28, 14))
    pubuserdefnvc6 = Column(Unicode(500))
    pubuserdefdecm6 = Column(Numeric(28, 14))
    pubuserdefnvc7 = Column(Unicode(500))
    pubuserdefdecm7 = Column(Numeric(28, 14))
    pubuserdefnvc8 = Column(Unicode(500))
    pubuserdefdecm8 = Column(Numeric(28, 14))
    pubuserdefnvc9 = Column(Unicode(500))
    pubuserdefdecm9 = Column(Numeric(28, 14))
    pubuserdefnvc10 = Column(Unicode(500))
    pubuserdefdecm10 = Column(Numeric(28, 14))
    freeItem0 = Column(Unicode(300))
    freeItem1 = Column(Unicode(300))
    freeItem2 = Column(Unicode(300))
    freeItem3 = Column(Unicode(300))
    freeItem4 = Column(Unicode(300))
    freeItem5 = Column(Unicode(300))
    freeItem6 = Column(Unicode(300))
    freeItem7 = Column(Unicode(300))
    freeItem8 = Column(Unicode(300))
    freeItem9 = Column(Unicode(300))
    SourceVoucherTs = Column(LargeBinary(8))
    SourceVoucherDetailTs = Column(LargeBinary(8))
    id = Column(Integer, primary_key=True)
    idbom = Column(Integer)
    idinventory = Column(Integer)
    idcustomer = Column(Integer)
    idproject = Column(Integer)
    idbaseunit = Column(Integer)
    idsubunit = Column(Integer)
    idunit = Column(Integer)
    idunit2 = Column(Integer)
    idWarehouse = Column(Integer)
    sourceVoucherId = Column(Integer)
    sourceVoucherDetailId = Column(Integer)
    idPraVoucherDTO = Column(Integer)
    saleOrderId = Column(Integer)
    saleorderdetailid = Column(Integer)
    idsourcevouchertype = Column(Integer)


t_MP_PRA_PraOption = Table(
    'MP_PRA_PraOption', metadata,
    Column('code', Unicode(30)),
    Column('name', Unicode(200)),
    Column('isPraInventory', Integer),
    Column('isPurchaseInventory', Integer),
    Column('isCarriedForwardOut', Integer),
    Column('isCarriedForwardIn', Integer),
    Column('getavailablebeforesomedate', Integer),
    Column('availablequantitydate', String(19, u'Chinese_PRC_CI_AS')),
    Column('notquantityonfreeitems', Integer),
    Column('onquantityonfreeitems', Integer),
    Column('containsnullwarehouse', Integer),
    Column('existingquantity', Integer),
    Column('safequantity', Integer),
    Column('lowquantity', Integer),
    Column('purchaseonwayquantity', Integer),
    Column('purchaseorderonwayquantity', Integer),
    Column('purchaseorderonwayunaudit', Integer),
    Column('purchasearrivalquantity', Integer),
    Column('purchaseforreceivequantity', Integer),
    Column('onProducingQuantity', Integer),
    Column('manufacturequantity', Integer),
    Column('manufacturequantityunaudit', Integer),
    Column('productforreceivequantity', Integer),
    Column('transonwayquantity', Integer),
    Column('otheronwayquantity', Integer),
    Column('saleonwayquantity', Integer),
    Column('saleorderquantity', Integer),
    Column('saleorderquantityunaudit', Integer),
    Column('saledeliveryquantity', Integer),
    Column('forsaledispatchquantity', Integer),
    Column('manufactureMaterialsQuantity', Integer),
    Column('manufactureforsendquantity', Integer),
    Column('manufactureforsendunaudit', Integer),
    Column('materialforsendquantity', Integer),
    Column('transfordispatchquantity', Integer),
    Column('otherfordispatchquantity', Integer),
    Column('purchaserequisitionquantity', Integer),
    Column('purchaserequisitionunaudit', Integer),
    Column('createdtime', String(19, u'Chinese_PRC_CI_AS')),
    Column('sequencenumber', Integer),
    Column('ts', TIMESTAMP, nullable=False),
    Column('updated', String(19, u'Chinese_PRC_CI_AS')),
    Column('updatedBy', Unicode(32)),
    Column('DeliveryOnWayQuantity', BIT),
    Column('DeliveryOnWayQuantityUnaudit', BIT),
    Column('id', Integer, nullable=False),
    Column('completmentType', Integer),
    Column('completmentTypeForHeigh', Integer),
    Column('GeneratedType', Integer),
    Column('resultmergetype', Integer),
    Column('SourceDocType', Integer),
    Column('suggestiontype', Integer)
)


class MPPRAPraResult(Base):
    __tablename__ = 'MP_PRA_PraResult'

    code = Column(Unicode(30))
    name = Column(Unicode(200))
    topQuantity = Column(Numeric(28, 14))
    sourceVoucherCode = Column(Unicode(50))
    saleOrderCode = Column(Unicode(30))
    demandingDate = Column(String(19, u'Chinese_PRC_CI_AS'))
    grossDemand = Column(Numeric(28, 14))
    actualDemand = Column(Numeric(28, 14))
    actualDemand2 = Column(Numeric(28, 14))
    existingQuantity = Column(Numeric(28, 14))
    lowquantity = Column(Numeric(28, 14))
    safeQuantity = Column(Numeric(28, 14))
    purchaseRequisitionQuantity = Column(Numeric(28, 14))
    purchaseOnWayQuantity = Column(Numeric(28, 14))
    onProducingQuantity = Column(Numeric(28, 14))
    transOnWayQuantity = Column(Numeric(28, 14))
    otherOnWayQuantity = Column(Numeric(28, 14))
    saleDeliveryQuantity = Column(Numeric(28, 14))
    manufactureMaterialsQuantity = Column(Numeric(28, 14))
    transForDispatchQuantity = Column(Numeric(28, 14))
    otherForDispatchQuantity = Column(Numeric(28, 14))
    suggestionQuantity = Column(Numeric(28, 14))
    suggestionQuantity2 = Column(Numeric(28, 14))
    unitExchangeRate = Column(Numeric(28, 14))
    sortno = Column(Integer)
    mergetype = Column(Integer)
    openingquantity = Column(Numeric(28, 14))
    watchtime = Column(String(19, u'Chinese_PRC_CI_AS'))
    closingquantity = Column(Numeric(28, 14))
    quantity = Column(Numeric(28, 14))
    availablequantity = Column(Numeric(28, 14))
    tempbatchaq = Column(Numeric(28, 14))
    createdtime = Column(String(19, u'Chinese_PRC_CI_AS'))
    sequencenumber = Column(Integer)
    ts = Column(TIMESTAMP, nullable=False)
    updated = Column(String(19, u'Chinese_PRC_CI_AS'))
    updatedBy = Column(Unicode(32))
    tempOpeningQuantity = Column(Numeric(28, 14))
    tempClosingQuantity = Column(Numeric(28, 14))
    freeItem0 = Column(Unicode(300))
    freeItem1 = Column(Unicode(300))
    freeItem2 = Column(Unicode(300))
    freeItem3 = Column(Unicode(300))
    freeItem4 = Column(Unicode(300))
    freeItem5 = Column(Unicode(300))
    freeItem6 = Column(Unicode(300))
    freeItem7 = Column(Unicode(300))
    freeItem8 = Column(Unicode(300))
    freeItem9 = Column(Unicode(300))
    RealLevel = Column(Integer)
    isEnd = Column(Integer, nullable=False, server_default=text("((1))"))
    StockRequestOnWayQuantity = Column(Numeric(28, 14))
    id = Column(Integer, primary_key=True)
    idbom = Column(Integer)
    idbomchild = Column(Integer)
    idinventory = Column(Integer)
    idsourceinventory = Column(Integer)
    idcustomer = Column(Integer)
    idproject = Column(Integer)
    idunit = Column(Integer)
    idunit2 = Column(Integer)
    sourceVoucherId = Column(Integer)
    sourceVoucherDetailId = Column(Integer)
    parentid = Column(Integer)
    computervoucherid = Column(Integer)
    idPraVoucherDTO = Column(Integer)
    saleOrderId = Column(Integer)
    saleorderdetailid = Column(Integer)
    idsourcevouchertype = Column(Integer)


t_MP_PRA_PraWarehouse = Table(
    'MP_PRA_PraWarehouse', metadata,
    Column('code', Unicode(30)),
    Column('name', Unicode(200)),
    Column('isselected', Integer),
    Column('createdtime', String(19, u'Chinese_PRC_CI_AS')),
    Column('sequencenumber', Integer),
    Column('ts', TIMESTAMP, nullable=False),
    Column('updated', String(19, u'Chinese_PRC_CI_AS')),
    Column('updatedBy', Unicode(32)),
    Column('id', Integer, nullable=False),
    Column('idwarehouse', Integer),
    Column('idPraOptionDTO', Integer)
)


t_MP_PRA_PurSuggestion2PurOrder = Table(
    'MP_PRA_PurSuggestion2PurOrder', metadata,
    Column('code', Unicode(30)),
    Column('name', Unicode(200)),
    Column('currentquantity', Numeric(28, 14)),
    Column('currentquantity2', Numeric(28, 14)),
    Column('purchasedate', String(19, u'Chinese_PRC_CI_AS')),
    Column('arrivalDate', String(19, u'Chinese_PRC_CI_AS')),
    Column('price', Numeric(28, 14)),
    Column('taxRate', Numeric(28, 14)),
    Column('taxPrice', Numeric(28, 14)),
    Column('unitexchangerate', Numeric(28, 14)),
    Column('exchangerate', Numeric(28, 14)),
    Column('createdtime', String(19, u'Chinese_PRC_CI_AS')),
    Column('sequencenumber', Integer),
    Column('ts', TIMESTAMP, nullable=False),
    Column('updated', String(19, u'Chinese_PRC_CI_AS')),
    Column('updatedBy', Unicode(32)),
    Column('isNoModify', Unicode(400)),
    Column('freeItem0', Unicode(300)),
    Column('freeItem1', Unicode(300)),
    Column('freeItem2', Unicode(300)),
    Column('freeItem3', Unicode(300)),
    Column('freeItem4', Unicode(300)),
    Column('freeItem5', Unicode(300)),
    Column('freeItem6', Unicode(300)),
    Column('freeItem7', Unicode(300)),
    Column('freeItem8', Unicode(300)),
    Column('freeItem9', Unicode(300)),
    Column('id', Integer, nullable=False),
    Column('idcurrency', Integer),
    Column('iddepartment', Integer),
    Column('idinventory', Integer),
    Column('idpartner', Integer),
    Column('idclerk', Integer),
    Column('idproject', Integer),
    Column('idunit', Integer),
    Column('idunit2', Integer),
    Column('iduser', Integer),
    Column('idpurchasesuggestion', Integer)
)


t_MP_PRA_PurSuggestion2PurRequisition = Table(
    'MP_PRA_PurSuggestion2PurRequisition', metadata,
    Column('code', Unicode(30)),
    Column('name', Unicode(200)),
    Column('currentquantity2', Numeric(28, 14)),
    Column('purchasedate', String(19, u'Chinese_PRC_CI_AS')),
    Column('price', Numeric(28, 14)),
    Column('taxRate', Numeric(28, 14)),
    Column('taxPrice', Numeric(28, 14)),
    Column('currentquantity', Numeric(28, 14)),
    Column('unitexchangerate', Numeric(28, 14)),
    Column('demanddate', String(19, u'Chinese_PRC_CI_AS')),
    Column('createdtime', String(19, u'Chinese_PRC_CI_AS')),
    Column('sequencenumber', Integer),
    Column('ts', TIMESTAMP, nullable=False),
    Column('updated', String(19, u'Chinese_PRC_CI_AS')),
    Column('updatedBy', Unicode(32)),
    Column('isNoModify', Unicode(400)),
    Column('freeItem0', Unicode(300)),
    Column('freeItem1', Unicode(300)),
    Column('freeItem2', Unicode(300)),
    Column('freeItem3', Unicode(300)),
    Column('freeItem4', Unicode(300)),
    Column('freeItem5', Unicode(300)),
    Column('freeItem6', Unicode(300)),
    Column('freeItem7', Unicode(300)),
    Column('freeItem8', Unicode(300)),
    Column('freeItem9', Unicode(300)),
    Column('id', Integer, nullable=False),
    Column('iddepartment', Integer),
    Column('idinventory', Integer),
    Column('idpartner', Integer),
    Column('idclerk', Integer),
    Column('idproject', Integer),
    Column('idunit', Integer),
    Column('idunit2', Integer),
    Column('iduser', Integer),
    Column('idpurchasesuggestion', Integer)
)


class MPPRAPurchaseSuggestion(Base):
    __tablename__ = 'MP_PRA_PurchaseSuggestion'

    code = Column(Unicode(30))
    name = Column(Unicode(200))
    quantity = Column(Numeric(28, 14))
    demandingDate = Column(String(19, u'Chinese_PRC_CI_AS'))
    saleOrderCode = Column(Unicode(30))
    sourceVoucherCode = Column(Unicode(50))
    quantity2 = Column(Numeric(28, 14))
    subQuantity = Column(Numeric(28, 14))
    baseQuantity = Column(Numeric(28, 14))
    ExecutedQuantity = Column(Numeric(28, 14))
    ExecutedQuantity2 = Column(Numeric(28, 14))
    unitExchangeRate = Column(Numeric(28, 14))
    watchtime = Column(String(19, u'Chinese_PRC_CI_AS'))
    createdtime = Column(String(19, u'Chinese_PRC_CI_AS'))
    sequencenumber = Column(Integer)
    ts = Column(TIMESTAMP, nullable=False)
    updated = Column(String(19, u'Chinese_PRC_CI_AS'))
    updatedBy = Column(Unicode(32))
    freeItem0 = Column(Unicode(300))
    freeItem1 = Column(Unicode(300))
    freeItem2 = Column(Unicode(300))
    freeItem3 = Column(Unicode(300))
    freeItem4 = Column(Unicode(300))
    freeItem5 = Column(Unicode(300))
    freeItem6 = Column(Unicode(300))
    freeItem7 = Column(Unicode(300))
    freeItem8 = Column(Unicode(300))
    freeItem9 = Column(Unicode(300))
    mergetype = Column(Integer)
    id = Column(Integer, primary_key=True)
    idbom = Column(Integer)
    idinventory = Column(Integer)
    idsourceinventory = Column(Integer)
    idcustomer = Column(Integer)
    idproject = Column(Integer)
    idbaseunit = Column(Integer)
    idsubunit = Column(Integer)
    idunit = Column(Integer)
    idunit2 = Column(Integer)
    sourceVoucherId = Column(Integer)
    sourceVoucherDetailId = Column(Integer)
    suggestionSource = Column(Integer)
    computevoucherid = Column(Integer)
    resultid = Column(Integer)
    idPraVoucherDTO = Column(Integer)
    saleOrderId = Column(Integer)
    saleorderdetailid = Column(Integer)
    idsourcevouchertype = Column(Integer)


class MPPRAPurchaseSuggestionSourceTrace(Base):
    __tablename__ = 'MP_PRA_PurchaseSuggestionSourceTrace'

    code = Column(Unicode(30))
    name = Column(Unicode(200))
    sourceVoucherCode = Column(Unicode(50))
    createdtime = Column(String(19, u'Chinese_PRC_CI_AS'))
    sequencenumber = Column(Integer)
    ts = Column(TIMESTAMP, nullable=False)
    updated = Column(String(19, u'Chinese_PRC_CI_AS'))
    updatedBy = Column(Unicode(32))
    id = Column(Integer, primary_key=True)
    sourceVoucherId = Column(Integer)
    sourceVoucherDetailId = Column(Integer)
    idPraPurchaseSuggestionDTO = Column(Integer)
    voucherId = Column(Integer)
    idsourcevouchertype = Column(Integer)


t_MP_PRA_PurchaseSuggestion_Temp = Table(
    'MP_PRA_PurchaseSuggestion_Temp', metadata,
    Column('id', Integer, nullable=False)
)


class MPPRAResultSourceRelation(Base):
    __tablename__ = 'MP_PRA_ResultSourceRelation'

    code = Column(Unicode(30))
    name = Column(Unicode(200))
    sourceVoucherCode = Column(Unicode(50))
    quantity = Column(Numeric(28, 14))
    quantity2 = Column(Numeric(28, 14))
    basequantity = Column(Numeric(28, 14))
    subquantity = Column(Numeric(28, 14))
    unitexchangerate = Column(Numeric(28, 14))
    createdtime = Column(String(19, u'Chinese_PRC_CI_AS'))
    sequencenumber = Column(Integer)
    ts = Column(TIMESTAMP, nullable=False)
    updated = Column(String(19, u'Chinese_PRC_CI_AS'))
    updatedBy = Column(Unicode(32))
    id = Column(Integer, primary_key=True)
    idbaseunit = Column(Integer)
    idsubunit = Column(Integer)
    idunit = Column(Integer)
    idunit2 = Column(Integer)
    sourceVoucherId = Column(Integer)
    sourceVoucherDetailId = Column(Integer)
    idPraResultDTO = Column(Integer)
    voucherid = Column(Integer)
    idsourcevouchertype = Column(Integer)


class MPPRAResultSourceTrace(Base):
    __tablename__ = 'MP_PRA_ResultSourceTrace'

    code = Column(Unicode(30))
    name = Column(Unicode(200))
    sourceVoucherCode = Column(Unicode(50))
    createdtime = Column(String(19, u'Chinese_PRC_CI_AS'))
    sequencenumber = Column(Integer)
    ts = Column(TIMESTAMP, nullable=False)
    updated = Column(String(19, u'Chinese_PRC_CI_AS'))
    updatedBy = Column(Unicode(32))
    id = Column(Integer, primary_key=True)
    sourceVoucherId = Column(Integer)
    sourceVoucherDetailId = Column(Integer)
    idPraResultDTO = Column(Integer)
    voucherId = Column(Integer)
    idsourcevouchertype = Column(Integer)


t_MP_PRA_SourceType = Table(
    'MP_PRA_SourceType', metadata,
    Column('code', Unicode(30)),
    Column('name', Unicode(200)),
    Column('sourceType', Unicode(50)),
    Column('ts', TIMESTAMP, nullable=False),
    Column('updated', String(19, u'Chinese_PRC_CI_AS')),
    Column('updatedBy', Unicode(32)),
    Column('id', Integer, nullable=False),
    Column('userId', Integer)
)


class MPPRASuggestionSourceRelation(Base):
    __tablename__ = 'MP_PRA_SuggestionSourceRelation'

    code = Column(Unicode(30))
    name = Column(Unicode(200))
    sourceVoucherCode = Column(Unicode(50))
    quantity = Column(Numeric(28, 14))
    quantity2 = Column(Numeric(28, 14))
    basequantity = Column(Numeric(28, 14))
    subquantity = Column(Numeric(28, 14))
    unitexchangerate = Column(Numeric(28, 14))
    createdtime = Column(String(19, u'Chinese_PRC_CI_AS'))
    sequencenumber = Column(Integer)
    ts = Column(TIMESTAMP, nullable=False)
    updated = Column(String(19, u'Chinese_PRC_CI_AS'))
    updatedBy = Column(Unicode(32))
    id = Column(Integer, primary_key=True)
    idbaseunit = Column(Integer)
    idsubunit = Column(Integer)
    idunit = Column(Integer)
    idunit2 = Column(Integer)
    sourceVoucherId = Column(Integer)
    sourceVoucherDetailId = Column(Integer)
    idPraPurchaseSuggestionDTO = Column(Integer)
    voucherid = Column(Integer)
    idsourcevouchertype = Column(Integer)


class MPPRAVoucher(Base):
    __tablename__ = 'MP_PRA_Voucher'

    code = Column(Unicode(30))
    name = Column(Unicode(200))
    docno = Column(Unicode(36))
    docclass = Column(Unicode(36))
    accountingperiod = Column(Integer)
    docid = Column(Unicode(36))
    accountingyear = Column(Integer)
    memo = Column(Unicode(200))
    voucherdate = Column(String(19, u'Chinese_PRC_CI_AS'))
    madedate = Column(String(19, u'Chinese_PRC_CI_AS'))
    maker = Column(Unicode(50))
    auditor = Column(Unicode(50))
    auditeddate = Column(String(19, u'Chinese_PRC_CI_AS'))
    reviser = Column(Unicode(50))
    iscarriedforwardout = Column(Integer)
    iscarriedforwardin = Column(Integer)
    ismodifiedcode = Column(Integer)
    createdtime = Column(String(19, u'Chinese_PRC_CI_AS'))
    sequencenumber = Column(Integer)
    ts = Column(TIMESTAMP, nullable=False)
    updated = Column(String(19, u'Chinese_PRC_CI_AS'))
    updatedBy = Column(Unicode(32))
    priuserdefnvc1 = Column(Unicode(500))
    priuserdefdecm1 = Column(Numeric(28, 14))
    priuserdefnvc2 = Column(Unicode(500))
    priuserdefdecm2 = Column(Numeric(28, 14))
    priuserdefnvc3 = Column(Unicode(500))
    priuserdefdecm3 = Column(Numeric(28, 14))
    priuserdefnvc4 = Column(Unicode(500))
    priuserdefdecm4 = Column(Numeric(28, 14))
    priuserdefnvc5 = Column(Unicode(500))
    priuserdefdecm5 = Column(Numeric(28, 14))
    priuserdefnvc6 = Column(Unicode(500))
    priuserdefdecm6 = Column(Numeric(28, 14))
    pubuserdefnvc1 = Column(Unicode(500))
    pubuserdefdecm1 = Column(Numeric(28, 14))
    pubuserdefnvc2 = Column(Unicode(500))
    pubuserdefdecm2 = Column(Numeric(28, 14))
    pubuserdefnvc3 = Column(Unicode(500))
    pubuserdefdecm3 = Column(Numeric(28, 14))
    pubuserdefnvc4 = Column(Unicode(500))
    pubuserdefdecm4 = Column(Numeric(28, 14))
    pubuserdefnvc5 = Column(Unicode(500))
    pubuserdefdecm5 = Column(Numeric(28, 14))
    pubuserdefnvc6 = Column(Unicode(500))
    pubuserdefdecm6 = Column(Numeric(28, 14))
    id = Column(Integer, primary_key=True)
    voucherstate = Column(Integer)
    auditorid = Column(Integer)
    makerid = Column(Integer)


t_MP_ProduceToolPreManufactureOrder = Table(
    'MP_ProduceToolPreManufactureOrder', metadata,
    Column('code', Unicode(30)),
    Column('name', Unicode(200)),
    Column('bomtype', Unicode(50)),
    Column('bomversion', Unicode(50)),
    Column('quantity', Numeric(28, 14)),
    Column('unitExchangeRate', Numeric(28, 14)),
    Column('quantity2', Numeric(28, 14)),
    Column('preStartDate', String(19, u'Chinese_PRC_CI_AS')),
    Column('preFinishDate', String(19, u'Chinese_PRC_CI_AS')),
    Column('sourceVoucherCode', Unicode(50)),
    Column('sourceVoucherTs', Unicode(50)),
    Column('sourceVoucherDetailTs', Unicode(50)),
    Column('saleOrderCode', Unicode(30)),
    Column('createdtime', String(19, u'Chinese_PRC_CI_AS')),
    Column('sequencenumber', Integer),
    Column('ts', TIMESTAMP, nullable=False),
    Column('updated', String(19, u'Chinese_PRC_CI_AS')),
    Column('updatedBy', Unicode(32)),
    Column('freeItem0', String(36, u'Chinese_PRC_CI_AS')),
    Column('freeItem1', String(36, u'Chinese_PRC_CI_AS')),
    Column('freeItem2', String(36, u'Chinese_PRC_CI_AS')),
    Column('freeItem3', String(36, u'Chinese_PRC_CI_AS')),
    Column('freeItem4', String(36, u'Chinese_PRC_CI_AS')),
    Column('freeItem5', String(36, u'Chinese_PRC_CI_AS')),
    Column('freeItem6', String(36, u'Chinese_PRC_CI_AS')),
    Column('freeItem7', String(36, u'Chinese_PRC_CI_AS')),
    Column('freeItem8', String(36, u'Chinese_PRC_CI_AS')),
    Column('freeItem9', String(36, u'Chinese_PRC_CI_AS')),
    Column('id', Integer, nullable=False, server_default=text("((0))")),
    Column('produceType', Integer),
    Column('bomid', Integer),
    Column('expandType', Integer),
    Column('sourceVoucherId', Integer),
    Column('sourceVoucherDetailId', Integer),
    Column('saleOrderId', Integer),
    Column('saleOrderDetailId', Integer),
    Column('idinventory', Integer),
    Column('idunit', Integer),
    Column('idunit2', Integer),
    Column('iddepartment', Integer),
    Column('idperson', Integer),
    Column('idpartner', Integer),
    Column('idsourcevouchertype', Integer),
    Column('idproject', Integer),
    Column('idbom', Integer),
    Column('idwarehouse', Integer)
)


t_MP_ProduceToolSourceVoucherSelected = Table(
    'MP_ProduceToolSourceVoucherSelected', metadata,
    Column('code', Unicode(30)),
    Column('name', Unicode(200)),
    Column('bomtype', Unicode(50)),
    Column('bomversion', Unicode(50)),
    Column('quantity', Numeric(28, 14)),
    Column('unitExchangeRate', Numeric(28, 14)),
    Column('quantity2', Numeric(28, 14)),
    Column('demandingDate', String(19, u'Chinese_PRC_CI_AS')),
    Column('sourceVoucherCode', Unicode(50)),
    Column('sourceVoucherTs', Unicode(50)),
    Column('sourceVoucherDetailTs', Unicode(50)),
    Column('saleOrderCode', Unicode(30)),
    Column('createdtime', String(19, u'Chinese_PRC_CI_AS')),
    Column('sequencenumber', Integer),
    Column('ts', TIMESTAMP, nullable=False),
    Column('updated', String(19, u'Chinese_PRC_CI_AS')),
    Column('updatedBy', Unicode(32)),
    Column('freeItem0', String(36, u'Chinese_PRC_CI_AS')),
    Column('freeItem1', String(36, u'Chinese_PRC_CI_AS')),
    Column('freeItem2', String(36, u'Chinese_PRC_CI_AS')),
    Column('freeItem3', String(36, u'Chinese_PRC_CI_AS')),
    Column('freeItem4', String(36, u'Chinese_PRC_CI_AS')),
    Column('freeItem5', String(36, u'Chinese_PRC_CI_AS')),
    Column('freeItem6', String(36, u'Chinese_PRC_CI_AS')),
    Column('freeItem7', String(36, u'Chinese_PRC_CI_AS')),
    Column('freeItem8', String(36, u'Chinese_PRC_CI_AS')),
    Column('freeItem9', String(36, u'Chinese_PRC_CI_AS')),
    Column('id', Integer, nullable=False, server_default=text("((0))")),
    Column('bomid', Integer),
    Column('sourceVoucherId', Integer),
    Column('sourceVoucherDetailId', Integer),
    Column('saleOrderId', Integer),
    Column('saleOrderDetailId', Integer),
    Column('idinventory', Integer),
    Column('idunit', Integer),
    Column('idunit2', Integer),
    Column('idpartner', Integer),
    Column('idsourcevouchertype', Integer),
    Column('idproject', Integer),
    Column('idbom', Integer),
    Column('idwarehouse', Integer)
)


class MPResultTemp(Base):
    __tablename__ = 'MP_ResultTemp'

    suggestionQuantity = Column(Numeric(28, 14))
    suggestionQuantity2 = Column(Numeric(28, 14))
    grossDemand = Column(Numeric(28, 14))
    actualDemand = Column(Numeric(28, 14))
    actualDemand2 = Column(Numeric(28, 14))
    demandingDate = Column(String(19, u'Chinese_PRC_CI_AS'))
    freeItem0 = Column(Unicode(300))
    freeItem1 = Column(Unicode(300))
    freeItem2 = Column(Unicode(300))
    freeItem3 = Column(Unicode(300))
    freeItem4 = Column(Unicode(300))
    freeItem5 = Column(Unicode(300))
    freeItem6 = Column(Unicode(300))
    freeItem7 = Column(Unicode(300))
    freeItem8 = Column(Unicode(300))
    freeItem9 = Column(Unicode(300))
    MergeSourceVoucherCode = Column(Unicode(50))
    MergeSaleOrderCode = Column(Unicode(30))
    ID = Column(Integer, primary_key=True)
    idBom = Column(Integer)
    idInventory = Column(Integer)
    MergeIdSourceInventory = Column(Integer)
    MergeIdCustomer = Column(Integer)
    MergeSourceVoucherId = Column(Integer)
    sourceVoucherId = Column(Integer)
    sourceVoucherDetailId = Column(Integer)
    idVoucherDTO = Column(Integer)
    MergeSaleOrderId = Column(Integer)
    MergeIdSourcevouchertype = Column(Integer)


class MPSKU(Base):
    __tablename__ = 'MP_SKU'

    FreeItem0 = Column(Unicode(300))
    FreeItem1 = Column(Unicode(300))
    FreeItem2 = Column(Unicode(300))
    FreeItem3 = Column(Unicode(300))
    FreeItem4 = Column(Unicode(300))
    FreeItem5 = Column(Unicode(300))
    FreeItem6 = Column(Unicode(300))
    FreeItem7 = Column(Unicode(300))
    FreeItem8 = Column(Unicode(300))
    FreeItem9 = Column(Unicode(300))
    createdtime = Column(String(19, u'Chinese_PRC_CI_AS'), server_default=text("(CONVERT([char](19),getdate(),(120)))"))
    Code = Column(Unicode(30))
    id = Column(Integer, primary_key=True)
    IdInventory = Column(Integer)


t_MP_Step = Table(
    'MP_Step', metadata,
    Column('Step', Integer, nullable=False),
    Column('IsMRP', Integer, nullable=False),
    Column('Status', Integer),
    Column('Message', Unicode(1000), server_default=text("('')"))
)


t_MP_TEMP_DAQ = Table(
    'MP_TEMP_DAQ', metadata,
    Column('Quantity', Numeric(28, 14), server_default=text("((0))")),
    Column('IdSku', Integer)
)


t_My_tmp_Inventory = Table(
    'My_tmp_Inventory', metadata,
    Column('Unit1Code', Unicode(50)),
    Column('Unit1Name', Unicode(200)),
    Column('Unit1ChangeRate', Numeric(28, 14)),
    Column('Unit2Code', Unicode(50)),
    Column('Unit2Name', Unicode(200)),
    Column('Unit2ChangeRate', Numeric(28, 14)),
    Column('Unit3Code', Unicode(50)),
    Column('Unit3Name', Unicode(200)),
    Column('Unit3ChangeRate', Numeric(28, 14)),
    Column('Unit4Code', Unicode(50)),
    Column('Unit4Name', Unicode(200)),
    Column('Unit4ChangeRate', Numeric(28, 14)),
    Column('IDInventory', Integer),
    Column('IDUnit1', Integer),
    Column('IDUnit2', Integer),
    Column('IDUnit3', Integer),
    Column('IDUnit4', Integer)
)


t_PRE_AA_AssetClass = Table(
    'PRE_AA_AssetClass', metadata,
    Column('TradeKind', Unicode(100), nullable=False),
    Column('code', Unicode(30)),
    Column('name', Unicode(100)),
    Column('depth', Integer),
    Column('inid', Unicode(750)),
    Column('isendnode', Integer),
    Column('ispreset', Integer),
    Column('isdisPlay', Integer),
    Column('imageFile', Unicode(500)),
    Column('defaultyears', Integer),
    Column('defaultmonths', Integer),
    Column('defaultnrvrate', Numeric(9, 6)),
    Column('defaultoffsetinputtax', Integer),
    Column('defaultinputtaxrate', Numeric(5, 2)),
    Column('updated', String(19, u'Chinese_PRC_CI_AS')),
    Column('updatedBy', Unicode(32)),
    Column('createdTime', String(19, u'Chinese_PRC_CI_AS')),
    Column('UsedYearAndMonth', Unicode(200)),
    Column('IsSystem', Integer, nullable=False, server_default=text("((0))")),
    Column('id', Integer, nullable=False, server_default=text("((0))")),
    Column('idassetprop', Integer),
    Column('iddeprmethod', Integer),
    Column('idbarcode', Integer),
    Column('idunit', Integer),
    Column('idlabelstyle', Integer),
    Column('idcardstyle', Integer),
    Column('idparent', Integer)
)


t_PRE_AA_AssetClass_Ext = Table(
    'PRE_AA_AssetClass_Ext', metadata,
    Column('TradeKind', Unicode(100), nullable=False),
    Column('id', UNIQUEIDENTIFIER, nullable=False),
    Column('assetClassid_lev1', UNIQUEIDENTIFIER),
    Column('assetClasscode_lev1', Unicode(40)),
    Column('assetClassname_lev1', Unicode(100)),
    Column('assetClassid_lev2', UNIQUEIDENTIFIER),
    Column('assetClasscode_lev2', Unicode(40)),
    Column('assetClassname_lev2', Unicode(100)),
    Column('assetClassid_lev3', UNIQUEIDENTIFIER),
    Column('assetClasscode_lev3', Unicode(40)),
    Column('assetClassname_lev3', Unicode(100)),
    Column('assetClassid_lev4', UNIQUEIDENTIFIER),
    Column('assetClasscode_lev4', Unicode(40)),
    Column('assetClassname_lev4', Unicode(100)),
    Column('assetClassid_lev5', UNIQUEIDENTIFIER),
    Column('assetClasscode_lev5', Unicode(40)),
    Column('assetClassname_lev5', Unicode(100)),
    Column('assetClassid_lev6', UNIQUEIDENTIFIER),
    Column('assetClasscode_lev6', Unicode(40)),
    Column('assetClassname_lev6', Unicode(100)),
    Column('assetClassid_lev7', UNIQUEIDENTIFIER),
    Column('assetClasscode_lev7', Unicode(40)),
    Column('assetClassname_lev7', Unicode(100)),
    Column('assetClassid_lev8', UNIQUEIDENTIFIER),
    Column('assetClasscode_lev8', Unicode(40)),
    Column('assetClassname_lev8', Unicode(100)),
    Column('assetClassid_lev9', UNIQUEIDENTIFIER),
    Column('assetClasscode_lev9', Unicode(40)),
    Column('assetClassname_lev9', Unicode(100)),
    Column('assetClassid_lev10', UNIQUEIDENTIFIER),
    Column('assetClasscode_lev10', Unicode(40)),
    Column('assetClassname_lev10', Unicode(100)),
    Column('assetClassid_lev11', UNIQUEIDENTIFIER),
    Column('assetClasscode_lev11', Unicode(40)),
    Column('assetClassname_lev11', Unicode(100)),
    Column('assetClassid_lev12', UNIQUEIDENTIFIER),
    Column('assetClasscode_lev12', Unicode(40)),
    Column('assetClassname_lev12', Unicode(100)),
    Column('assetClassid_lev13', UNIQUEIDENTIFIER),
    Column('assetClasscode_lev13', Unicode(40)),
    Column('assetClassname_lev13', Unicode(100)),
    Column('assetClassid_lev14', UNIQUEIDENTIFIER),
    Column('assetClasscode_lev14', Unicode(40)),
    Column('assetClassname_lev14', Unicode(100)),
    Column('assetClassid_lev15', UNIQUEIDENTIFIER),
    Column('assetClasscode_lev15', Unicode(40)),
    Column('assetClassname_lev15', Unicode(100)),
    Column('depth', Unicode(10)),
    Column('createTime', String(19, u'Chinese_PRC_CI_AS')),
    Column('IsSystem', Integer, nullable=False, server_default=text("((0))"))
)


t_PRE_AA_AssetProp = Table(
    'PRE_AA_AssetProp', metadata,
    Column('TradeKind', Unicode(100), nullable=False),
    Column('code', Unicode(30)),
    Column('name', Unicode(100)),
    Column('isdepr', Integer),
    Column('ispreset', Integer),
    Column('IsSystem', Integer, nullable=False, server_default=text("((0))")),
    Column('id', Integer, nullable=False, server_default=text("((0))")),
    Column('provisionway', Integer)
)


t_PRE_AA_DeprMethod = Table(
    'PRE_AA_DeprMethod', metadata,
    Column('TradeKind', Unicode(100), nullable=False),
    Column('code', Unicode(30)),
    Column('name', Unicode(100)),
    Column('depramount', Unicode(500)),
    Column('deprrate', Unicode(500)),
    Column('sequenceNumber', Integer),
    Column('updated', String(19, u'Chinese_PRC_CI_AS')),
    Column('updatedBy', Unicode(32)),
    Column('createdTime', String(19, u'Chinese_PRC_CI_AS')),
    Column('IsSystem', Integer, nullable=False, server_default=text("((0))")),
    Column('id', Integer, nullable=False, server_default=text("((0))"))
)


t_PRE_AA_ParentAssetClass = Table(
    'PRE_AA_ParentAssetClass', metadata,
    Column('TradeKind', Unicode(100), nullable=False),
    Column('id', UNIQUEIDENTIFIER, nullable=False),
    Column('updatedBy', Unicode(32)),
    Column('updated', String(19, u'Chinese_PRC_CI_AS')),
    Column('name', Unicode(100)),
    Column('code', Unicode(32)),
    Column('idSon', UNIQUEIDENTIFIER),
    Column('idParent', UNIQUEIDENTIFIER),
    Column('Depth', Integer),
    Column('isEndNode', Integer),
    Column('IsSystem', Integer, nullable=False, server_default=text("((0))"))
)


t_PRE_FI_SM_TransferredCode = Table(
    'PRE_FI_SM_TransferredCode', metadata,
    Column('TradeKind', Unicode(100), nullable=False),
    Column('basearchivecode', Unicode(30), nullable=False),
    Column('basearchivename', Unicode(200), nullable=False),
    Column('transferredcode', Unicode(30)),
    Column('IsSystem', Integer, nullable=False),
    Column('id', Integer, nullable=False),
    Column('basearchiveid', Integer, nullable=False, server_default=text("((0))")),
    Column('idcodingprefixion', Integer, nullable=False, server_default=text("((0))"))
)


class PREGLReferenceDoc(Base):
    __tablename__ = 'PRE_GL_ReferenceDoc'

    TradeKind = Column(Unicode(100), nullable=False)
    code = Column(Unicode(30))
    name = Column(Unicode(200))
    attachedvouchernum = Column(Integer)
    docno = Column(Unicode(50))
    docclass = Column(Unicode(50))
    accountingperiod = Column(Integer)
    docid = Column(Unicode(50))
    accountingyear = Column(Integer)
    memo = Column(Unicode(50))
    voucherdate = Column(String(19, u'Chinese_PRC_CI_AS'))
    madedate = Column(String(19, u'Chinese_PRC_CI_AS'))
    maker = Column(Unicode(50))
    auditor = Column(Unicode(50))
    auditeddate = Column(String(19, u'Chinese_PRC_CI_AS'))
    reviser = Column(Unicode(50))
    ismodifiedcode = Column(Integer)
    createdtime = Column(String(19, u'Chinese_PRC_CI_AS'))
    sequencenumber = Column(Integer)
    updated = Column(String(19, u'Chinese_PRC_CI_AS'))
    updatedBy = Column(Unicode(32))
    priuserdefnvc1 = Column(Unicode(60))
    priuserdefdecm1 = Column(Numeric(28, 14))
    priuserdefnvc2 = Column(Unicode(60))
    priuserdefdecm2 = Column(Numeric(28, 14))
    priuserdefnvc3 = Column(Unicode(60))
    priuserdefdecm3 = Column(Numeric(28, 14))
    priuserdefnvc4 = Column(Unicode(60))
    priuserdefdecm4 = Column(Numeric(28, 14))
    priuserdefnvc5 = Column(Unicode(60))
    priuserdefdecm5 = Column(Numeric(28, 14))
    priuserdefnvc6 = Column(Unicode(60))
    priuserdefdecm6 = Column(Numeric(28, 14))
    IsCashFlowed = Column(Integer)
    id = Column(Integer, primary_key=True)
    iddoctype = Column(Integer)
    CashFlowedState = Column(Integer)
    referencedoctype = Column(Integer)
    voucherstate = Column(Integer)
    auditorid = Column(Integer)
    makerid = Column(Integer)
    idreferencedocclass = Column(Integer)


class PREGLReferenceDocClass(Base):
    __tablename__ = 'PRE_GL_ReferenceDocClass'

    TradeKind = Column(Unicode(100), nullable=False)
    code = Column(Unicode(32))
    name = Column(Unicode(50))
    Updated = Column(DateTime)
    UpdatedBy = Column(Unicode(32))
    madeDate = Column(String(19, u'Chinese_PRC_CI_AS'))
    createdTime = Column(String(19, u'Chinese_PRC_CI_AS'))
    id = Column(Integer, primary_key=True)


class PREGLReferenceEntry(Base):
    __tablename__ = 'PRE_GL_ReferenceEntry'

    TradeKind = Column(Unicode(100), nullable=False)
    code = Column(Unicode(30))
    name = Column(Unicode(200))
    summary = Column(Unicode(200))
    exchangerate = Column(Numeric(28, 14))
    origamountdr = Column(Numeric(28, 14))
    origamountcr = Column(Numeric(28, 14))
    amountdr = Column(Numeric(28, 14))
    amountcr = Column(Numeric(28, 14))
    quantitydr = Column(Numeric(28, 14))
    quantitycr = Column(Numeric(28, 14))
    price = Column(Numeric(28, 14))
    createdtime = Column(String(19, u'Chinese_PRC_CI_AS'))
    sequencenumber = Column(Integer)
    updated = Column(String(19, u'Chinese_PRC_CI_AS'))
    updatedBy = Column(Unicode(32))
    priuserdefnvc1 = Column(Unicode(60))
    priuserdefdecm1 = Column(Numeric(28, 14))
    priuserdefnvc2 = Column(Unicode(60))
    priuserdefdecm2 = Column(Numeric(28, 14))
    priuserdefnvc3 = Column(Unicode(60))
    priuserdefdecm3 = Column(Numeric(28, 14))
    priuserdefnvc4 = Column(Unicode(60))
    priuserdefdecm4 = Column(Numeric(28, 14))
    accountcode = Column(Unicode(200))
    accountname = Column(Unicode(200))
    AuxiliaryItems = Column(Unicode(200))
    id = Column(Integer, primary_key=True)
    idaccount = Column(Integer)
    idcurrency = Column(Integer)
    idReferenceDocDTO = Column(Integer)


t_PRE_SM_FC_AccountExtendRule = Table(
    'PRE_SM_FC_AccountExtendRule', metadata,
    Column('TradeKind', Unicode(100), nullable=False),
    Column('code', Unicode(30)),
    Column('name', Unicode(200)),
    Column('rowidx', Integer),
    Column('checkstate', UNIQUEIDENTIFIER),
    Column('adjusttype', UNIQUEIDENTIFIER),
    Column('inventorypriuserdefdecm0', Numeric(28, 14)),
    Column('inventorypriuserdefnvc0', Unicode(50)),
    Column('inventorypriuserdefdecm1', Numeric(28, 14)),
    Column('inventorypriuserdefnvc1', Unicode(50)),
    Column('inventorypriuserdefdecm2', Numeric(28, 14)),
    Column('inventorypriuserdefnvc2', Unicode(50)),
    Column('inventorypriuserdefdecm3', Numeric(28, 14)),
    Column('inventorypriuserdefnvc3', Unicode(50)),
    Column('inventorypriuserdefdecm4', Numeric(28, 14)),
    Column('inventorypriuserdefnvc4', Unicode(50)),
    Column('headerpubuserdefdecm0', Numeric(28, 14)),
    Column('headerpubuserdefnvc0', Unicode(60)),
    Column('headerpubuserdefdecm1', Numeric(28, 14)),
    Column('headerpubuserdefnvc1', Unicode(60)),
    Column('headerpubuserdefdecm2', Numeric(28, 14)),
    Column('headerpubuserdefnvc2', Unicode(60)),
    Column('headerpubuserdefdecm3', Numeric(28, 14)),
    Column('headerpubuserdefnvc3', Unicode(60)),
    Column('headerpubuserdefdecm4', Numeric(28, 14)),
    Column('headerpubuserdefnvc4', Unicode(60)),
    Column('headerpubuserdefdecm5', Numeric(28, 14)),
    Column('headerpubuserdefnvc5', Unicode(60)),
    Column('headerpriuserdefdecm0', Numeric(28, 14)),
    Column('headerpriuserdefnvc0', Unicode(60)),
    Column('headerpriuserdefdecm1', Numeric(28, 14)),
    Column('headerpriuserdefnvc1', Unicode(60)),
    Column('headerpriuserdefdecm2', Numeric(28, 14)),
    Column('headerpriuserdefnvc2', Unicode(60)),
    Column('headerpriuserdefdecm3', Numeric(28, 14)),
    Column('headerpriuserdefnvc3', Unicode(60)),
    Column('headerpriuserdefdecm4', Numeric(28, 14)),
    Column('headerpriuserdefnvc4', Unicode(60)),
    Column('headerpriuserdefdecm5', Numeric(28, 14)),
    Column('headerpriuserdefnvc5', Unicode(60)),
    Column('detailspubuserdefdecm0', Numeric(28, 14)),
    Column('detailspubuserdefnvc0', Unicode(60)),
    Column('detailspubuserdefdecm1', Numeric(28, 14)),
    Column('detailspubuserdefnvc1', Unicode(60)),
    Column('detailspubuserdefdecm2', Numeric(28, 14)),
    Column('detailspubuserdefnvc2', Unicode(60)),
    Column('detailspubuserdefdecm3', Numeric(28, 14)),
    Column('detailspubuserdefnvc3', Unicode(60)),
    Column('detailspriuserdefdecm0', Numeric(28, 14)),
    Column('detailspriuserdefnvc0', Unicode(60)),
    Column('detailspriuserdefdecm1', Numeric(28, 14)),
    Column('detailspriuserdefnvc1', Unicode(60)),
    Column('detailspriuserdefdecm2', Numeric(28, 14)),
    Column('detailspriuserdefnvc2', Unicode(60)),
    Column('detailspriuserdefdecm3', Numeric(28, 14)),
    Column('detailspriuserdefnvc3', Unicode(60)),
    Column('accountcode', Unicode(50)),
    Column('accountname', Unicode(50)),
    Column('createdtime', String(19, u'Chinese_PRC_CI_AS')),
    Column('sequencenumber', Integer),
    Column('updated', String(19, u'Chinese_PRC_CI_AS')),
    Column('updatedBy', Unicode(32)),
    Column('idbusitype', UNIQUEIDENTIFIER),
    Column('idwarehouse', UNIQUEIDENTIFIER),
    Column('iddistrict', UNIQUEIDENTIFIER),
    Column('idcurrency', UNIQUEIDENTIFIER),
    Column('idpartner', UNIQUEIDENTIFIER),
    Column('idpartnerclass', UNIQUEIDENTIFIER),
    Column('idincome', UNIQUEIDENTIFIER),
    Column('idbankaccount', UNIQUEIDENTIFIER),
    Column('idinventoryclass', UNIQUEIDENTIFIER),
    Column('idinventory', UNIQUEIDENTIFIER),
    Column('idexpenseitem', UNIQUEIDENTIFIER),
    Column('idproject', UNIQUEIDENTIFIER),
    Column('iddepartment', UNIQUEIDENTIFIER),
    Column('idaccount', UNIQUEIDENTIFIER),
    Column('idrdstyle', UNIQUEIDENTIFIER),
    Column('islaborcost', Integer),
    Column('idprojectclass', UNIQUEIDENTIFIER),
    Column('idassetProp', UNIQUEIDENTIFIER),
    Column('idincDecWay', UNIQUEIDENTIFIER),
    Column('summary', Unicode(200)),
    Column('idhandleReason', UNIQUEIDENTIFIER),
    Column('id', Integer, nullable=False),
    Column('expensetype', Integer),
    Column('incomeExpensesType', Integer),
    Column('profitlosstype', Integer),
    Column('idassetClass', Integer),
    Column('idAccountRuleDTO', Integer),
    Column('idvouchertype', Integer)
)


class PRSalePromotionOrderCalled(Base):
    __tablename__ = 'PR_SalePromotion_OrderCalled'

    OrderCalledTableName = Column(Unicode(200))
    OrderCalledPromotionCodeField = Column(Unicode(200))
    OrderCalledPromotionTypeField = Column(Unicode(200))
    id = Column(Integer, primary_key=True)


class PRSalesPromotion(Base):
    __tablename__ = 'PR_SalesPromotion'

    code = Column(Unicode(30))
    name = Column(Unicode(200))
    voucherdate = Column(String(19, u'Chinese_PRC_CI_AS'))
    begindate = Column(String(19, u'Chinese_PRC_CI_AS'))
    enddate = Column(String(19, u'Chinese_PRC_CI_AS'))
    begintime = Column(String(8, u'Chinese_PRC_CI_AS'))
    endtime = Column(String(8, u'Chinese_PRC_CI_AS'))
    week = Column(Unicode(50))
    ismonday = Column(Integer)
    istuesday = Column(Integer)
    iswednesday = Column(Integer)
    isthursday = Column(Integer)
    isfriday = Column(Integer)
    issaturday = Column(Integer)
    issunday = Column(Integer)
    membertype = Column(Unicode(1000))
    overalldiscountrate = Column(Numeric(28, 14))
    ismemberdiscount = Column(Integer)
    ismemberintegral = Column(Integer)
    isoriginalprice = Column(Integer)
    quantitymeet = Column(Numeric(28, 14))
    amountmeet = Column(Numeric(28, 14))
    giftitem = Column(Numeric(28, 14))
    usequantity = Column(Integer)
    effectdate = Column(String(19, u'Chinese_PRC_CI_AS'))
    promotiondetails = Column(Unicode(1000))
    promotiondesc = Column(Unicode(1000))
    docno = Column(Unicode(36))
    docclass = Column(Unicode(36))
    accountingperiod = Column(Integer)
    docid = Column(Unicode(36))
    accountingyear = Column(Integer)
    memo = Column(Unicode(200))
    madedate = Column(String(19, u'Chinese_PRC_CI_AS'))
    maker = Column(Unicode(50))
    auditeddate = Column(String(19, u'Chinese_PRC_CI_AS'))
    auditor = Column(Unicode(50))
    changedate = Column(String(19, u'Chinese_PRC_CI_AS'))
    changer = Column(Unicode(50))
    reviser = Column(Unicode(50))
    iscarriedforwardout = Column(Integer)
    iscarriedforwardin = Column(Integer)
    ismodifiedcode = Column(Integer)
    createdtime = Column(String(19, u'Chinese_PRC_CI_AS'))
    sequencenumber = Column(Integer)
    ts = Column(TIMESTAMP, nullable=False)
    updated = Column(String(19, u'Chinese_PRC_CI_AS'))
    updatedBy = Column(Unicode(32))
    IsMultipleGift = Column(Integer)
    IsUseIntegralAndCash = Column(Integer)
    IsUseStorage = Column(Integer)
    AboveDiscountEffect = Column(Numeric(28, 14))
    IsMeetCondition = Column(Integer)
    PrintCount = Column(Integer)
    IsSameGift = Column(Integer)
    id = Column(Integer, primary_key=True)
    idmarketingorgan = Column(Integer)
    PromotionStore = Column(Integer)
    cashbackway = Column(Integer)
    discountway = Column(Integer)
    meetcondition = Column(Integer)
    PromotionCustomer = Column(Integer)
    promotionobject = Column(Integer)
    PromotionProperty = Column(Integer)
    promotiontype = Column(Integer)
    TrussCondition = Column(Integer)
    voucherstate = Column(Integer)
    auditorid = Column(Integer)
    makerid = Column(Integer)
    changerid = Column(Integer)


class PRSalesPromotionCustomer(Base):
    __tablename__ = 'PR_SalesPromotion_Customer'

    code = Column(Unicode(30))
    name = Column(Unicode(200))
    createdtime = Column(String(19, u'Chinese_PRC_CI_AS'))
    sequencenumber = Column(Integer)
    ts = Column(TIMESTAMP, nullable=False)
    updated = Column(String(19, u'Chinese_PRC_CI_AS'))
    updatedBy = Column(Unicode(32))
    id = Column(Integer, primary_key=True)
    idDepartment = Column(Integer)
    idDistrict = Column(Integer)
    idCustomer = Column(Integer)
    idCustomerClass = Column(Integer)
    idPerson = Column(Integer)
    idsalesPromotionDTO = Column(Integer)


class PRSalesPromotionLimitSale(Base):
    __tablename__ = 'PR_SalesPromotion_LimitSale'

    createdtime = Column(String(19, u'Chinese_PRC_CI_AS'))
    SaleQuantity = Column(Numeric(28, 14))
    LimitSaleQuantity = Column(Numeric(28, 14))
    ID = Column(Integer, primary_key=True)
    idstore = Column(Integer)
    idinventory = Column(Integer)
    idSalesPromotionDTO = Column(Integer)
    idSalesPromotionDetailDTO = Column(Integer)


class PRSalesPromotionMemberType(Base):
    __tablename__ = 'PR_SalesPromotion_MemberType'

    code = Column(Unicode(30))
    name = Column(Unicode(200))
    createdtime = Column(String(19, u'Chinese_PRC_CI_AS'))
    sequencenumber = Column(Integer)
    ts = Column(TIMESTAMP, nullable=False)
    updated = Column(String(19, u'Chinese_PRC_CI_AS'))
    updatedBy = Column(Unicode(32))
    id = Column(Integer, primary_key=True)
    idmembertype = Column(Integer)
    idSalesPromotionDTO = Column(Integer)


class PRSalesPromotionMult(Base):
    __tablename__ = 'PR_SalesPromotion_Mult'

    code = Column(Unicode(30))
    name = Column(Unicode(200))
    inid = Column(Unicode(560))
    retailprice = Column(Numeric(28, 14))
    additionalprice = Column(Numeric(28, 14))
    discountrate = Column(Numeric(28, 14))
    discountamount = Column(Numeric(28, 14))
    promotiondesc = Column(Unicode(1000))
    createdtime = Column(String(19, u'Chinese_PRC_CI_AS'))
    sequencenumber = Column(Integer)
    ts = Column(TIMESTAMP, nullable=False)
    updated = Column(String(19, u'Chinese_PRC_CI_AS'))
    updatedBy = Column(Unicode(32))
    LimitedGiftQuantity = Column(Numeric(28, 14))
    DayLimitedGiftQuantity = Column(Numeric(28, 14))
    InventoryBarCode = Column(Unicode(100))
    id = Column(Integer, primary_key=True)
    idinventory = Column(Integer)
    idinventoryclass = Column(Integer)
    idunit = Column(Integer)
    corpbrand = Column(Integer)
    idSalesPromotionDTO = Column(Integer)
    idSalesPromotionDetailDTO = Column(Integer)


class PRSalesPromotionStore(Base):
    __tablename__ = 'PR_SalesPromotion_Store'

    code = Column(Unicode(30))
    name = Column(Unicode(200))
    createdtime = Column(String(19, u'Chinese_PRC_CI_AS'))
    sequencenumber = Column(Integer)
    ts = Column(TIMESTAMP, nullable=False)
    updated = Column(String(19, u'Chinese_PRC_CI_AS'))
    updatedBy = Column(Unicode(32))
    id = Column(Integer, primary_key=True)
    idstore = Column(Integer)
    StoreType = Column(Integer)
    idDepartment = Column(Integer)
    idDistrict = Column(Integer)
    idSalesPromotionDTO = Column(Integer)


class PRSalesPromotionSubs(Base):
    __tablename__ = 'PR_SalesPromotion_Subs'

    code = Column(Unicode(30))
    name = Column(Unicode(200))
    retailprice = Column(Numeric(28, 14))
    additionalprice = Column(Numeric(28, 14))
    quantitymeet = Column(Numeric(28, 14))
    amountmeet = Column(Numeric(28, 14))
    discountrate = Column(Numeric(28, 14))
    discountamount = Column(Numeric(28, 14))
    promotiondesc = Column(Unicode(1000))
    createdtime = Column(String(19, u'Chinese_PRC_CI_AS'))
    sequencenumber = Column(Integer)
    ts = Column(TIMESTAMP, nullable=False)
    updated = Column(String(19, u'Chinese_PRC_CI_AS'))
    updatedBy = Column(Unicode(32))
    LimitedGiftQuantity = Column(Numeric(28, 14))
    DayLimitedGiftQuantity = Column(Numeric(28, 14))
    InventoryBarCode = Column(Unicode(100))
    PieceMeet = Column(Numeric(28, 14))
    ID = Column(Integer, primary_key=True)
    idinventory = Column(Integer)
    idunit = Column(Integer)
    idSalesPromotionDTO = Column(Integer)


class PRSalesPromotionB(Base):
    __tablename__ = 'PR_SalesPromotion_b'

    code = Column(Unicode(30))
    name = Column(Unicode(200))
    inid = Column(Unicode(560))
    retailprice = Column(Numeric(28, 14))
    memberprice = Column(Numeric(28, 14))
    discountrate = Column(Numeric(28, 14))
    discountamount = Column(Numeric(28, 14))
    discountprice = Column(Numeric(28, 14))
    restrictionquantity = Column(Numeric(28, 14))
    quantitymeet = Column(Numeric(28, 14))
    amountmeet = Column(Numeric(28, 14))
    giftitem = Column(Numeric(28, 14))
    promotiondesc = Column(Unicode(1000))
    createdtime = Column(String(19, u'Chinese_PRC_CI_AS'))
    sequencenumber = Column(Integer)
    ts = Column(TIMESTAMP, nullable=False)
    updated = Column(String(19, u'Chinese_PRC_CI_AS'))
    updatedBy = Column(Unicode(32))
    LimitedSaleQuantity = Column(Numeric(28, 14))
    DayLimitedSaleQuantity = Column(Numeric(28, 14))
    TrussQuantity = Column(Numeric(28, 14))
    PieceMeet = Column(Numeric(28, 14))
    InventoryBarCode = Column(Unicode(100))
    DiscountPriceFormula = Column(Unicode(100))
    id = Column(Integer, primary_key=True)
    idinventory = Column(Integer)
    idinventoryclass = Column(Integer)
    idunit = Column(Integer)
    corpbrand = Column(Integer)
    idSalesPromotionDTO = Column(Integer)


class PUPurchaseArrival(Base):
    __tablename__ = 'PU_PurchaseArrival'

    code = Column(Unicode(30), index=True)
    purchaseInvoiceNo = Column(Unicode(30))
    discountRate = Column(Numeric(28, 14))
    exchangeRate = Column(Numeric(28, 14))
    acceptAddress = Column(Unicode(200))
    linkMan = Column(Unicode(50))
    linkTelphone = Column(Unicode(100))
    origPaymentCashAmount = Column(Numeric(28, 14))
    paymentCashAmount = Column(Numeric(28, 14))
    origTotalTaxAmount = Column(Numeric(28, 14))
    totalTaxAmount = Column(Numeric(28, 14))
    origtotalAmount = Column(Numeric(28, 14))
    totalAmount = Column(Numeric(28, 14))
    isPriceCheck = Column(Integer)
    isReduceArrival = Column(Integer)
    isAutoGenerateInvoice = Column(Integer)
    isAutoGenerateInStock = Column(Integer)
    memo = Column(Unicode(200))
    saleOrderCode = Column(Unicode(30))
    isNoArapBookkeeping = Column(Integer)
    isNoModify = Column(Unicode(1000))
    maker = Column(Unicode(50))
    auditor = Column(Unicode(50))
    reviser = Column(Unicode(50))
    iscarriedforwardout = Column(Integer)
    iscarriedforwardin = Column(Integer)
    ismodifiedcode = Column(Integer)
    docclass = Column(Unicode(36))
    docid = Column(Unicode(36))
    ts = Column(TIMESTAMP)
    updatedBy = Column(Unicode(32))
    priuserdefnvc1 = Column(Unicode(500))
    priuserdefdecm1 = Column(Numeric(28, 14))
    priuserdefnvc2 = Column(Unicode(500))
    priuserdefdecm2 = Column(Numeric(28, 14))
    priuserdefnvc3 = Column(Unicode(500))
    priuserdefdecm3 = Column(Numeric(28, 14))
    priuserdefnvc4 = Column(Unicode(500))
    priuserdefdecm4 = Column(Numeric(28, 14))
    priuserdefnvc5 = Column(Unicode(500))
    priuserdefdecm5 = Column(Numeric(28, 14))
    priuserdefnvc6 = Column(Unicode(500))
    priuserdefdecm6 = Column(Numeric(28, 14))
    pubuserdefnvc1 = Column(Unicode(500))
    pubuserdefdecm1 = Column(Numeric(28, 14))
    pubuserdefnvc2 = Column(Unicode(500))
    pubuserdefdecm2 = Column(Numeric(28, 14))
    pubuserdefnvc3 = Column(Unicode(500))
    pubuserdefdecm3 = Column(Numeric(28, 14))
    pubuserdefnvc4 = Column(Unicode(500))
    pubuserdefdecm4 = Column(Numeric(28, 14))
    pubuserdefnvc5 = Column(Unicode(500))
    pubuserdefdecm5 = Column(Numeric(28, 14))
    pubuserdefnvc6 = Column(Unicode(500))
    pubuserdefdecm6 = Column(Numeric(28, 14))
    origPaymentAmount = Column(Numeric(28, 14))
    paymentAmount = Column(Numeric(28, 14))
    sourceVoucherCode = Column(Unicode(30))
    IsBeforeSystemInuse = Column(Integer)
    changer = Column(Unicode(50))
    PrintCount = Column(Integer)
    collaborateVoucherCode = Column(Unicode(30))
    id = Column(Integer, primary_key=True)
    idbusinesstype = Column(Integer)
    idcurrency = Column(Integer)
    iddepartment = Column(Integer, index=True)
    idMarketingOrgan = Column(Integer)
    idpartner = Column(Integer, index=True)
    idclerk = Column(Integer, index=True)
    idqualityclerk = Column(Integer, index=True)
    idproject = Column(Integer, index=True)
    idrdstyle = Column(Integer)
    idCollaborateDownVoucherType = Column(Integer)
    CollaborateState = Column(Integer)
    idCollaborateDownDraftVoucher = Column(Integer)
    idwarehouse = Column(Integer, index=True)
    deliveryMode = Column(Integer)
    inStockState = Column(Integer)
    invoiceType = Column(Integer)
    payType = Column(Integer)
    settleState = Column(Integer)
    voucherState = Column(Integer)
    auditorid = Column(Integer)
    makerid = Column(Integer)
    changerid = Column(Integer)
    idCollaborateUpVoucherType = Column(Integer)
    idCollaborateUpVoucher = Column(Integer)
    saleOrderId = Column(Integer)
    idsourcevouchertype = Column(Integer, index=True)
    acceptDate = Column(DateTime)
    payDate = Column(DateTime)
    voucherdate = Column(DateTime, index=True)
    madedate = Column(DateTime)
    auditeddate = Column(DateTime)
    createdtime = Column(DateTime, index=True)
    updated = Column(DateTime)
    sourceVoucherDate = Column(DateTime)
    changedate = Column(DateTime)


class PUPurchaseArrivalMultiSettle(Base):
    __tablename__ = 'PU_PurchaseArrival_MultiSettle'

    code = Column(Unicode(30))
    documentCode = Column(Unicode(30))
    origAmount = Column(Numeric(28, 14))
    amount = Column(Numeric(28, 14))
    ts = Column(TIMESTAMP)
    updatedBy = Column(Unicode(32))
    id = Column(Integer, primary_key=True)
    idbankaccount = Column(Integer)
    idsettlestyle = Column(Integer)
    idPurchaseArrivalDTO = Column(Integer, index=True)
    updated = Column(DateTime)


class PUPurchaseArrivalSourceRelation(Base):
    __tablename__ = 'PU_PurchaseArrival_SourceRelation'

    quantity = Column(Numeric(28, 14))
    unitExchangeRate = Column(Numeric(28, 14))
    quantity2 = Column(Numeric(28, 14))
    baseQuantity = Column(Numeric(28, 14))
    subQuantity = Column(Numeric(28, 14))
    ts = Column(TIMESTAMP)
    updatedBy = Column(Unicode(32))
    id = Column(Integer, primary_key=True)
    idbaseunit = Column(Integer)
    idsubunit = Column(Integer)
    idunit = Column(Integer)
    idunit2 = Column(Integer)
    sourceVoucherId = Column(Integer)
    voucherId = Column(Integer, index=True)
    idPurchaseArrivalDetailDTO = Column(Integer, index=True)
    sourceVoucherDetailId = Column(Integer, index=True)
    idsourcevouchertype = Column(Integer, index=True)
    updated = Column(DateTime)


class PUPurchaseArrivalB(Base):
    __tablename__ = 'PU_PurchaseArrival_b'
    __table_args__ = (
        Index('IDX_PU_PurchaseArrival_b_idPurchaseArrivalDTO__taxAmount', 'idPurchaseArrivalDTO', 'taxAmount'),
        Index('IDX_PU_PurchaseArrival_b_idPurchaseArrivalDTO__origSettleAmount', 'idPurchaseArrivalDTO', 'origSettleAmount')
    )

    code = Column(Unicode(30))
    taxFlag = Column(Integer)
    compositionQuantity = Column(Unicode(100))
    inventoryLocation = Column(Unicode(50))
    quantity = Column(Numeric(28, 14))
    origDiscountPrice = Column(Numeric(28, 14))
    quantity2 = Column(Numeric(28, 14))
    origDiscountPrice2 = Column(Numeric(28, 14))
    baseQuantity = Column(Numeric(28, 14))
    subQuantity = Column(Numeric(28, 14))
    unitExchangeRate = Column(Numeric(28, 14))
    origPrice = Column(Numeric(28, 14))
    price = Column(Numeric(28, 14))
    discountRate = Column(Numeric(28, 14))
    taxRate = Column(Numeric(28, 14))
    origTaxPrice = Column(Numeric(28, 14))
    origDiscountAmount = Column(Numeric(28, 14))
    origTax = Column(Numeric(28, 14))
    origTaxAmount = Column(Numeric(28, 14))
    origDiscount = Column(Numeric(28, 14))
    discountPrice = Column(Numeric(28, 14))
    discountPrice2 = Column(Numeric(28, 14))
    taxPrice = Column(Numeric(28, 14))
    discountAmount = Column(Numeric(28, 14))
    tax = Column(Numeric(28, 14))
    taxAmount = Column(Numeric(28, 14))
    discount = Column(Numeric(28, 14))
    isPresent = Column(Integer)
    sourceVoucherCode = Column(Unicode(50))
    saleOrderCode = Column(Unicode(30))
    totalInvoiceQuantity = Column(Numeric(28, 14))
    totalInvoiceQuantity2 = Column(Numeric(28, 14))
    totalInQuantity = Column(Numeric(28, 14))
    totalInQuantity2 = Column(Numeric(28, 14))
    totalSettleQuantity = Column(Numeric(28, 14))
    totalSettleQuantity2 = Column(Numeric(28, 14))
    totalReturnQuantity = Column(Numeric(28, 14))
    totalReturnQuantity2 = Column(Numeric(28, 14))
    totalReduceQuantity = Column(Numeric(28, 14))
    totalReduceQuantity2 = Column(Numeric(28, 14))
    origSettleAmount = Column(Numeric(28, 14))
    settleAmount = Column(Numeric(28, 14))
    batch = Column(Unicode(50))
    arrivalQuantity = Column(Numeric(28, 14))
    acceptanceQuantity = Column(Numeric(28, 14))
    arrivalQuantity2 = Column(Numeric(28, 14))
    acceptanceQuantity2 = Column(Numeric(28, 14))
    warehouseAdjustAmount = Column(Numeric(28, 14))
    isNoModify = Column(Unicode(1000))
    basePrice = Column(Numeric(28, 14))
    baseDiscountPrice = Column(Numeric(28, 14))
    baseTaxPrice = Column(Numeric(28, 14))
    totalSettleTaxAmount = Column(Numeric(28, 14))
    receiveVoucherCode = Column(Unicode(50))
    inventoryBarCode = Column(Unicode(200))
    partnerInventoryCode = Column(Unicode(300))
    ts = Column(TIMESTAMP)
    updatedBy = Column(Unicode(32))
    freeItem0 = Column(Unicode(300))
    freeItem1 = Column(Unicode(300))
    freeItem2 = Column(Unicode(300))
    freeItem3 = Column(Unicode(300))
    freeItem4 = Column(Unicode(300))
    freeItem5 = Column(Unicode(300))
    freeItem6 = Column(Unicode(300))
    freeItem7 = Column(Unicode(300))
    freeItem8 = Column(Unicode(300))
    freeItem9 = Column(Unicode(300))
    priuserdefnvc1 = Column(Unicode(500))
    priuserdefdecm1 = Column(Numeric(28, 14))
    priuserdefnvc2 = Column(Unicode(500))
    priuserdefdecm2 = Column(Numeric(28, 14))
    priuserdefnvc3 = Column(Unicode(500))
    priuserdefdecm3 = Column(Numeric(28, 14))
    priuserdefnvc4 = Column(Unicode(500))
    priuserdefdecm4 = Column(Numeric(28, 14))
    pubuserdefnvc1 = Column(Unicode(500))
    pubuserdefdecm1 = Column(Numeric(28, 14))
    pubuserdefnvc2 = Column(Unicode(500))
    pubuserdefdecm2 = Column(Numeric(28, 14))
    pubuserdefnvc3 = Column(Unicode(500))
    pubuserdefdecm3 = Column(Numeric(28, 14))
    pubuserdefnvc4 = Column(Unicode(500))
    pubuserdefdecm4 = Column(Numeric(28, 14))
    totalSettleBaseQuantity = Column(Numeric(28, 14))
    totalSettleSubQuantity = Column(Numeric(28, 14))
    arrivalBaseQuantity = Column(Numeric(28, 14))
    arrivalSubQuantity = Column(Numeric(28, 14))
    purchaseOrderCode = Column(Unicode(30))
    partnerInventoryName = Column(Unicode(300))
    shrinkageQuantity = Column(Numeric(28, 14))
    shrinkageQuantity2 = Column(Numeric(28, 14))
    shrinkageBaseQuantity = Column(Numeric(28, 14))
    shrinkageSubQuantity = Column(Numeric(28, 14))
    cumInstockShrinkageQuantity = Column(Numeric(28, 14))
    cumInstockShrinkageQuantity2 = Column(Numeric(28, 14))
    cumInvoiceShrinkageQuantity = Column(Numeric(28, 14))
    cumInvoiceShrinkageQuantity2 = Column(Numeric(28, 14))
    cumReturnShrinkageQuantity = Column(Numeric(28, 14))
    cumReturnShrinkageQuantity2 = Column(Numeric(28, 14))
    cumReduceShrinkageQuantity = Column(Numeric(28, 14))
    cumReduceShrinkageQuantity2 = Column(Numeric(28, 14))
    origShrinkageQuantity = Column(Numeric(28, 14))
    origShrinkageQuantity2 = Column(Numeric(28, 14))
    cumAccountAmount = Column(Numeric(28, 14))
    islaborcost = Column(Integer)
    RetailPrice = Column(Numeric(28, 14))
    ID = Column(Integer, primary_key=True)
    idinventory = Column(Integer, index=True)
    idproject = Column(Integer, index=True)
    idbaseunit = Column(Integer)
    idsubunit = Column(Integer)
    idunit = Column(Integer)
    idunit2 = Column(Integer)
    idwarehouse = Column(Integer, index=True)
    sourceVoucherId = Column(Integer)
    idPurchaseArrivalDTO = Column(Integer, index=True)
    sourceVoucherDetailId = Column(Integer, index=True)
    purchaseOrderDetailID = Column(Integer)
    saleOrderId = Column(Integer)
    saleOrderDetailId = Column(Integer)
    idsourcevouchertype = Column(Integer, index=True)
    receiveVoucherId = Column(Integer, index=True)
    receiveVoucherDetailId = Column(Integer)
    acceptDate = Column(DateTime)
    expiryDate = Column(DateTime)
    updated = Column(DateTime)
    ProductionDate = Column(DateTime)


class PUPurchaseArrivalBInvLocation(Base):
    __tablename__ = 'PU_PurchaseArrival_b_InvLocation'

    code = Column(Unicode(30))
    quantity = Column(Numeric(28, 14))
    quantity2 = Column(Numeric(28, 14))
    unitExchangeRate = Column(Numeric(28, 14))
    memo = Column(Unicode(200))
    ts = Column(TIMESTAMP)
    updatedBy = Column(Unicode(32))
    id = Column(Integer, primary_key=True)
    idinvlocation = Column(Integer, index=True)
    idunit = Column(Integer)
    idunit2 = Column(Integer)
    idPurchaseArrivalDetailDTO = Column(Integer, index=True)
    addDate = Column(DateTime)
    updated = Column(DateTime)


class PUPurchaseInvoice(Base):
    __tablename__ = 'PU_PurchaseInvoice'

    code = Column(Unicode(30), index=True)
    purchaseInvoiceNo = Column(Unicode(30))
    discountRate = Column(Numeric(28, 14))
    exchangeRate = Column(Numeric(28, 14))
    memo = Column(Unicode(200))
    totalTaxAmount = Column(Numeric(28, 14))
    origTotalTaxAmount = Column(Numeric(28, 14))
    totalAmount = Column(Numeric(28, 14))
    origTotalAmount = Column(Numeric(28, 14))
    saleOrderCode = Column(Unicode(30))
    isNoModify = Column(Unicode(1000))
    maker = Column(Unicode(50))
    auditor = Column(Unicode(50))
    reviser = Column(Unicode(50))
    iscarriedforwardout = Column(Integer)
    iscarriedforwardin = Column(Integer)
    ismodifiedcode = Column(Integer)
    docclass = Column(Unicode(36))
    docid = Column(Unicode(36))
    ts = Column(TIMESTAMP)
    updatedBy = Column(Unicode(32))
    priuserdefnvc1 = Column(Unicode(500))
    priuserdefdecm1 = Column(Numeric(28, 14))
    priuserdefnvc2 = Column(Unicode(500))
    priuserdefdecm2 = Column(Numeric(28, 14))
    priuserdefnvc3 = Column(Unicode(500))
    priuserdefdecm3 = Column(Numeric(28, 14))
    priuserdefnvc4 = Column(Unicode(500))
    priuserdefdecm4 = Column(Numeric(28, 14))
    priuserdefnvc5 = Column(Unicode(500))
    priuserdefdecm5 = Column(Numeric(28, 14))
    priuserdefnvc6 = Column(Unicode(500))
    priuserdefdecm6 = Column(Numeric(28, 14))
    pubuserdefnvc1 = Column(Unicode(500))
    pubuserdefdecm1 = Column(Numeric(28, 14))
    pubuserdefnvc2 = Column(Unicode(500))
    pubuserdefdecm2 = Column(Numeric(28, 14))
    pubuserdefnvc3 = Column(Unicode(500))
    pubuserdefdecm3 = Column(Numeric(28, 14))
    pubuserdefnvc4 = Column(Unicode(500))
    pubuserdefdecm4 = Column(Numeric(28, 14))
    pubuserdefnvc5 = Column(Unicode(500))
    pubuserdefdecm5 = Column(Numeric(28, 14))
    pubuserdefnvc6 = Column(Unicode(500))
    pubuserdefdecm6 = Column(Numeric(28, 14))
    origPaymentAmount = Column(Numeric(28, 14))
    paymentAmount = Column(Numeric(28, 14))
    isPriceCheck = Column(Integer)
    paymentCashAmount = Column(Numeric(28, 14))
    origPaymentCashAmount = Column(Numeric(28, 14))
    sourceVoucherCode = Column(Unicode(30))
    isNoArapBookkeeping = Column(Integer)
    PrintCount = Column(Integer)
    ID = Column(Integer, primary_key=True)
    idbusinesstype = Column(Integer)
    idcurrency = Column(Integer)
    iddepartment = Column(Integer, index=True)
    idMarketingOrgan = Column(Integer)
    idinvoicepartner = Column(Integer, index=True)
    idpartner = Column(Integer, index=True)
    idclerk = Column(Integer, index=True)
    idproject = Column(Integer, index=True)
    idwarehouse = Column(Integer, index=True)
    accountState = Column(Integer)
    invoiceType = Column(Integer)
    payType = Column(Integer)
    settlestate = Column(Integer)
    voucherState = Column(Integer)
    auditorid = Column(Integer)
    makerid = Column(Integer)
    saleOrderId = Column(Integer)
    idsourcevouchertype = Column(Integer, index=True)
    voucherdate = Column(DateTime, index=True)
    madedate = Column(DateTime)
    auditeddate = Column(DateTime)
    createdtime = Column(DateTime, index=True)
    updated = Column(DateTime)
    payDate = Column(DateTime)
    sourceVoucherDate = Column(DateTime)


class PUPurchaseInvoiceMultiSettle(Base):
    __tablename__ = 'PU_PurchaseInvoice_MultiSettle'

    code = Column(Unicode(30))
    documentCode = Column(Unicode(30))
    origAmount = Column(Numeric(28, 14))
    amount = Column(Numeric(28, 14))
    ts = Column(TIMESTAMP, nullable=False)
    updatedBy = Column(Unicode(32))
    id = Column(Integer, primary_key=True)
    idbankaccount = Column(Integer, index=True)
    idsettlestyle = Column(Integer)
    idPurchaseInvoiceDTO = Column(Integer, index=True)
    updated = Column(DateTime)


class PUPurchaseInvoiceSourceRelation(Base):
    __tablename__ = 'PU_PurchaseInvoice_SourceRelation'

    quantity = Column(Numeric(28, 14))
    unitExchangeRate = Column(Numeric(28, 14))
    quantity2 = Column(Numeric(28, 14))
    baseQuantity = Column(Numeric(28, 14))
    subQuantity = Column(Numeric(28, 14))
    ts = Column(TIMESTAMP)
    updatedBy = Column(Unicode(32))
    id = Column(Integer, primary_key=True)
    idbaseunit = Column(Integer)
    idsubunit = Column(Integer)
    idunit = Column(Integer)
    idunit2 = Column(Integer)
    sourceVoucherId = Column(Integer)
    sourceVoucherDetailId = Column(Integer, index=True)
    voucherId = Column(Integer, index=True)
    idPurchaseInvoiceDetailDTO = Column(Integer, index=True)
    idsourcevouchertype = Column(Integer, index=True)
    updated = Column(DateTime)


class PUPurchaseInvoiceB(Base):
    __tablename__ = 'PU_PurchaseInvoice_b'

    code = Column(Unicode(30))
    baseTaxPrice = Column(Numeric(28, 14))
    baseDiscountPrice = Column(Numeric(28, 14))
    basePrice = Column(Numeric(28, 14))
    batch = Column(Unicode(50))
    quantity = Column(Numeric(28, 14))
    quantity2 = Column(Numeric(28, 14))
    unitExchangeRate = Column(Numeric(28, 14))
    compositionQuantity = Column(Unicode(100))
    discountRate = Column(Numeric(28, 14))
    origPrice = Column(Numeric(28, 14))
    origDiscountPrice = Column(Numeric(28, 14))
    taxRate = Column(Numeric(28, 14))
    origTaxAmount = Column(Numeric(28, 14))
    origDiscountAmount = Column(Numeric(28, 14))
    origTaxPrice = Column(Numeric(28, 14))
    origTax = Column(Numeric(28, 14))
    origDiscount = Column(Numeric(28, 14))
    discountPrice = Column(Numeric(28, 14))
    discountAmount = Column(Numeric(28, 14))
    tax = Column(Numeric(28, 14))
    taxPrice = Column(Numeric(28, 14))
    taxAmount = Column(Numeric(28, 14))
    discount = Column(Numeric(28, 14))
    saleOrderCode = Column(Unicode(30))
    taxFlag = Column(Integer)
    sourceVoucherCode = Column(Unicode(50))
    price = Column(Numeric(28, 14))
    subQuantity = Column(Numeric(28, 14))
    baseQuantity = Column(Numeric(28, 14))
    isNoModify = Column(Unicode(1000))
    inventoryBarCode = Column(Unicode(200))
    partnerInventoryCode = Column(Unicode(300))
    ts = Column(TIMESTAMP)
    updatedBy = Column(Unicode(32))
    freeItem0 = Column(Unicode(300))
    freeItem1 = Column(Unicode(300))
    freeItem2 = Column(Unicode(300))
    freeItem3 = Column(Unicode(300))
    freeItem4 = Column(Unicode(300))
    freeItem5 = Column(Unicode(300))
    freeItem6 = Column(Unicode(300))
    freeItem7 = Column(Unicode(300))
    freeItem8 = Column(Unicode(300))
    freeItem9 = Column(Unicode(300))
    priuserdefnvc1 = Column(Unicode(500))
    priuserdefdecm1 = Column(Numeric(28, 14))
    priuserdefnvc2 = Column(Unicode(500))
    priuserdefdecm2 = Column(Numeric(28, 14))
    priuserdefnvc3 = Column(Unicode(500))
    priuserdefdecm3 = Column(Numeric(28, 14))
    priuserdefnvc4 = Column(Unicode(500))
    priuserdefdecm4 = Column(Numeric(28, 14))
    pubuserdefnvc1 = Column(Unicode(500))
    pubuserdefdecm1 = Column(Numeric(28, 14))
    pubuserdefnvc2 = Column(Unicode(500))
    pubuserdefdecm2 = Column(Numeric(28, 14))
    pubuserdefnvc3 = Column(Unicode(500))
    pubuserdefdecm3 = Column(Numeric(28, 14))
    pubuserdefnvc4 = Column(Unicode(500))
    pubuserdefdecm4 = Column(Numeric(28, 14))
    partnerInventoryName = Column(Unicode(300))
    shrinkageQuantity = Column(Numeric(28, 14))
    shrinkageQuantity2 = Column(Numeric(28, 14))
    shrinkageBaseQuantity = Column(Numeric(28, 14))
    shrinkageSubQuantity = Column(Numeric(28, 14))
    totalSettleBaseQuantity = Column(Numeric(28, 14))
    totalSettleShrinkageBaseQuantity = Column(Numeric(28, 14))
    origSettleAmount = Column(Numeric(28, 14))
    settleAmount = Column(Numeric(28, 14))
    isPresent = Column(Integer)
    cumAccountAmount = Column(Numeric(28, 14))
    purchaseOrderCode = Column(Unicode(30))
    RetailPrice = Column(Numeric(28, 14))
    ID = Column(Integer, primary_key=True)
    idinventory = Column(Integer, index=True)
    idproject = Column(Integer, index=True)
    idbaseunit = Column(Integer)
    idsubunit = Column(Integer)
    idunit = Column(Integer)
    idunit2 = Column(Integer)
    idwarehouse = Column(Integer, index=True)
    sourceVoucherId = Column(Integer)
    sourceVoucherDetailId = Column(Integer, index=True)
    idPurchaseInvoiceDTO = Column(Integer, index=True)
    saleOrderId = Column(Integer)
    saleOrderDetailId = Column(Integer)
    idsourcevouchertype = Column(Integer, index=True)
    expiryDate = Column(DateTime)
    updated = Column(DateTime)
    ProductionDate = Column(DateTime)


class PUPurchaseOrder(Base):
    __tablename__ = 'PU_PurchaseOrder'

    code = Column(Unicode(30), index=True)
    discountRate = Column(Numeric(28, 14))
    exchangeRate = Column(Numeric(28, 14))
    linkMan = Column(Unicode(50))
    linkTelphone = Column(Unicode(100))
    contractId = Column(Unicode(30))
    earnestMoney = Column(Numeric(28, 14))
    memo = Column(Unicode(200))
    origTotalAmount = Column(Numeric(28, 14))
    totalAmount = Column(Numeric(28, 14))
    origTotalTaxAmount = Column(Numeric(28, 14))
    totalTaxAmount = Column(Numeric(28, 14))
    saleOrderCode = Column(Unicode(30))
    acceptAddress = Column(Unicode(200))
    isNoModify = Column(Unicode(1000))
    origEarnestMoney = Column(Numeric(28, 14))
    maker = Column(Unicode(50))
    auditor = Column(Unicode(50))
    reviser = Column(Unicode(50))
    iscarriedforwardout = Column(Integer)
    iscarriedforwardin = Column(Integer)
    ismodifiedcode = Column(Integer)
    docclass = Column(Unicode(36))
    docid = Column(Unicode(36))
    ts = Column(TIMESTAMP)
    updatedBy = Column(Unicode(32))
    priuserdefnvc1 = Column(Unicode(500))
    priuserdefdecm1 = Column(Numeric(28, 14))
    priuserdefnvc2 = Column(Unicode(500))
    priuserdefdecm2 = Column(Numeric(28, 14))
    priuserdefnvc3 = Column(Unicode(500))
    priuserdefdecm3 = Column(Numeric(28, 14))
    priuserdefnvc4 = Column(Unicode(500))
    priuserdefdecm4 = Column(Numeric(28, 14))
    priuserdefnvc5 = Column(Unicode(500))
    priuserdefdecm5 = Column(Numeric(28, 14))
    priuserdefnvc6 = Column(Unicode(500))
    priuserdefdecm6 = Column(Numeric(28, 14))
    pubuserdefnvc1 = Column(Unicode(500))
    pubuserdefdecm1 = Column(Numeric(28, 14))
    pubuserdefnvc2 = Column(Unicode(500))
    pubuserdefdecm2 = Column(Numeric(28, 14))
    pubuserdefnvc3 = Column(Unicode(500))
    pubuserdefdecm3 = Column(Numeric(28, 14))
    pubuserdefnvc4 = Column(Unicode(500))
    pubuserdefdecm4 = Column(Numeric(28, 14))
    pubuserdefnvc5 = Column(Unicode(500))
    pubuserdefdecm5 = Column(Numeric(28, 14))
    pubuserdefnvc6 = Column(Unicode(500))
    pubuserdefdecm6 = Column(Numeric(28, 14))
    sourceVoucherCode = Column(Unicode(30))
    changer = Column(Unicode(50))
    PrintCount = Column(Integer)
    prePaymentAmount = Column(Numeric(28, 14))
    origPrePaymentAmount = Column(Numeric(28, 14))
    collaborateVoucherCode = Column(Unicode(30))
    id = Column(Integer, primary_key=True)
    idbusinesstype = Column(Integer)
    idcurrency = Column(Integer)
    iddepartment = Column(Integer, index=True)
    idmarketingOrgan = Column(Integer)
    idpartner = Column(Integer, index=True)
    idclerk = Column(Integer, index=True)
    idproject = Column(Integer, index=True)
    idCollaborateDownVoucherType = Column(Integer)
    CollaborateState = Column(Integer)
    idCollaborateDownDraftVoucher = Column(Integer)
    idwarehouse = Column(Integer)
    arrivalState = Column(Integer)
    deliveryMode = Column(Integer)
    inStockState = Column(Integer)
    payType = Column(Integer)
    voucherState = Column(Integer)
    auditorid = Column(Integer)
    makerid = Column(Integer)
    changerid = Column(Integer)
    idCollaborateUpVoucherType = Column(Integer)
    idCollaborateUpVoucher = Column(Integer)
    saleOrderId = Column(Integer)
    idsourcevouchertype = Column(Integer, index=True)
    acceptDate = Column(DateTime)
    voucherdate = Column(DateTime, index=True)
    madedate = Column(DateTime)
    auditeddate = Column(DateTime)
    createdtime = Column(DateTime, index=True)
    updated = Column(DateTime)
    sourceVoucherDate = Column(DateTime)
    changedate = Column(DateTime)


class PUPurchaseOrderArnestMoney(Base):
    __tablename__ = 'PU_PurchaseOrder_ArnestMoney'

    code = Column(Unicode(30))
    billNo = Column(Unicode(30))
    origAmount = Column(Numeric(28, 14))
    amount = Column(Numeric(28, 14))
    ts = Column(TIMESTAMP)
    updatedBy = Column(Unicode(32))
    id = Column(Integer, primary_key=True)
    idbankaccount = Column(Integer, index=True)
    idsettlestyle = Column(Integer)
    idPurchaseOrderDTO = Column(Integer, index=True)
    updated = Column(DateTime)


class PUPurchaseOrderSourceRelation(Base):
    __tablename__ = 'PU_PurchaseOrder_SourceRelation'

    quantity = Column(Numeric(28, 14))
    unitExchangeRate = Column(Numeric(28, 14))
    quantity2 = Column(Numeric(28, 14))
    baseQuantity = Column(Numeric(28, 14))
    subQuantity = Column(Numeric(28, 14))
    ts = Column(TIMESTAMP)
    updatedBy = Column(Unicode(32))
    id = Column(Integer, primary_key=True)
    idbaseunit = Column(Integer)
    idsubunit = Column(Integer)
    idunit = Column(Integer)
    idunit2 = Column(Integer)
    sourceVoucherId = Column(Integer)
    sourceVoucherDetailId = Column(Integer, index=True)
    voucherId = Column(Integer, index=True)
    idPurchaseOrderDetailDTO = Column(Integer, index=True)
    idsourcevouchertype = Column(Integer, index=True)
    updated = Column(DateTime)


class PUPurchaseOrderB(Base):
    __tablename__ = 'PU_PurchaseOrder_b'

    code = Column(Unicode(30))
    quantity = Column(Numeric(28, 14))
    compositionQuantity = Column(Unicode(100))
    quantity2 = Column(Numeric(28, 14))
    unitExchangeRate = Column(Numeric(28, 14))
    price = Column(Numeric(28, 14))
    discountRate = Column(Numeric(28, 14))
    origDiscountPrice = Column(Numeric(28, 14))
    taxRate = Column(Numeric(28, 14))
    origTaxPrice = Column(Numeric(28, 14))
    origDiscountAmount = Column(Numeric(28, 14))
    origTax = Column(Numeric(28, 14))
    countInQuantity2 = Column(Numeric(28, 14))
    origTaxAmount = Column(Numeric(28, 14))
    origDiscount = Column(Numeric(28, 14))
    discountPrice = Column(Numeric(28, 14))
    taxPrice = Column(Numeric(28, 14))
    discountAmount = Column(Numeric(28, 14))
    tax = Column(Numeric(28, 14))
    taxAmount = Column(Numeric(28, 14))
    discount = Column(Numeric(28, 14))
    isPresent = Column(Integer)
    countArrivalQuantity = Column(Numeric(28, 14))
    countArrivalQuantity2 = Column(Numeric(28, 14))
    countInQuantity = Column(Numeric(28, 14))
    countQuantity = Column(Numeric(28, 14))
    countQuantity2 = Column(Numeric(28, 14))
    baseQuantity = Column(Numeric(28, 14))
    subQuantity = Column(Numeric(28, 14))
    taxFlag = Column(Integer)
    saleOrderCode = Column(Unicode(30))
    sourceVoucherCode = Column(Unicode(50))
    origPrice = Column(Numeric(28, 14))
    baseTaxPrice = Column(Numeric(28, 14))
    baseDiscountPrice = Column(Numeric(28, 14))
    basePrice = Column(Numeric(28, 14))
    isNoModify = Column(Unicode(1000))
    arrivalTimes = Column(Integer)
    stockTimes = Column(Integer)
    inventoryBarCode = Column(Unicode(200))
    partnerInventoryCode = Column(Unicode(300))
    ts = Column(TIMESTAMP)
    updatedBy = Column(Unicode(32))
    freeItem0 = Column(Unicode(300))
    freeItem1 = Column(Unicode(300))
    freeItem2 = Column(Unicode(300))
    freeItem3 = Column(Unicode(300))
    freeItem4 = Column(Unicode(300))
    freeItem5 = Column(Unicode(300))
    freeItem6 = Column(Unicode(300))
    freeItem7 = Column(Unicode(300))
    freeItem8 = Column(Unicode(300))
    freeItem9 = Column(Unicode(300))
    priuserdefnvc1 = Column(Unicode(500))
    priuserdefdecm1 = Column(Numeric(28, 14))
    priuserdefnvc2 = Column(Unicode(500))
    priuserdefdecm2 = Column(Numeric(28, 14))
    priuserdefnvc3 = Column(Unicode(500))
    priuserdefdecm3 = Column(Numeric(28, 14))
    priuserdefnvc4 = Column(Unicode(500))
    priuserdefdecm4 = Column(Numeric(28, 14))
    pubuserdefnvc1 = Column(Unicode(500))
    pubuserdefdecm1 = Column(Numeric(28, 14))
    pubuserdefnvc2 = Column(Unicode(500))
    pubuserdefdecm2 = Column(Numeric(28, 14))
    pubuserdefnvc3 = Column(Unicode(500))
    pubuserdefdecm3 = Column(Numeric(28, 14))
    pubuserdefnvc4 = Column(Unicode(500))
    pubuserdefdecm4 = Column(Numeric(28, 14))
    partnerInventoryName = Column(Unicode(300))
    cumInstockShrinkageQuantity = Column(Numeric(28, 14))
    cumInstockShrinkageQuantity2 = Column(Numeric(28, 14))
    islaborcost = Column(Integer)
    detailVoucherState = Column(Unicode(20))
    Retailprice = Column(Numeric(28, 14))
    id = Column(Integer, primary_key=True)
    idinventory = Column(Integer, index=True)
    idproject = Column(Integer, index=True)
    idbaseunit = Column(Integer)
    idsubunit = Column(Integer)
    idunit = Column(Integer)
    idunit2 = Column(Integer)
    idwarehouse = Column(Integer)
    sourceVoucherId = Column(Integer)
    sourceVoucherDetailId = Column(Integer, index=True)
    manufactureOrderId = Column(Integer)
    idPurchaseOrderDTO = Column(Integer, index=True)
    saleOrderId = Column(Integer)
    saleOrderDetailId = Column(Integer)
    idsourcevouchertype = Column(Integer, index=True)
    acceptDate = Column(DateTime)
    updated = Column(DateTime)


t_Pos_Guidtoint = Table(
    'Pos_Guidtoint', metadata,
    Column('Gid', UNIQUEIDENTIFIER),
    Column('iid', Integer)
)


class PuPurchaseArrivalMultiPayment(Base):
    __tablename__ = 'Pu_PurchaseArrival_MultiPayment'

    code = Column(Unicode(30))
    cancelAmount = Column(Numeric(28, 14))
    origCancelAmount = Column(Numeric(28, 14))
    voucherCode = Column(Unicode(30))
    origAmount = Column(Numeric(28, 14))
    origNoCancelAmount = Column(Numeric(28, 14))
    ts = Column(TIMESTAMP, nullable=False)
    updatedBy = Column(Unicode(32))
    SourceVoucherTs = Column(Unicode(1000))
    memo = Column(Unicode(200))
    id = Column(Integer, primary_key=True)
    iddepartment = Column(Integer, index=True)
    idperson = Column(Integer, index=True)
    idproject = Column(Integer)
    idPurchaseArrivalDTO = Column(Integer, index=True)
    voucherID = Column(Integer)
    idvouchertype = Column(Integer, index=True)
    voucherDate = Column(DateTime)
    updated = Column(DateTime)


class PuPurchaseArrivalTrace(Base):
    __tablename__ = 'Pu_PurchaseArrival_Trace'

    code = Column(Unicode(30))
    sourceVoucherCode = Column(Unicode(50))
    ts = Column(TIMESTAMP, nullable=False)
    updatedBy = Column(Unicode(32))
    id = Column(Integer, primary_key=True)
    sourceVoucherID = Column(Integer)
    voucherID = Column(Integer)
    sourceVoucherDetailID = Column(Integer)
    idPurchaseArrivalDetailDTO = Column(Integer, index=True)
    idsourcevouchertype = Column(Integer, index=True)
    updated = Column(DateTime)


class PuPurchaseInvoiceMultiPayment(Base):
    __tablename__ = 'Pu_PurchaseInvoice_MultiPayment'

    code = Column(Unicode(30))
    cancelAmount = Column(Numeric(28, 14))
    origCancelAmount = Column(Numeric(28, 14))
    voucherCode = Column(Unicode(30))
    origAmount = Column(Numeric(28, 14))
    origNoCancelAmount = Column(Numeric(28, 14))
    ts = Column(TIMESTAMP, nullable=False)
    updatedBy = Column(Unicode(32))
    SourceVoucherTs = Column(Unicode(1000))
    memo = Column(Unicode(200))
    id = Column(Integer, primary_key=True)
    iddepartment = Column(Integer, index=True)
    idperson = Column(Integer, index=True)
    idproject = Column(Integer)
    idPurchaseInvoiceDTO = Column(Integer, index=True)
    voucherID = Column(Integer)
    idvouchertype = Column(Integer)
    voucherDate = Column(DateTime)
    updated = Column(DateTime)


class PuPurchaseInvoiceTrace(Base):
    __tablename__ = 'Pu_PurchaseInvoice_Trace'

    code = Column(Unicode(30))
    sourceVoucherCode = Column(Unicode(50))
    ts = Column(TIMESTAMP, nullable=False)
    id = Column(Integer, primary_key=True)
    sourceVoucherID = Column(Integer)
    sourceVoucherDetailID = Column(Integer)
    voucherID = Column(Integer)
    idPurchaseInvoiceDetailDTO = Column(Integer, index=True)
    idsourcevouchertype = Column(Integer, index=True)


class PuPurchaseOrderTrace(Base):
    __tablename__ = 'Pu_PurchaseOrder_Trace'

    code = Column(Unicode(30))
    sourceVoucherCode = Column(Unicode(50))
    ts = Column(TIMESTAMP, nullable=False)
    id = Column(Integer, primary_key=True)
    sourceVoucherID = Column(Integer)
    sourceVoucherDetailID = Column(Integer)
    voucherID = Column(Integer)
    idPurchaseOrderDetailDTO = Column(Integer, index=True)
    SaleTraceGroupID = Column(Integer)
    idsourcevouchertype = Column(Integer, index=True)


class PuPurchaseRequisition(Base):
    __tablename__ = 'Pu_PurchaseRequisition'

    code = Column(Unicode(30), index=True)
    acceptAddress = Column(Unicode(200))
    saleOrderCode = Column(Unicode(50))
    sourceVoucherCode = Column(Unicode(50))
    memo = Column(Unicode(200))
    isNoModify = Column(Unicode(1000))
    maker = Column(Unicode(50))
    auditor = Column(Unicode(50))
    reviser = Column(Unicode(50))
    iscarriedforwardout = Column(Integer)
    iscarriedforwardin = Column(Integer)
    ismodifiedcode = Column(Integer)
    docclass = Column(Unicode(36))
    docid = Column(Unicode(36))
    ts = Column(TIMESTAMP, nullable=False)
    updatedBy = Column(Unicode(32))
    priuserdefnvc1 = Column(Unicode(500))
    priuserdefdecm1 = Column(Numeric(28, 14))
    priuserdefnvc2 = Column(Unicode(500))
    priuserdefdecm2 = Column(Numeric(28, 14))
    priuserdefnvc3 = Column(Unicode(500))
    priuserdefdecm3 = Column(Numeric(28, 14))
    priuserdefnvc4 = Column(Unicode(500))
    priuserdefdecm4 = Column(Numeric(28, 14))
    priuserdefnvc5 = Column(Unicode(500))
    priuserdefdecm5 = Column(Numeric(28, 14))
    priuserdefnvc6 = Column(Unicode(500))
    priuserdefdecm6 = Column(Numeric(28, 14))
    pubuserdefnvc1 = Column(Unicode(500))
    pubuserdefdecm1 = Column(Numeric(28, 14))
    pubuserdefnvc2 = Column(Unicode(500))
    pubuserdefdecm2 = Column(Numeric(28, 14))
    pubuserdefnvc3 = Column(Unicode(500))
    pubuserdefdecm3 = Column(Numeric(28, 14))
    pubuserdefnvc4 = Column(Unicode(500))
    pubuserdefdecm4 = Column(Numeric(28, 14))
    pubuserdefnvc5 = Column(Unicode(500))
    pubuserdefdecm5 = Column(Numeric(28, 14))
    pubuserdefnvc6 = Column(Unicode(500))
    pubuserdefdecm6 = Column(Numeric(28, 14))
    OrigTotalAmount = Column(Numeric(28, 14))
    TotalAmount = Column(Numeric(28, 14))
    OrigTotalTaxAmount = Column(Numeric(28, 14))
    TotalTaxAmount = Column(Numeric(28, 14))
    PrintCount = Column(Integer)
    id = Column(Integer, primary_key=True)
    iddepartment = Column(Integer, index=True)
    idmarketingOrgan = Column(Integer)
    idsuggpartner = Column(Integer, index=True)
    idrequisitionperson = Column(Integer, index=True)
    idproject = Column(Integer, index=True)
    voucherState = Column(Integer)
    auditorid = Column(Integer)
    makerid = Column(Integer)
    idsourcevouchertype = Column(Integer, index=True)
    requireDate = Column(DateTime)
    sourceVoucherDate = Column(DateTime)
    voucherdate = Column(DateTime, index=True)
    madedate = Column(DateTime)
    auditeddate = Column(DateTime)
    createdtime = Column(DateTime, index=True)
    updated = Column(DateTime)


class PuPurchaseRequisitionSourceRelation(Base):
    __tablename__ = 'Pu_PurchaseRequisition_SourceRelation'

    code = Column(Unicode(30))
    quantity = Column(Numeric(28, 14))
    unitExchangeRate = Column(Numeric(28, 14))
    quantity2 = Column(Numeric(28, 14))
    baseQuantity = Column(Numeric(28, 14))
    subQuantity = Column(Numeric(28, 14))
    ts = Column(TIMESTAMP, nullable=False)
    updatedBy = Column(Unicode(32))
    id = Column(Integer, primary_key=True)
    idbaseunit = Column(Integer)
    idsubunit = Column(Integer)
    idunit = Column(Integer)
    idunit2 = Column(Integer)
    sourceVoucherID = Column(Integer)
    sourceVoucherDetailID = Column(Integer)
    voucherID = Column(Integer)
    idPurchaseRequisitionDetailDTO = Column(Integer, index=True)
    idsourcevouchertype = Column(Integer, index=True)
    updated = Column(DateTime)


class PuPurchaseRequisitionTrace(Base):
    __tablename__ = 'Pu_PurchaseRequisition_Trace'

    code = Column(Unicode(30))
    sourceVoucherCode = Column(Unicode(50))
    ts = Column(TIMESTAMP, nullable=False)
    id = Column(Integer, primary_key=True)
    sourceVoucherID = Column(Integer)
    sourceVoucherDetailID = Column(Integer)
    voucherID = Column(Integer)
    idPurchaseRequisitionDetailDTO = Column(Integer, index=True)
    SaleTraceGroupID = Column(Integer)
    idsourcevouchertype = Column(Integer, index=True)


class PuPurchaseRequisitionB(Base):
    __tablename__ = 'Pu_PurchaseRequisition_b'

    code = Column(Unicode(30))
    inventoryBarCode = Column(Unicode(200))
    quantity = Column(Numeric(28, 14))
    unitExchangeRate = Column(Numeric(28, 14))
    quantity2 = Column(Numeric(28, 14))
    compositionQuantity = Column(Unicode(100))
    price = Column(Numeric(28, 14))
    discountRate = Column(Numeric(28, 14))
    discountPrice = Column(Numeric(28, 14))
    taxRate = Column(Numeric(28, 14))
    taxPrice = Column(Numeric(28, 14))
    discountAmount = Column(Numeric(28, 14))
    tax = Column(Numeric(28, 14))
    taxAmount = Column(Numeric(28, 14))
    discount = Column(Numeric(28, 14))
    cumExecuteQuantity = Column(Numeric(28, 14))
    cumExecuteQuantity2 = Column(Numeric(28, 14))
    isPraRequire = Column(Integer)
    sourceVoucherCode = Column(Unicode(50))
    saleOrderCode = Column(Unicode(50))
    baseQuantity = Column(Numeric(28, 14))
    subQuantity = Column(Numeric(28, 14))
    praRequireTimes = Column(Integer)
    ts = Column(TIMESTAMP, nullable=False)
    updatedBy = Column(Unicode(32))
    freeItem0 = Column(Unicode(300))
    freeItem1 = Column(Unicode(300))
    freeItem2 = Column(Unicode(300))
    freeItem3 = Column(Unicode(300))
    freeItem4 = Column(Unicode(300))
    freeItem5 = Column(Unicode(300))
    freeItem6 = Column(Unicode(300))
    freeItem7 = Column(Unicode(300))
    freeItem8 = Column(Unicode(300))
    freeItem9 = Column(Unicode(300))
    priuserdefnvc1 = Column(Unicode(500))
    priuserdefdecm1 = Column(Numeric(28, 14))
    priuserdefnvc2 = Column(Unicode(500))
    priuserdefdecm2 = Column(Numeric(28, 14))
    priuserdefnvc3 = Column(Unicode(500))
    priuserdefdecm3 = Column(Numeric(28, 14))
    priuserdefnvc4 = Column(Unicode(500))
    priuserdefdecm4 = Column(Numeric(28, 14))
    pubuserdefnvc1 = Column(Unicode(500))
    pubuserdefdecm1 = Column(Numeric(28, 14))
    pubuserdefnvc2 = Column(Unicode(500))
    pubuserdefdecm2 = Column(Numeric(28, 14))
    pubuserdefnvc3 = Column(Unicode(500))
    pubuserdefdecm3 = Column(Numeric(28, 14))
    pubuserdefnvc4 = Column(Unicode(500))
    pubuserdefdecm4 = Column(Numeric(28, 14))
    taxFlag = Column(Integer)
    baseCumExecuteQuantity = Column(Numeric(28, 14))
    subCumExecuteQuantity = Column(Numeric(28, 14))
    isNoModify = Column(Unicode(1000))
    islaborcost = Column(Integer)
    Retailprice = Column(Numeric(28, 14))
    id = Column(Integer, primary_key=True)
    idinventory = Column(Integer, index=True)
    idsuggpartner = Column(Integer, index=True)
    idproject = Column(Integer, index=True)
    idbaseunit = Column(Integer)
    idsubunit = Column(Integer)
    idunit = Column(Integer)
    idunit2 = Column(Integer)
    sourceVoucherId = Column(Integer)
    sourceVoucherDetailId = Column(Integer)
    idPurchaseRequisitionDTO = Column(Integer, index=True)
    saleOrderId = Column(Integer)
    saleOrderDetailId = Column(Integer)
    idsourcevouchertype = Column(Integer, index=True)
    requireDate = Column(DateTime)
    updated = Column(DateTime)


t_RE_BatchSaleOutController = Table(
    'RE_BatchSaleOutController', metadata,
    Column('flag', Integer),
    Column('username', Unicode(200)),
    Column('createdtime', String(19, u'Chinese_PRC_CI_AS')),
    Column('isAuto', Integer, server_default=text("((0))")),
    Column('idstore', Integer)
)


class REDailyDetail(Base):
    __tablename__ = 'RE_DailyDetail'

    code = Column(Unicode(50))
    name = Column(Unicode(200))
    docno = Column(Unicode(36))
    docclass = Column(Unicode(36))
    accountingperiod = Column(Integer)
    docid = Column(Unicode(36))
    accountingyear = Column(Integer)
    memo = Column(Unicode(200))
    voucherdate = Column(String(19, u'Chinese_PRC_CI_AS'))
    madedate = Column(String(19, u'Chinese_PRC_CI_AS'))
    maker = Column(Unicode(50))
    auditor = Column(Unicode(50))
    auditeddate = Column(String(19, u'Chinese_PRC_CI_AS'))
    reviser = Column(Unicode(50))
    iscarriedforwardout = Column(Integer)
    iscarriedforwardin = Column(Integer)
    ismodifiedcode = Column(Integer)
    createdtime = Column(String(19, u'Chinese_PRC_CI_AS'))
    sequencenumber = Column(Integer)
    uploadtime = Column(String(19, u'Chinese_PRC_CI_AS'))
    poscode = Column(Unicode(50))
    pos = Column(Unicode(50))
    usercode = Column(Unicode(50))
    username = Column(Unicode(50))
    ts = Column(TIMESTAMP, nullable=False)
    updated = Column(String(19, u'Chinese_PRC_CI_AS'))
    updatedBy = Column(Unicode(32))
    isUnClosed = Column(Integer)
    startdate = Column(String(19, u'Chinese_PRC_CI_AS'))
    starttime = Column(String(8, u'Chinese_PRC_CI_AS'))
    dailydate = Column(String(19, u'Chinese_PRC_CI_AS'))
    dailytime = Column(String(8, u'Chinese_PRC_CI_AS'))
    retailcount = Column(Numeric(28, 14))
    retailamount = Column(Numeric(28, 14))
    retailreturncount = Column(Numeric(28, 14))
    returnamount = Column(Numeric(28, 14))
    removecount = Column(Numeric(28, 14))
    removeamount = Column(Numeric(28, 14))
    totalcount = Column(Integer)
    price = Column(Numeric(28, 14))
    totalsettleamount = Column(Numeric(28, 14))
    initialamount = Column(Numeric(28, 14))
    imprestamount = Column(Numeric(28, 14))
    voucherdiscountamount = Column(Numeric(28, 14))
    Id = Column(Integer, primary_key=True)
    idstore = Column(Integer)
    idmarketingorgan = Column(Integer)
    iscancel = Column(Integer)
    voucherstate = Column(Integer)
    dailystate = Column(Integer)
    auditorid = Column(Integer)
    makerid = Column(Integer)
    userid = Column(Integer)


class REDailyDetailB(Base):
    __tablename__ = 'RE_DailyDetail_b'

    code = Column(Unicode(30))
    name = Column(Unicode(200))
    createdtime = Column(String(19, u'Chinese_PRC_CI_AS'))
    sequencenumber = Column(Integer)
    origamount = Column(Numeric(28, 14))
    amount = Column(Numeric(28, 14))
    origsettleamount = Column(Numeric(28, 14))
    settleamount = Column(Numeric(28, 14))
    initialamount = Column(Numeric(28, 14))
    imprestamount = Column(Numeric(28, 14))
    ts = Column(TIMESTAMP, nullable=False)
    updated = Column(String(19, u'Chinese_PRC_CI_AS'))
    updatedBy = Column(Unicode(32))
    id = Column(Integer, primary_key=True)
    idbankaccount = Column(Integer)
    idsettlestyle = Column(Integer)
    idDailyDetailDTO = Column(Integer)


class REReceiveDetail(Base):
    __tablename__ = 'RE_ReceiveDetail'

    code = Column(Unicode(30))
    name = Column(Unicode(200))
    createdtime = Column(String(19, u'Chinese_PRC_CI_AS'))
    sequencenumber = Column(Integer)
    iscarriedforwardout = Column(Integer)
    iscarriedforwardin = Column(Integer)
    shiftvouchercode = Column(Unicode(50))
    shiftvoucherdate = Column(String(19, u'Chinese_PRC_CI_AS'))
    poscode = Column(Unicode(50))
    posname = Column(Unicode(50))
    usercode = Column(Unicode(50))
    username = Column(Unicode(50))
    receivercode = Column(Unicode(50))
    receivername = Column(Unicode(50))
    workingdate = Column(String(19, u'Chinese_PRC_CI_AS'))
    workingtime = Column(Unicode(8))
    shiftdate = Column(String(19, u'Chinese_PRC_CI_AS'))
    shifttime = Column(String(8, u'Chinese_PRC_CI_AS'))
    receivedate = Column(String(19, u'Chinese_PRC_CI_AS'))
    receivetime = Column(String(8, u'Chinese_PRC_CI_AS'))
    origamount = Column(Numeric(28, 14))
    origsettleamount = Column(Numeric(28, 14))
    origfactsettleamount = Column(Numeric(28, 14))
    amount = Column(Numeric(28, 14))
    settleamount = Column(Numeric(28, 14))
    factsettleamount = Column(Numeric(28, 14))
    initialamount = Column(Numeric(28, 14))
    imprestamount = Column(Numeric(28, 14))
    imprestbalanceamount = Column(Numeric(28, 14))
    extendflag = Column(Integer)
    exchangerate = Column(Numeric(28, 14))
    ts = Column(TIMESTAMP, nullable=False)
    updated = Column(String(19, u'Chinese_PRC_CI_AS'))
    updatedBy = Column(Unicode(32))
    dailyDetailCode = Column(Unicode(50))
    dailyDetailDate = Column(String(19, u'Chinese_PRC_CI_AS'))
    dailyTime = Column(String(8, u'Chinese_PRC_CI_AS'))
    id = Column(Integer, primary_key=True)
    idbankaccount = Column(Integer)
    idreceivebankaccount = Column(Integer)
    idcurrency = Column(Integer)
    idstore = Column(Integer)
    idsettlestyle = Column(Integer)
    userid = Column(Integer)
    receiverid = Column(Integer)
    dailyDetailID = Column(Integer)
    shiftvoucherid = Column(Integer)


class REReceiveDetailB(Base):
    __tablename__ = 'RE_ReceiveDetail_b'

    RetailCode = Column(Unicode(50))
    createdtime = Column(String(19, u'Chinese_PRC_CI_AS'))
    ts = Column(TIMESTAMP, nullable=False)
    id = Column(Integer, primary_key=True)
    idReceiveDetailDTO = Column(Integer)
    idRetailDTO = Column(Integer)


class RERetail(Base):
    __tablename__ = 'RE_Retail'

    code = Column(Unicode(50))
    name = Column(Unicode(200))
    docno = Column(Unicode(36))
    docclass = Column(Unicode(36))
    accountingperiod = Column(Integer)
    docid = Column(Unicode(36))
    accountingyear = Column(Integer)
    memo = Column(Unicode(200))
    voucherdate = Column(String(19, u'Chinese_PRC_CI_AS'))
    madedate = Column(String(19, u'Chinese_PRC_CI_AS'))
    maker = Column(Unicode(50))
    auditor = Column(Unicode(50))
    auditeddate = Column(String(19, u'Chinese_PRC_CI_AS'))
    reviser = Column(Unicode(50))
    iscarriedforwardout = Column(Integer)
    iscarriedforwardin = Column(Integer)
    ismodifiedcode = Column(Integer)
    createdtime = Column(String(19, u'Chinese_PRC_CI_AS'))
    sequencenumber = Column(Integer)
    customername = Column(Unicode(50))
    customeraddress = Column(Unicode(50))
    customerlinkman = Column(Unicode(50))
    customerphone = Column(Unicode(50))
    customerrequest = Column(Unicode(50))
    shiftcode = Column(Unicode(50))
    auditedtime = Column(String(8, u'Chinese_PRC_CI_AS'))
    poscode = Column(Unicode(50))
    posname = Column(Unicode(50))
    isdealed = Column(Integer, nullable=False, server_default=text("((0))"))
    totalretailamount = Column(Numeric(28, 14))
    totaltaxamount = Column(Numeric(28, 14))
    discountsandallowances = Column(Numeric(28, 14))
    totaldiscountamount = Column(Numeric(28, 14))
    wipechange = Column(Numeric(28, 14))
    integral = Column(Numeric(28, 14))
    iscleared = Column(Integer)
    usercode = Column(Unicode(50))
    username = Column(Unicode(50))
    ts = Column(TIMESTAMP, nullable=False)
    updated = Column(String(19, u'Chinese_PRC_CI_AS'))
    updatedBy = Column(Unicode(32))
    priuserdefnvc1 = Column(Unicode(500))
    priuserdefdecm1 = Column(Numeric(28, 14))
    priuserdefnvc2 = Column(Unicode(500))
    priuserdefdecm2 = Column(Numeric(28, 14))
    priuserdefnvc3 = Column(Unicode(500))
    priuserdefdecm3 = Column(Numeric(28, 14))
    priuserdefnvc4 = Column(Unicode(500))
    priuserdefdecm4 = Column(Numeric(28, 14))
    priuserdefnvc5 = Column(Unicode(500))
    priuserdefdecm5 = Column(Numeric(28, 14))
    priuserdefnvc6 = Column(Unicode(500))
    priuserdefdecm6 = Column(Numeric(28, 14))
    pubuserdefnvc1 = Column(Unicode(100))
    pubuserdefdecm1 = Column(Numeric(28, 14))
    pubuserdefnvc2 = Column(Unicode(100))
    pubuserdefdecm2 = Column(Numeric(28, 14))
    pubuserdefnvc3 = Column(Unicode(100))
    pubuserdefdecm3 = Column(Numeric(28, 14))
    pubuserdefnvc4 = Column(Unicode(100))
    pubuserdefdecm4 = Column(Numeric(28, 14))
    pubuserdefnvc5 = Column(Unicode(100))
    pubuserdefdecm5 = Column(Numeric(28, 14))
    pubuserdefnvc6 = Column(Unicode(100))
    pubuserdefdecm6 = Column(Numeric(28, 14))
    SteadCashIntegral = Column(Numeric(28, 14))
    receivingmaturity = Column(String(19, u'Chinese_PRC_CI_AS'))
    balancestorage = Column(Numeric(28, 14))
    dailycode = Column(Unicode(50))
    storagesettleamount = Column(Numeric(28, 14))
    integralsteadcashamount = Column(Numeric(28, 14))
    givechangeforstorageamount = Column(Numeric(28, 14))
    PrintCount = Column(Integer)
    balanceintegral = Column(Numeric(28, 14))
    RetailSettleCode = Column(Unicode(50))
    ExternalCode = Column(Unicode(30))
    id = Column(Integer, primary_key=True)
    idbusitype = Column(Integer)
    idmember = Column(Integer)
    idstore = Column(Integer)
    idmarketingorgan = Column(Integer)
    idperson = Column(Integer)
    idRetailSettle = Column(Integer)
    idDepartment_Store = Column(Integer)
    idDistrict_Member = Column(Integer)
    idMembertype = Column(Integer)
    iscancel = Column(Integer)
    issaleout = Column(Integer)
    shift = Column(Integer)
    voucherstate = Column(Integer)
    auditorid = Column(Integer)
    makerid = Column(Integer)
    userid = Column(Integer)
    iddailyvoucher = Column(Integer)
    idshiftvoucher = Column(Integer)


class RERetailDetailMerge(Base):
    __tablename__ = 'RE_RetailDetail_Merge'

    code = Column(Unicode(30))
    name = Column(Unicode(200))
    createdtime = Column(String(19, u'Chinese_PRC_CI_AS'))
    sequencenumber = Column(Integer)
    ts = Column(TIMESTAMP, nullable=False)
    updated = Column(String(19, u'Chinese_PRC_CI_AS'))
    updatedBy = Column(Unicode(32))
    id = Column(Integer, primary_key=True)
    sourcevoucherid = Column(Integer)
    vourcherid = Column(Integer)
    idRetailSettleDTO = Column(Integer)
    idVoucherType = Column(Integer)


class RERetailSettle(Base):
    __tablename__ = 'RE_RetailSettle'

    code = Column(Unicode(30))
    name = Column(Unicode(200))
    docno = Column(Unicode(36))
    docclass = Column(Unicode(36))
    accountingperiod = Column(Integer)
    docid = Column(Unicode(36))
    accountingyear = Column(Integer)
    memo = Column(Unicode(200))
    voucherdate = Column(String(19, u'Chinese_PRC_CI_AS'))
    madedate = Column(String(19, u'Chinese_PRC_CI_AS'))
    maker = Column(Unicode(50))
    auditor = Column(Unicode(50))
    auditeddate = Column(String(19, u'Chinese_PRC_CI_AS'))
    reviser = Column(Unicode(50))
    iscarriedforwardout = Column(Integer)
    iscarriedforwardin = Column(Integer)
    ismodifiedcode = Column(Integer)
    createdtime = Column(String(19, u'Chinese_PRC_CI_AS'))
    sequencenumber = Column(Integer)
    settleamount = Column(Numeric(28, 14))
    receivingmaturity = Column(String(19, u'Chinese_PRC_CI_AS'))
    deductionrate = Column(Numeric(28, 14))
    isauto = Column(Integer, server_default=text("((0))"))
    totalSettleAmount = Column(Numeric(28, 14))
    totalAmount = Column(Numeric(28, 14))
    totalTaxAmount = Column(Numeric(28, 14))
    totalSettleTax = Column(Numeric(28, 14))
    totalSettleTaxAmount = Column(Numeric(28, 14))
    wipechange = Column(Numeric(28, 14))
    ts = Column(TIMESTAMP, nullable=False)
    updated = Column(String(19, u'Chinese_PRC_CI_AS'))
    updatedBy = Column(Unicode(32))
    priuserdefnvc1 = Column(Unicode(500))
    priuserdefdecm1 = Column(Numeric(28, 14))
    priuserdefnvc2 = Column(Unicode(500))
    priuserdefdecm2 = Column(Numeric(28, 14))
    priuserdefnvc3 = Column(Unicode(500))
    priuserdefdecm3 = Column(Numeric(28, 14))
    priuserdefnvc4 = Column(Unicode(500))
    priuserdefdecm4 = Column(Numeric(28, 14))
    priuserdefnvc5 = Column(Unicode(500))
    priuserdefdecm5 = Column(Numeric(28, 14))
    priuserdefnvc6 = Column(Unicode(500))
    priuserdefdecm6 = Column(Numeric(28, 14))
    pubuserdefnvc1 = Column(Unicode(500))
    pubuserdefdecm1 = Column(Numeric(28, 14))
    pubuserdefnvc2 = Column(Unicode(500))
    pubuserdefdecm2 = Column(Numeric(28, 14))
    pubuserdefnvc3 = Column(Unicode(500))
    pubuserdefdecm3 = Column(Numeric(28, 14))
    pubuserdefnvc4 = Column(Unicode(500))
    pubuserdefdecm4 = Column(Numeric(28, 14))
    pubuserdefnvc5 = Column(Unicode(500))
    pubuserdefdecm5 = Column(Numeric(28, 14))
    pubuserdefnvc6 = Column(Unicode(500))
    pubuserdefdecm6 = Column(Numeric(28, 14))
    UseStorageAmount = Column(Numeric(28, 14))
    IntegralStorageAmount = Column(Numeric(28, 14))
    PreReceiveAmount = Column(Numeric(28, 14))
    ConvertToStorageAmount = Column(Numeric(28, 14))
    PrintCount = Column(Integer)
    ID = Column(Integer, primary_key=True)
    idstore = Column(Integer)
    idmarketingorgan = Column(Integer)
    idcustomer = Column(Integer)
    idsettlecustomer = Column(Integer)
    idperson = Column(Integer)
    idproject = Column(Integer)
    branchstrikebalance = Column(Integer)
    datasource = Column(Integer)
    headquartersstrikebalance = Column(Integer)
    iscancle = Column(Integer)
    receivetype = Column(Integer)
    voucherstate = Column(Integer)
    auditorid = Column(Integer)
    makerid = Column(Integer)


class RERetailSettleMutiSettle(Base):
    __tablename__ = 'RE_RetailSettle_MutiSettle'

    code = Column(Unicode(30))
    name = Column(Unicode(200))
    createdtime = Column(String(19, u'Chinese_PRC_CI_AS'))
    sequencenumber = Column(Integer)
    amount = Column(Numeric(28, 14))
    billno = Column(Unicode(30))
    ts = Column(TIMESTAMP, nullable=False)
    updated = Column(String(19, u'Chinese_PRC_CI_AS'))
    updatedBy = Column(Unicode(32))
    id = Column(Integer, primary_key=True)
    idbankaccount = Column(Integer)
    idsettlestyle = Column(Integer)
    idRetailSettleDTO = Column(Integer)


class RERetailSettlePreReceive(Base):
    __tablename__ = 'RE_RetailSettle_PreReceive'

    code = Column(Unicode(30))
    name = Column(Unicode(200))
    voucherdate = Column(String(19, u'Chinese_PRC_CI_AS'))
    vouchercode = Column(Unicode(50))
    origamount = Column(Numeric(28, 14))
    orignocancelamount = Column(Numeric(28, 14))
    origcancelamount = Column(Numeric(28, 14))
    cancelamount = Column(Numeric(28, 14))
    createdtime = Column(String(19, u'Chinese_PRC_CI_AS'))
    sequencenumber = Column(Integer)
    ts = Column(TIMESTAMP)
    updated = Column(String(19, u'Chinese_PRC_CI_AS'))
    updatedBy = Column(Unicode(32))
    SourceVoucherCode = Column(Unicode(30))
    SourceVoucherTs = Column(Unicode(1000))
    id = Column(Integer, primary_key=True)
    iddepartment = Column(Integer)
    idperson = Column(Integer)
    voucherid = Column(Integer)
    SourceVoucherId = Column(Integer)
    idRetailSettleDTO = Column(Integer)
    idVoucherType = Column(Integer)


class RERetailSettleB(Base):
    __tablename__ = 'RE_RetailSettle_b'

    code = Column(Unicode(30))
    name = Column(Unicode(200))
    createdtime = Column(String(19, u'Chinese_PRC_CI_AS'))
    sequencenumber = Column(Integer)
    ispresent = Column(Integer)
    quantity = Column(Numeric(28, 14))
    retailprice = Column(Numeric(28, 14))
    discountrate = Column(Numeric(28, 14))
    price = Column(Numeric(28, 14))
    taxrate = Column(Numeric(28, 14))
    taxprice = Column(Numeric(28, 14))
    amount = Column(Numeric(28, 14))
    taxamount = Column(Numeric(28, 14))
    tax = Column(Numeric(28, 14))
    deductionrate = Column(Numeric(28, 14))
    settleamount = Column(Numeric(28, 14))
    settleTax = Column(Numeric(28, 14))
    settleTaxAmount = Column(Numeric(28, 14))
    totalsettleamount = Column(Numeric(28, 14))
    expenseamount = Column(Numeric(28, 14))
    wipechange = Column(Numeric(28, 14))
    issource = Column(Integer, server_default=text("((1))"))
    taxflag = Column(Integer)
    ts = Column(TIMESTAMP, nullable=False)
    updated = Column(String(19, u'Chinese_PRC_CI_AS'))
    updatedBy = Column(Unicode(32))
    priuserdefnvc0 = Column(Unicode(100))
    priuserdefdecm0 = Column(Numeric(28, 14))
    priuserdefnvc1 = Column(Unicode(500))
    priuserdefdecm1 = Column(Numeric(28, 14))
    priuserdefnvc2 = Column(Unicode(500))
    priuserdefdecm2 = Column(Numeric(28, 14))
    priuserdefnvc3 = Column(Unicode(500))
    priuserdefdecm3 = Column(Numeric(28, 14))
    priuserdefnvc4 = Column(Unicode(500))
    priuserdefdecm4 = Column(Numeric(28, 14))
    pubuserdefnvc1 = Column(Unicode(500))
    pubuserdefdecm1 = Column(Numeric(28, 14))
    pubuserdefnvc2 = Column(Unicode(500))
    pubuserdefdecm2 = Column(Numeric(28, 14))
    pubuserdefnvc3 = Column(Unicode(500))
    pubuserdefdecm3 = Column(Numeric(28, 14))
    pubuserdefnvc4 = Column(Unicode(500))
    pubuserdefdecm4 = Column(Numeric(28, 14))
    freeItem0 = Column(Unicode(300))
    freeItem1 = Column(Unicode(300))
    freeItem2 = Column(Unicode(300))
    freeItem3 = Column(Unicode(300))
    freeItem4 = Column(Unicode(300))
    freeItem5 = Column(Unicode(300))
    freeItem6 = Column(Unicode(300))
    freeItem7 = Column(Unicode(300))
    freeItem8 = Column(Unicode(300))
    freeItem9 = Column(Unicode(300))
    VirtualSettleAmount = Column(Numeric(28, 14))
    CashSettleAmount = Column(Numeric(28, 14))
    VirtualDeductionAmount = Column(Numeric(28, 14))
    CashDeductionAmount = Column(Numeric(28, 14))
    StorageSettleAmount = Column(Numeric(28, 14))
    unitExchangeRate = Column(Numeric(28, 14))
    quantity2 = Column(Numeric(28, 14))
    baseQuantity = Column(Numeric(28, 14))
    subQuantity = Column(Numeric(28, 14))
    ID = Column(Integer, primary_key=True)
    idmember = Column(Integer)
    idinventory = Column(Integer)
    idunit = Column(Integer)
    idunit2 = Column(Integer)
    idbaseunit = Column(Integer)
    idsubunit = Column(Integer)
    idDistrict_Member = Column(Integer)
    idMembertype = Column(Integer)
    idperson = Column(Integer)
    promotiontype = Column(Integer)
    idRetailSettleDTO = Column(Integer)


class RERetailPayment(Base):
    __tablename__ = 'RE_Retail_Payment'

    code = Column(Unicode(30))
    name = Column(Unicode(200))
    createdtime = Column(String(19, u'Chinese_PRC_CI_AS'))
    sequencenumber = Column(Integer)
    memo = Column(Unicode(50))
    origamount = Column(Numeric(28, 14))
    amount = Column(Numeric(28, 14))
    givechange = Column(Numeric(28, 14))
    exchangerate = Column(Numeric(28, 14))
    ts = Column(TIMESTAMP, nullable=False)
    updated = Column(String(19, u'Chinese_PRC_CI_AS'))
    updatedBy = Column(Unicode(32))
    OverchargesAmount = Column(Numeric(28, 14))
    steadCashIntegral = Column(Numeric(28, 14))
    givechangeforstorage = Column(Numeric(28, 14))
    integralforstorage = Column(Numeric(28, 14))
    id = Column(Integer, primary_key=True)
    idbankaccount = Column(Integer)
    idcurrency = Column(Integer)
    idsettlestyle = Column(Integer)
    idRetailDTO = Column(Integer)


class RERetailPaymentBak(Base):
    __tablename__ = 'RE_Retail_Payment_bak'

    code = Column(Unicode(30))
    name = Column(Unicode(200))
    createdtime = Column(String(19, u'Chinese_PRC_CI_AS'))
    sequencenumber = Column(Integer)
    memo = Column(Unicode(50))
    origamount = Column(Numeric(28, 14))
    amount = Column(Numeric(28, 14))
    givechange = Column(Numeric(28, 14))
    exchangerate = Column(Numeric(28, 14))
    ts = Column(TIMESTAMP, nullable=False)
    updated = Column(String(19, u'Chinese_PRC_CI_AS'))
    updatedBy = Column(Unicode(32))
    OverchargesAmount = Column(Numeric(28, 14))
    steadCashIntegral = Column(Numeric(28, 14))
    givechangeforstorage = Column(Numeric(28, 14))
    integralforstorage = Column(Numeric(28, 14))
    id = Column(Integer, primary_key=True)
    idbankaccount = Column(Integer)
    idcurrency = Column(Integer)
    idsettlestyle = Column(Integer)
    idRetailDTO = Column(Integer)


class RERetailStorage(Base):
    __tablename__ = 'RE_Retail_Storage'

    code = Column(Unicode(30))
    name = Column(Unicode(200))
    createdtime = Column(String(19, u'Chinese_PRC_CI_AS'))
    sequencenumber = Column(Integer)
    storagepaymentamount = Column(Numeric(28, 14))
    balancestorage = Column(Numeric(28, 14))
    ts = Column(TIMESTAMP, nullable=False)
    updated = Column(String(19, u'Chinese_PRC_CI_AS'))
    updatedBy = Column(Unicode(32))
    id = Column(Integer, primary_key=True)
    idmember = Column(Integer)
    idRetailDTO = Column(Integer)


class RERetailStorageBak(Base):
    __tablename__ = 'RE_Retail_Storage_bak'

    code = Column(Unicode(30))
    name = Column(Unicode(200))
    createdtime = Column(String(19, u'Chinese_PRC_CI_AS'))
    sequencenumber = Column(Integer)
    storagepaymentamount = Column(Numeric(28, 14))
    balancestorage = Column(Numeric(28, 14))
    ts = Column(TIMESTAMP, nullable=False)
    updated = Column(String(19, u'Chinese_PRC_CI_AS'))
    updatedBy = Column(Unicode(32))
    id = Column(Integer, primary_key=True)
    idmember = Column(Integer)
    idRetailDTO = Column(Integer)


class RERetailB(Base):
    __tablename__ = 'RE_Retail_b'

    code = Column(Unicode(30))
    name = Column(Unicode(200))
    createdtime = Column(String(19, u'Chinese_PRC_CI_AS'))
    sequencenumber = Column(Integer)
    promotioncode = Column(Unicode(50))
    ispresent = Column(Integer)
    inventorybarcode = Column(Unicode(50))
    quantity = Column(Numeric(28, 14))
    basequantity = Column(Numeric(28, 14))
    subquantity = Column(Numeric(28, 14))
    retailprice = Column(Numeric(28, 14))
    memberprice = Column(Numeric(28, 14))
    memberdiscountrate = Column(Numeric(28, 14))
    discountrate = Column(Numeric(28, 14))
    price = Column(Numeric(28, 14))
    retailamount = Column(Numeric(28, 14))
    amount = Column(Numeric(28, 14))
    taxrate = Column(Numeric(28, 14))
    taxprice = Column(Numeric(28, 14))
    tax = Column(Numeric(28, 14))
    taxamount = Column(Numeric(28, 14))
    detailDiscountAmount = Column(Numeric(28, 14))
    memo = Column(Unicode(200))
    isdel = Column(Integer)
    batch = Column(Unicode(50))
    expirydate = Column(String(19, u'Chinese_PRC_CI_AS'))
    unitexchangerate = Column(Numeric(28, 14))
    ts = Column(TIMESTAMP, nullable=False)
    updated = Column(String(19, u'Chinese_PRC_CI_AS'))
    updatedBy = Column(Unicode(32))
    priuserdefnvc1 = Column(Unicode(500))
    priuserdefdecm1 = Column(Numeric(28, 14))
    priuserdefnvc2 = Column(Unicode(500))
    priuserdefdecm2 = Column(Numeric(28, 14))
    priuserdefnvc3 = Column(Unicode(500))
    priuserdefdecm3 = Column(Numeric(28, 14))
    priuserdefnvc4 = Column(Unicode(500))
    priuserdefdecm4 = Column(Numeric(28, 14))
    pubuserdefnvc1 = Column(Unicode(100))
    pubuserdefdecm1 = Column(Numeric(28, 14))
    pubuserdefnvc2 = Column(Unicode(100))
    pubuserdefdecm2 = Column(Numeric(28, 14))
    pubuserdefnvc3 = Column(Unicode(100))
    pubuserdefdecm3 = Column(Numeric(28, 14))
    pubuserdefnvc4 = Column(Unicode(100))
    freeItem0 = Column(Unicode(300))
    freeItem1 = Column(Unicode(300))
    pubuserdefdecm4 = Column(Numeric(28, 14))
    freeItem2 = Column(Unicode(300))
    freeItem3 = Column(Unicode(300))
    freeItem4 = Column(Unicode(300))
    freeItem5 = Column(Unicode(300))
    freeItem6 = Column(Unicode(300))
    freeItem7 = Column(Unicode(300))
    freeItem8 = Column(Unicode(300))
    freeItem9 = Column(Unicode(300))
    CashSettleAmount = Column(Numeric(28, 14))
    VirtualSettleAmount = Column(Numeric(28, 14))
    storagesettleamount = Column(Numeric(28, 14))
    isuseintegralandcash = Column(Integer)
    isusestorage = Column(Integer)
    ismemberstorageprojet = Column(Integer)
    discountAuthorize = Column(Unicode(50))
    quantity2 = Column(Numeric(28, 14))
    ProductionDate = Column(String(19, u'Chinese_PRC_CI_AS'))
    RdRecordCode = Column(Unicode(50))
    id = Column(Integer, primary_key=True)
    idinventory = Column(Integer)
    idperson = Column(Integer)
    idbaseUnit = Column(Integer)
    idsubUnit = Column(Integer)
    idunit = Column(Integer)
    discountAuthorizeId = Column(Integer)
    idunit2 = Column(Integer)
    idRdRecord = Column(Integer)
    issaleout = Column(Integer)
    promotiontype = Column(Integer)
    promotionid = Column(Integer)
    limitedsaleid = Column(Integer)
    limitedsalesubid = Column(Integer)
    idRetailDTO = Column(Integer)


class RERetailBBak(Base):
    __tablename__ = 'RE_Retail_b_bak'

    code = Column(Unicode(30))
    name = Column(Unicode(200))
    createdtime = Column(String(19, u'Chinese_PRC_CI_AS'))
    sequencenumber = Column(Integer)
    promotioncode = Column(Unicode(50))
    ispresent = Column(Integer)
    inventorybarcode = Column(Unicode(50))
    quantity = Column(Numeric(28, 14))
    basequantity = Column(Numeric(28, 14))
    subquantity = Column(Numeric(28, 14))
    retailprice = Column(Numeric(28, 14))
    memberprice = Column(Numeric(28, 14))
    memberdiscountrate = Column(Numeric(28, 14))
    discountrate = Column(Numeric(28, 14))
    price = Column(Numeric(28, 14))
    retailamount = Column(Numeric(28, 14))
    amount = Column(Numeric(28, 14))
    taxrate = Column(Numeric(28, 14))
    taxprice = Column(Numeric(28, 14))
    tax = Column(Numeric(28, 14))
    taxamount = Column(Numeric(28, 14))
    detailDiscountAmount = Column(Numeric(28, 14))
    memo = Column(Unicode(200))
    isdel = Column(Integer)
    batch = Column(Unicode(50))
    expirydate = Column(String(19, u'Chinese_PRC_CI_AS'))
    unitexchangerate = Column(Numeric(28, 14))
    ts = Column(TIMESTAMP, nullable=False)
    updated = Column(String(19, u'Chinese_PRC_CI_AS'))
    updatedBy = Column(Unicode(32))
    priuserdefnvc1 = Column(Unicode(100))
    priuserdefdecm1 = Column(Numeric(28, 14))
    priuserdefnvc2 = Column(Unicode(100))
    priuserdefdecm2 = Column(Numeric(28, 14))
    priuserdefnvc3 = Column(Unicode(100))
    priuserdefdecm3 = Column(Numeric(28, 14))
    priuserdefnvc4 = Column(Unicode(100))
    priuserdefdecm4 = Column(Numeric(28, 14))
    pubuserdefnvc1 = Column(Unicode(100))
    pubuserdefdecm1 = Column(Numeric(28, 14))
    pubuserdefnvc2 = Column(Unicode(100))
    pubuserdefdecm2 = Column(Numeric(28, 14))
    pubuserdefnvc3 = Column(Unicode(100))
    pubuserdefdecm3 = Column(Numeric(28, 14))
    pubuserdefnvc4 = Column(Unicode(100))
    freeItem0 = Column(Unicode(300))
    freeItem1 = Column(Unicode(300))
    pubuserdefdecm4 = Column(Numeric(28, 14))
    freeItem2 = Column(Unicode(300))
    freeItem3 = Column(Unicode(300))
    freeItem4 = Column(Unicode(300))
    freeItem5 = Column(Unicode(300))
    freeItem6 = Column(Unicode(300))
    freeItem7 = Column(Unicode(300))
    freeItem8 = Column(Unicode(300))
    freeItem9 = Column(Unicode(300))
    CashSettleAmount = Column(Numeric(28, 14))
    VirtualSettleAmount = Column(Numeric(28, 14))
    storagesettleamount = Column(Numeric(28, 14))
    isuseintegralandcash = Column(Integer)
    isusestorage = Column(Integer)
    ismemberstorageprojet = Column(Integer)
    discountAuthorize = Column(Unicode(50))
    quantity2 = Column(Numeric(28, 14))
    ProductionDate = Column(String(19, u'Chinese_PRC_CI_AS'))
    RdRecordCode = Column(Unicode(50))
    id = Column(Integer, primary_key=True)
    idinventory = Column(Integer)
    idperson = Column(Integer)
    idunit = Column(Integer)
    idbaseunit = Column(Integer)
    idsubunit = Column(Integer)
    discountAuthorizeId = Column(Integer)
    idunit2 = Column(Integer)
    idRdRecord = Column(Integer)
    issaleout = Column(Integer)
    promotiontype = Column(Integer)
    promotionid = Column(Integer)
    limitedsaleid = Column(Integer)
    limitedsalesubid = Column(Integer)
    idRetailDTO = Column(Integer)


class RERetailBak(Base):
    __tablename__ = 'RE_Retail_bak'

    code = Column(Unicode(50))
    name = Column(Unicode(200))
    docno = Column(Unicode(36))
    docclass = Column(Unicode(36))
    accountingperiod = Column(Integer)
    docid = Column(Unicode(36))
    accountingyear = Column(Integer)
    memo = Column(Unicode(200))
    voucherdate = Column(String(19, u'Chinese_PRC_CI_AS'))
    madedate = Column(String(19, u'Chinese_PRC_CI_AS'))
    maker = Column(Unicode(50))
    auditor = Column(Unicode(50))
    auditeddate = Column(String(19, u'Chinese_PRC_CI_AS'))
    reviser = Column(Unicode(50))
    iscarriedforwardout = Column(Integer)
    iscarriedforwardin = Column(Integer)
    ismodifiedcode = Column(Integer)
    createdtime = Column(String(19, u'Chinese_PRC_CI_AS'))
    sequencenumber = Column(Integer)
    customername = Column(Unicode(50))
    customeraddress = Column(Unicode(50))
    customerlinkman = Column(Unicode(50))
    customerphone = Column(Unicode(50))
    customerrequest = Column(Unicode(50))
    shiftcode = Column(Unicode(50))
    auditedtime = Column(String(8, u'Chinese_PRC_CI_AS'))
    poscode = Column(Unicode(50))
    posname = Column(Unicode(50))
    isdealed = Column(Integer)
    totalretailamount = Column(Numeric(28, 14))
    totaltaxamount = Column(Numeric(28, 14))
    discountsandallowances = Column(Numeric(28, 14))
    totaldiscountamount = Column(Numeric(28, 14))
    wipechange = Column(Numeric(28, 14))
    integral = Column(Numeric(28, 14))
    iscleared = Column(Integer)
    usercode = Column(Unicode(50))
    username = Column(Unicode(50))
    ts = Column(TIMESTAMP, nullable=False)
    updated = Column(String(19, u'Chinese_PRC_CI_AS'))
    updatedBy = Column(Unicode(32))
    priuserdefnvc1 = Column(Unicode(100))
    priuserdefdecm1 = Column(Numeric(28, 14))
    priuserdefnvc2 = Column(Unicode(100))
    priuserdefdecm2 = Column(Numeric(28, 14))
    priuserdefnvc3 = Column(Unicode(100))
    priuserdefdecm3 = Column(Numeric(28, 14))
    priuserdefnvc4 = Column(Unicode(100))
    priuserdefdecm4 = Column(Numeric(28, 14))
    priuserdefnvc5 = Column(Unicode(100))
    priuserdefdecm5 = Column(Numeric(28, 14))
    priuserdefnvc6 = Column(Unicode(100))
    priuserdefdecm6 = Column(Numeric(28, 14))
    pubuserdefnvc1 = Column(Unicode(100))
    pubuserdefdecm1 = Column(Numeric(28, 14))
    pubuserdefnvc2 = Column(Unicode(100))
    pubuserdefdecm2 = Column(Numeric(28, 14))
    pubuserdefnvc3 = Column(Unicode(100))
    pubuserdefdecm3 = Column(Numeric(28, 14))
    pubuserdefnvc4 = Column(Unicode(100))
    pubuserdefdecm4 = Column(Numeric(28, 14))
    pubuserdefnvc5 = Column(Unicode(100))
    pubuserdefdecm5 = Column(Numeric(28, 14))
    pubuserdefnvc6 = Column(Unicode(100))
    pubuserdefdecm6 = Column(Numeric(28, 14))
    SteadCashIntegral = Column(Numeric(28, 14))
    receivingmaturity = Column(String(19, u'Chinese_PRC_CI_AS'))
    balancestorage = Column(Numeric(28, 14))
    dailycode = Column(Unicode(50))
    storagesettleamount = Column(Numeric(28, 14))
    integralsteadcashamount = Column(Numeric(28, 14))
    givechangeforstorageamount = Column(Numeric(28, 14))
    PrintCount = Column(Integer)
    balanceintegral = Column(Numeric(28, 14))
    RetailSettleCode = Column(Unicode(50))
    ExternalCode = Column(Unicode(30))
    id = Column(Integer, primary_key=True)
    idbusitype = Column(Integer)
    idmember = Column(Integer)
    idstore = Column(Integer)
    shift = Column(Integer)
    idmarketingorgan = Column(Integer)
    idperson = Column(Integer)
    idRetailSettle = Column(Integer)
    idDepartment_Store = Column(Integer)
    idDistrict_Member = Column(Integer)
    idMembertype = Column(Integer)
    iscancel = Column(Integer)
    issaleout = Column(Integer)
    voucherstate = Column(Integer)
    auditorid = Column(Integer)
    makerid = Column(Integer)
    userid = Column(Integer)
    iddailyvoucher = Column(Integer)
    idshiftvoucher = Column(Integer)


t_RE_ShiftVoucher = Table(
    'RE_ShiftVoucher', metadata,
    Column('code', Unicode(50)),
    Column('name', Unicode(200)),
    Column('docno', Unicode(36)),
    Column('docclass', Unicode(36)),
    Column('accountingperiod', Integer),
    Column('docid', Unicode(36)),
    Column('accountingyear', Integer),
    Column('memo', Unicode(200)),
    Column('voucherdate', String(19, u'Chinese_PRC_CI_AS')),
    Column('madedate', String(19, u'Chinese_PRC_CI_AS')),
    Column('maker', Unicode(50)),
    Column('auditor', Unicode(50)),
    Column('auditeddate', String(19, u'Chinese_PRC_CI_AS')),
    Column('reviser', Unicode(50)),
    Column('iscarriedforwardout', Integer),
    Column('iscarriedforwardin', Integer),
    Column('ismodifiedcode', Integer),
    Column('createdtime', String(19, u'Chinese_PRC_CI_AS')),
    Column('sequencenumber', Integer),
    Column('poscode', Unicode(50)),
    Column('posname', Unicode(50)),
    Column('usercode', Unicode(50)),
    Column('username', Unicode(50)),
    Column('workingdate', String(19, u'Chinese_PRC_CI_AS')),
    Column('workingtime', String(8, u'Chinese_PRC_CI_AS')),
    Column('shiftdate', String(19, u'Chinese_PRC_CI_AS')),
    Column('shifttime', String(8, u'Chinese_PRC_CI_AS')),
    Column('retailcount', Numeric(28, 14)),
    Column('retailamount', Numeric(28, 14)),
    Column('retailreturncount', Numeric(28, 14)),
    Column('returnamount', Numeric(28, 14)),
    Column('removecount', Numeric(28, 14)),
    Column('removeamount', Numeric(28, 14)),
    Column('totalcount', Integer),
    Column('price', Numeric(28, 14)),
    Column('totalsettleamount', Numeric(28, 14)),
    Column('initialamount', Numeric(28, 14)),
    Column('imprestamount', Numeric(28, 14)),
    Column('ts', TIMESTAMP, nullable=False),
    Column('updated', String(19, u'Chinese_PRC_CI_AS')),
    Column('updatedBy', Unicode(32)),
    Column('voucherdiscountamount', Numeric(28, 14)),
    Column('id', Integer, nullable=False),
    Column('idstore', Integer),
    Column('idmarketingorgan', Integer),
    Column('iscancel', Integer),
    Column('shift', Integer),
    Column('voucherstate', Integer),
    Column('auditorid', Integer),
    Column('makerid', Integer),
    Column('userid', Integer)
)


t_RE_ShiftVoucher_b = Table(
    'RE_ShiftVoucher_b', metadata,
    Column('code', Unicode(30)),
    Column('name', Unicode(200)),
    Column('createdtime', String(19, u'Chinese_PRC_CI_AS')),
    Column('sequencenumber', Integer),
    Column('origamount', Numeric(28, 14)),
    Column('amount', Numeric(28, 14)),
    Column('origsettleamount', Numeric(28, 14)),
    Column('settleamount', Numeric(28, 14)),
    Column('initialamount', Numeric(28, 14)),
    Column('imprestamount', Numeric(28, 14)),
    Column('ts', TIMESTAMP, nullable=False),
    Column('updated', String(19, u'Chinese_PRC_CI_AS')),
    Column('updatedBy', Unicode(32)),
    Column('id', Integer, nullable=False),
    Column('idbankaccount', Integer),
    Column('idsettlestyle', Integer),
    Column('idShiftVoucherDTO', Integer)
)


class RTReportCenter(Base):
    __tablename__ = 'RT_ReportCenter'

    code = Column(Unicode(32))
    name = Column(Unicode(200))
    stylepicturepath = Column(Unicode(200))
    ordernum = Column(Integer)
    level = Column(Integer)
    ts = Column(TIMESTAMP)
    updatedBy = Column(Unicode(32))
    IsSystem = Column(Integer, nullable=False, server_default=text("((0))"))
    id = Column(Integer, primary_key=True)
    idparent = Column(Integer)
    updated = Column(DateTime)


class SACreditOccupancy(Base):
    __tablename__ = 'SA_CreditOccupancy'

    orderunoutamount = Column(Numeric(28, 14))
    outunsettleamount = Column(Numeric(28, 14))
    salesettleamount = Column(Numeric(28, 14))
    incomeunsettleamount = Column(Numeric(28, 14))
    receiveuncancelamount = Column(Numeric(28, 14))
    ts = Column(TIMESTAMP, nullable=False)
    iscarriedforwardout = Column(Integer)
    iscarriedforwardin = Column(Integer)
    expenseSettleAmount = Column(Numeric(28, 14))
    orderUnOutAmountForAudit = Column(Numeric(28, 14))
    outUnSettleAmountForAudit = Column(Numeric(28, 14))
    saleSettleAmountForAudit = Column(Numeric(28, 14))
    incomeUnSettleAmountForAudit = Column(Numeric(28, 14))
    receiveUnCancelAmountForAudit = Column(Numeric(28, 14))
    expenseSettleAmountForAudit = Column(Numeric(28, 14))
    id = Column(Integer, primary_key=True)
    idcustomer = Column(Integer, index=True)
    idclerk = Column(Integer, index=True)
    updated = Column(DateTime, index=True)


class SAInventoryLocation(Base):
    __tablename__ = 'SA_InventoryLocation'

    code = Column(Unicode(30))
    quantity = Column(Numeric(28, 14))
    quantity2 = Column(Numeric(28, 14))
    memoto = Column(Unicode(200))
    ts = Column(TIMESTAMP)
    updatedBy = Column(Unicode(32))
    id = Column(Integer, primary_key=True)
    idinvlocation = Column(Integer, index=True)
    idunit = Column(Integer)
    idunit2 = Column(Integer)
    idSaleDeliveryDetailDTO = Column(Integer, index=True)
    updated = Column(DateTime, index=True)


class SASaleDelivery(Base):
    __tablename__ = 'SA_SaleDelivery'
    __table_args__ = (
        Index('IDX_SA_SaleDelivery_isBeforeSystemInuse', 'isBeforeSystemInuse', 'ID', 'code', 'origTaxAmount', 'voucherState', 'memo', 'voucherdate', 'maker', 'auditor', 'idcustomer', 'iddepartment', 'createdtime', 'idbusinesstype', 'ts', 'SourceVoucherCode', 'changer'),
        Index('IDX_SA_SaleDelivery_id_Code_VoucherDate_VoucherSate', 'ID', 'voucherdate', 'voucherState', 'code'),
        Index('Idx_SA_SaleDelivery_createdtime_voucherdate', 'createdtime', 'voucherdate', 'ID', 'idcustomer', 'idsettlecustomer', 'iddepartment', 'idclerk', 'makerid')
    )

    code = Column(Unicode(30), index=True)
    origCancelAmount = Column(Numeric(28, 14))
    origAmount = Column(Numeric(28, 14))
    amount = Column(Numeric(28, 14))
    origTaxAmount = Column(Numeric(28, 14))
    taxAmount = Column(Numeric(28, 14))
    isCounteractDelivery = Column(Integer)
    discountAmount = Column(Numeric(28, 14))
    discountRate = Column(Numeric(28, 14))
    discountsAndAllowances = Column(Numeric(28, 14))
    exchangeRate = Column(Numeric(28, 14))
    address = Column(Unicode(200))
    linkMan = Column(Unicode(50))
    cancelAmount = Column(Numeric(28, 14))
    isPriceTrace = Column(Integer)
    memo = Column(Unicode(200))
    saleInvoiceNo = Column(Unicode(30))
    isAutoGenerateInvoice = Column(Integer)
    isAutoGenerateSaleOut = Column(Integer)
    origSettleAmount = Column(Numeric(28, 14))
    settleAmount = Column(Numeric(28, 14))
    contactPhone = Column(Unicode(100))
    isNoModify = Column(Unicode(1000))
    isBeforeSystemInuse = Column(Integer)
    maker = Column(Unicode(50))
    auditor = Column(Unicode(50))
    reviser = Column(Unicode(50))
    iscarriedforwardout = Column(Integer)
    iscarriedforwardin = Column(Integer)
    ismodifiedcode = Column(Integer)
    docid = Column(Unicode(36))
    ts = Column(TIMESTAMP)
    updatedBy = Column(Unicode(32))
    priuserdefnvc1 = Column(Unicode(500))
    priuserdefdecm1 = Column(Numeric(28, 14))
    priuserdefnvc2 = Column(Unicode(500))
    priuserdefdecm2 = Column(Numeric(28, 14))
    priuserdefnvc3 = Column(Unicode(500))
    priuserdefdecm3 = Column(Numeric(28, 14))
    priuserdefnvc4 = Column(Unicode(500))
    priuserdefdecm4 = Column(Numeric(28, 14))
    priuserdefnvc5 = Column(Unicode(500))
    priuserdefdecm5 = Column(Numeric(28, 14))
    priuserdefnvc6 = Column(Unicode(500))
    priuserdefdecm6 = Column(Numeric(28, 14))
    pubuserdefnvc1 = Column(Unicode(500))
    pubuserdefdecm1 = Column(Numeric(28, 14))
    pubuserdefnvc2 = Column(Unicode(500))
    pubuserdefdecm2 = Column(Numeric(28, 14))
    pubuserdefnvc3 = Column(Unicode(500))
    pubuserdefdecm3 = Column(Numeric(28, 14))
    pubuserdefnvc4 = Column(Unicode(500))
    pubuserdefdecm4 = Column(Numeric(28, 14))
    pubuserdefnvc5 = Column(Unicode(500))
    pubuserdefdecm5 = Column(Numeric(28, 14))
    pubuserdefnvc6 = Column(Unicode(500))
    pubuserdefdecm6 = Column(Numeric(28, 14))
    isNoArapBookkeeping = Column(Integer)
    origprereceiveamount = Column(Numeric(28, 14))
    PreReceiveAmount = Column(Numeric(28, 14))
    ReceiveBalance = Column(Numeric(28, 14))
    SourceVoucherCode = Column(Unicode(50))
    changer = Column(Unicode(50))
    OrigInvoiceTaxAmount = Column(Numeric(28, 14))
    thisBalanceIntegral = Column(BigInteger)
    Mobilephone = Column(Unicode(50))
    MemberAddress = Column(Unicode(50))
    PrintCount = Column(Integer)
    IsSeparateByWareHouse = Column(Integer)
    Allowances = Column(Numeric(28, 14))
    origAllowances = Column(Numeric(28, 14))
    IsAutoSaleOut = Column(Integer)
    ExternalCode = Column(Unicode(50))
    collaborateVoucherCode = Column(Unicode(30))
    ID = Column(Integer, primary_key=True)
    idbusinesstype = Column(Integer)
    idcurrency = Column(Integer, index=True)
    iddepartment = Column(Integer, index=True)
    IdMember = Column(Integer)
    idmarketingOrgan = Column(Integer, index=True)
    idcustomer = Column(Integer, index=True)
    idsettlecustomer = Column(Integer, index=True)
    idclerk = Column(Integer, index=True)
    idproject = Column(Integer, index=True)
    idrdstyle = Column(Integer)
    idwarehouse = Column(Integer, index=True)
    idCollaborateUpVoucherType = Column(Integer)
    idCollaborateUpVoucher = Column(Integer)
    DataSource = Column(Integer)
    deliveryMode = Column(Integer)
    invoiceType = Column(Integer)
    isCancel = Column(Integer)
    isSaleOut = Column(Integer)
    reciveType = Column(Integer)
    voucherState = Column(Integer)
    auditorid = Column(Integer)
    makerid = Column(Integer)
    changerid = Column(Integer)
    idCollaborateDownVoucherType = Column(Integer)
    CollaborateState = Column(Integer)
    idCollaborateDownDraftVoucher = Column(Integer)
    saleInvoiceID = Column(Integer)
    idsourcevouchertype = Column(Integer, index=True)
    deliveryDate = Column(DateTime)
    recivingMaturity = Column(DateTime)
    voucherdate = Column(DateTime, index=True)
    madedate = Column(DateTime)
    auditeddate = Column(DateTime)
    createdtime = Column(DateTime, index=True)
    updated = Column(DateTime)
    SourceVoucherDate = Column(DateTime)
    changedate = Column(DateTime)


class SASaleDeliveryPreReceive(Base):
    __tablename__ = 'SA_SaleDeliveryPreReceive'

    code = Column(Unicode(30))
    vouchercode = Column(Unicode(50))
    origamount = Column(Numeric(28, 14))
    orignocancelamount = Column(Numeric(28, 14))
    origcancelamount = Column(Numeric(28, 14))
    cancelamount = Column(Numeric(28, 14))
    ts = Column(TIMESTAMP)
    updatedBy = Column(Unicode(32))
    saleOrderCode = Column(Unicode(30))
    memo = Column(Unicode(200))
    id = Column(Integer, primary_key=True)
    iddepartment = Column(Integer, index=True)
    idperson = Column(Integer, index=True)
    idproject = Column(Integer)
    voucherid = Column(Integer)
    idSaleDeliveryDTO = Column(Integer, index=True)
    SaleOrderId = Column(Integer)
    idvouchertype = Column(Integer, index=True)
    voucherdate = Column(DateTime)
    updated = Column(DateTime)


class SASaleDeliverySettlement(Base):
    __tablename__ = 'SA_SaleDeliverySettlement'

    code = Column(Unicode(30))
    amount = Column(Numeric(28, 14))
    origAmount = Column(Numeric(28, 14))
    billNo = Column(Unicode(30))
    ts = Column(TIMESTAMP)
    updatedBy = Column(Unicode(32))
    id = Column(Integer, primary_key=True)
    idbankaccount = Column(Integer)
    idsettlestyle = Column(Integer)
    idSaleDeliveryDTO = Column(Integer, index=True)
    createdtime = Column(DateTime)
    updated = Column(DateTime, index=True)


class SASaleDeliverySourceRelation(Base):
    __tablename__ = 'SA_SaleDeliverySourceRelation'
    __table_args__ = (
        Index('IDX_SA_SaleDeliverySourceRelation_Ids', 'voucherId', 'idSaleDeliveryDetailDTO', 'sourceVoucherDetailId', 'quantity', 'baseQuantity', 'subQuantity'),
    )

    quantity = Column(Numeric(28, 14))
    quantity2 = Column(Numeric(28, 14))
    baseQuantity = Column(Numeric(28, 14))
    subQuantity = Column(Numeric(28, 14))
    ts = Column(TIMESTAMP)
    updatedBy = Column(Unicode(32))
    id = Column(Integer, primary_key=True)
    idbaseunit = Column(Integer)
    idsubunit = Column(Integer)
    idunit = Column(Integer)
    idunit2 = Column(Integer)
    sourceVoucherId = Column(Integer)
    voucherId = Column(Integer, index=True)
    idSaleDeliveryDetailDTO = Column(Integer, index=True)
    sourceVoucherDetailId = Column(Integer, index=True)
    idsourcevouchertype = Column(Integer, index=True)
    updated = Column(DateTime, index=True)


class SASaleDeliveryB(Base):
    __tablename__ = 'SA_SaleDelivery_b'
    __table_args__ = (
        Index('IDX_SA_SaleDelivery_b_idSaleDeliveryDTO__origSettleAmount', 'idSaleDeliveryDTO', 'origSettleAmount'),
        Index('IDX_SA_SaleDelivery_b_idSaleDeliveryDTO_id_saleOrderId', 'idSaleDeliveryDTO', 'updated', 'ID', 'saleOrderId'),
        Index('IDX_SA_SaleDelivery_b_idSaleDeliveryDTO__taxAmount', 'idSaleDeliveryDTO', 'taxAmount'),
        Index('IDX_SA_SaleDelivery_b_idwarehouse', 'idwarehouse', 'idSaleDeliveryDTO'),
        Index('IDX_Sa_SaleDelivery_b_PromotionSingle', 'PromotionSingleTypeID', 'PromotionSingleVoucherCode'),
        Index('IDX_Sa_SaleDelivery_b_PromotionPresent', 'PromotionPresentTypeID', 'PromotionPresentVoucherCode')
    )

    code = Column(Unicode(30))
    isNoModify = Column(Unicode(1000))
    quantity = Column(Numeric(28, 14))
    quantity2 = Column(Numeric(28, 14))
    unitExchangeRate = Column(Numeric(28, 14))
    baseQuantity = Column(Numeric(28, 14))
    subQuantity = Column(Numeric(28, 14))
    compositionQuantity = Column(Unicode(100))
    origPrice = Column(Numeric(28, 14))
    price = Column(Numeric(28, 14))
    basePrice = Column(Numeric(28, 14))
    discountRate = Column(Numeric(28, 14))
    origDiscountPrice = Column(Numeric(28, 14))
    discountPrice = Column(Numeric(28, 14))
    baseDiscountPrice = Column(Numeric(28, 14))
    taxRate = Column(Numeric(28, 14))
    origTaxPrice = Column(Numeric(28, 14))
    taxPrice = Column(Numeric(28, 14))
    baseTaxPrice = Column(Numeric(28, 14))
    origDiscountAmount = Column(Numeric(28, 14))
    discountAmount = Column(Numeric(28, 14))
    origTax = Column(Numeric(28, 14))
    tax = Column(Numeric(28, 14))
    origTaxAmount = Column(Numeric(28, 14))
    taxAmount = Column(Numeric(28, 14))
    origDiscount = Column(Numeric(28, 14))
    discount = Column(Numeric(28, 14))
    costPrice = Column(Numeric(28, 14))
    costAmount = Column(Numeric(28, 14))
    receiveVoucherCode = Column(Unicode(50))
    saleOrderCode = Column(Unicode(30))
    batch = Column(Unicode(50))
    adjustAmount = Column(Numeric(28, 14))
    isPresent = Column(Integer)
    counteractQuntity = Column(Numeric(28, 14))
    counteractQuntity2 = Column(Numeric(28, 14))
    returnQuntity = Column(Numeric(28, 14))
    returnQuntity2 = Column(Numeric(28, 14))
    saleoutquantity2 = Column(Numeric(28, 14))
    saleOutQuantity = Column(Numeric(28, 14))
    invoiceQuantity2 = Column(Numeric(28, 14))
    invoiceQuantity = Column(Numeric(28, 14))
    settleAmount = Column(Numeric(28, 14))
    origSettleAmount = Column(Numeric(28, 14))
    origExpenseAmount = Column(Numeric(28, 14))
    expenseAmount = Column(Numeric(28, 14))
    inventoryLocation = Column(Unicode(50))
    sourceVoucherCode = Column(Unicode(50))
    taxFlag = Column(Integer)
    isManualCost = Column(Integer)
    inventoryBarCode = Column(Unicode(200))
    partnerInventoryCode = Column(Unicode(300))
    ts = Column(TIMESTAMP)
    updatedBy = Column(Unicode(32))
    freeItem0 = Column(Unicode(300))
    freeItem1 = Column(Unicode(300))
    freeItem2 = Column(Unicode(300))
    freeItem3 = Column(Unicode(300))
    freeItem4 = Column(Unicode(300))
    freeItem5 = Column(Unicode(300))
    freeItem6 = Column(Unicode(300))
    freeItem7 = Column(Unicode(300))
    freeItem8 = Column(Unicode(300))
    freeItem9 = Column(Unicode(300))
    priuserdefnvc1 = Column(Unicode(500))
    priuserdefdecm1 = Column(Numeric(28, 14), index=True)
    priuserdefnvc2 = Column(Unicode(500))
    priuserdefdecm2 = Column(Numeric(28, 14))
    priuserdefnvc3 = Column(Unicode(500))
    priuserdefdecm3 = Column(Numeric(28, 14))
    priuserdefnvc4 = Column(Unicode(500))
    priuserdefdecm4 = Column(Numeric(28, 14))
    pubuserdefnvc1 = Column(Unicode(500))
    pubuserdefdecm1 = Column(Numeric(28, 14))
    pubuserdefnvc2 = Column(Unicode(500))
    pubuserdefdecm2 = Column(Numeric(28, 14))
    pubuserdefnvc3 = Column(Unicode(500))
    pubuserdefdecm3 = Column(Numeric(28, 14))
    pubuserdefnvc4 = Column(Unicode(500))
    pubuserdefdecm4 = Column(Numeric(28, 14))
    partnerInventoryName = Column(Unicode(300))
    virtualBaseQuantity = Column(Numeric(28, 14))
    virtualBaseAmount = Column(Numeric(28, 14))
    sentBaseQuantityAssociated = Column(Numeric(28, 14))
    sentBaseAmountAssociated = Column(Numeric(28, 14))
    backSentAmount = Column(Numeric(28, 14))
    backSentQuantity = Column(Numeric(28, 14))
    associatedDocIDs = Column(Unicode(400))
    Retailprice = Column(Numeric(28, 14))
    DistributionQuantity = Column(Numeric(28, 14))
    DistributionQuantity2 = Column(Numeric(28, 14))
    BoxNumber = Column(Unicode(50))
    OrigInvoiceTaxAmount = Column(Numeric(28, 14))
    PriceStrategyTypeName = Column(Unicode(200))
    PriceStrategySchemeIds = Column(Unicode(1000))
    PriceStrategySchemeNames = Column(Unicode(400))
    PromotionVoucherCodes = Column(Unicode(400))
    PromotionVoucherIds = Column(Unicode(400))
    IsMemberIntegral = Column(Integer)
    IsPromotionPresent = Column(Integer)
    PromotionPresentVoucherCode = Column(Unicode(50))
    PromotionSingleVoucherCode = Column(Unicode(50))
    PromotionPresentGroupID = Column(Unicode(150))
    PromotionSingleGroupID = Column(Unicode(150))
    SuperSourceVoucherTypeCode = Column(Unicode(50))
    DetailMemo = Column(Unicode(200))
    ID = Column(Integer, primary_key=True)
    idinventory = Column(Integer, index=True)
    idproject = Column(Integer, index=True)
    idbaseunit = Column(Integer)
    idsubunit = Column(Integer)
    idunit = Column(Integer)
    idunit2 = Column(Integer)
    idwarehouse = Column(Integer)
    isCancel = Column(Integer)
    isSaleOut = Column(Integer)
    CashbackWay = Column(Integer)
    PriceStrategyTypeId = Column(Integer)
    PromotionPresentTypeID = Column(Integer)
    PromotionSingleTypeID = Column(Integer)
    docid = Column(Integer)
    PromotionPresentVoucherID = Column(Integer)
    PromotionSingleVoucherID = Column(Integer)
    sourceVoucherId = Column(Integer, index=True)
    idSaleDeliveryDTO = Column(Integer, index=True)
    sourceVoucherDetailId = Column(Integer, index=True)
    saleOrderId = Column(Integer)
    saleOrderDetailId = Column(Integer)
    idsourcevouchertype = Column(Integer, index=True)
    receiveVoucherId = Column(Integer, index=True)
    receiveVoucherDetailId = Column(Integer)
    expiryDate = Column(DateTime)
    deliveryDate = Column(DateTime)
    createdtime = Column(DateTime)
    updated = Column(DateTime)
    ProductionDate = Column(DateTime)
    LatestCost = Column(Numeric(28, 14), server_default=text("(NULL)"))
    LatestPOrigTaxPrice = Column(Numeric(28, 14), server_default=text("(NULL)"))
    LatestSaleOrigTaxPrice = Column(Numeric(28, 14), server_default=text("(NULL)"))
    LowestSalePrice = Column(Numeric(28, 14), server_default=text("(NULL)"))
    SingleInvGrossProfit = Column(Numeric(28, 14), server_default=text("(NULL)"))
    GrossProfit = Column(Numeric(28, 14), server_default=text("(NULL)"))
    GrossProfitRate = Column(Numeric(28, 14), server_default=text("(NULL)"))
    DataSource = Column(Integer, server_default=text("(NULL)"))


class SASaleExpenseAllocation(Base):
    __tablename__ = 'SA_SaleExpenseAllocation'
    __table_args__ = (
        Index('Idx__SA_SaleExpenseAllocation_createdtime_voucherdate', 'createdtime', 'voucherdate', 'id', 'makerid'),
    )

    code = Column(Unicode(30), index=True)
    isCreateAuto = Column(Integer)
    maker = Column(Unicode(50))
    auditor = Column(Unicode(50))
    reviser = Column(Unicode(50))
    iscarriedforwardout = Column(Integer)
    iscarriedforwardin = Column(Integer)
    ismodifiedcode = Column(Integer)
    ts = Column(TIMESTAMP)
    updatedBy = Column(Unicode(32))
    PrintCount = Column(Integer)
    id = Column(Integer, primary_key=True)
    idmarketingOrgan = Column(Integer, index=True)
    allocateType = Column(Integer)
    auditorid = Column(Integer)
    makerid = Column(Integer)
    idsourcevouchertype = Column(Integer, index=True)
    voucherdate = Column(DateTime, index=True)
    madedate = Column(DateTime)
    auditeddate = Column(DateTime)
    createdtime = Column(DateTime, index=True)
    updated = Column(DateTime)


class SASaleExpenseAllocationDetail(Base):
    __tablename__ = 'SA_SaleExpenseAllocationDetail'
    __table_args__ = (
        Index('Idx__SA_SaleExpenseAllocationDetail_idsaleexpenseallocationdto', 'idSaleExpenseAllocationDTO', 'id', 'iddepartment', 'idpartner', 'idsettlecustomer', 'idperson', 'idproject', 'idinventory'),
    )

    code = Column(Unicode(30))
    amount = Column(Numeric(28, 14))
    ts = Column(TIMESTAMP)
    updatedBy = Column(Unicode(32))
    freeItem0 = Column(Unicode(300))
    freeItem1 = Column(Unicode(300))
    freeItem2 = Column(Unicode(300))
    freeItem3 = Column(Unicode(300))
    freeItem4 = Column(Unicode(300))
    freeItem5 = Column(Unicode(300))
    freeItem6 = Column(Unicode(300))
    freeItem7 = Column(Unicode(300))
    freeItem8 = Column(Unicode(300))
    freeItem9 = Column(Unicode(300))
    SourceVoucherCode = Column(Unicode(50))
    SourceVoucherMemo = Column(Unicode(200))
    Quantity = Column(Numeric(28, 14))
    DiscountAmount = Column(Numeric(28, 14))
    ispresent = Column(Integer)
    id = Column(Integer, primary_key=True)
    iddepartment = Column(Integer, index=True)
    idinventory = Column(Integer, index=True)
    idpartner = Column(Integer, index=True)
    idsettlecustomer = Column(Integer, index=True)
    idperson = Column(Integer, index=True)
    idproject = Column(Integer)
    idunit = Column(Integer)
    SourceVoucherId = Column(Integer)
    SourceVoucherDetailId = Column(Integer)
    idsaledelivery = Column(Integer)
    idsaledeliverydetail = Column(Integer)
    idSaleExpenseAllocationDTO = Column(Integer, index=True)
    idsaleinvoice = Column(Integer)
    idsaleinvoicedetail = Column(Integer)
    idsourcevouchertype = Column(Integer, index=True)
    updated = Column(DateTime, index=True)
    SourceVoucherDate = Column(DateTime)


class SASaleExpenseAllocationExpenseDetail(Base):
    __tablename__ = 'SA_SaleExpenseAllocationExpenseDetail'

    code = Column(Unicode(30))
    ts = Column(TIMESTAMP)
    updatedBy = Column(Unicode(32))
    id = Column(Integer, primary_key=True)
    iddepartment = Column(Integer, index=True)
    idexpenseitem = Column(Integer, index=True)
    idperson = Column(Integer, index=True)
    idproject = Column(Integer)
    idexpensevoucher = Column(Integer, index=True)
    idexpensevoucherdetail = Column(Integer, index=True)
    idSaleExpenseAllocationDTO = Column(Integer, index=True)
    updated = Column(DateTime, index=True)


class SASaleInvoice(Base):
    __tablename__ = 'SA_SaleInvoice'
    __table_args__ = (
        Index('Idx_SA_SaleInvoice_createdtime_voucherdate', 'createdtime', 'voucherdate', 'id', 'iddepartment', 'idclerk', 'makerid', 'idcustomer', 'idsettlecustomer', 'idinvoicecustomer'),
    )

    code = Column(Unicode(30), index=True)
    isNoModify = Column(Unicode(1000))
    saleInvoiceNo = Column(Unicode(30))
    discountRate = Column(Numeric(28, 14))
    discountAmount = Column(Numeric(28, 14))
    discountsAndAllowances = Column(Numeric(28, 14))
    exchangeRate = Column(Numeric(28, 14))
    address = Column(Unicode(200))
    linkMan = Column(Unicode(50))
    origAmount = Column(Numeric(28, 14))
    amount = Column(Numeric(28, 14))
    origTaxAmount = Column(Numeric(28, 14))
    taxAmount = Column(Numeric(28, 14))
    origSettleAmount = Column(Numeric(28, 14))
    settleAmount = Column(Numeric(28, 14))
    origCancelAmount = Column(Numeric(28, 14))
    cancelAmount = Column(Numeric(28, 14))
    isPriceTrace = Column(Integer)
    customerAddressPhone = Column(Unicode(250))
    memo = Column(Unicode(200))
    contactPhone = Column(Unicode(100))
    isOutPut = Column(Integer)
    maker = Column(Unicode(50))
    auditor = Column(Unicode(50))
    reviser = Column(Unicode(50))
    iscarriedforwardout = Column(Integer)
    iscarriedforwardin = Column(Integer)
    ismodifiedcode = Column(Integer)
    docid = Column(Unicode(36))
    ts = Column(TIMESTAMP)
    updatedBy = Column(Unicode(32))
    priuserdefnvc1 = Column(Unicode(500))
    priuserdefdecm1 = Column(Numeric(28, 14))
    priuserdefnvc2 = Column(Unicode(500))
    priuserdefdecm2 = Column(Numeric(28, 14))
    priuserdefnvc3 = Column(Unicode(500))
    priuserdefdecm3 = Column(Numeric(28, 14))
    priuserdefnvc4 = Column(Unicode(500))
    priuserdefdecm4 = Column(Numeric(28, 14))
    priuserdefnvc5 = Column(Unicode(500))
    priuserdefdecm5 = Column(Numeric(28, 14))
    priuserdefnvc6 = Column(Unicode(500))
    priuserdefdecm6 = Column(Numeric(28, 14))
    pubuserdefnvc1 = Column(Unicode(500))
    pubuserdefdecm1 = Column(Numeric(28, 14))
    pubuserdefnvc2 = Column(Unicode(500))
    pubuserdefdecm2 = Column(Numeric(28, 14))
    pubuserdefnvc3 = Column(Unicode(500))
    pubuserdefdecm3 = Column(Numeric(28, 14))
    pubuserdefnvc4 = Column(Unicode(500))
    pubuserdefdecm4 = Column(Numeric(28, 14))
    pubuserdefnvc5 = Column(Unicode(500))
    pubuserdefdecm5 = Column(Numeric(28, 14))
    pubuserdefnvc6 = Column(Unicode(500))
    pubuserdefdecm6 = Column(Numeric(28, 14))
    origprereceiveamount = Column(Numeric(28, 14))
    PreReceiveAmount = Column(Numeric(28, 14))
    ReceiveBalance = Column(Numeric(28, 14))
    SourceVoucherCode = Column(Unicode(50))
    isNoArapbookkeeping = Column(Integer)
    thisBalanceIntegral = Column(BigInteger)
    Mobilephone = Column(Unicode(50))
    MemberAddress = Column(Unicode(50))
    PrintCount = Column(Integer)
    Allowances = Column(Numeric(28, 14))
    origAllowances = Column(Numeric(28, 14))
    id = Column(Integer, primary_key=True)
    idbusinesstype = Column(Integer)
    idcurrency = Column(Integer)
    iddepartment = Column(Integer, index=True)
    IdMember = Column(Integer)
    idmarketingOrgan = Column(Integer, index=True)
    idcustomer = Column(Integer, index=True)
    idinvoicecustomer = Column(Integer, index=True)
    idsettlecustomer = Column(Integer, index=True)
    idclerk = Column(Integer, index=True)
    idproject = Column(Integer, index=True)
    idwarehouse = Column(Integer, index=True)
    DataSource = Column(Integer)
    deliveryMode = Column(Integer)
    invoiceType = Column(Integer)
    isCancel = Column(Integer)
    reciveType = Column(Integer)
    voucherState = Column(Integer)
    auditorid = Column(Integer)
    makerid = Column(Integer)
    idsourcevouchertype = Column(Integer, index=True)
    deliveryDate = Column(DateTime)
    recivingMaturity = Column(DateTime)
    voucherdate = Column(DateTime, index=True)
    madedate = Column(DateTime)
    auditeddate = Column(DateTime)
    createdtime = Column(DateTime, index=True)
    updated = Column(DateTime)
    SourceVoucherDate = Column(DateTime)


class SASaleInvoicePreReceive(Base):
    __tablename__ = 'SA_SaleInvoicePreReceive'

    code = Column(Unicode(30))
    vouchercode = Column(Unicode(50))
    origamount = Column(Numeric(28, 14))
    orignocancelamount = Column(Numeric(28, 14))
    origcancelamount = Column(Numeric(28, 14))
    cancelamount = Column(Numeric(28, 14))
    ts = Column(TIMESTAMP)
    updatedBy = Column(Unicode(32))
    saleOrderCode = Column(Unicode(30))
    memo = Column(Unicode(200))
    id = Column(Integer, primary_key=True)
    iddepartment = Column(Integer, index=True)
    idperson = Column(Integer, index=True)
    idproject = Column(Integer)
    voucherid = Column(Integer)
    idSaleInvoiceDTO = Column(Integer, index=True)
    SaleOrderId = Column(Integer)
    idvouchertype = Column(Integer, index=True)
    voucherdate = Column(DateTime)
    updated = Column(DateTime)


class SASaleInvoiceSettlement(Base):
    __tablename__ = 'SA_SaleInvoiceSettlement'

    code = Column(Unicode(30))
    amount = Column(Numeric(28, 14))
    origAmount = Column(Numeric(28, 14))
    billNo = Column(Unicode(30))
    ts = Column(TIMESTAMP)
    updatedBy = Column(Unicode(32))
    id = Column(Integer, primary_key=True)
    idbankaccount = Column(Integer)
    idsettlestyle = Column(Integer)
    idSaleInvoiceDTO = Column(Integer, index=True)
    updated = Column(DateTime, index=True)


class SASaleInvoiceSourceRelation(Base):
    __tablename__ = 'SA_SaleInvoiceSourceRelation'

    subQuantity = Column(Numeric(28, 14))
    baseQuantity = Column(Numeric(28, 14))
    quantity2 = Column(Numeric(28, 14))
    quantity = Column(Numeric(28, 14))
    ts = Column(TIMESTAMP)
    updatedBy = Column(Unicode(32))
    id = Column(Integer, primary_key=True)
    idbaseunit = Column(Integer)
    idsubunit = Column(Integer)
    idunit = Column(Integer)
    idunit2 = Column(Integer)
    sourceVoucherId = Column(Integer)
    sourceVoucherDetailId = Column(Integer)
    voucherId = Column(Integer, index=True)
    idSaleInvoiceDetailDTO = Column(Integer, index=True)
    idsourcevouchertype = Column(Integer, index=True)
    updated = Column(DateTime, index=True)


class SASaleInvoiceB(Base):
    __tablename__ = 'SA_SaleInvoice_b'
    __table_args__ = (
        Index('IDX_SA_SaleInvoice_b_PromotionSingle', 'PromotionSingleTypeID', 'PromotionSingleVoucherCode'),
        Index('IDX_SA_SaleInvoice_b_PromotionPresent', 'PromotionPresentTypeID', 'PromotionPresentVoucherCode')
    )

    code = Column(Unicode(30))
    isNoModify = Column(Unicode(1000))
    quantity = Column(Numeric(28, 14))
    quantity2 = Column(Numeric(28, 14))
    compositionQuantity = Column(Unicode(100))
    subQuantity = Column(Numeric(28, 14))
    baseQuantity = Column(Numeric(28, 14))
    unitExchangeRate = Column(Numeric(28, 14))
    discountRate = Column(Numeric(28, 14))
    price = Column(Numeric(28, 14))
    origPrice = Column(Numeric(28, 14))
    origDiscountPrice = Column(Numeric(28, 14))
    discountPrice = Column(Numeric(28, 14))
    baseDiscountPrice = Column(Numeric(28, 14))
    taxRate = Column(Numeric(28, 14))
    origTaxPrice = Column(Numeric(28, 14))
    taxPrice = Column(Numeric(28, 14))
    baseTaxPrice = Column(Numeric(28, 14))
    origDiscount = Column(Numeric(28, 14))
    discount = Column(Numeric(28, 14))
    origDiscountAmount = Column(Numeric(28, 14))
    discountAmount = Column(Numeric(28, 14))
    origTax = Column(Numeric(28, 14))
    tax = Column(Numeric(28, 14))
    origTaxAmount = Column(Numeric(28, 14))
    taxAmount = Column(Numeric(28, 14))
    costPrice = Column(Numeric(28, 14))
    costAmount = Column(Numeric(28, 14))
    saleOrderCode = Column(Unicode(30))
    adjustAmount = Column(Numeric(28, 14))
    batch = Column(Unicode(50))
    isPresent = Column(Integer)
    returnQuntity = Column(Numeric(28, 14))
    returnQuntity2 = Column(Numeric(28, 14))
    counteractQuntity2 = Column(Numeric(28, 14))
    counteractQuntity = Column(Numeric(28, 14))
    invoiceQuantity2 = Column(Numeric(28, 14))
    invoiceQuantity = Column(Numeric(28, 14))
    saleOutQuantity = Column(Numeric(28, 14))
    settleAmount = Column(Numeric(28, 14))
    origSettleAmount = Column(Numeric(28, 14))
    origExpenseAmount = Column(Numeric(28, 14))
    expenseAmount = Column(Numeric(28, 14))
    saleoutquantity2 = Column(Numeric(28, 14))
    sourceVoucherCode = Column(Unicode(50))
    taxFlag = Column(Integer)
    basePrice = Column(Numeric(28, 14))
    inventoryBarCode = Column(Unicode(200))
    partnerInventoryCode = Column(Unicode(300))
    ts = Column(TIMESTAMP)
    updatedBy = Column(Unicode(32))
    freeItem0 = Column(Unicode(300))
    freeItem1 = Column(Unicode(300))
    freeItem2 = Column(Unicode(300))
    freeItem3 = Column(Unicode(300))
    freeItem4 = Column(Unicode(300))
    freeItem5 = Column(Unicode(300))
    freeItem6 = Column(Unicode(300))
    freeItem7 = Column(Unicode(300))
    freeItem8 = Column(Unicode(300))
    freeItem9 = Column(Unicode(300))
    priuserdefnvc1 = Column(Unicode(500))
    priuserdefdecm1 = Column(Numeric(28, 14))
    priuserdefnvc2 = Column(Unicode(500))
    priuserdefdecm2 = Column(Numeric(28, 14))
    priuserdefnvc3 = Column(Unicode(500))
    priuserdefdecm3 = Column(Numeric(28, 14))
    priuserdefnvc4 = Column(Unicode(500))
    priuserdefdecm4 = Column(Numeric(28, 14))
    pubuserdefnvc1 = Column(Unicode(500))
    pubuserdefdecm1 = Column(Numeric(28, 14))
    pubuserdefnvc2 = Column(Unicode(500))
    pubuserdefdecm2 = Column(Numeric(28, 14))
    pubuserdefnvc3 = Column(Unicode(500))
    pubuserdefdecm3 = Column(Numeric(28, 14))
    pubuserdefnvc4 = Column(Unicode(500))
    pubuserdefdecm4 = Column(Numeric(28, 14))
    partnerInventoryName = Column(Unicode(300))
    virtualBaseQuantity = Column(Numeric(28, 14))
    virtualBaseAmount = Column(Numeric(28, 14))
    backSentAmount = Column(Numeric(28, 14))
    backSentQuantity = Column(Numeric(28, 14))
    associatedDocIDs = Column(Unicode(400))
    Retailprice = Column(Numeric(28, 14))
    PriceStrategyTypeName = Column(Unicode(200))
    PriceStrategySchemeIds = Column(Unicode(1000))
    PriceStrategySchemeNames = Column(Unicode(400))
    PromotionVoucherCodes = Column(Unicode(400))
    PromotionVoucherIds = Column(Unicode(400))
    IsMemberIntegral = Column(Integer)
    IsPromotionPresent = Column(Integer)
    PromotionPresentVoucherCode = Column(Unicode(50))
    PromotionSingleVoucherCode = Column(Unicode(50))
    PromotionPresentGroupID = Column(Unicode(150))
    PromotionSingleGroupID = Column(Unicode(150))
    ID = Column(Integer, primary_key=True)
    idinventory = Column(Integer, index=True)
    idproject = Column(Integer, index=True)
    idbaseunit = Column(Integer)
    idsubunit = Column(Integer)
    idunit = Column(Integer)
    idunit2 = Column(Integer)
    idwarehouse = Column(Integer, index=True)
    isCancel = Column(Integer)
    CashbackWay = Column(Integer)
    PriceStrategyTypeId = Column(Integer)
    PromotionPresentTypeID = Column(Integer)
    PromotionSingleTypeID = Column(Integer)
    docid = Column(Integer)
    PromotionPresentVoucherID = Column(Integer)
    PromotionSingleVoucherID = Column(Integer)
    sourceVoucherId = Column(Integer, index=True)
    sourceVoucherDetailId = Column(Integer, index=True)
    idSaleInvoiceDTO = Column(Integer, index=True)
    saleOrderId = Column(Integer)
    saleOrderDetailId = Column(Integer)
    idsourcevouchertype = Column(Integer, index=True)
    expiryDate = Column(DateTime)
    deliveryDate = Column(DateTime)
    createdtime = Column(DateTime)
    updated = Column(DateTime)
    ProductionDate = Column(DateTime)


class SASaleOrder(Base):
    __tablename__ = 'SA_SaleOrder'
    __table_args__ = (
        Index('IDX_SA_SaleOrder_createdtime_voucherdate', 'createdtime', 'voucherdate', 'ID', 'idclerk', 'makerid', 'idcustomer', 'iddepartment', 'idsettlecustomer'),
    )

    code = Column(Unicode(30), index=True)
    name = Column(Unicode(200))
    discountRate = Column(Numeric(28, 14))
    discountAmount = Column(Numeric(28, 14))
    origDiscountAmount = Column(Numeric(28, 14))
    exchangeRate = Column(Numeric(28, 14))
    address = Column(Unicode(200))
    linkMan = Column(Unicode(50))
    contractCode = Column(Unicode(30))
    origEarnestMoney = Column(Numeric(28, 14))
    earnestMoney = Column(Numeric(28, 14))
    memo = Column(Unicode(200))
    origAmount = Column(Numeric(28, 14))
    amount = Column(Numeric(28, 14))
    origTaxAmount = Column(Numeric(28, 14))
    taxAmount = Column(Numeric(28, 14))
    contactPhone = Column(Unicode(100))
    maker = Column(Unicode(50))
    auditor = Column(Unicode(50))
    reviser = Column(Unicode(50))
    iscarriedforwardout = Column(Integer)
    iscarriedforwardin = Column(Integer)
    ismodifiedcode = Column(Integer)
    docid = Column(Unicode(36))
    ts = Column(TIMESTAMP)
    updatedBy = Column(Unicode(32))
    priuserdefnvc1 = Column(Unicode(500))
    priuserdefdecm1 = Column(Numeric(28, 14))
    priuserdefnvc2 = Column(Unicode(500))
    priuserdefdecm2 = Column(Numeric(28, 14))
    priuserdefnvc3 = Column(Unicode(500))
    priuserdefdecm3 = Column(Numeric(28, 14))
    priuserdefnvc4 = Column(Unicode(500))
    priuserdefdecm4 = Column(Numeric(28, 14))
    priuserdefnvc5 = Column(Unicode(500))
    priuserdefdecm5 = Column(Numeric(28, 14))
    priuserdefnvc6 = Column(Unicode(500))
    priuserdefdecm6 = Column(Numeric(28, 14))
    pubuserdefnvc1 = Column(Unicode(500))
    pubuserdefdecm1 = Column(Numeric(28, 14))
    pubuserdefnvc2 = Column(Unicode(500))
    pubuserdefdecm2 = Column(Numeric(28, 14))
    pubuserdefnvc3 = Column(Unicode(500))
    pubuserdefdecm3 = Column(Numeric(28, 14))
    pubuserdefnvc4 = Column(Unicode(500))
    pubuserdefdecm4 = Column(Numeric(28, 14))
    pubuserdefnvc5 = Column(Unicode(500))
    pubuserdefdecm5 = Column(Numeric(28, 14))
    pubuserdefnvc6 = Column(Unicode(500))
    pubuserdefdecm6 = Column(Numeric(28, 14))
    IsAutoGenerateSaleOrderBOM = Column(Integer)
    IsAutoGenerateRouting = Column(Integer)
    SourceVoucherCode = Column(Unicode(50))
    isnomodify = Column(Unicode(1000))
    changer = Column(Unicode(50))
    Mobilephone = Column(Unicode(50))
    MemberAddress = Column(Unicode(50))
    PrintCount = Column(Integer)
    IsSeparateByWareHouse = Column(Integer)
    OrigReceiveAmount = Column(Numeric(28, 14))
    ReceiveAmount = Column(Numeric(28, 14))
    collaborateVoucherCode = Column(Unicode(30))
    ExternalCode = Column(Unicode(50))
    ID = Column(Integer, primary_key=True)
    idbusinesstype = Column(Integer)
    idcurrency = Column(Integer, index=True)
    iddepartment = Column(Integer, index=True)
    IdMember = Column(Integer)
    idmarketingOrgan = Column(Integer, index=True)
    idcustomer = Column(Integer, index=True)
    idsettlecustomer = Column(Integer, index=True)
    idclerk = Column(Integer, index=True)
    idproject = Column(Integer, index=True)
    idwarehouse = Column(Integer, index=True)
    idCollaborateUpVoucherType = Column(Integer)
    idCollaborateUpVoucher = Column(Integer)
    DataSource = Column(Integer)
    deliveryMode = Column(Integer)
    isCancel = Column(Integer)
    isSaleDelivery = Column(Integer)
    isSaleOut = Column(Integer)
    reciveType = Column(Integer)
    voucherState = Column(Integer)
    auditorid = Column(Integer)
    makerid = Column(Integer)
    changerid = Column(Integer)
    idCollaborateDownVoucherType = Column(Integer)
    CollaborateState = Column(Integer)
    idCollaborateDownDraftVoucher = Column(Integer)
    SourceVoucherID = Column(Integer)
    idsourcevouchertype = Column(Integer, index=True)
    deliveryDate = Column(DateTime)
    voucherdate = Column(DateTime, index=True)
    madedate = Column(DateTime)
    auditeddate = Column(DateTime)
    createdtime = Column(DateTime, index=True)
    updated = Column(DateTime)
    changedate = Column(DateTime)
    ExternalVoucherCode = Column(Unicode(50), server_default=text("(NULL)"))


class SASaleOrderSubscription(Base):
    __tablename__ = 'SA_SaleOrderSubscription'

    code = Column(Unicode(30))
    amount = Column(Numeric(28, 14))
    origAmount = Column(Numeric(28, 14))
    billNo = Column(Unicode(30))
    ts = Column(TIMESTAMP)
    updatedBy = Column(Unicode(32))
    id = Column(Integer, primary_key=True)
    idbankaccount = Column(Integer)
    idsettlestyle = Column(Integer)
    idSaleOrderDTO = Column(Integer, index=True)
    SourceVoucherId = Column(Integer)
    SourceVoucherDetailId = Column(Integer)
    updated = Column(DateTime, index=True)


class SASaleOrderSourceRelation(Base):
    __tablename__ = 'SA_SaleOrder_SourceRelation'

    quantity = Column(Numeric(28, 14))
    quantity2 = Column(Numeric(28, 14))
    baseQuantity = Column(Numeric(28, 14))
    subQuantity = Column(Numeric(28, 14))
    ts = Column(TIMESTAMP, nullable=False)
    updatedBy = Column(Unicode(32))
    id = Column(Integer, primary_key=True)
    idbaseunit = Column(Integer)
    idsubunit = Column(Integer)
    idunit = Column(Integer)
    idunit2 = Column(Integer)
    voucherId = Column(Integer)
    idSaleOrderDetailDTO = Column(Integer, index=True)
    sourceVoucherId = Column(Integer)
    sourceVoucherDetailId = Column(Integer)
    idsourcevouchertype = Column(Integer, index=True)
    updated = Column(DateTime)


class SASaleOrderB(Base):
    __tablename__ = 'SA_SaleOrder_b'
    __table_args__ = (
        Index('IDX_SA_SaleOrder_b_PromotionSingle', 'PromotionSingleTypeID', 'PromotionSingleVoucherCode'),
        Index('IDX_SA_SaleOrder_b_PromotionPresent', 'PromotionPresentTypeID', 'PromotionPresentVoucherCode'),
        Index('IDX_SA_SaleOrder_b_mix1', 'detailVoucherState', 'id', 'idSaleOrderDTO', 'idinventory', 'idbaseunit', 'quantity', 'baseQuantity', 'origTaxPrice', 'taxPrice', 'origTaxAmount', 'iddestvouchertype')
    )

    code = Column(Unicode(30))
    quantity = Column(Numeric(28, 14))
    quantity2 = Column(Numeric(28, 14))
    baseQuantity = Column(Numeric(28, 14))
    subQuantity = Column(Numeric(28, 14))
    compositionQuantity = Column(Unicode(100))
    origPrice = Column(Numeric(28, 14))
    price = Column(Numeric(28, 14))
    basePrice = Column(Numeric(28, 14))
    discountRate = Column(Numeric(28, 14))
    origDiscountPrice = Column(Numeric(28, 14))
    discountPrice = Column(Numeric(28, 14))
    baseDiscountPrice = Column(Numeric(28, 14))
    taxRate = Column(Numeric(28, 14))
    origTaxPrice = Column(Numeric(28, 14))
    taxPrice = Column(Numeric(28, 14))
    baseTaxPrice = Column(Numeric(28, 14))
    origDiscountAmount = Column(Numeric(28, 14))
    discountAmount = Column(Numeric(28, 14))
    origTax = Column(Numeric(28, 14))
    tax = Column(Numeric(28, 14))
    origTaxAmount = Column(Numeric(28, 14))
    taxAmount = Column(Numeric(28, 14))
    isPresent = Column(Integer)
    manufactureQuantity = Column(Numeric(28, 14))
    manufactureQuantity2 = Column(Numeric(28, 14))
    purchaseQuantity = Column(Numeric(28, 14))
    purchaseQuantity2 = Column(Numeric(28, 14))
    deliveryQuantity = Column(Numeric(28, 14))
    deliveryQuantity2 = Column(Numeric(28, 14))
    saleOutQuantity = Column(Numeric(28, 14))
    saleOutQuantity2 = Column(Numeric(28, 14))
    executedQuantity = Column(Numeric(28, 14))
    executedQuantity2 = Column(Numeric(28, 14))
    unitExchangeRate = Column(Numeric(28, 14))
    origDiscount = Column(Numeric(28, 14))
    discount = Column(Numeric(28, 14))
    taxFlag = Column(Integer)
    inventoryBarCode = Column(Unicode(200))
    partnerInventoryCode = Column(Unicode(300))
    ts = Column(TIMESTAMP)
    updatedBy = Column(Unicode(32))
    freeItem0 = Column(Unicode(300))
    freeItem1 = Column(Unicode(300))
    freeItem2 = Column(Unicode(300))
    freeItem3 = Column(Unicode(300))
    freeItem4 = Column(Unicode(300))
    freeItem5 = Column(Unicode(300))
    freeItem6 = Column(Unicode(300))
    freeItem7 = Column(Unicode(300))
    freeItem8 = Column(Unicode(300))
    freeItem9 = Column(Unicode(300))
    priuserdefnvc1 = Column(Unicode(500))
    priuserdefdecm1 = Column(Numeric(28, 14))
    priuserdefnvc2 = Column(Unicode(500))
    priuserdefdecm2 = Column(Numeric(28, 14))
    priuserdefnvc3 = Column(Unicode(500))
    priuserdefdecm3 = Column(Numeric(28, 14))
    priuserdefnvc4 = Column(Unicode(500))
    priuserdefdecm4 = Column(Numeric(28, 14))
    pubuserdefnvc1 = Column(Unicode(500))
    pubuserdefdecm1 = Column(Numeric(28, 14))
    pubuserdefnvc2 = Column(Unicode(500))
    pubuserdefdecm2 = Column(Numeric(28, 14))
    pubuserdefnvc3 = Column(Unicode(500))
    pubuserdefdecm3 = Column(Numeric(28, 14))
    pubuserdefnvc4 = Column(Unicode(500))
    pubuserdefdecm4 = Column(Numeric(28, 14))
    partnerInventoryName = Column(Unicode(300))
    HasPRA = Column(Integer)
    prarequiretimes = Column(Integer)
    hasorderbom = Column(Integer)
    isnomodify = Column(Unicode(1000))
    SourceVoucherCode = Column(Unicode(50))
    detailVoucherState = Column(Unicode(20))
    Retailprice = Column(Numeric(28, 14))
    DistributionQuantity = Column(Numeric(28, 14))
    DistributionQuantity2 = Column(Numeric(28, 14))
    PriceStrategyTypeName = Column(Unicode(200))
    PriceStrategySchemeIds = Column(Unicode(1000))
    PriceStrategySchemeNames = Column(Unicode(400))
    PromotionVoucherCodes = Column(Unicode(400))
    PromotionVoucherIds = Column(Unicode(400))
    IsMemberIntegral = Column(Integer)
    IsPromotionPresent = Column(Integer)
    PromotionPresentVoucherCode = Column(Unicode(50))
    PromotionSingleVoucherCode = Column(Unicode(50))
    PromotionPresentGroupID = Column(Unicode(150))
    PromotionSingleGroupID = Column(Unicode(150))
    DetailMemo = Column(Unicode(200))
    id = Column(Integer, primary_key=True)
    idbom = Column(Integer, index=True)
    idinventory = Column(Integer, index=True)
    idproject = Column(Integer, index=True)
    idbaseunit = Column(Integer)
    idsubunit = Column(Integer)
    idunit = Column(Integer)
    idunit2 = Column(Integer)
    idwarehouse = Column(Integer)
    CashbackWay = Column(Integer)
    PriceStrategyTypeId = Column(Integer)
    PromotionPresentTypeID = Column(Integer)
    PromotionSingleTypeID = Column(Integer)
    PromotionPresentVoucherID = Column(Integer)
    PromotionSingleVoucherID = Column(Integer)
    idSaleOrderDTO = Column(Integer, index=True)
    SourceVoucherId = Column(Integer)
    SourceVoucherDetailId = Column(Integer)
    iddestvouchertype = Column(Integer, index=True)
    idsourcevouchertype = Column(Integer, index=True)
    deliveryDate = Column(DateTime)
    updated = Column(DateTime)
    LatestCost = Column(Numeric(28, 14), server_default=text("(NULL)"))
    LatestPOrigTaxPrice = Column(Numeric(28, 14), server_default=text("(NULL)"))
    LatestSaleOrigTaxPrice = Column(Numeric(28, 14), server_default=text("(NULL)"))
    LowestSalePrice = Column(Numeric(28, 14), server_default=text("(NULL)"))
    SingleInvGrossProfit = Column(Numeric(28, 14), server_default=text("(NULL)"))
    GrossProfit = Column(Numeric(28, 14), server_default=text("(NULL)"))
    GrossProfitRate = Column(Numeric(28, 14), server_default=text("(NULL)"))
    DataSource = Column(Integer, server_default=text("(NULL)"))


class SASaleQuotation(Base):
    __tablename__ = 'SA_SaleQuotation'

    code = Column(Unicode(30), index=True)
    name = Column(Unicode(200))
    exchangeRate = Column(Numeric(28, 14))
    discountRate = Column(Numeric(28, 14))
    memo = Column(Unicode(200))
    origTaxAmount = Column(Numeric(28, 14))
    origamount = Column(Numeric(28, 14))
    origdiscountamount = Column(Numeric(28, 14))
    discountamount = Column(Numeric(28, 14))
    amount = Column(Numeric(28, 14))
    taxamount = Column(Numeric(28, 14))
    maker = Column(Unicode(50))
    auditor = Column(Unicode(50))
    reviser = Column(Unicode(50))
    iscarriedforwardout = Column(Integer)
    iscarriedforwardin = Column(Integer)
    ismodifiedcode = Column(Integer)
    docid = Column(Unicode(36))
    ts = Column(TIMESTAMP)
    updatedBy = Column(Unicode(32))
    isNoModify = Column(Unicode(1000))
    priuserdefnvc1 = Column(Unicode(500))
    priuserdefdecm1 = Column(Numeric(28, 14))
    priuserdefnvc2 = Column(Unicode(500))
    priuserdefdecm2 = Column(Numeric(28, 14))
    priuserdefnvc3 = Column(Unicode(500))
    priuserdefdecm3 = Column(Numeric(28, 14))
    priuserdefnvc4 = Column(Unicode(500))
    priuserdefdecm4 = Column(Numeric(28, 14))
    priuserdefnvc5 = Column(Unicode(500))
    priuserdefdecm5 = Column(Numeric(28, 14))
    priuserdefnvc6 = Column(Unicode(500))
    priuserdefdecm6 = Column(Numeric(28, 14))
    pubuserdefnvc1 = Column(Unicode(500))
    pubuserdefdecm1 = Column(Numeric(28, 14))
    pubuserdefnvc2 = Column(Unicode(500))
    pubuserdefdecm2 = Column(Numeric(28, 14))
    pubuserdefnvc3 = Column(Unicode(500))
    pubuserdefdecm3 = Column(Numeric(28, 14))
    pubuserdefnvc4 = Column(Unicode(500))
    pubuserdefdecm4 = Column(Numeric(28, 14))
    pubuserdefnvc5 = Column(Unicode(500))
    pubuserdefdecm5 = Column(Numeric(28, 14))
    pubuserdefnvc6 = Column(Unicode(500))
    pubuserdefdecm6 = Column(Numeric(28, 14))
    Mobilephone = Column(Unicode(50))
    MemberAddress = Column(Unicode(50))
    PrintCount = Column(Integer)
    id = Column(Integer, primary_key=True)
    idcurrency = Column(Integer)
    iddepartment = Column(Integer, index=True)
    IdMember = Column(Integer)
    idmarketingOrgan = Column(Integer, index=True)
    idcustomer = Column(Integer, index=True)
    idclerk = Column(Integer, index=True)
    idproject = Column(Integer, index=True)
    recivetype = Column(Integer)
    transactionFlag = Column(Integer)
    voucherstate = Column(Integer)
    auditorid = Column(Integer)
    makerid = Column(Integer)
    expirydate = Column(DateTime)
    voucherdate = Column(DateTime, index=True)
    madedate = Column(DateTime)
    auditeddate = Column(DateTime)
    createdtime = Column(DateTime, index=True)
    updated = Column(DateTime)


class SASaleQuotationB(Base):
    __tablename__ = 'SA_SaleQuotation_b'
    __table_args__ = (
        Index('IDX_SA_SaleQuotation_b_PromotionSingle', 'PromotionSingleTypeID', 'PromotionSingleVoucherCode'),
        Index('IDX_SA_SaleQuotation_b_PromotionPresent', 'PromotionPresentTypeID', 'PromotionPresentVoucherCode')
    )

    code = Column(Unicode(30))
    isNoModify = Column(Unicode(1000))
    inventorybarcode = Column(Unicode(200))
    partnerinventoryname = Column(Unicode(300))
    partnerinventorycode = Column(Unicode(300))
    quantity = Column(Numeric(28, 14))
    quantity2 = Column(Numeric(28, 14))
    baseQuantity = Column(Numeric(28, 14))
    subQuantity = Column(Numeric(28, 14))
    UnitExchangeRate = Column(Numeric(28, 14))
    compositionquantity = Column(Unicode(50))
    origPrice = Column(Numeric(28, 14))
    origDiscountPrice = Column(Numeric(28, 14))
    origTaxPrice = Column(Numeric(28, 14))
    DiscountRate = Column(Numeric(28, 14))
    taxRate = Column(Numeric(28, 14))
    origDiscountAmount = Column(Numeric(28, 14))
    origTaxAmount = Column(Numeric(28, 14))
    origTax = Column(Numeric(28, 14))
    origDiscount = Column(Numeric(28, 14))
    price = Column(Numeric(28, 14))
    discountPrice = Column(Numeric(28, 14))
    taxPrice = Column(Numeric(28, 14))
    discountAmount = Column(Numeric(28, 14))
    taxAmount = Column(Numeric(28, 14))
    tax = Column(Numeric(28, 14))
    discount = Column(Numeric(28, 14))
    saleOrderIssueQuantity = Column(Numeric(28, 14))
    saleOrderIssueQuantity2 = Column(Numeric(28, 14))
    ts = Column(TIMESTAMP)
    updatedBy = Column(Unicode(32))
    origAmount = Column(Numeric(28, 14))
    amount = Column(Numeric(28, 14))
    taxFlag = Column(Integer)
    freeItem0 = Column(Unicode(300))
    freeItem1 = Column(Unicode(300))
    freeItem2 = Column(Unicode(300))
    freeItem3 = Column(Unicode(300))
    freeItem4 = Column(Unicode(300))
    freeItem5 = Column(Unicode(300))
    freeItem6 = Column(Unicode(300))
    freeItem7 = Column(Unicode(300))
    freeItem8 = Column(Unicode(300))
    freeItem9 = Column(Unicode(300))
    priuserdefnvc1 = Column(Unicode(500))
    priuserdefdecm1 = Column(Numeric(28, 14))
    priuserdefnvc2 = Column(Unicode(500))
    priuserdefdecm2 = Column(Numeric(28, 14))
    priuserdefnvc3 = Column(Unicode(500))
    priuserdefdecm3 = Column(Numeric(28, 14))
    priuserdefnvc4 = Column(Unicode(500))
    priuserdefdecm4 = Column(Numeric(28, 14))
    pubuserdefnvc1 = Column(Unicode(500))
    pubuserdefdecm1 = Column(Numeric(28, 14))
    pubuserdefnvc2 = Column(Unicode(500))
    pubuserdefdecm2 = Column(Numeric(28, 14))
    pubuserdefnvc3 = Column(Unicode(500))
    pubuserdefdecm3 = Column(Numeric(28, 14))
    pubuserdefnvc4 = Column(Unicode(500))
    pubuserdefdecm4 = Column(Numeric(28, 14))
    Retailprice = Column(Numeric(28, 14))
    PriceStrategyTypeName = Column(Unicode(200))
    PriceStrategySchemeIds = Column(Unicode(1000))
    PriceStrategySchemeNames = Column(Unicode(400))
    PromotionVoucherCodes = Column(Unicode(400))
    PromotionVoucherIds = Column(Unicode(400))
    IsMemberIntegral = Column(Integer)
    IsPromotionPresent = Column(Integer)
    PromotionPresentVoucherCode = Column(Unicode(50))
    PromotionSingleVoucherCode = Column(Unicode(50))
    PromotionPresentGroupID = Column(Unicode(150))
    PromotionSingleGroupID = Column(Unicode(150))
    ID = Column(Integer, primary_key=True)
    idinventory = Column(Integer, index=True)
    idproject = Column(Integer, index=True)
    idbaseunit = Column(Integer)
    idsubunit = Column(Integer)
    idunit = Column(Integer)
    idunit2 = Column(Integer)
    CashbackWay = Column(Integer)
    PriceStrategyTypeId = Column(Integer)
    PromotionPresentTypeID = Column(Integer)
    PromotionSingleTypeID = Column(Integer)
    PromotionPresentVoucherID = Column(Integer)
    PromotionSingleVoucherID = Column(Integer)
    idSaleQuotationDTO = Column(Integer, index=True)
    sourcevoucherdetailid = Column(Integer)
    expirydate = Column(DateTime)
    updated = Column(DateTime, index=True)
    LatestCost = Column(Numeric(28, 14), server_default=text("(NULL)"))
    LatestPOrigTaxPrice = Column(Numeric(28, 14), server_default=text("(NULL)"))
    LatestSaleOrigTaxPrice = Column(Numeric(28, 14), server_default=text("(NULL)"))
    LowestSalePrice = Column(Numeric(28, 14), server_default=text("(NULL)"))
    SingleInvGrossProfit = Column(Numeric(28, 14), server_default=text("(NULL)"))
    GrossProfit = Column(Numeric(28, 14), server_default=text("(NULL)"))
    GrossProfitRate = Column(Numeric(28, 14), server_default=text("(NULL)"))


t_SCM_PrintMemory = Table(
    'SCM_PrintMemory', metadata,
    Column('voucherName', Unicode(200), nullable=False),
    Column('flag', BIT, nullable=False)
)


class SMCodingPrefixion(Base):
    __tablename__ = 'SM_CodingPrefixion'

    code = Column(Unicode(30), nullable=False)
    name = Column(Unicode(200))
    prefixionlength = Column(Integer)
    usedtime = Column(Integer, nullable=False)
    isneedtransferred = Column(Integer)
    ts = Column(TIMESTAMP, nullable=False)
    id = Column(Integer, primary_key=True)
    prefixionInterceptType = Column(Integer, nullable=False, server_default=text("((0))"))


class SMCodingRuleRelationWithPrefixion(Base):
    __tablename__ = 'SM_CodingRuleRelationWithPrefixion'

    code = Column(Unicode(30))
    name = Column(Unicode(200))
    ts = Column(TIMESTAMP, nullable=False)
    ddlOrder = Column(Integer)
    IsSystem = Column(Integer, nullable=False, server_default=text("((1))"))
    id = Column(Integer, primary_key=True)
    ExpressionName = Column(Unicode(60))
    idcodingprefixion = Column(Integer, nullable=False, server_default=text("((0))"))
    idvouchertype = Column(Integer, nullable=False, server_default=text("((0))"))


class SMFCAccountExtendRule(Base):
    __tablename__ = 'SM_FC_AccountExtendRule'

    code = Column(Unicode(30))
    name = Column(Unicode(200))
    rowidx = Column(Integer)
    inventorypriuserdefdecm0 = Column(Numeric(28, 14))
    inventorypriuserdefnvc0 = Column(Unicode(500))
    inventorypriuserdefdecm1 = Column(Numeric(28, 14))
    inventorypriuserdefnvc1 = Column(Unicode(500))
    inventorypriuserdefdecm2 = Column(Numeric(28, 14))
    inventorypriuserdefnvc2 = Column(Unicode(500))
    inventorypriuserdefdecm3 = Column(Numeric(28, 14))
    inventorypriuserdefnvc3 = Column(Unicode(500))
    inventorypriuserdefdecm4 = Column(Numeric(28, 14))
    inventorypriuserdefnvc4 = Column(Unicode(500))
    headerpubuserdefdecm0 = Column(Numeric(28, 14))
    headerpubuserdefnvc0 = Column(Unicode(500))
    headerpubuserdefdecm1 = Column(Numeric(28, 14))
    headerpubuserdefnvc1 = Column(Unicode(500))
    headerpubuserdefdecm2 = Column(Numeric(28, 14))
    headerpubuserdefnvc2 = Column(Unicode(500))
    headerpubuserdefdecm3 = Column(Numeric(28, 14))
    headerpubuserdefnvc3 = Column(Unicode(500))
    headerpubuserdefdecm4 = Column(Numeric(28, 14))
    headerpubuserdefnvc4 = Column(Unicode(500))
    headerpubuserdefdecm5 = Column(Numeric(28, 14))
    headerpubuserdefnvc5 = Column(Unicode(500))
    headerpriuserdefdecm0 = Column(Numeric(28, 14))
    headerpriuserdefnvc0 = Column(Unicode(500))
    headerpriuserdefdecm1 = Column(Numeric(28, 14))
    headerpriuserdefnvc1 = Column(Unicode(500))
    headerpriuserdefdecm2 = Column(Numeric(28, 14))
    headerpriuserdefnvc2 = Column(Unicode(500))
    headerpriuserdefdecm3 = Column(Numeric(28, 14))
    headerpriuserdefnvc3 = Column(Unicode(500))
    headerpriuserdefdecm4 = Column(Numeric(28, 14))
    headerpriuserdefnvc4 = Column(Unicode(500))
    headerpriuserdefdecm5 = Column(Numeric(28, 14))
    headerpriuserdefnvc5 = Column(Unicode(500))
    detailspubuserdefdecm0 = Column(Numeric(28, 14))
    detailspubuserdefnvc0 = Column(Unicode(500))
    detailspubuserdefdecm1 = Column(Numeric(28, 14))
    detailspubuserdefnvc1 = Column(Unicode(500))
    detailspubuserdefdecm2 = Column(Numeric(28, 14))
    detailspubuserdefnvc2 = Column(Unicode(500))
    detailspubuserdefdecm3 = Column(Numeric(28, 14))
    detailspubuserdefnvc3 = Column(Unicode(500))
    detailspriuserdefdecm0 = Column(Numeric(28, 14))
    detailspriuserdefnvc0 = Column(Unicode(500))
    detailspriuserdefdecm1 = Column(Numeric(28, 14))
    detailspriuserdefnvc1 = Column(Unicode(500))
    detailspriuserdefdecm2 = Column(Numeric(28, 14))
    detailspriuserdefnvc2 = Column(Unicode(500))
    detailspriuserdefdecm3 = Column(Numeric(28, 14))
    detailspriuserdefnvc3 = Column(Unicode(500))
    accountcode = Column(Unicode(50))
    accountname = Column(Unicode(50))
    sequencenumber = Column(Integer)
    ts = Column(TIMESTAMP, nullable=False)
    updatedBy = Column(Unicode(32))
    islaborcost = Column(Integer)
    summary = Column(Unicode(200))
    id = Column(Integer, primary_key=True)
    idaccount = Column(Integer)
    idassetClass = Column(Integer)
    idassetProp = Column(Integer)
    idbankaccount = Column(Integer)
    idbusitype = Column(Integer)
    idcurrency = Column(Integer)
    iddepartment = Column(Integer)
    iddistrict = Column(Integer)
    idexpenseitem = Column(Integer)
    idhandleReason = Column(Integer)
    idincDecWay = Column(Integer)
    idincome = Column(Integer)
    idinventory = Column(Integer)
    idinventoryclass = Column(Integer)
    idpartner = Column(Integer)
    idpartnerclass = Column(Integer)
    idproject = Column(Integer)
    idprojectClass = Column(Integer)
    idrdstyle = Column(Integer)
    idwarehouse = Column(Integer)
    adjusttype = Column(Integer)
    checkstate = Column(Integer)
    expensetype = Column(Integer)
    incomeExpensesType = Column(Integer)
    ProfitLossType = Column(Integer)
    idAccountRuleDTO = Column(Integer)
    idvouchertype = Column(Integer)
    createdtime = Column(DateTime)
    updated = Column(DateTime)


class SMFCAccountExtendRuleColumn(Base):
    __tablename__ = 'SM_FC_AccountExtendRuleColumn'

    code = Column(Unicode(30))
    name = Column(Unicode(200))
    idx = Column(Integer)
    isdisplay = Column(Integer)
    iscombin = Column(Integer)
    displayname = Column(Unicode(50))
    ismatchby = Column(Integer)
    issystemhidden = Column(Integer)
    baseinfo = Column(Unicode(50))
    idfieldname = Column(Unicode(50))
    sequencenumber = Column(Integer)
    ts = Column(TIMESTAMP, nullable=False)
    updatedBy = Column(Unicode(32))
    id = Column(Integer, primary_key=True)
    idedittablecolumn = Column(Integer)
    accountruletype = Column(Integer)
    geneaccountbytype = Column(Integer)
    createdtime = Column(DateTime)
    updated = Column(DateTime)


class SMFCAccountExtractCompositeColumn(Base):
    __tablename__ = 'SM_FC_AccountExtractCompositeColumn'

    code = Column(Unicode(30))
    name = Column(Unicode(200))
    baseinfo1 = Column(Unicode(50))
    baseinfo2 = Column(Unicode(50))
    ts = Column(TIMESTAMP, nullable=False)
    updatedBy = Column(Unicode(32))
    id = Column(Integer, primary_key=True)
    updated = Column(DateTime)


t_SM_FC_AccountRule = Table(
    'SM_FC_AccountRule', metadata,
    Column('code', Unicode(30)),
    Column('name', Unicode(200)),
    Column('visible', Integer),
    Column('extendrulemodelid', Unicode(50)),
    Column('extendrulecontrollerid', Unicode(50)),
    Column('extractmodelid', Unicode(50)),
    Column('extractcontrollerid', Unicode(50)),
    Column('accountcode', Unicode(50)),
    Column('accountname', Unicode(50)),
    Column('sequencenumber', Integer),
    Column('ts', TIMESTAMP, nullable=False),
    Column('updatedBy', Unicode(32)),
    Column('category', Unicode(50)),
    Column('id', Integer, nullable=False),
    Column('idaccount', Integer),
    Column('idedittable', Integer),
    Column('createdtime', DateTime),
    Column('updated', DateTime)
)


class SMFCDocSimpleSourceVoucher(Base):
    __tablename__ = 'SM_FC_DocSimpleSourceVoucher'

    code = Column(Unicode(30))
    name = Column(Unicode(200))
    voucherCode = Column(Unicode(30))
    selected = Column(Integer)
    saledispatchcode = Column(Unicode(50))
    executedquantity = Column(Numeric(28, 14))
    executedquantity2 = Column(Numeric(28, 14))
    costprice = Column(Numeric(28, 14))
    costamount = Column(Numeric(28, 14))
    billno = Column(Unicode(50))
    ts = Column(TIMESTAMP, nullable=False)
    updatedBy = Column(Unicode(32))
    id = Column(Integer, primary_key=True)
    VoucherTs = Column(BINARY(8))
    VoucherDetailTs = Column(BINARY(8))
    MergeCode = Column(Unicode(50))
    OrigAmount = Column(Unicode(50))
    Amount = Column(Unicode(50))
    Memo = Column(Unicode(200))
    InvoiceCode = Column(Unicode(200))
    sequencenumber = Column(Integer)
    idbankaccount = Column(Integer)
    idbusitype = Column(Integer)
    idcurrency = Column(Integer)
    iddepartment = Column(Integer)
    idinventory = Column(Integer)
    idcustomer = Column(Integer)
    idsecondcustomer = Column(Integer)
    idsecondsupplier = Column(Integer)
    idsupplier = Column(Integer)
    idclerck = Column(Integer)
    idproject = Column(Integer)
    idinrdstyle = Column(Integer)
    idoutrdstyle = Column(Integer)
    idbaesunit = Column(Integer)
    idBankAccount2 = Column(Integer)
    idExpenseItem = Column(Integer)
    idIncome = Column(Integer)
    voucherID = Column(Integer)
    userid = Column(Integer)
    voucherdetailid = Column(Integer)
    idvouchertype = Column(Integer)
    voucherDate = Column(DateTime)
    saledispatchdate = Column(DateTime)
    billdate = Column(DateTime)
    createdtime = Column(DateTime)
    updated = Column(DateTime)


class SMFCDocSourceVoucherCodtion(Base):
    __tablename__ = 'SM_FC_DocSourceVoucherCodtion'

    code = Column(Unicode(30))
    name = Column(Unicode(200))
    isPurchaseArrivalRelatedVoucher = Column(Integer)
    isclosingaccountcarryforward = Column(Integer)
    maxmergecode = Column(Integer)
    sequencenumber = Column(Integer)
    ts = Column(TIMESTAMP, nullable=False)
    updatedBy = Column(Unicode(32))
    id = Column(Integer, primary_key=True)
    idpropertyfilter = Column(Integer)
    createdtime = Column(DateTime)
    updated = Column(DateTime)


class SMFCDocSourceVoucherPropertyFilter(Base):
    __tablename__ = 'SM_FC_DocSourceVoucherPropertyFilter'

    code = Column(Unicode(30))
    name = Column(Unicode(200))
    startVoucherCode = Column(Unicode(50))
    endVoucherCode = Column(Unicode(50))
    startSupplierCode = Column(Unicode(50))
    endSupplierCode = Column(Unicode(50))
    startCustomerCode = Column(Unicode(50))
    endCustomerCode = Column(Unicode(50))
    startInventoryCode = Column(Unicode(50))
    endInventoryCode = Column(Unicode(50))
    outRdStyles = Column(Unicode(50))
    inRdStyles = Column(Unicode(50))
    inventoryClasss = Column(Unicode(50))
    departments = Column(Unicode(50))
    persons = Column(Unicode(50))
    warehouses = Column(Unicode(50))
    projects = Column(Unicode(50))
    bankaccounts = Column(Unicode(50))
    currencys = Column(Unicode(50))
    settleStyles = Column(Unicode(50))
    voucherGeneDocStatus = Column(Integer)
    inventory = Column(Unicode(50))
    customerclasses = Column(Unicode(50))
    startperiod = Column(Unicode(50))
    endperiod = Column(Unicode(50))
    sequencenumber = Column(Integer)
    ts = Column(TIMESTAMP, nullable=False)
    updatedBy = Column(Unicode(32))
    id = Column(Integer, primary_key=True)
    carryforwardtype = Column(Integer)
    rdPurchaseVoucherAccountState = Column(Integer)
    startVoucherDate = Column(DateTime)
    endVoucherDate = Column(DateTime)
    createdtime = Column(DateTime)
    updated = Column(DateTime)


class SMFCDocSourceVoucherType(Base):
    __tablename__ = 'SM_FC_DocSourceVoucherType'

    code = Column(Unicode(30))
    name = Column(Unicode(200))
    selected = Column(Integer)
    isvisiable = Column(Integer)
    tablename = Column(Unicode(50))
    sequencenumber = Column(Integer)
    ts = Column(TIMESTAMP, nullable=False)
    updatedBy = Column(Unicode(32))
    GroupType = Column(Unicode(50))
    id = Column(Integer, primary_key=True)
    idbusitype = Column(Integer)
    idDocSourceVoucherCondtionDTO = Column(Integer)
    idvouchertype = Column(Integer)
    createdtime = Column(DateTime)
    updated = Column(DateTime)


class SMFCDocSummaryDetailRule(Base):
    __tablename__ = 'SM_FC_DocSummaryDetailRule'

    code = Column(Unicode(30))
    name = Column(Unicode(200))
    summarytextofhead = Column(Unicode(60))
    isvouchertype = Column(Integer)
    isbusitype = Column(Integer)
    ispartner = Column(Integer)
    isdepartment = Column(Integer)
    isperson = Column(Integer)
    ismemo = Column(Integer)
    summarytextoftail = Column(Unicode(60))
    busitypename = Column(Unicode(50))
    partnername = Column(Unicode(50))
    personname = Column(Unicode(50))
    memoname = Column(Unicode(50))
    sequencenumber = Column(Integer)
    ts = Column(TIMESTAMP, nullable=False)
    updatedBy = Column(Unicode(32))
    id = Column(Integer, primary_key=True)
    idbusitype = Column(Integer)
    idvoucherType = Column(Integer)
    idDocSummaryRuleDTO = Column(Integer)
    createdtime = Column(DateTime)
    updated = Column(DateTime)


class SMFCDocSummaryRule(Base):
    __tablename__ = 'SM_FC_DocSummaryRule'

    code = Column(Unicode(30))
    name = Column(Unicode(200))
    summarytext = Column(Unicode(200))
    sequencenumber = Column(Integer)
    ts = Column(TIMESTAMP, nullable=False)
    updatedBy = Column(Unicode(32))
    id = Column(Integer, primary_key=True)
    createdtime = Column(DateTime)
    updated = Column(DateTime)


t_SM_FC_History_TransactionAuxiliaryInfo = Table(
    'SM_FC_History_TransactionAuxiliaryInfo', metadata,
    Column('id', UNIQUEIDENTIFIER, nullable=False),
    Column('code', Unicode(30)),
    Column('name', Unicode(200)),
    Column('dcdirection', UNIQUEIDENTIFIER),
    Column('vouchercode', Unicode(50)),
    Column('invoicecode', Unicode(50)),
    Column('origamount', Numeric(28, 14)),
    Column('amount', Numeric(28, 14)),
    Column('quantity', Numeric(28, 14)),
    Column('price', Numeric(28, 14)),
    Column('sequencenumber', Integer),
    Column('ts', TIMESTAMP, nullable=False),
    Column('updatedBy', Unicode(32)),
    Column('idTransactionEntryHistoryDTO', UNIQUEIDENTIFIER),
    Column('voucherdate', DateTime),
    Column('duedate', DateTime),
    Column('createdtime', DateTime),
    Column('updated', DateTime)
)


class SMFCHistoryTransactionDoc(Base):
    __tablename__ = 'SM_FC_History_TransactionDoc'

    code = Column(Unicode(30))
    name = Column(Unicode(200))
    attachedvouchernum = Column(Integer)
    sequencenumber = Column(Integer)
    ts = Column(TIMESTAMP, nullable=False)
    updatedBy = Column(Unicode(32))
    id = Column(Integer, primary_key=True)
    userid = Column(Integer)
    TransDocId = Column(Unicode(50))
    voucherdate = Column(DateTime)
    generatedate = Column(DateTime)
    createdtime = Column(DateTime)
    updated = Column(DateTime)


t_SM_FC_History_TransactionDocSourceRelation = Table(
    'SM_FC_History_TransactionDocSourceRelation', metadata,
    Column('code', Unicode(30)),
    Column('name', Unicode(200)),
    Column('sourcevoucherts', Unicode(50)),
    Column('sequencenumber', Integer),
    Column('ts', TIMESTAMP, nullable=False),
    Column('updatedBy', Unicode(32)),
    Column('id', Integer, nullable=False),
    Column('sourcevoucherid', Integer),
    Column('idTransactionDocHistoryDTO', Integer),
    Column('sourcevouchertypeid', Integer),
    Column('createdtime', DateTime),
    Column('updated', DateTime)
)


class SMFCHistoryTransactionEntry(Base):
    __tablename__ = 'SM_FC_History_TransactionEntry'

    code = Column(Unicode(30))
    name = Column(Unicode(200))
    summary = Column(Unicode(200))
    exchangerate = Column(Numeric(28, 14))
    origamountdr = Column(Numeric(28, 14))
    origamountcr = Column(Numeric(28, 14))
    amountdr = Column(Numeric(28, 14))
    amountcr = Column(Numeric(28, 14))
    quantitydr = Column(Numeric(28, 14))
    quantitycr = Column(Numeric(28, 14))
    price = Column(Numeric(28, 14))
    mergecode = Column(Unicode(50))
    origamount = Column(Numeric(28, 14))
    billno = Column(Unicode(50))
    memoto = Column(Unicode(200))
    accounttype = Column(Unicode(50))
    extend1 = Column(Unicode(50))
    extend2 = Column(Unicode(50))
    extend3 = Column(Unicode(50))
    sequencenumber = Column(Integer)
    ts = Column(TIMESTAMP, nullable=False)
    updatedBy = Column(Unicode(32))
    idauxiliaryinfo = Column(UNIQUEIDENTIFIER)
    id = Column(Integer, primary_key=True)
    dcdirection = Column(Integer)
    idTransactionDocHistoryDTO = Column(Integer)
    billdate = Column(DateTime)
    generatedate = Column(DateTime)
    createdtime = Column(DateTime)
    updated = Column(DateTime)


class SMFCHistoryTransactionEntrySourceRelation(Base):
    __tablename__ = 'SM_FC_History_TransactionEntrySourceRelation'

    code = Column(Unicode(30))
    name = Column(Unicode(200))
    sourcevoucherts = Column(Unicode(50))
    sourcevoucherdetailts = Column(Unicode(50))
    sequencenumber = Column(Integer)
    ts = Column(TIMESTAMP, nullable=False)
    updatedBy = Column(Unicode(32))
    id = Column(Integer, primary_key=True)
    carryforwardtype = Column(Integer)
    sourcevoucherid = Column(Integer)
    sourcevoucherdetailid = Column(Integer)
    idTransactionEntryHistoryDTO = Column(Integer)
    sourcevouchertypeid = Column(Integer)
    createdtime = Column(DateTime)
    updated = Column(DateTime)


t_SM_FC_MergeOption = Table(
    'SM_FC_MergeOption', metadata,
    Column('SequenceNumber', Integer),
    Column('Code', Unicode(30)),
    Column('Name', Unicode(200)),
    Column('IsEnabled', Integer),
    Column('IsVisible', Integer),
    Column('UpdatedBy', Unicode(32)),
    Column('Ts', TIMESTAMP, nullable=False),
    Column('ID', Integer, nullable=False),
    Column('CreatedTime', DateTime),
    Column('Updated', DateTime)
)


class SMFCMergeRule(Base):
    __tablename__ = 'SM_FC_MergeRule'

    code = Column(Unicode(30))
    name = Column(Unicode(200))
    isbusitype = Column(Integer)
    isdepartment = Column(Integer)
    ispartner = Column(Integer)
    isrdstyle = Column(Integer)
    isbanckaccount = Column(Integer)
    idbusitypename = Column(Unicode(50))
    iddepartmentname = Column(Unicode(50))
    idpartnername = Column(Unicode(50))
    idrdstylename = Column(Unicode(50))
    iddepartmentname2 = Column(Unicode(50))
    idpartnername2 = Column(Unicode(50))
    idrdstylename2 = Column(Unicode(50))
    idcurrencyname = Column(Unicode(50))
    idbanckaccountname = Column(Unicode(50))
    iscurrency = Column(Integer)
    isbusitypeenable = Column(Integer)
    isdepartmentenable = Column(Integer)
    ispartnerenable = Column(Integer)
    isrdstyleenable = Column(Integer)
    iscurrencyenable = Column(Integer)
    isbanckaccountenable = Column(Integer)
    sequencenumber = Column(Integer)
    ts = Column(TIMESTAMP, nullable=False)
    updatedBy = Column(Unicode(32))
    id = Column(Integer, primary_key=True)
    timeintervaltype = Column(Integer)
    idvoucherType = Column(Integer)
    createdtime = Column(DateTime)
    updated = Column(DateTime)


class SMFCPeriodBeginSyncAcc(Base):
    __tablename__ = 'SM_FC_PeriodBeginSyncAcc'

    code = Column(Unicode(30))
    name = Column(Unicode(200))
    origbalance = Column(Numeric(28, 14))
    balance = Column(Numeric(28, 14))
    sequencenumber = Column(Integer)
    ts = Column(TIMESTAMP, nullable=False)
    updatedBy = Column(Unicode(32))
    quantity = Column(Numeric(28, 14))
    id = Column(Integer, primary_key=True)
    idaccount = Column(Integer)
    idcurrency = Column(Integer)
    createdtime = Column(DateTime)
    updated = Column(DateTime)


class SMFCPeriodBeginSyncBizData(Base):
    __tablename__ = 'SM_FC_PeriodBeginSyncBizData'

    code = Column(Unicode(30))
    name = Column(Unicode(200))
    origbalance = Column(Numeric(28, 14))
    balance = Column(Numeric(28, 14))
    inventorypriuserdefnvc0 = Column(Unicode(500))
    inventorypriuserdefnvc1 = Column(Unicode(500))
    inventorypriuserdefnvc2 = Column(Unicode(500))
    inventorypriuserdefnvc3 = Column(Unicode(500))
    inventorypriuserdefnvc4 = Column(Unicode(500))
    inventorypriuserdefdecm0 = Column(Numeric(28, 14))
    inventorypriuserdefdecm1 = Column(Numeric(28, 14))
    inventorypriuserdefdecm2 = Column(Numeric(28, 14))
    inventorypriuserdefdecm3 = Column(Numeric(28, 14))
    inventorypriuserdefdecm4 = Column(Numeric(28, 14))
    periodbeginsynctype = Column(Integer)
    basequantity = Column(Numeric(28, 14))
    baseprice = Column(Numeric(28, 14))
    ts = Column(TIMESTAMP, nullable=False)
    updatedBy = Column(Unicode(32))
    amPropNote = Column(Unicode(200))
    arrivalDate = Column(DateTime)
    voucherDate = Column(DateTime)
    id = Column(Integer, primary_key=True)
    idAssetClass = Column(Integer)
    idAssetProp = Column(Integer)
    idbankaccount = Column(Integer)
    idcurrency = Column(Integer)
    iddepartment = Column(Integer)
    iddistrict = Column(Integer)
    idinventory = Column(Integer)
    idinventoryclass = Column(Integer)
    idinvlocation = Column(Integer)
    idpartner = Column(Integer)
    idpartnerclass = Column(Integer)
    idperson = Column(Integer)
    idproject = Column(Integer)
    idProjectClass = Column(Integer)
    idrdstyle = Column(Integer)
    idwarehouse = Column(Integer)
    bizdataid = Column(Integer)
    updated = Column(DateTime)


class SMFCPeriodBeginSyncData(Base):
    __tablename__ = 'SM_FC_PeriodBeginSyncData'

    code = Column(Unicode(30))
    name = Column(Unicode(200))
    periodbeginsynctype = Column(Integer)
    balance = Column(Numeric(28, 14))
    origbalance = Column(Numeric(28, 14))
    sequencenumber = Column(Integer)
    ts = Column(TIMESTAMP, nullable=False)
    updatedBy = Column(Unicode(32))
    quantity = Column(Numeric(28, 14))
    id = Column(Integer, primary_key=True)
    idaccount = Column(Integer)
    idcurrency = Column(Integer)
    idauxaccdepartment = Column(Integer)
    idauxaccinventory = Column(Integer)
    idauxacccustomer = Column(Integer)
    idauxaccsupplier = Column(Integer)
    idauxaccperson = Column(Integer)
    idauxaccproject = Column(Integer)
    idexauxacc1 = Column(Integer)
    idexauxacc10 = Column(Integer)
    idexauxacc2 = Column(Integer)
    idexauxacc3 = Column(Integer)
    idexauxacc4 = Column(Integer)
    idexauxacc5 = Column(Integer)
    idexauxacc6 = Column(Integer)
    idexauxacc7 = Column(Integer)
    idexauxacc8 = Column(Integer)
    idexauxacc9 = Column(Integer)
    idbizdata = Column(Integer)
    createdtime = Column(DateTime)
    updated = Column(DateTime)


class SMFCPeriodBeginSyncError(Base):
    __tablename__ = 'SM_FC_PeriodBeginSyncError'

    code = Column(Unicode(30))
    name = Column(Unicode(200))
    keywordinfo = Column(Unicode(200))
    failreason = Column(Unicode(200))
    sequencenumber = Column(Integer)
    ts = Column(TIMESTAMP, nullable=False)
    updatedBy = Column(Unicode(32))
    id = Column(Integer, primary_key=True)
    periodbeginsyncmodule = Column(Integer)
    createdtime = Column(DateTime)
    updated = Column(DateTime)


t_SM_FC_QryVoucherURL = Table(
    'SM_FC_QryVoucherURL', metadata,
    Column('code', Unicode(30)),
    Column('name', Unicode(200)),
    Column('vouchertypecode', Unicode(30)),
    Column('requeststr', Unicode(200)),
    Column('urlstr', String(200, u'Chinese_PRC_CI_AS')),
    Column('sequencenumber', Integer),
    Column('ts', TIMESTAMP),
    Column('updatedBy', Unicode(32)),
    Column('id', Integer, nullable=False),
    Column('idvouchertype', Integer),
    Column('createdtime', DateTime),
    Column('updated', DateTime)
)


class SMIndMessageRule(Base):
    __tablename__ = 'SM_IndMessageRule'

    code = Column(Unicode(30))
    name = Column(Unicode(200))
    messageobject = Column(Unicode(50))
    template = Column(Unicode(50))
    receivers = Column(Integer)
    im = Column(Integer)
    sms = Column(Integer)
    mail = Column(Integer)
    internalmessage = Column(Integer)
    ts = Column(TIMESTAMP)
    updatedBy = Column(Unicode(32))
    associatereceiver = Column(Unicode(512))
    subject = Column(Unicode(254))
    body = Column(LargeBinary)
    ReceiversAttachment = Column(Integer)
    sns = Column(Integer)
    id = Column(Integer, primary_key=True)
    messagetype = Column(Integer)
    priority = Column(Integer)
    iduser = Column(Integer)
    ReceiversAttachmentId = Column(Unicode(100))
    idsendtimerule = Column(Integer)
    updated = Column(DateTime)


class SMInformation(Base):
    __tablename__ = 'SM_Information'

    Id = Column(Integer, primary_key=True)
    Item = Column(Unicode(50), nullable=False)
    Data = Column(Text(2147483647, u'Chinese_PRC_CI_AS'))
    Ts = Column(TIMESTAMP, nullable=False)


class SMMessageAssociateInfo(Base):
    __tablename__ = 'SM_MessageAssociateInfo'

    messageobject = Column(Unicode(50))
    associatefield = Column(Unicode(500))
    associatetype = Column(Unicode(500))
    ts = Column(TIMESTAMP)
    associateSelectField = Column(Unicode(50))
    id = Column(Integer, primary_key=True)
    isUse = Column(BIT, server_default=text("((1))"))


t_SM_MessageMultiTemplate = Table(
    'SM_MessageMultiTemplate', metadata,
    Column('Key_Word', Unicode(50)),
    Column('Value_Word', Unicode(200))
)


class SMMessageReceivers(Base):
    __tablename__ = 'SM_MessageReceivers'

    personcode = Column(Unicode(50))
    personname = Column(Unicode(50))
    department = Column(Unicode(50))
    email = Column(Unicode(100))
    phone = Column(Unicode(50))
    useraccount = Column(Unicode(50))
    username = Column(Unicode(50))
    messageobject = Column(Unicode(50))
    ts = Column(TIMESTAMP)
    updatedBy = Column(Unicode(32))
    id = Column(Integer, primary_key=True)
    idperson = Column(Integer)
    idmember = Column(Integer)
    messagetype = Column(Integer)
    iduser = Column(Integer)
    idMessageRule = Column(Integer)
    updated = Column(DateTime)


class SMMessageTemplate(Base):
    __tablename__ = 'SM_MessageTemplate'

    name = Column(Unicode(200))
    bodytemplate = Column(LargeBinary)
    messageobject = Column(Unicode(50))
    subjecttemplate = Column(Unicode(200))
    ts = Column(TIMESTAMP)
    id = Column(Integer, primary_key=True)
    messagetype = Column(Integer)
    TemplateType = Column(Integer)


class SMPeriod(Base):
    __tablename__ = 'SM_Period'

    currentyear = Column(Integer)
    currentperiod = Column(Integer)
    begindate = Column(DateTime)
    enddate = Column(DateTime)
    BizTerminalState = Column(Integer, nullable=False, server_default=text("((0))"))
    FiTerminalState = Column(Integer, nullable=False, server_default=text("((0))"))
    ts = Column(TIMESTAMP)
    isadjustment = Column(Integer)
    id = Column(Integer, primary_key=True)


class SMPrintSolution(Base):
    __tablename__ = 'SM_PrintSolution'

    name = Column(Unicode(200), nullable=False)
    ts = Column(TIMESTAMP, nullable=False)
    ObjectName = Column(Unicode(200))
    MenuCode = Column(Unicode(200))
    id = Column(Integer, primary_key=True)
    PrintSolutionType = Column(Integer)
    IdQuerySolution = Column(Integer)
    IdPrintType = Column(Integer, nullable=False, server_default=text("((0))"))


class SMPrintSolutionType(Base):
    __tablename__ = 'SM_PrintSolutionType'

    ts = Column(TIMESTAMP, nullable=False)
    name = Column(Unicode(200), nullable=False)
    IsSystem = Column(Integer)
    Visible = Column(Integer)
    IsEnable = Column(Integer)
    InId = Column(Unicode(200))
    IsLeaf = Column(Integer)
    id = Column(Integer, primary_key=True)
    IdParent = Column(Integer)


class SMReportManualSendRule(Base):
    __tablename__ = 'SM_ReportManualSendRule'

    code = Column(Unicode(30))
    name = Column(Unicode(200))
    subject = Column(Unicode(254))
    sendtemplate = Column(Unicode(50))
    ts = Column(TIMESTAMP)
    updatedBy = Column(Unicode(32))
    body = Column(LargeBinary)
    id = Column(Integer, primary_key=True)
    attformat = Column(Integer)
    iduser = Column(Integer)
    updated = Column(DateTime)
    madeDate = Column(DateTime)


class SMSMSTemplate(Base):
    __tablename__ = 'SM_SMSTemplate'

    subjectvalue = Column(Unicode(1000))
    subjecttitle = Column(Unicode(300))
    bodyvalue = Column(Unicode(1000))
    bodytitle = Column(Unicode(300))
    messageobject = Column(Unicode(40))
    ts = Column(TIMESTAMP)
    selectfields = Column(Unicode(2000))
    isControlSendNum = Column(Integer)
    SendNum = Column(Integer)
    id = Column(Integer, primary_key=True)
    messagetype = Column(Integer)


class SMSearchMessageRule(Base):
    __tablename__ = 'SM_SearchMessageRule'

    code = Column(Unicode(30))
    name = Column(Unicode(200))
    searchwhere = Column(Unicode(2000))
    sms = Column(Integer)
    mail = Column(Integer)
    internalmessage = Column(Integer)
    im = Column(Integer)
    ts = Column(TIMESTAMP)
    updatedBy = Column(Unicode(32))
    sns = Column(Integer)
    gzq = Column(Integer)
    id = Column(Integer, primary_key=True)
    messageobject = Column(Integer)
    messagetype = Column(Integer)
    priority = Column(Integer)
    SearchPlanID = Column(Integer)
    iduser = Column(Integer)
    idsendtimerule = Column(Integer)
    idsmstemplate = Column(Integer)
    updated = Column(DateTime)


class SMSendTimeRule(Base):
    __tablename__ = 'SM_SendTimeRule'

    perxdays = Column(Integer)
    perxweeks = Column(Integer)
    week = Column(Unicode(300))
    perxmonth = Column(Integer)
    day = Column(Integer)
    leaddays = Column(Integer)
    timeformat = Column(Unicode(100))
    sendtimetype = Column(Unicode(50))
    ts = Column(TIMESTAMP)
    updatedBy = Column(Unicode(32))
    id = Column(Integer, primary_key=True)
    begindate = Column(DateTime)
    enddate = Column(DateTime)
    sendtime = Column(DateTime)
    updated = Column(DateTime)


class SMTransferredCode(Base):
    __tablename__ = 'SM_TransferredCode'

    basearchivecode = Column(Unicode(30), nullable=False)
    basearchivename = Column(Unicode(200), nullable=False)
    transferredcode = Column(Unicode(30))
    ts = Column(TIMESTAMP, nullable=False)
    id = Column(Integer, primary_key=True)
    IsSystem = Column(Integer, nullable=False, server_default=text("((1))"))
    basearchiveid = Column(Integer, nullable=False, server_default=text("((0))"))
    idcodingprefixion = Column(Integer, nullable=False, server_default=text("((0))"))


t_SM_Upgrade = Table(
    'SM_Upgrade', metadata,
    Column('ID', Integer, nullable=False),
    Column('Version', Unicode(50), nullable=False),
    Column('ScriptFileName', Unicode(50)),
    Column('ItemType', Unicode(20), nullable=False),
    Column('UpdateClass', Unicode(200)),
    Column('Parameter', Unicode(50)),
    Column('OrderNo', Integer, nullable=False),
    Column('DBType', Integer, nullable=False),
    Column('Location', Unicode(50)),
    Column('LanguageType', Unicode(50)),
    Column('Status', Integer, server_default=text("((0))")),
    Column('Product', Unicode(100)),
    Column('ExecutionTime', DateTime)
)


class SMUsedRule(Base):
    __tablename__ = 'SM_UsedRule'

    prefixion1 = Column(Unicode(30), nullable=False)
    prefixion2 = Column(Unicode(30), nullable=False)
    prefixion3 = Column(Unicode(30), nullable=False)
    separator = Column(Unicode(1), nullable=False)
    codelen = Column(Integer, nullable=False)
    serialnolength = Column(Integer, nullable=False)
    allprefixion = Column(Unicode(30), nullable=False)
    ts = Column(TIMESTAMP, nullable=False)
    startcode = Column(Unicode(40), nullable=False)
    endcode = Column(Unicode(40), nullable=False)
    id = Column(Integer, primary_key=True)
    idvouchertype = Column(Integer)


class SMVoucherMessageRule(Base):
    __tablename__ = 'SM_VoucherMessageRule'

    code = Column(Unicode(36))
    name = Column(Unicode(200))
    template = Column(Unicode(50))
    associatereceiver = Column(Unicode(500))
    searchwhere = Column(Unicode(2000))
    sms = Column(Integer)
    mail = Column(Integer)
    internalmessage = Column(Integer)
    im = Column(Integer)
    ts = Column(TIMESTAMP)
    sns = Column(Integer)
    sendtimeName = Column(Unicode(500))
    GZQ = Column(Integer)
    id = Column(Integer, primary_key=True)
    category = Column(Integer)
    messagetype = Column(Integer)
    priority = Column(Integer)
    SendTime = Column(Integer)
    SearchPlanID = Column(Integer)
    iduser = Column(Integer)
    idsmstemplate = Column(Integer)
    idmessageobject = Column(Integer)
    isVisiable = Column(BIT, server_default=text("((1))"))


class SMVoucherType(Base):
    __tablename__ = 'SM_VoucherType'

    code = Column(Unicode(30), nullable=False)
    name = Column(Unicode(200))
    moduleName = Column(Unicode(20), nullable=False)
    AuditModule = Column(Unicode(20))
    isautofillbreakpoint = Column(Integer)
    iseditable = Column(Integer)
    isneedaudit = Column(Integer)
    prefixion1 = Column(Unicode(20))
    prefixion1length = Column(Integer)
    prefixion1content = Column(Unicode(30))
    iscreatorderbyprefixion1 = Column(Integer)
    prefixion2 = Column(Unicode(20))
    prefixion2content = Column(Unicode(30))
    prefixion2length = Column(Integer)
    iscreatorderbyprefixion2 = Column(Integer)
    prefixion3 = Column(Unicode(20))
    prefixion3content = Column(Unicode(30))
    prefixion3length = Column(Integer)
    iscreatorderbyprefixion3 = Column(Integer)
    separator = Column(Unicode(1))
    serialnolength = Column(Integer)
    startordenalnumber = Column(Numeric(30, 0))
    disabled = Column(Integer, nullable=False)
    issystem = Column(Integer, nullable=False)
    isCodingVisible = Column(Integer, nullable=False, server_default=text("((0))"))
    isAudingVisible = Column(Integer, nullable=False, server_default=text("((0))"))
    vouchertypealias = Column(Unicode(20))
    isautocreate = Column(Integer)
    ts = Column(TIMESTAMP, nullable=False)
    DisplayOrder = Column(Integer)
    DtoName = Column(Unicode(60))
    VoucherName = Column(Unicode(200))
    DataType = Column(Unicode(10), server_default=text("('0')"))
    isMessageCenterVisible = Column(Integer, nullable=False, server_default=text("((1))"))
    isVoucherSearchVisible = Column(Integer, nullable=False)
    prefixion1InterceptType = Column(Integer, nullable=False, server_default=text("((0))"))
    prefixion2InterceptType = Column(Integer, nullable=False, server_default=text("((0))"))
    prefixion3InterceptType = Column(Integer, nullable=False, server_default=text("((0))"))
    IsNeedWorkFlow = Column(Integer)
    CodeManner = Column(Integer)
    IsPrefix1ReadOnly = Column(Integer)
    SysPropFields = Column(Unicode(300))
    isAuditPrint = Column(Integer)
    ExpressionName = Column(Unicode(100))
    IsEnableWFEmail = Column(Integer)
    ID = Column(Integer, primary_key=True)


class SMVoucherTypeToBusinessType(Base):
    __tablename__ = 'SM_VoucherTypeToBusinessType'

    disabled = Column(Integer, nullable=False)
    ts = Column(TIMESTAMP, nullable=False)
    id = Column(Integer, primary_key=True)
    idbusitype = Column(Integer, nullable=False, server_default=text("((0))"))
    idvouchertype = Column(Integer, nullable=False, server_default=text("((0))"))


class SMWarningMessageRule(Base):
    __tablename__ = 'SM_WarningMessageRule'

    code = Column(Unicode(30))
    name = Column(Unicode(200))
    isexport = Column(Integer)
    associatereceiver = Column(Unicode(200))
    searchwhere = Column(Unicode(2000))
    sms = Column(Integer)
    mail = Column(Integer)
    internalmessage = Column(Integer)
    im = Column(Integer)
    ts = Column(TIMESTAMP)
    updatedBy = Column(Unicode(32))
    sns = Column(Integer)
    id = Column(Integer, primary_key=True)
    MessageObject = Column(Integer)
    messagetype = Column(Integer)
    priority = Column(Integer)
    SearchPlanID = Column(Integer)
    iduser = Column(Integer)
    idsendtimerule = Column(Integer)
    idsmstemplate = Column(Integer)
    updated = Column(DateTime)


class STAdjustCostVoucher(Base):
    __tablename__ = 'ST_AdjustCostVoucher'

    code = Column(Unicode(30), index=True)
    memo = Column(Unicode(200))
    sumAmount = Column(Numeric(28, 14))
    maker = Column(Unicode(50))
    auditor = Column(Unicode(50))
    reviser = Column(Unicode(50))
    iscarriedforwardout = Column(Integer)
    iscarriedforwardin = Column(Integer)
    ismodifiedcode = Column(Integer)
    accountingperiod = Column(Integer)
    docid = Column(Unicode(36))
    accountingyear = Column(Integer)
    ts = Column(TIMESTAMP)
    updatedBy = Column(Unicode(32))
    priuserdefnvc1 = Column(Unicode(500))
    priuserdefdecm1 = Column(Numeric(28, 14))
    priuserdefnvc2 = Column(Unicode(500))
    priuserdefdecm2 = Column(Numeric(28, 14))
    priuserdefnvc3 = Column(Unicode(500))
    priuserdefdecm3 = Column(Numeric(28, 14))
    priuserdefnvc4 = Column(Unicode(500))
    priuserdefdecm4 = Column(Numeric(28, 14))
    priuserdefnvc5 = Column(Unicode(500))
    priuserdefdecm5 = Column(Numeric(28, 14))
    priuserdefnvc6 = Column(Unicode(500))
    priuserdefdecm6 = Column(Numeric(28, 14))
    pubuserdefnvc1 = Column(Unicode(500))
    pubuserdefdecm1 = Column(Numeric(28, 14))
    pubuserdefnvc2 = Column(Unicode(500))
    pubuserdefdecm2 = Column(Numeric(28, 14))
    pubuserdefnvc3 = Column(Unicode(500))
    pubuserdefdecm3 = Column(Numeric(28, 14))
    pubuserdefnvc4 = Column(Unicode(500))
    pubuserdefdecm4 = Column(Numeric(28, 14))
    pubuserdefnvc5 = Column(Unicode(500))
    pubuserdefdecm5 = Column(Numeric(28, 14))
    pubuserdefnvc6 = Column(Unicode(500))
    pubuserdefdecm6 = Column(Numeric(28, 14))
    PrintCount = Column(Integer)
    id = Column(Integer, primary_key=True)
    iddepartment = Column(Integer, index=True)
    IdMarketingOrgan = Column(Integer)
    idpartner = Column(Integer, index=True)
    idclerk = Column(Integer, index=True)
    idproject = Column(Integer, index=True)
    idrdstyle = Column(Integer)
    idwarehouse = Column(Integer, index=True)
    adjustType = Column(Integer)
    voucherState = Column(Integer)
    auditorid = Column(Integer)
    makerid = Column(Integer)
    idvouchertype = Column(Integer, index=True)
    voucherdate = Column(DateTime)
    madedate = Column(DateTime)
    auditeddate = Column(DateTime)
    createdtime = Column(DateTime, index=True)
    updated = Column(DateTime)


class STAdjustCostVoucherB(Base):
    __tablename__ = 'ST_AdjustCostVoucher_b'
    __table_args__ = (
        Index('IDX_ST_AdjustCostVoucher_b_id', 'idAdjustCostVoucherDTO', 'id', 'idinventory', 'idwarehouse', 'batch'),
        Index('IDX_ST_AdjustCostVoucher_b_mix1', 'idinventory', 'sourceVoucherID', 'sourceVoucherDetailID', 'fromVoucherDetailID')
    )

    code = Column(Unicode(30))
    sourceVoucherCode = Column(Unicode(50))
    processCode = Column(Unicode(50))
    batch = Column(Unicode(50))
    amount = Column(Numeric(28, 14))
    ts = Column(TIMESTAMP)
    updatedBy = Column(Unicode(32))
    freeItem0 = Column(Unicode(300))
    freeItem1 = Column(Unicode(300))
    freeItem2 = Column(Unicode(300))
    freeItem3 = Column(Unicode(300))
    freeItem4 = Column(Unicode(300))
    freeItem5 = Column(Unicode(300))
    freeItem6 = Column(Unicode(300))
    freeItem7 = Column(Unicode(300))
    freeItem8 = Column(Unicode(300))
    freeItem9 = Column(Unicode(300))
    priuserdefnvc1 = Column(Unicode(500))
    priuserdefdecm1 = Column(Numeric(28, 14))
    priuserdefnvc2 = Column(Unicode(500))
    priuserdefdecm2 = Column(Numeric(28, 14))
    priuserdefnvc3 = Column(Unicode(500))
    priuserdefdecm3 = Column(Numeric(28, 14))
    priuserdefnvc4 = Column(Unicode(500))
    priuserdefdecm4 = Column(Numeric(28, 14))
    pubuserdefnvc1 = Column(Unicode(500))
    pubuserdefdecm1 = Column(Numeric(28, 14))
    pubuserdefnvc2 = Column(Unicode(500))
    pubuserdefdecm2 = Column(Numeric(28, 14))
    pubuserdefnvc3 = Column(Unicode(500))
    pubuserdefdecm3 = Column(Numeric(28, 14))
    pubuserdefnvc4 = Column(Unicode(500))
    InvBarCode = Column(Unicode(128))
    pubuserdefdecm4 = Column(Numeric(28, 14))
    id = Column(Integer, primary_key=True)
    idinventory = Column(Integer, index=True)
    idproduct = Column(Integer, index=True)
    idproject = Column(Integer, index=True)
    idBaseUnit = Column(Integer)
    idSubUnit = Column(Integer)
    idwarehouse = Column(Integer, index=True)
    adjustFlag = Column(Integer)
    idsourcevouchertype = Column(Integer, index=True)
    idAdjustCostVoucherDTO = Column(Integer, index=True)
    fromVoucherID = Column(Integer)
    fromVoucherDetailID = Column(Integer)
    sourceVoucherID = Column(Integer)
    rdvoucherDetailID = Column(Integer, index=True)
    sourceVoucherDetailID = Column(Integer)
    createdtime = Column(DateTime)
    updated = Column(DateTime, index=True)
    idFromVoucherType = Column(Integer, index=True)


class STAgeAnalysisRptSet(Base):
    __tablename__ = 'ST_AgeAnalysisRptSet'

    reportName = Column(Unicode(200))
    days = Column(Integer)
    isArFlag = Column(Integer)
    id = Column(Integer, primary_key=True)
    userId = Column(Integer)


class STAssemDetachVoucher(Base):
    __tablename__ = 'ST_AssemDetachVoucher'
    __table_args__ = (
        Index('IDX_ST_AssemDetachVoucher_createdtime_voucherdate', 'idvouchertype', 'createdtime', 'voucherdate', 'id', 'iddepartment', 'makerid', 'idclerk', 'idproject'),
    )

    code = Column(Unicode(30), index=True)
    expense = Column(Numeric(28, 14))
    memo = Column(Unicode(200))
    level = Column(Unicode(12))
    maker = Column(Unicode(50))
    auditor = Column(Unicode(50))
    reviser = Column(Unicode(50))
    iscarriedforwardout = Column(Integer)
    iscarriedforwardin = Column(Integer)
    ismodifiedcode = Column(Integer)
    docid = Column(Unicode(36))
    ts = Column(TIMESTAMP)
    updatedBy = Column(Unicode(32))
    priuserdefnvc1 = Column(Unicode(500))
    priuserdefdecm1 = Column(Numeric(28, 14))
    priuserdefnvc2 = Column(Unicode(500))
    priuserdefdecm2 = Column(Numeric(28, 14))
    priuserdefnvc3 = Column(Unicode(500))
    priuserdefdecm3 = Column(Numeric(28, 14))
    priuserdefnvc4 = Column(Unicode(500))
    priuserdefdecm4 = Column(Numeric(28, 14))
    priuserdefnvc5 = Column(Unicode(500))
    priuserdefdecm5 = Column(Numeric(28, 14))
    priuserdefnvc6 = Column(Unicode(500))
    priuserdefdecm6 = Column(Numeric(28, 14))
    pubuserdefnvc1 = Column(Unicode(500))
    pubuserdefdecm1 = Column(Numeric(28, 14))
    pubuserdefnvc2 = Column(Unicode(500))
    pubuserdefdecm2 = Column(Numeric(28, 14))
    pubuserdefnvc3 = Column(Unicode(500))
    pubuserdefdecm3 = Column(Numeric(28, 14))
    pubuserdefnvc4 = Column(Unicode(500))
    pubuserdefdecm4 = Column(Numeric(28, 14))
    pubuserdefnvc5 = Column(Unicode(500))
    pubuserdefdecm5 = Column(Numeric(28, 14))
    pubuserdefnvc6 = Column(Unicode(500))
    pubuserdefdecm6 = Column(Numeric(28, 14))
    DiffAmount = Column(Numeric(28, 14))
    DocId2 = Column(Unicode(36))
    DocNo2 = Column(Unicode(36))
    DocClass2 = Column(Unicode(36))
    AccountingYear2 = Column(Integer)
    AccountingPeriod2 = Column(Integer)
    SaleOrderCode = Column(Unicode(30))
    PrintCount = Column(Integer)
    IsManualCost = Column(Integer)
    Changer = Column(Unicode(50))
    id = Column(Integer, primary_key=True)
    idbom = Column(Integer, index=True)
    idbusitype = Column(Integer)
    iddepartment = Column(Integer, index=True)
    idinventory = Column(Integer, index=True)
    idmarketingOrgan = Column(Integer)
    idclerk = Column(Integer, index=True)
    idproject = Column(Integer, index=True)
    iddispatchstyle = Column(Integer)
    idreceivestyle = Column(Integer)
    voucherState = Column(Integer)
    auditorid = Column(Integer)
    makerid = Column(Integer)
    SaleOrderId = Column(Integer)
    idvouchertype = Column(Integer, index=True)
    ChangerId = Column(Integer)
    voucherdate = Column(DateTime, index=True)
    madedate = Column(DateTime)
    auditeddate = Column(DateTime)
    createdtime = Column(DateTime, index=True)
    updated = Column(DateTime)
    ChangeDate = Column(DateTime)


class STAssemDetachVoucherB(Base):
    __tablename__ = 'ST_AssemDetachVoucher_b'
    __table_args__ = (
        Index('IDX_ST_AssemDetachVoucher_b_idwarehouse_idinventory', 'idwarehouse', 'idinventory'),
    )

    code = Column(Unicode(30))
    quotaQuantity = Column(Numeric(28, 14))
    quantity = Column(Numeric(28, 14))
    price = Column(Numeric(28, 14))
    materialAmount = Column(Numeric(28, 14))
    feeAmount = Column(Numeric(28, 14))
    amount = Column(Numeric(28, 14))
    changeRate = Column(Numeric(28, 14))
    quantity2 = Column(Numeric(28, 14))
    quotaLoss = Column(Numeric(28, 14))
    actualLoss = Column(Numeric(28, 14))
    batch = Column(Unicode(50))
    inventoryLocation = Column(Unicode(50))
    quotaProduceQuantity = Column(Numeric(28, 14))
    receiveVoucherCode = Column(Unicode(50))
    baseQuantity = Column(Numeric(28, 14))
    subQuantity = Column(Numeric(28, 14))
    ts = Column(TIMESTAMP)
    updatedBy = Column(Unicode(32))
    freeItem0 = Column(Unicode(300))
    freeItem1 = Column(Unicode(300))
    freeItem2 = Column(Unicode(300))
    freeItem3 = Column(Unicode(300))
    freeItem4 = Column(Unicode(300))
    freeItem5 = Column(Unicode(300))
    freeItem6 = Column(Unicode(300))
    freeItem7 = Column(Unicode(300))
    freeItem8 = Column(Unicode(300))
    freeItem9 = Column(Unicode(300))
    priuserdefnvc1 = Column(Unicode(500))
    priuserdefdecm1 = Column(Numeric(28, 14))
    priuserdefnvc2 = Column(Unicode(500))
    priuserdefdecm2 = Column(Numeric(28, 14))
    priuserdefnvc3 = Column(Unicode(500))
    priuserdefdecm3 = Column(Numeric(28, 14))
    priuserdefnvc4 = Column(Unicode(500))
    priuserdefdecm4 = Column(Numeric(28, 14))
    pubuserdefnvc1 = Column(Unicode(500))
    pubuserdefdecm1 = Column(Numeric(28, 14))
    pubuserdefnvc2 = Column(Unicode(500))
    pubuserdefdecm2 = Column(Numeric(28, 14))
    pubuserdefnvc3 = Column(Unicode(500))
    pubuserdefdecm3 = Column(Numeric(28, 14))
    pubuserdefnvc4 = Column(Unicode(500))
    InvBarCode = Column(Unicode(128))
    pubuserdefdecm4 = Column(Numeric(28, 14))
    WasteRate = Column(Numeric(28, 14))
    compositionQuantity = Column(Unicode(50))
    SaleOrderCode = Column(Unicode(30))
    ID = Column(Integer, primary_key=True)
    idinventory = Column(Integer, index=True)
    idproject = Column(Integer, index=True)
    idbaseunit = Column(Integer)
    idsubunit = Column(Integer)
    idunit = Column(Integer)
    idunit2 = Column(Integer)
    idwarehouse = Column(Integer, index=True)
    type = Column(Integer)
    SaleOrderId = Column(Integer)
    SaleOrderDetailId = Column(Integer)
    idAssemDetachVoucherDTO = Column(Integer, index=True)
    receiveVoucherId = Column(Integer)
    receiveVoucherDetailId = Column(Integer)
    expiryDate = Column(DateTime)
    createdtime = Column(DateTime)
    updated = Column(DateTime, index=True)
    ProductionDate = Column(DateTime)


class STAssistantDataBook(Base):
    __tablename__ = 'ST_AssistantDataBook'
    __table_args__ = (
        Index('IDX_ST_AssistantDataBook_mix1', 'inVoucherID', 'inVoucherDetailID', 'idinventory', 'accountDate', 'orderNo', 'idwarehouse', 'batch'),
    )

    accountYear = Column(Integer)
    accountPeriod = Column(Integer)
    voucherCode = Column(Unicode(30))
    voucherCodeFlowUnite = Column(Unicode(50))
    batch = Column(Unicode(50))
    inQuantity = Column(Numeric(28, 14))
    inPrice = Column(Numeric(28, 14))
    inAmount = Column(Numeric(28, 14))
    outQuantity = Column(Numeric(28, 14))
    outAmount = Column(Numeric(28, 14))
    asOutQuantityAmount = Column(Numeric(28, 14))
    expenseAmount = Column(Numeric(28, 14))
    adjustAmount = Column(Numeric(28, 14))
    inVoucherAmount = Column(Numeric(28, 14))
    orderNo = Column(Integer)
    estimatePrice = Column(Numeric(28, 14))
    estimateAmount = Column(Numeric(28, 14))
    settleAccountYear = Column(Integer)
    settleAccountPeriod = Column(Integer)
    iscarriedforwardout = Column(Integer)
    iscarriedforwardin = Column(Integer)
    inVoucherPrice = Column(Numeric(28, 14))
    outExpenseAmount = Column(Numeric(28, 14))
    outAdjustAmount = Column(Numeric(28, 14))
    outVoucherAmount = Column(Numeric(28, 14))
    ts = Column(TIMESTAMP)
    updatedBy = Column(Unicode(32))
    freeItem0 = Column(Unicode(300))
    freeItem1 = Column(Unicode(300))
    freeItem2 = Column(Unicode(300))
    freeItem3 = Column(Unicode(300))
    freeItem4 = Column(Unicode(300))
    freeItem5 = Column(Unicode(300))
    freeItem6 = Column(Unicode(300))
    freeItem7 = Column(Unicode(300))
    freeItem8 = Column(Unicode(300))
    freeItem9 = Column(Unicode(300))
    AccountYearPeriod = Column(Unicode(6))
    id = Column(Integer, primary_key=True)
    idbusitype = Column(Integer)
    idbusitypeflowunite = Column(Integer, index=True)
    idinventory = Column(Integer, index=True)
    idwarehouse = Column(Integer, index=True)
    idvouchertype = Column(Integer, index=True)
    idvouchertypeflowunite = Column(Integer, index=True)
    purchaseSettleVoucherID = Column(Integer)
    purchaseSettleDetailID = Column(Integer, index=True)
    inVoucherID = Column(Integer)
    inVoucherDetailID = Column(Integer)
    inSubID = Column(Integer, index=True)
    voucherDate = Column(DateTime)
    auditedDate = Column(DateTime)
    accountDate = Column(DateTime, index=True)
    expiryDate = Column(DateTime)
    settleDate = Column(DateTime)
    createdtime = Column(DateTime)
    updated = Column(DateTime)
    productionDate = Column(DateTime)


class STAssistantDataOutOtherAmount(Base):
    __tablename__ = 'ST_AssistantDataOutOtherAmount'
    __table_args__ = (
        Index('IDX_ST_AssistantDataOutOtherAmount_id', 'assistantDataRelationID', 'assistantDataShareOtherAmountID', 'id'),
    )

    iscarriedforwardin = Column(Integer)
    iscarriedforwardout = Column(Integer)
    amount = Column(Numeric(28, 14))
    ts = Column(TIMESTAMP)
    updatedBy = Column(Unicode(32))
    id = Column(Integer, primary_key=True)
    assistantDataRelationID = Column(Integer)
    assistantDataShareOtherAmountID = Column(Integer)
    updated = Column(DateTime, index=True)


class STAssistantDataRelation(Base):
    __tablename__ = 'ST_AssistantDataRelation'
    __table_args__ = (
        Index('IDX_ST_AssistantDataRelation_id', 'assistantDataBookID', 'id', 'voucherID', 'voucherDetailID', 'outAmount', 'outPrice', 'quantity'),
    )

    quantity = Column(Numeric(28, 14))
    amount = Column(Numeric(28, 14))
    price = Column(Numeric(28, 14))
    isManual = Column(Integer)
    iscarriedforwardout = Column(Integer)
    iscarriedforwardin = Column(Integer)
    accountYear = Column(Integer)
    accountPeriod = Column(Integer)
    outAmount = Column(Numeric(28, 14))
    outPrice = Column(Numeric(28, 14))
    ts = Column(TIMESTAMP)
    updatedBy = Column(Unicode(32))
    adjustAmount = Column(Numeric(28, 14))
    isInStock = Column(Integer, server_default=text("(0)"))
    IsRedVoucher = Column(Integer, server_default=text("(0)"))
    outVoucherAmount = Column(Numeric(28, 14))
    AccountYearPeriod = Column(Unicode(6))
    id = Column(Integer, primary_key=True)
    idvouchertype = Column(Integer, index=True)
    assistantDataBookID = Column(Integer)
    voucherID = Column(Integer)
    voucherDetailID = Column(Integer)
    subsidiaryBookID = Column(Integer, index=True)
    accountDate = Column(DateTime)
    createdtime = Column(DateTime)
    updated = Column(DateTime, index=True)
    subsidiaryAmount = Column(Numeric(28, 14))


class STAssistantDataShareOtherAmount(Base):
    __tablename__ = 'ST_AssistantDataShareOtherAmount'
    __table_args__ = (
        Index('IDX_ST_AssistantDataShareOtherAmount_id', 'assistantDataBookID', 'id'),
    )

    code = Column(Unicode(30))
    name = Column(Unicode(200))
    iscarriedforwardout = Column(Integer)
    iscarriedforwardin = Column(Integer)
    amount = Column(Numeric(28, 14))
    accountYear = Column(Integer)
    accountPeriod = Column(Integer)
    outAmount = Column(Numeric(28, 14))
    sequencenumber = Column(Integer)
    ts = Column(TIMESTAMP)
    updatedBy = Column(Unicode(32))
    id = Column(Integer, primary_key=True)
    idvouchertype = Column(Integer, index=True)
    assistantDataBookID = Column(Integer)
    voucherID = Column(Integer)
    voucherDetailID = Column(Integer, index=True)
    voucherDate = Column(DateTime)
    createdtime = Column(DateTime)
    updated = Column(DateTime, index=True)


class STCheckVoucher(Base):
    __tablename__ = 'ST_CheckVoucher'
    __table_args__ = (
        Index('IDX_ST_CheckVoucher_createdtime_voucherdate', 'createdtime', 'voucherdate', 'id', 'iddepartment', 'makerid', 'idclerk', 'idwarehouse', 'idproject'),
    )

    code = Column(Unicode(30), index=True)
    memo = Column(Unicode(200))
    isLocked = Column(Integer)
    maker = Column(Unicode(50))
    auditor = Column(Unicode(50))
    reviser = Column(Unicode(50))
    iscarriedforwardout = Column(Integer)
    iscarriedforwardin = Column(Integer)
    ismodifiedcode = Column(Integer)
    docid = Column(Unicode(36))
    ts = Column(TIMESTAMP)
    updatedBy = Column(Unicode(32))
    priuserdefnvc1 = Column(Unicode(500))
    priuserdefdecm1 = Column(Numeric(28, 14))
    priuserdefnvc2 = Column(Unicode(500))
    priuserdefdecm2 = Column(Numeric(28, 14))
    priuserdefnvc3 = Column(Unicode(500))
    priuserdefdecm3 = Column(Numeric(28, 14))
    priuserdefnvc4 = Column(Unicode(500))
    priuserdefdecm4 = Column(Numeric(28, 14))
    priuserdefnvc5 = Column(Unicode(500))
    priuserdefdecm5 = Column(Numeric(28, 14))
    priuserdefnvc6 = Column(Unicode(500))
    priuserdefdecm6 = Column(Numeric(28, 14))
    pubuserdefnvc1 = Column(Unicode(500))
    pubuserdefdecm1 = Column(Numeric(28, 14))
    pubuserdefnvc2 = Column(Unicode(500))
    pubuserdefdecm2 = Column(Numeric(28, 14))
    pubuserdefnvc3 = Column(Unicode(500))
    pubuserdefdecm3 = Column(Numeric(28, 14))
    pubuserdefnvc4 = Column(Unicode(500))
    pubuserdefdecm4 = Column(Numeric(28, 14))
    pubuserdefnvc5 = Column(Unicode(500))
    pubuserdefdecm5 = Column(Numeric(28, 14))
    pubuserdefnvc6 = Column(Unicode(500))
    pubuserdefdecm6 = Column(Numeric(28, 14))
    DocId2 = Column(Unicode(36))
    DocNo2 = Column(Unicode(36))
    DocClass2 = Column(Unicode(36))
    AccountingYear2 = Column(Integer)
    AccountingPeriod2 = Column(Integer)
    TotalBalanceAmount = Column(Numeric(28, 14))
    PrintCount = Column(Integer)
    IsManualCost = Column(Integer)
    id = Column(Integer, primary_key=True)
    iddepartment = Column(Integer, index=True)
    idinvlocation = Column(Integer, index=True)
    idmarketingOrgan = Column(Integer)
    idclerk = Column(Integer, index=True)
    idproject = Column(Integer, index=True)
    iddispatchstyle = Column(Integer)
    idreceivestyle = Column(Integer)
    idwarehouse = Column(Integer, index=True)
    voucherState = Column(Integer)
    auditorid = Column(Integer)
    makerid = Column(Integer)
    idvouchertype = Column(Integer, index=True)
    voucherdate = Column(DateTime, index=True)
    madedate = Column(DateTime)
    auditeddate = Column(DateTime)
    createdtime = Column(DateTime, index=True)
    updated = Column(DateTime)
    VoucherDateInStock = Column(DateTime)


t_ST_CheckVoucherSelectInventoryClassSetting = Table(
    'ST_CheckVoucherSelectInventoryClassSetting', metadata,
    Column('idCheckVoucher', Integer),
    Column('idInventoryClass', Integer)
)


class STCheckVoucherB(Base):
    __tablename__ = 'ST_CheckVoucher_b'

    code = Column(Unicode(30))
    quantityInStock = Column(Numeric(28, 14))
    quantity = Column(Numeric(28, 14))
    balanceQuantity = Column(Numeric(28, 14))
    price = Column(Numeric(28, 14))
    amountInStock = Column(Numeric(28, 14))
    amount = Column(Numeric(28, 14))
    balanceAmount = Column(Numeric(28, 14))
    quantityInStock2 = Column(Numeric(28, 14))
    quantity2 = Column(Numeric(28, 14))
    balanceQuantity2 = Column(Numeric(28, 14))
    changeRate = Column(Numeric(28, 14))
    batch = Column(Unicode(50))
    receiveVoucherCode = Column(Unicode(50))
    baseQuantityInStock = Column(Numeric(28, 14))
    baseQuantity = Column(Numeric(28, 14))
    baseBalanceQuantity = Column(Numeric(28, 14))
    subQuantityInStock = Column(Numeric(28, 14))
    subQuantity = Column(Numeric(28, 14))
    subBalanceQuantity = Column(Numeric(28, 14))
    ts = Column(TIMESTAMP)
    updatedBy = Column(Unicode(32))
    freeItem0 = Column(Unicode(300))
    freeItem1 = Column(Unicode(300))
    freeItem2 = Column(Unicode(300))
    freeItem3 = Column(Unicode(300))
    freeItem4 = Column(Unicode(300))
    freeItem5 = Column(Unicode(300))
    freeItem6 = Column(Unicode(300))
    freeItem7 = Column(Unicode(300))
    freeItem8 = Column(Unicode(300))
    freeItem9 = Column(Unicode(300))
    priuserdefnvc1 = Column(Unicode(500))
    priuserdefdecm1 = Column(Numeric(28, 14))
    priuserdefnvc2 = Column(Unicode(500))
    priuserdefdecm2 = Column(Numeric(28, 14))
    priuserdefnvc3 = Column(Unicode(500))
    priuserdefdecm3 = Column(Numeric(28, 14))
    priuserdefnvc4 = Column(Unicode(500))
    priuserdefdecm4 = Column(Numeric(28, 14))
    pubuserdefnvc1 = Column(Unicode(500))
    pubuserdefdecm1 = Column(Numeric(28, 14))
    pubuserdefnvc2 = Column(Unicode(500))
    pubuserdefdecm2 = Column(Numeric(28, 14))
    pubuserdefnvc3 = Column(Unicode(500))
    pubuserdefdecm3 = Column(Numeric(28, 14))
    pubuserdefnvc4 = Column(Unicode(500))
    InvBarCode = Column(Unicode(128))
    pubuserdefdecm4 = Column(Numeric(28, 14))
    compositionQuantityInStock = Column(Unicode(50))
    compositionQuantity = Column(Unicode(50))
    id = Column(Integer, primary_key=True)
    idinventory = Column(Integer, index=True)
    idinvlocation = Column(Integer, index=True)
    idproject = Column(Integer, index=True)
    idbaseunit = Column(Integer)
    idsubunit = Column(Integer)
    idunit = Column(Integer)
    idunit2 = Column(Integer)
    idCheckVoucherDTO = Column(Integer, index=True)
    receiveVoucherId = Column(Integer)
    receiveVoucherDetailId = Column(Integer)
    expiryDate = Column(DateTime)
    createdtime = Column(DateTime)
    updated = Column(DateTime, index=True)
    ProductionDate = Column(DateTime)


class STCurrentStock(Base):
    __tablename__ = 'ST_CurrentStock'
    __table_args__ = (
        Index('IDX_ST_CurrentStock_idinventory_idwarehouse_batch', 'idinventory', 'idwarehouse', 'batch'),
    )

    batch = Column(Unicode(50))
    baseQuantity = Column(Numeric(28, 14))
    subQuantity = Column(Numeric(28, 14))
    canUseBaseQuantity = Column(Numeric(28, 14))
    canUseSubQuantity = Column(Numeric(28, 14))
    onWayBaseQuantity = Column(Numeric(28, 14))
    onWaySubQuantity = Column(Numeric(28, 14))
    forDispatchBaseQuantity = Column(Numeric(28, 14))
    forDispatchSubQuantity = Column(Numeric(28, 14))
    purchaseOrderOnWayBaseQuantity = Column(Numeric(28, 14))
    purchaseOrderOnWaySubQuantity = Column(Numeric(28, 14))
    purchaseArrivalBaseQuantity = Column(Numeric(28, 14))
    purchaseArrivalSubQuantity = Column(Numeric(28, 14))
    purchaseForReceiveBaseQuantity = Column(Numeric(28, 14))
    purchaseForReceiveSubQuantity = Column(Numeric(28, 14))
    onProducingBaseQuantity = Column(Numeric(28, 14))
    onProducingSubQuantity = Column(Numeric(28, 14))
    productForReceiveBaseQuantity = Column(Numeric(28, 14))
    productForReceiveSubQuantity = Column(Numeric(28, 14))
    transOnWayBaseQuantity = Column(Numeric(28, 14))
    transOnWaySubQuantity = Column(Numeric(28, 14))
    transForDispatchBaseQuantity = Column(Numeric(28, 14))
    transForDispatchSubQuantity = Column(Numeric(28, 14))
    otherOnWayBaseQuantity = Column(Numeric(28, 14))
    otherOnWaySubQuantity = Column(Numeric(28, 14))
    otherForDispatchBaseQuantity = Column(Numeric(28, 14))
    otherForDispatchSubQuantity = Column(Numeric(28, 14))
    forSaleOrderBaseQuantity = Column(Numeric(28, 14))
    forSaleOrderSubQuantity = Column(Numeric(28, 14))
    saleDeliveryBaseQuantity = Column(Numeric(28, 14))
    saleDeliverySubQuantity = Column(Numeric(28, 14))
    forSaleDispatchBaseQuantity = Column(Numeric(28, 14))
    forSaleDispatchSubQuantity = Column(Numeric(28, 14))
    materialForSendBaseQuantity = Column(Numeric(28, 14))
    materialForSendSubQuantity = Column(Numeric(28, 14))
    receiveVoucherCode = Column(Unicode(50))
    voucherQuantity = Column(Numeric(28, 14))
    voucherQuantity2 = Column(Numeric(28, 14))
    preBaseQuantity = Column(Numeric(28, 14))
    preSubQuantity = Column(Numeric(28, 14))
    lowQuantity = Column(Numeric(28, 14))
    topQuantity = Column(Numeric(28, 14))
    changeRate = Column(Numeric(28, 14))
    isCarriedForwardOut = Column(Integer)
    isCarriedForwardIn = Column(Integer)
    ts = Column(TIMESTAMP)
    updatedBy = Column(Unicode(32))
    freeItem0 = Column(Unicode(300))
    freeItem1 = Column(Unicode(300))
    freeItem2 = Column(Unicode(300))
    freeItem3 = Column(Unicode(300))
    freeItem4 = Column(Unicode(300))
    freeItem5 = Column(Unicode(300))
    freeItem6 = Column(Unicode(300))
    freeItem7 = Column(Unicode(300))
    freeItem8 = Column(Unicode(300))
    freeItem9 = Column(Unicode(300))
    ProduceForDispatchBaseQuantity = Column(Numeric(28, 14))
    ProduceForDispatchSubQuantity = Column(Numeric(28, 14))
    stockRequestBaseQuantity = Column(Numeric(28, 14))
    stockRequestSubQuantity = Column(Numeric(28, 14))
    id = Column(Integer, primary_key=True)
    idinventory = Column(Integer, index=True)
    IdMarketingOrgan = Column(Integer)
    idbaseunit = Column(Integer)
    idsubunit = Column(Integer)
    idvoucherunit = Column(Integer)
    idvoucherunit2 = Column(Integer)
    idwarehouse = Column(Integer, index=True)
    idBatchDispatchDTO = Column(Integer)
    receiveVoucherId = Column(Integer)
    receiveVoucherDetailId = Column(Integer)
    expiryDate = Column(DateTime)
    createdtime = Column(DateTime)
    updated = Column(DateTime, index=True)
    productionDate = Column(DateTime)


class STLocationAccount(Base):
    __tablename__ = 'ST_LocationAccount'

    baseQuantity = Column(Numeric(28, 14))
    subQuantity = Column(Numeric(28, 14))
    batch = Column(Unicode(50))
    voucherQuantity = Column(Numeric(28, 14))
    voucherQuantity2 = Column(Numeric(28, 14))
    isCarriedForwardOut = Column(Integer)
    isCarriedForwardIn = Column(Integer)
    ts = Column(TIMESTAMP)
    updatedBy = Column(Unicode(32))
    freeItem0 = Column(Unicode(300))
    freeItem1 = Column(Unicode(300))
    freeItem2 = Column(Unicode(300))
    freeItem3 = Column(Unicode(300))
    freeItem4 = Column(Unicode(300))
    freeItem5 = Column(Unicode(300))
    freeItem6 = Column(Unicode(300))
    freeItem7 = Column(Unicode(300))
    freeItem8 = Column(Unicode(300))
    freeItem9 = Column(Unicode(300))
    id = Column(Integer, primary_key=True)
    idinventory = Column(Integer, index=True)
    idinvlocation = Column(Integer, index=True)
    idbaseunit = Column(Integer)
    idsubunit = Column(Integer)
    idwarehouse = Column(Integer, index=True)
    expiryDate = Column(DateTime)
    createdtime = Column(DateTime)
    updated = Column(DateTime, index=True)
    productionDate = Column(DateTime)


class STLocationDetail(Base):
    __tablename__ = 'ST_LocationDetail'

    quantity = Column(Numeric(28, 14))
    quantity2 = Column(Numeric(28, 14))
    baseQuantity = Column(Numeric(28, 14))
    subQuantity = Column(Numeric(28, 14))
    changeRate = Column(Numeric(28, 14))
    batch = Column(Unicode(50))
    memo = Column(Unicode(200))
    ts = Column(TIMESTAMP)
    id = Column(Integer, primary_key=True)
    idinvlocation = Column(Integer, index=True)
    idbaseunit = Column(Integer)
    idsubunit = Column(Integer)
    idunit = Column(Integer)
    idunit2 = Column(Integer)
    idAssemDetachDetailDTO = Column(Integer, index=True)
    idRDRecordDetailDTO = Column(Integer, index=True)
    idShapeDetailDTO = Column(Integer, index=True)
    expiryDate = Column(DateTime)
    productionDate = Column(DateTime)


class STMultiLocationDetail(Base):
    __tablename__ = 'ST_MultiLocationDetail'

    quantity = Column(Numeric(28, 14))
    quantity2 = Column(Numeric(28, 14))
    baseQuantity = Column(Numeric(28, 14))
    subQuantity = Column(Numeric(28, 14))
    batch = Column(Unicode(50))
    memo = Column(Unicode(200))
    changeRate = Column(Numeric(28, 14))
    ts = Column(TIMESTAMP)
    updatedBy = Column(Unicode(32))
    id = Column(Integer, primary_key=True)
    idinvlocation = Column(Integer, index=True)
    idbaseunit = Column(Integer)
    idsubunit = Column(Integer)
    idunit = Column(Integer)
    idunit2 = Column(Integer)
    idPositionInitDetailDTO = Column(Integer, index=True)
    expiryDate = Column(DateTime)
    createdtime = Column(DateTime)
    updated = Column(DateTime, index=True)
    productionDate = Column(DateTime)


class STPositionAdjustVoucher(Base):
    __tablename__ = 'ST_PositionAdjustVoucher'
    __table_args__ = (
        Index('IDX_ST_PositionAdjustVoucher_createdtime_voucherdate', 'idvouchertype', 'createdtime', 'voucherdate', 'id', 'iddepartment', 'makerid', 'idclerk'),
    )

    code = Column(Unicode(30), index=True)
    memo = Column(Unicode(200))
    maker = Column(Unicode(50))
    auditor = Column(Unicode(50))
    reviser = Column(Unicode(50))
    iscarriedforwardout = Column(Integer)
    iscarriedforwardin = Column(Integer)
    ismodifiedcode = Column(Integer)
    docno = Column(Unicode(36))
    docclass = Column(Unicode(36))
    docid = Column(Unicode(36))
    ts = Column(TIMESTAMP)
    updatedBy = Column(Unicode(32))
    priuserdefnvc1 = Column(Unicode(500))
    priuserdefdecm1 = Column(Numeric(28, 14))
    priuserdefnvc2 = Column(Unicode(500))
    priuserdefdecm2 = Column(Numeric(28, 14))
    priuserdefnvc3 = Column(Unicode(500))
    priuserdefdecm3 = Column(Numeric(28, 14))
    priuserdefnvc4 = Column(Unicode(500))
    priuserdefdecm4 = Column(Numeric(28, 14))
    priuserdefnvc5 = Column(Unicode(500))
    priuserdefdecm5 = Column(Numeric(28, 14))
    priuserdefnvc6 = Column(Unicode(500))
    priuserdefdecm6 = Column(Numeric(28, 14))
    pubuserdefnvc1 = Column(Unicode(500))
    pubuserdefdecm1 = Column(Numeric(28, 14))
    pubuserdefnvc2 = Column(Unicode(500))
    pubuserdefdecm2 = Column(Numeric(28, 14))
    pubuserdefnvc3 = Column(Unicode(500))
    pubuserdefdecm3 = Column(Numeric(28, 14))
    pubuserdefnvc4 = Column(Unicode(500))
    pubuserdefdecm4 = Column(Numeric(28, 14))
    pubuserdefnvc5 = Column(Unicode(500))
    pubuserdefdecm5 = Column(Numeric(28, 14))
    pubuserdefnvc6 = Column(Unicode(500))
    pubuserdefdecm6 = Column(Numeric(28, 14))
    PrintCount = Column(Integer)
    id = Column(Integer, primary_key=True)
    iddepartment = Column(Integer, index=True)
    idmarketingOrgan = Column(Integer)
    idclerk = Column(Integer, index=True)
    idwarehouse = Column(Integer, index=True)
    voucherState = Column(Integer)
    auditorid = Column(Integer)
    makerid = Column(Integer)
    idvouchertype = Column(Integer, index=True)
    voucherdate = Column(DateTime, index=True)
    madedate = Column(DateTime)
    auditeddate = Column(DateTime)
    createdtime = Column(DateTime, index=True)
    updated = Column(DateTime)


class STPositionAdjustVoucherB(Base):
    __tablename__ = 'ST_PositionAdjustVoucher_b'

    code = Column(Unicode(30))
    quantity = Column(Numeric(28, 14))
    quantity2 = Column(Numeric(28, 14))
    baseQuantity = Column(Numeric(28, 14))
    subQuantity = Column(Numeric(28, 14))
    changeRate = Column(Numeric(28, 14))
    batch = Column(Unicode(50))
    ts = Column(TIMESTAMP)
    updatedBy = Column(Unicode(32))
    freeItem0 = Column(Unicode(300))
    freeItem1 = Column(Unicode(300))
    freeItem2 = Column(Unicode(300))
    freeItem3 = Column(Unicode(300))
    freeItem4 = Column(Unicode(300))
    freeItem5 = Column(Unicode(300))
    freeItem6 = Column(Unicode(300))
    freeItem7 = Column(Unicode(300))
    freeItem8 = Column(Unicode(300))
    freeItem9 = Column(Unicode(300))
    priuserdefnvc1 = Column(Unicode(500))
    priuserdefdecm1 = Column(Numeric(28, 14))
    priuserdefnvc2 = Column(Unicode(500))
    priuserdefdecm2 = Column(Numeric(28, 14))
    priuserdefnvc3 = Column(Unicode(500))
    priuserdefdecm3 = Column(Numeric(28, 14))
    priuserdefnvc4 = Column(Unicode(500))
    priuserdefdecm4 = Column(Numeric(28, 14))
    pubuserdefnvc1 = Column(Unicode(500))
    pubuserdefdecm1 = Column(Numeric(28, 14))
    pubuserdefnvc2 = Column(Unicode(500))
    pubuserdefdecm2 = Column(Numeric(28, 14))
    pubuserdefnvc3 = Column(Unicode(500))
    pubuserdefdecm3 = Column(Numeric(28, 14))
    pubuserdefnvc4 = Column(Unicode(500))
    InvBarCode = Column(Unicode(128))
    pubuserdefdecm4 = Column(Numeric(28, 14))
    compositionQuantity = Column(Unicode(50))
    id = Column(Integer, primary_key=True)
    idinventory = Column(Integer, index=True)
    idadjustfromlocation = Column(Integer, index=True)
    idadjusttolocation = Column(Integer, index=True)
    idbaseunit = Column(Integer)
    idsubunit = Column(Integer)
    idunit = Column(Integer)
    idunit2 = Column(Integer)
    idPositionAdjustVoucherDTO = Column(Integer, index=True)
    expiryDate = Column(DateTime)
    createdtime = Column(DateTime)
    updated = Column(DateTime, index=True)
    ProductionDate = Column(DateTime)


class STPositionInit(Base):
    __tablename__ = 'ST_PositionInit'

    memo = Column(Unicode(200))
    maker = Column(Unicode(50))
    auditor = Column(Unicode(50))
    reviser = Column(Unicode(50))
    iscarriedforwardout = Column(Integer)
    iscarriedforwardin = Column(Integer)
    ismodifiedcode = Column(Integer)
    ts = Column(TIMESTAMP)
    id = Column(Integer, primary_key=True)
    idposition = Column(Integer, index=True)
    idwarehouse = Column(Integer, index=True)
    auditorid = Column(Integer)
    makerid = Column(Integer)
    voucherdate = Column(DateTime, index=True)
    madedate = Column(DateTime)
    auditeddate = Column(DateTime)


class STPositionInitDetail(Base):
    __tablename__ = 'ST_PositionInitDetail'

    code = Column(Unicode(30))
    batch = Column(Unicode(50))
    subQuantity = Column(Numeric(28, 14))
    baseQuantity = Column(Numeric(28, 14))
    quantity = Column(Numeric(28, 14))
    quantity2 = Column(Numeric(28, 14))
    inventoryLocation = Column(Unicode(50))
    changeRate = Column(Numeric(28, 14))
    ts = Column(TIMESTAMP)
    freeItem0 = Column(Unicode(300))
    freeItem1 = Column(Unicode(300))
    freeItem2 = Column(Unicode(300))
    freeItem3 = Column(Unicode(300))
    freeItem4 = Column(Unicode(300))
    freeItem5 = Column(Unicode(300))
    freeItem6 = Column(Unicode(300))
    freeItem7 = Column(Unicode(300))
    freeItem8 = Column(Unicode(300))
    freeItem9 = Column(Unicode(300))
    iscarriedforwardout = Column(Integer)
    iscarriedforwardin = Column(Integer)
    id = Column(Integer, primary_key=True)
    idinventory = Column(Integer, index=True)
    idbaseunit = Column(Integer)
    idsubunit = Column(Integer)
    idunit = Column(Integer)
    idunit2 = Column(Integer)
    idwarehouse = Column(Integer, index=True)
    voucherState = Column(Integer)
    idPositionInitDTO = Column(Integer, index=True)
    recieveVoucherID = Column(Integer)
    addendumDate = Column(DateTime)
    expiryDate = Column(DateTime)
    createdtime = Column(DateTime)
    voucherDate = Column(DateTime)
    ProductionDate = Column(DateTime)


class STProductionCostDetail(Base):
    __tablename__ = 'ST_ProductionCostDetail'

    code = Column(Unicode(40))
    name = Column(Unicode(50))
    RefCost = Column(Numeric(28, 14))
    RefTotalCost = Column(Numeric(28, 14))
    BaseQuantity = Column(Numeric(28, 14))
    TotalAmount = Column(Numeric(28, 14))
    Batch = Column(Unicode(200))
    id = Column(Integer, primary_key=True)
    idinventory = Column(Integer, index=True)
    unit = Column(Integer)
    idwarehouse = Column(Integer)


class STPurchaseSettleVoucher(Base):
    __tablename__ = 'ST_PurchaseSettleVoucher'

    code = Column(Unicode(30), index=True)
    memo = Column(Unicode(200))
    sumSettleAmount = Column(Numeric(28, 14))
    createType = Column(Integer)
    maker = Column(Unicode(50))
    auditor = Column(Unicode(50))
    reviser = Column(Unicode(50))
    iscarriedforwardout = Column(Integer)
    iscarriedforwardin = Column(Integer)
    ismodifiedcode = Column(Integer)
    docno = Column(Unicode(36))
    docclass = Column(Unicode(36))
    docid = Column(Unicode(36))
    ts = Column(TIMESTAMP)
    updatedBy = Column(Unicode(32))
    PrintCount = Column(Integer)
    id = Column(Integer, primary_key=True)
    idbusitype = Column(Integer)
    iddepartment = Column(Integer, index=True)
    IdMarketingOrgan = Column(Integer)
    idpartner = Column(Integer, index=True)
    idclerk = Column(Integer, index=True)
    idproject = Column(Integer, index=True)
    voucherState = Column(Integer)
    auditorid = Column(Integer)
    makerid = Column(Integer)
    idvouchertype = Column(Integer, index=True)
    voucherdate = Column(DateTime, index=True)
    madedate = Column(DateTime)
    auditeddate = Column(DateTime)
    createdtime = Column(DateTime, index=True)
    updated = Column(DateTime)


class STPurchaseSettleVoucherB(Base):
    __tablename__ = 'ST_PurchaseSettleVoucher_b'

    code = Column(Unicode(30))
    settleQuantity = Column(Numeric(28, 14))
    settlePrice = Column(Numeric(28, 14))
    settleAmount = Column(Numeric(28, 14))
    estimatePrice = Column(Numeric(28, 14))
    estimateAmount = Column(Numeric(28, 14))
    accountVoucherCode = Column(Unicode(50))
    rdRecordCode = Column(Unicode(50))
    isHaveVoucher = Column(Integer)
    ts = Column(TIMESTAMP)
    updatedBy = Column(Unicode(32))
    freeItem0 = Column(Unicode(300))
    freeItem1 = Column(Unicode(300))
    freeItem2 = Column(Unicode(300))
    freeItem3 = Column(Unicode(300))
    freeItem4 = Column(Unicode(300))
    freeItem5 = Column(Unicode(300))
    freeItem6 = Column(Unicode(300))
    freeItem7 = Column(Unicode(300))
    freeItem8 = Column(Unicode(300))
    freeItem9 = Column(Unicode(300))
    ShrinkageSettleQuantity = Column(Numeric(28, 14))
    RdSettleQuantity = Column(Numeric(28, 14))
    id = Column(Integer, primary_key=True)
    idinventory = Column(Integer, index=True)
    idproject = Column(Integer, index=True)
    idunit = Column(Integer)
    accountVoucherID = Column(Integer)
    accountVoucherDetailID = Column(Integer)
    idaccountvouchertype = Column(Integer, index=True)
    idPurchaseSettleVoucherDTO = Column(Integer, index=True)
    idrdrecorddetail = Column(Integer, index=True)
    createdtime = Column(DateTime)
    updated = Column(DateTime, index=True)


class STRDRecord(Base):
    __tablename__ = 'ST_RDRecord'
    __table_args__ = (
        Index('IDX_ST_RDRecord_idvouchertype_voucherdate', 'idvouchertype', 'voucherdate'),
        Index('IDX_ST_RDRecord_ids', 'IdMarketingOrgan', 'voucherState', 'idvouchertype', 'voucherdate', 'idsettleCustomer', 'id'),
        Index('IDX_ST_RDRecord_mix1', 'idvouchertype', 'voucherdate', 'createdtime', 'id', 'makerid', 'idclerk', 'iddepartment', 'idpartner', 'idwarehouse', 'idsettleCustomer', 'IdStore')
    )

    code = Column(Unicode(30), index=True)
    dispatchAddress = Column(Unicode(200))
    contact = Column(Unicode(50))
    contactPhone = Column(Unicode(100))
    sourceVoucherCode = Column(Unicode(50))
    saleOrderCode = Column(Unicode(30))
    purchaseArrivalCode = Column(Unicode(50))
    productReceiveCode = Column(Unicode(50))
    saleDeliveryCode = Column(Unicode(50))
    printTime = Column(Integer)
    amount = Column(Numeric(28, 14))
    rdDirectionFlag = Column(Integer)
    isCostAccount = Column(Integer)
    isMergedFlow = Column(Integer)
    isAutoGenerate = Column(Integer)
    memo = Column(Unicode(200))
    isNoModify = Column(Unicode(400))
    maker = Column(Unicode(50))
    auditor = Column(Unicode(50))
    reviser = Column(Unicode(50))
    iscarriedforwardout = Column(Integer)
    iscarriedforwardin = Column(Integer)
    ismodifiedcode = Column(Integer)
    accountingperiod = Column(Integer)
    docid = Column(Unicode(36))
    accountingyear = Column(Integer)
    ts = Column(TIMESTAMP)
    updatedBy = Column(Unicode(32))
    priuserdefnvc1 = Column(Unicode(500))
    priuserdefdecm1 = Column(Numeric(28, 14))
    priuserdefnvc2 = Column(Unicode(500))
    priuserdefdecm2 = Column(Numeric(28, 14))
    priuserdefnvc3 = Column(Unicode(500))
    priuserdefdecm3 = Column(Numeric(28, 14))
    priuserdefnvc4 = Column(Unicode(500))
    priuserdefdecm4 = Column(Numeric(28, 14))
    priuserdefnvc5 = Column(Unicode(500))
    priuserdefdecm5 = Column(Numeric(28, 14))
    priuserdefnvc6 = Column(Unicode(500))
    priuserdefdecm6 = Column(Numeric(28, 14))
    pubuserdefnvc1 = Column(Unicode(500))
    pubuserdefdecm1 = Column(Numeric(28, 14))
    pubuserdefnvc2 = Column(Unicode(500))
    pubuserdefdecm2 = Column(Numeric(28, 14))
    pubuserdefnvc3 = Column(Unicode(500))
    pubuserdefdecm3 = Column(Numeric(28, 14))
    pubuserdefnvc4 = Column(Unicode(500))
    pubuserdefdecm4 = Column(Numeric(28, 14))
    pubuserdefnvc5 = Column(Unicode(500))
    pubuserdefdecm5 = Column(Numeric(28, 14))
    pubuserdefnvc6 = Column(Unicode(500))
    pubuserdefdecm6 = Column(Numeric(28, 14))
    VoucherYear = Column(Integer)
    VoucherPeriod = Column(Integer)
    SourceVoucherDate = Column(DateTime)
    exchangeRate = Column(Numeric(28, 14))
    ManufactureOrderCode = Column(Unicode(30))
    DelegateDispatchCode = Column(Unicode(30))
    BeforeUpgrade = Column(Unicode(100))
    TotalOrigTaxAmount = Column(Numeric(28, 14))
    TotalTaxAmount = Column(Numeric(28, 14))
    PrintCount = Column(Integer)
    Mobilephone = Column(Unicode(20))
    Address = Column(Unicode(50))
    ExternalCode = Column(Unicode(50))
    id = Column(Integer, primary_key=True)
    idbusitype = Column(Integer)
    idcurrency = Column(Integer)
    iddepartment = Column(Integer, index=True)
    iddistrict = Column(Integer)
    idmember = Column(Integer, index=True)
    IdStore = Column(Integer)
    IdMarketingOrgan = Column(Integer)
    idpartner = Column(Integer, index=True)
    idsettleCustomer = Column(Integer, index=True)
    idclerk = Column(Integer, index=True)
    idqualityinspector = Column(Integer)
    idproject = Column(Integer, index=True)
    idrdstyle = Column(Integer)
    idinwarehouse = Column(Integer)
    idwarehouse = Column(Integer, index=True)
    idCollaborateUpVoucherType = Column(Integer)
    idCollaborateUpVoucher = Column(Integer)
    accountState = Column(Integer)
    deliveryState = Column(Integer)
    settleStatus = Column(Integer)
    transportType = Column(Integer)
    voucherState = Column(Integer)
    auditorid = Column(Integer)
    makerid = Column(Integer)
    sourceVoucherId = Column(Integer, index=True)
    purchaseArrivalId = Column(Integer)
    saleDeliveryId = Column(Integer)
    saleOrderId = Column(Integer)
    idsourcevouchertype = Column(Integer, index=True)
    idvouchertype = Column(Integer, index=True)
    productReceiveId = Column(Integer)
    maturityDate = Column(DateTime)
    voucherdate = Column(DateTime, index=True)
    madedate = Column(DateTime)
    auditeddate = Column(DateTime)
    createdtime = Column(DateTime, index=True)
    updated = Column(DateTime)
    DataSource = Column(Integer, server_default=text("(NULL)"))


class STRDRecordSourceRelation(Base):
    __tablename__ = 'ST_RDRecordSourceRelation'

    quantity = Column(Numeric(28, 14))
    unitExchangeRate = Column(Numeric(28, 14))
    quantity2 = Column(Numeric(28, 14))
    baseQuantity = Column(Numeric(28, 14))
    subQuantity = Column(Numeric(28, 14))
    ts = Column(TIMESTAMP)
    updatedBy = Column(Unicode(32))
    id = Column(Integer, primary_key=True)
    idbaseunit = Column(Integer)
    idsubunit = Column(Integer)
    idunit = Column(Integer)
    idunit2 = Column(Integer)
    sourceVoucherId = Column(Integer, index=True)
    sourceVoucherDetailId = Column(Integer, index=True)
    idsourcevouchertype = Column(Integer, index=True)
    voucherId = Column(Integer, index=True)
    idRDRecordDetailDTO = Column(Integer, index=True)
    createdtime = Column(DateTime)
    updated = Column(DateTime, index=True)


t_ST_RDRecord_Trace = Table(
    'ST_RDRecord_Trace', metadata,
    Column('code', Unicode(30)),
    Column('name', Unicode(200)),
    Column('sourceVoucherCode', Unicode(50)),
    Column('sequencenumber', Integer),
    Column('ts', TIMESTAMP, nullable=False),
    Column('updatedBy', Unicode(32)),
    Column('id', Integer, nullable=False),
    Column('sourceVoucherId', Integer),
    Column('sourceVoucherDetailId', Integer),
    Column('IdsourceVoucherType', Integer, index=True),
    Column('voucherId', Integer),
    Column('idRDRecordDetailDTO', Integer, index=True),
    Column('createdtime', DateTime),
    Column('updated', DateTime, index=True),
    Index('IDX_ST_RDRecord_Trace_id', 'idRDRecordDetailDTO', 'id')
)


class STRDRecordB(Base):
    __tablename__ = 'ST_RDRecord_b'
    __table_args__ = (
        Index('IDX_ST_RDRecord_b_cost', 'idRDRecordDTO', 'updated', 'idsourcevouchertype', 'amount', 'dispatchAdjust'),
        Index('IDX_ST_RDRecord_b_PromotionPresent', 'PromotionPresentTypeID', 'PromotionPresentVoucherCode'),
        Index('IDX_ST_RDRecord_b_idinventory_idwarehouse', 'idinventory', 'idwarehouse', 'ID'),
        Index('IDX_ST_RDRecord_b_PromotionSingle', 'PromotionSingleTypeID', 'PromotionSingleVoucherCode')
    )

    code = Column(Unicode(30))
    arrivalQuantity = Column(Numeric(28, 14))
    arrivalQuantity2 = Column(Numeric(28, 14))
    quantity = Column(Numeric(28, 14))
    quantity2 = Column(Numeric(28, 14))
    compositionQuantity = Column(Unicode(50))
    baseQuantity = Column(Numeric(28, 14))
    subQuantity = Column(Numeric(28, 14))
    price = Column(Numeric(28, 14))
    price2 = Column(Numeric(28, 14))
    basePrice = Column(Numeric(28, 14))
    estimatedPrice2 = Column(Numeric(28, 14))
    baseEstimatedPrice = Column(Numeric(28, 14))
    estimatedPrice = Column(Numeric(28, 14))
    amount = Column(Numeric(28, 14))
    estimatedAmount = Column(Numeric(28, 14))
    cumulativeSettlementQuantity = Column(Numeric(28, 14))
    cumulativeSettlementQuantity2 = Column(Numeric(28, 14))
    cumulativeSettlementBaseQuantity = Column(Numeric(28, 14))
    cumulativeSettlementSubQuantity = Column(Numeric(28, 14))
    cumulativeSettlementAmount = Column(Numeric(28, 14))
    taxRate = Column(Numeric(28, 14))
    taxPrice = Column(Numeric(28, 14))
    tax = Column(Numeric(28, 14))
    taxAmount = Column(Numeric(28, 14))
    changeRate = Column(Numeric(28, 14))
    receiveAdjust = Column(Numeric(28, 14))
    dispatchAdjust = Column(Numeric(28, 14))
    feeAdjust = Column(Numeric(28, 14))
    totalAmount = Column(Numeric(28, 14))
    feeAmount = Column(Numeric(28, 14))
    materialAmount = Column(Numeric(28, 14))
    sourceVoucherCode = Column(Unicode(50))
    saleOrderCode = Column(Unicode(30))
    cumulativePurchaseArrivalQuantity = Column(Numeric(28, 14))
    cumulativePurchaseArrivalQuantity2 = Column(Numeric(28, 14))
    cumulativeSaleDispatchQuantity = Column(Numeric(28, 14))
    cumulativeSaleDispatchQuantity2 = Column(Numeric(28, 14))
    batch = Column(Unicode(50))
    memo = Column(Unicode(200))
    defectiveQuantity = Column(Numeric(28, 14))
    defectiveQuantity2 = Column(Numeric(28, 14))
    manHour = Column(Numeric(28, 14))
    receiveVoucherCode = Column(Unicode(50))
    isManualCost = Column(Integer)
    kitQuantity = Column(Numeric(28, 14))
    kitQuantity2 = Column(Numeric(28, 14))
    distributedQuantity = Column(Numeric(28, 14))
    distributedQuantity2 = Column(Numeric(28, 14))
    isCostAccounted = Column(Integer)
    taxFlag = Column(Integer)
    inventoryLocation = Column(Unicode(50))
    isNoModify = Column(Unicode(1000))
    cumulativeEstimateAmount = Column(Numeric(28, 14))
    ts = Column(TIMESTAMP)
    updatedBy = Column(Unicode(32))
    freeItem0 = Column(Unicode(300))
    freeItem1 = Column(Unicode(300))
    freeItem2 = Column(Unicode(300))
    freeItem3 = Column(Unicode(300))
    freeItem4 = Column(Unicode(300))
    freeItem5 = Column(Unicode(300))
    freeItem6 = Column(Unicode(300))
    freeItem7 = Column(Unicode(300))
    freeItem8 = Column(Unicode(300))
    freeItem9 = Column(Unicode(300))
    priuserdefnvc1 = Column(Unicode(500))
    priuserdefdecm1 = Column(Numeric(28, 14))
    priuserdefnvc2 = Column(Unicode(500))
    priuserdefdecm2 = Column(Numeric(28, 14))
    priuserdefnvc3 = Column(Unicode(500))
    priuserdefdecm3 = Column(Numeric(28, 14))
    priuserdefnvc4 = Column(Unicode(500))
    priuserdefdecm4 = Column(Numeric(28, 14))
    pubuserdefnvc1 = Column(Unicode(500))
    pubuserdefdecm1 = Column(Numeric(28, 14))
    pubuserdefnvc2 = Column(Unicode(500))
    CustomerInventoryPrice = Column(Unicode(300))
    pubuserdefdecm2 = Column(Numeric(28, 14))
    VendorInventoryPrice = Column(Unicode(300))
    pubuserdefnvc3 = Column(Unicode(500))
    InvBarCode = Column(Unicode(128))
    pubuserdefdecm3 = Column(Numeric(28, 14))
    pubuserdefnvc4 = Column(Unicode(500))
    pubuserdefdecm4 = Column(Numeric(28, 14))
    SourceVoucherCodeByMergedFlow = Column(Unicode(50))
    VendorInventoryName = Column(Unicode(300))
    PurchaseOrderCode = Column(Unicode(30))
    PartnerInventoryName = Column(Unicode(300))
    ShrinkageQuantity = Column(Numeric(28, 14))
    ShrinkageQuantity2 = Column(Numeric(28, 14))
    ShrinkageBaseQuantity = Column(Numeric(28, 14))
    ShrinkageSubQuantity = Column(Numeric(28, 14))
    OrigShrinkageQuantity = Column(Numeric(28, 14))
    OrigShrinkageQuantity2 = Column(Numeric(28, 14))
    CumPurchaseShrinkageQuantity = Column(Numeric(28, 14))
    CumPurchaseShrinkageQuantity2 = Column(Numeric(28, 14))
    productFreeItem0 = Column(Unicode(60))
    productFreeItem1 = Column(Unicode(60))
    productFreeItem2 = Column(Unicode(60))
    productFreeItem3 = Column(Unicode(60))
    productFreeItem4 = Column(Unicode(60))
    productFreeItem5 = Column(Unicode(60))
    productFreeItem6 = Column(Unicode(60))
    productFreeItem7 = Column(Unicode(60))
    productFreeItem8 = Column(Unicode(60))
    productFreeItem9 = Column(Unicode(60))
    origPrice = Column(Numeric(28, 14))
    origAmount = Column(Numeric(28, 14))
    origTaxPrice = Column(Numeric(28, 14))
    origTax = Column(Numeric(28, 14))
    origTaxAmount = Column(Numeric(28, 14))
    origSalePrice = Column(Numeric(28, 14))
    origTaxSalePrice = Column(Numeric(28, 14))
    origSaleAmount = Column(Numeric(28, 14))
    origTaxSaleAmount = Column(Numeric(28, 14))
    salePrice = Column(Numeric(28, 14))
    taxSalePrice = Column(Numeric(28, 14))
    saleAmount = Column(Numeric(28, 14))
    taxSaleAmount = Column(Numeric(28, 14))
    ManufactureOrderCode = Column(Unicode(30))
    CumReturnQuantity = Column(Numeric(28, 14))
    CumReturnQuantity2 = Column(Numeric(28, 14))
    OrigManuPrice = Column(Numeric(28, 14))
    OrigManuAmount = Column(Numeric(28, 14))
    OrigTaxManuPrice = Column(Numeric(28, 14))
    OrigTaxManuAmount = Column(Numeric(28, 14))
    ManuPrice = Column(Numeric(28, 14))
    ManuAmount = Column(Numeric(28, 14))
    TaxManuPrice = Column(Numeric(28, 14))
    TaxManuAmount = Column(Numeric(28, 14))
    ManuFeeDiff = Column(Numeric(28, 14))
    OrigManuPrice2 = Column(Numeric(28, 14))
    OrigTaxManuPrice2 = Column(Numeric(28, 14))
    ManuPrice2 = Column(Numeric(28, 14))
    TaxManuPrice2 = Column(Numeric(28, 14))
    baseManuPrice = Column(Numeric(28, 14))
    origPrice2 = Column(Numeric(28, 14))
    origTaxPrice2 = Column(Numeric(28, 14))
    TaxPrice2 = Column(Numeric(28, 14))
    origSalePrice2 = Column(Numeric(28, 14))
    origTaxSalePrice2 = Column(Numeric(28, 14))
    salePrice2 = Column(Numeric(28, 14))
    taxSalePrice2 = Column(Numeric(28, 14))
    NotSettleQuantity = Column(Numeric(28, 14))
    NotSettleQuantity2 = Column(Numeric(28, 14))
    SentBaseAmount = Column(Numeric(28, 14))
    SentBaseQuantity = Column(Numeric(28, 14))
    docid = Column(Unicode(38))
    IsPresent = Column(Integer)
    Retailprice = Column(Numeric(28, 14))
    RetailAmount = Column(Numeric(28, 14))
    differencequantity = Column(Numeric(28, 14))
    differencequantity2 = Column(Numeric(28, 14))
    BoxNumber = Column(Unicode(50))
    RetailNoTaxPrice = Column(Numeric(28, 14))
    RetailNoTaxAmount = Column(Numeric(28, 14))
    LastModifiedField = Column(Unicode(200))
    DiscountRate = Column(Numeric(28, 14))
    Discount = Column(Numeric(28, 14))
    OrigDiscount = Column(Numeric(28, 14))
    PriceStrategyTypeName = Column(Unicode(400))
    PriceStrategySchemeIds = Column(Unicode(400))
    PriceStrategySchemeNames = Column(Unicode(1000))
    PromotionVoucherCodes = Column(Unicode(200))
    PromotionVoucherIds = Column(Unicode(400))
    IsPromotionPresent = Column(Integer)
    PromotionPresentVoucherCode = Column(Unicode(50))
    PromotionSingleVoucherCode = Column(Unicode(50))
    PromotionPresentGroupID = Column(Unicode(150))
    PromotionSingleGroupID = Column(Unicode(150))
    SuperSourceVoucherTypeCode = Column(Unicode(50))
    ID = Column(Integer, primary_key=True)
    idbusiTypeByMergedFlow = Column(Integer)
    idinventory = Column(Integer, index=True)
    idProductInventory = Column(Integer, index=True)
    IdMarketingOrgan = Column(Integer)
    idproject = Column(Integer, index=True)
    PriceStrategyTypeId = Column(Integer)
    idbaseunit = Column(Integer)
    idsubunit = Column(Integer)
    idunit = Column(Integer)
    idunit2 = Column(Integer)
    idwarehouse = Column(Integer, index=True)
    indirectSourceVoucherDetailId = Column(Integer)
    CashbackWay = Column(Integer)
    PromotionPresentTypeID = Column(Integer)
    PromotionSingleTypeID = Column(Integer)
    sourceVoucherId = Column(Integer, index=True)
    ManufactureOrderId = Column(Integer)
    ManufactureOrderDetailId = Column(Integer)
    sourceVoucherDetailId = Column(Integer, index=True)
    ManufactureOrderMaterialDetailId = Column(Integer)
    PromotionPresentVoucherID = Column(Integer)
    PromotionSingleVoucherID = Column(Integer)
    SourceVoucherIdByMergedFlow = Column(Integer)
    SourceVoucherDetailIdByMergedFlow = Column(Integer)
    saleOrderId = Column(Integer)
    saleOrderDetailId = Column(Integer)
    SourceOrderDetailId = Column(Integer)
    idsourcevouchertype = Column(Integer, index=True)
    idsourceVoucherTypeByMergedFlow = Column(Integer, index=True)
    idIndirectSourceVoucherType = Column(Integer)
    receiveVoucherId = Column(Integer, index=True)
    idRDRecordDTO = Column(Integer, index=True)
    receiveVoucherDetailId = Column(Integer)
    expiryDate = Column(DateTime)
    receiveDate = Column(DateTime)
    createdtime = Column(DateTime)
    updated = Column(DateTime, index=True)
    ProductionDate = Column(DateTime)
    DataSource = Column(Integer, server_default=text("(NULL)"))


class STRedBlueBackVoucher(Base):
    __tablename__ = 'ST_RedBlueBackVoucher'

    code = Column(Unicode(30), index=True)
    memo = Column(Unicode(200))
    redBlue = Column(Integer)
    maker = Column(Unicode(50))
    auditor = Column(Unicode(50))
    reviser = Column(Unicode(50))
    iscarriedforwardout = Column(Integer)
    iscarriedforwardin = Column(Integer)
    ismodifiedcode = Column(Integer)
    docno = Column(Unicode(50))
    docclass = Column(Unicode(50))
    docid = Column(Unicode(50))
    ts = Column(TIMESTAMP)
    updatedBy = Column(Unicode(32))
    priuserdefnvc1 = Column(Unicode(500))
    priuserdefdecm1 = Column(Numeric(28, 14))
    priuserdefnvc2 = Column(Unicode(500))
    priuserdefdecm2 = Column(Numeric(28, 14))
    priuserdefnvc3 = Column(Unicode(500))
    priuserdefdecm3 = Column(Numeric(28, 14))
    priuserdefnvc4 = Column(Unicode(500))
    priuserdefdecm4 = Column(Numeric(28, 14))
    priuserdefnvc5 = Column(Unicode(500))
    priuserdefdecm5 = Column(Numeric(28, 14))
    priuserdefnvc6 = Column(Unicode(500))
    priuserdefdecm6 = Column(Numeric(28, 14))
    pubuserdefnvc1 = Column(Unicode(500))
    pubuserdefdecm1 = Column(Numeric(28, 14))
    pubuserdefnvc2 = Column(Unicode(500))
    pubuserdefdecm2 = Column(Numeric(28, 14))
    pubuserdefnvc3 = Column(Unicode(500))
    pubuserdefdecm3 = Column(Numeric(28, 14))
    pubuserdefnvc4 = Column(Unicode(500))
    pubuserdefdecm4 = Column(Numeric(28, 14))
    pubuserdefnvc5 = Column(Unicode(500))
    pubuserdefdecm5 = Column(Numeric(28, 14))
    pubuserdefnvc6 = Column(Unicode(500))
    pubuserdefdecm6 = Column(Numeric(28, 14))
    id = Column(Integer, primary_key=True)
    idbusitype = Column(Integer)
    iddepartment = Column(Integer, index=True)
    IdMarketingOrgan = Column(Integer)
    idpartner = Column(Integer, index=True)
    idclerk = Column(Integer, index=True)
    idrdstyle = Column(Integer)
    idwarehouse = Column(Integer, index=True)
    auditorid = Column(Integer)
    makerid = Column(Integer)
    idvouchertype = Column(Integer, index=True)
    voucherdate = Column(DateTime, index=True)
    madedate = Column(DateTime)
    auditeddate = Column(DateTime)
    createdtime = Column(DateTime)
    updated = Column(DateTime)


class STRedBlueBackVoucherB(Base):
    __tablename__ = 'ST_RedBlueBackVoucher_b'

    code = Column(Unicode(30))
    basePrice = Column(Numeric(28, 14))
    baseQuantity = Column(Numeric(28, 14))
    subQuantity = Column(Numeric(28, 14))
    amount = Column(Numeric(28, 14))
    batch = Column(Unicode(50))
    ts = Column(TIMESTAMP)
    updatedBy = Column(Unicode(32))
    freeItem0 = Column(Unicode(300))
    freeItem1 = Column(Unicode(300))
    freeItem2 = Column(Unicode(300))
    freeItem3 = Column(Unicode(300))
    freeItem4 = Column(Unicode(300))
    freeItem5 = Column(Unicode(300))
    freeItem6 = Column(Unicode(300))
    freeItem7 = Column(Unicode(300))
    freeItem8 = Column(Unicode(300))
    freeItem9 = Column(Unicode(300))
    priuserdefnvc1 = Column(Unicode(500))
    priuserdefdecm1 = Column(Numeric(28, 14))
    priuserdefnvc2 = Column(Unicode(500))
    priuserdefdecm2 = Column(Numeric(28, 14))
    priuserdefnvc3 = Column(Unicode(500))
    priuserdefdecm3 = Column(Numeric(28, 14))
    priuserdefnvc4 = Column(Unicode(500))
    priuserdefdecm4 = Column(Numeric(28, 14))
    pubuserdefnvc1 = Column(Unicode(500))
    pubuserdefdecm1 = Column(Numeric(28, 14))
    pubuserdefnvc2 = Column(Unicode(500))
    pubuserdefdecm2 = Column(Numeric(28, 14))
    pubuserdefnvc3 = Column(Unicode(500))
    pubuserdefdecm3 = Column(Numeric(28, 14))
    pubuserdefnvc4 = Column(Unicode(500))
    pubuserdefdecm4 = Column(Numeric(28, 14))
    id = Column(Integer, primary_key=True)
    idinventory = Column(Integer, index=True)
    idbaseunit = Column(Integer)
    idsubunit = Column(Integer)
    idwarehouse = Column(Integer, index=True)
    idRedBlueBackVoucherDTO = Column(Integer, index=True)
    expiryDate = Column(DateTime)
    createdtime = Column(DateTime)
    updated = Column(DateTime, index=True)
    ProductionDate = Column(DateTime)


class STReplenishment(Base):
    __tablename__ = 'ST_Replenishment'

    name = Column(Unicode(200), nullable=False)
    code = Column(Unicode(32))
    Quantity = Column(Numeric(28, 14))
    ExistedQuantity = Column(Numeric(28, 14))
    AccordQuantity = Column(Numeric(28, 14))
    Ts = Column(TIMESTAMP)
    id = Column(Integer, primary_key=True)
    IdInventory = Column(Integer)
    IdPartner = Column(Integer)
    IdUnit = Column(Integer)
    idWarehouse = Column(Integer)
    Userid = Column(Integer)


class STShapeVoucher(Base):
    __tablename__ = 'ST_ShapeVoucher'
    __table_args__ = (
        Index('IDX_ST_ShapeVoucher_createdtime_voucherdate', 'createdtime', 'voucherdate', 'id', 'iddepartment', 'makerid', 'idclerk', 'idproject'),
    )

    code = Column(Unicode(30), index=True)
    totalExpense = Column(Numeric(28, 14))
    memo = Column(Unicode(200))
    maker = Column(Unicode(50))
    auditor = Column(Unicode(50))
    reviser = Column(Unicode(50))
    iscarriedforwardout = Column(Integer)
    iscarriedforwardin = Column(Integer)
    ismodifiedcode = Column(Integer)
    docid = Column(Unicode(36))
    ts = Column(TIMESTAMP)
    updatedBy = Column(Unicode(32))
    priuserdefnvc1 = Column(Unicode(500))
    priuserdefdecm1 = Column(Numeric(28, 14))
    priuserdefnvc2 = Column(Unicode(500))
    priuserdefdecm2 = Column(Numeric(28, 14))
    priuserdefnvc3 = Column(Unicode(500))
    priuserdefdecm3 = Column(Numeric(28, 14))
    priuserdefnvc4 = Column(Unicode(500))
    priuserdefdecm4 = Column(Numeric(28, 14))
    priuserdefnvc5 = Column(Unicode(500))
    priuserdefdecm5 = Column(Numeric(28, 14))
    priuserdefnvc6 = Column(Unicode(500))
    priuserdefdecm6 = Column(Numeric(28, 14))
    pubuserdefnvc1 = Column(Unicode(500))
    pubuserdefdecm1 = Column(Numeric(28, 14))
    pubuserdefnvc2 = Column(Unicode(500))
    pubuserdefdecm2 = Column(Numeric(28, 14))
    pubuserdefnvc3 = Column(Unicode(500))
    pubuserdefdecm3 = Column(Numeric(28, 14))
    pubuserdefnvc4 = Column(Unicode(500))
    pubuserdefdecm4 = Column(Numeric(28, 14))
    pubuserdefnvc5 = Column(Unicode(500))
    pubuserdefdecm5 = Column(Numeric(28, 14))
    pubuserdefnvc6 = Column(Unicode(500))
    pubuserdefdecm6 = Column(Numeric(28, 14))
    DiffAmount = Column(Numeric(28, 14))
    DocId2 = Column(Unicode(36))
    DocNo2 = Column(Unicode(36))
    DocClass2 = Column(Unicode(36))
    AccountingYear2 = Column(Integer)
    AccountingPeriod2 = Column(Integer)
    SaleOrderCode = Column(Unicode(30))
    TotalAfterAmount = Column(Numeric(28, 14))
    PrintCount = Column(Integer)
    IsManualCost = Column(Integer)
    Changer = Column(Unicode(50))
    id = Column(Integer, primary_key=True)
    idbusitype = Column(Integer)
    iddepartment = Column(Integer, index=True)
    idmarketingOrgan = Column(Integer)
    idclerk = Column(Integer, index=True)
    idproject = Column(Integer, index=True)
    iddispatchstyle = Column(Integer)
    idreceivestyle = Column(Integer, index=True)
    voucherState = Column(Integer)
    auditorid = Column(Integer)
    makerid = Column(Integer)
    SaleOrderId = Column(Integer)
    idvouchertype = Column(Integer, index=True)
    ChangerId = Column(Integer)
    voucherdate = Column(DateTime, index=True)
    madedate = Column(DateTime)
    auditeddate = Column(DateTime)
    createdtime = Column(DateTime, index=True)
    updated = Column(DateTime)
    ChangeDate = Column(DateTime)


class STShapeVoucherB(Base):
    __tablename__ = 'ST_ShapeVoucher_b'
    __table_args__ = (
        Index('IDX_ST_ShapeVoucher_b_idwarehouse_idinventory', 'idwarehouse', 'idinventory'),
    )

    code = Column(Unicode(30))
    quantity = Column(Numeric(28, 14))
    baseQuantity = Column(Numeric(28, 14))
    subQuantity = Column(Numeric(28, 14))
    price = Column(Numeric(28, 14))
    materialAmount = Column(Numeric(28, 14))
    feeAmount = Column(Numeric(28, 14))
    amount = Column(Numeric(28, 14))
    changeRate = Column(Numeric(28, 14))
    quantity2 = Column(Numeric(28, 14))
    batch = Column(Unicode(50))
    inventoryLocation = Column(Unicode(50))
    receiveVoucherCode = Column(Unicode(50))
    ts = Column(TIMESTAMP)
    updatedBy = Column(Unicode(32))
    freeItem0 = Column(Unicode(300))
    freeItem1 = Column(Unicode(300))
    freeItem2 = Column(Unicode(300))
    freeItem3 = Column(Unicode(300))
    freeItem4 = Column(Unicode(300))
    freeItem5 = Column(Unicode(300))
    freeItem6 = Column(Unicode(300))
    freeItem7 = Column(Unicode(300))
    freeItem8 = Column(Unicode(300))
    freeItem9 = Column(Unicode(300))
    priuserdefnvc1 = Column(Unicode(500))
    priuserdefdecm1 = Column(Numeric(28, 14))
    priuserdefnvc2 = Column(Unicode(500))
    priuserdefdecm2 = Column(Numeric(28, 14))
    priuserdefnvc3 = Column(Unicode(500))
    priuserdefdecm3 = Column(Numeric(28, 14))
    priuserdefnvc4 = Column(Unicode(500))
    priuserdefdecm4 = Column(Numeric(28, 14))
    pubuserdefnvc1 = Column(Unicode(500))
    pubuserdefdecm1 = Column(Numeric(28, 14))
    pubuserdefnvc2 = Column(Unicode(500))
    pubuserdefdecm2 = Column(Numeric(28, 14))
    pubuserdefnvc3 = Column(Unicode(500))
    pubuserdefdecm3 = Column(Numeric(28, 14))
    InvBarCode = Column(Unicode(128))
    pubuserdefnvc4 = Column(Unicode(500))
    pubuserdefdecm4 = Column(Numeric(28, 14))
    compositionQuantity = Column(Unicode(50))
    price2 = Column(Numeric(28, 14))
    SaleOrderCode = Column(Unicode(30))
    id = Column(Integer, primary_key=True)
    idinventory = Column(Integer, index=True)
    idproject = Column(Integer, index=True)
    idbaseunit = Column(Integer)
    idsubunit = Column(Integer)
    idunit = Column(Integer)
    idunit2 = Column(Integer)
    idwarehouse = Column(Integer, index=True)
    transformType = Column(Integer)
    SaleOrderId = Column(Integer)
    SaleOrderDetailId = Column(Integer)
    receiveVoucherId = Column(Integer)
    receiveVoucherDetailId = Column(Integer)
    idshapeVoucher = Column(Integer, index=True)
    idShapeVoucherDTO = Column(Integer, index=True)
    expiryDate = Column(DateTime)
    createdtime = Column(DateTime)
    updated = Column(DateTime, index=True)
    ProductionDate = Column(DateTime)


class STShareExpenseVoucher(Base):
    __tablename__ = 'ST_ShareExpenseVoucher'

    code = Column(Unicode(30), index=True)
    memo = Column(Unicode(200))
    maker = Column(Unicode(50))
    auditor = Column(Unicode(50))
    reviser = Column(Unicode(50))
    iscarriedforwardout = Column(Integer)
    iscarriedforwardin = Column(Integer)
    ismodifiedcode = Column(Integer)
    docno = Column(Unicode(36))
    docclass = Column(Unicode(36))
    accountingperiod = Column(Integer)
    docid = Column(Unicode(36))
    accountingyear = Column(Integer)
    ts = Column(TIMESTAMP)
    updatedBy = Column(Unicode(32))
    shareExpenseAmount = Column(Numeric(28, 14))
    PrintCount = Column(Integer)
    id = Column(Integer, primary_key=True)
    iddepartment = Column(Integer, index=True)
    IdMarketingOrgan = Column(Integer)
    idclerk = Column(Integer, index=True)
    shareExpenseType = Column(Integer)
    voucherState = Column(Integer)
    auditorid = Column(Integer)
    makerid = Column(Integer)
    idvouchertype = Column(Integer, index=True)
    voucherdate = Column(DateTime, index=True)
    madedate = Column(DateTime)
    auditeddate = Column(DateTime)
    createdtime = Column(DateTime, index=True)
    updated = Column(DateTime)


class STShareExpenseVoucherExpenseDetail(Base):
    __tablename__ = 'ST_ShareExpenseVoucherExpenseDetail'

    code = Column(Unicode(30))
    ts = Column(TIMESTAMP)
    updatedBy = Column(Unicode(32))
    id = Column(Integer, primary_key=True)
    iddepartment = Column(Integer, index=True)
    idexpenseitem = Column(Integer, index=True)
    idpartner = Column(Integer, index=True)
    idclerk = Column(Integer, index=True)
    idproject = Column(Integer, index=True)
    idexpensevoucher = Column(Integer, index=True)
    idexpensevoucherdetail = Column(Integer, index=True)
    idShareExpenseVoucherDTO = Column(Integer, index=True)
    createdtime = Column(DateTime)
    updated = Column(DateTime, index=True)


class STShareExpenseVoucherRdDetail(Base):
    __tablename__ = 'ST_ShareExpenseVoucherRdDetail'

    code = Column(Unicode(30))
    expenseAmount = Column(Numeric(28, 14))
    ts = Column(TIMESTAMP)
    updatedBy = Column(Unicode(32))
    Amount = Column(Numeric(28, 14))
    id = Column(Integer, primary_key=True)
    idinventory = Column(Integer, index=True)
    idpartner = Column(Integer, index=True)
    idproject = Column(Integer, index=True)
    idunit = Column(Integer)
    idrdrecord = Column(Integer, index=True)
    idrdrecorddetail = Column(Integer, index=True)
    idShareExpenseVoucherDTO = Column(Integer, index=True)
    createdtime = Column(DateTime)
    updated = Column(DateTime, index=True)


t_ST_SubTemp = Table(
    'ST_SubTemp', metadata,
    Column('Batch', Unicode(50)),
    Column('orderno', Integer),
    Column('AccountYear', Integer),
    Column('AccountPeriod', Integer),
    Column('AccountYearPeriod', String(6, u'Chinese_PRC_CI_AS')),
    Column('Idinventory', Integer, nullable=False, server_default=text("((0))")),
    Column('Idwarehouse', Integer),
    Column('valuetype', Integer),
    Column('fromVoucherID', Integer),
    Column('fromVoucherDetailID', Integer),
    Column('AccountDate', DateTime),
    Column('fromVoucherTypeID', Integer)
)


class STSubsidiaryBook(Base):
    __tablename__ = 'ST_SubsidiaryBook'
    __table_args__ = (
        Index('IDX_ST_SubsidiaryBook_mix1', 'idinventory', 'idwarehouse', 'batch', 'accountDate', 'AccountYearPeriod', 'accountYear', 'accountPeriod', 'orderNo', 'inQuantity', 'inSubQuantity', 'inAmount', 'outQuantity', 'outSubQuantity', 'outAmount', 'outPrice', 'voucherDetailID', 'isInStock', 'isManual', 'backVoucher', 'isAdjustVoucher', 'voucherID', 'voucherIDFlowUnite', 'voucherDetailIDFlowUnite'),
        Index('IDX_ST_SubsidiaryBook_voucherdate', 'voucherdate', 'voucherDetailID', 'inQuantity', 'inAmount', 'outQuantity', 'outAmount', 'individualID', 'inSubQuantity', 'outSubQuantity', 'idwarehouse', 'idinventory')
    )

    code = Column(Unicode(30))
    accountYear = Column(Integer)
    accountPeriod = Column(Integer)
    voucherCode = Column(Unicode(30))
    inQuantity = Column(Numeric(28, 14))
    inPrice = Column(Numeric(28, 14))
    inAmount = Column(Numeric(28, 14))
    outQuantity = Column(Numeric(28, 14))
    outPrice = Column(Numeric(28, 14))
    outAmount = Column(Numeric(28, 14))
    batch = Column(Unicode(50))
    isPeriodInit = Column(Integer)
    isInStock = Column(Integer)
    isManual = Column(Integer)
    inSubQuantity = Column(Numeric(28, 14))
    isTrueAccount = Column(Integer)
    isRedVoucher = Column(Integer)
    backVoucher = Column(Integer)
    outSubQuantity = Column(Numeric(28, 14))
    orderNo = Column(Integer)
    voucherCodeFlowUnite = Column(Unicode(50))
    isAdjustVoucher = Column(Integer)
    iscarriedforwardout = Column(Integer)
    iscarriedforwardin = Column(Integer)
    docid = Column(Unicode(50))
    ts = Column(TIMESTAMP)
    AccountYearPeriod = Column(Unicode(6))
    id = Column(Integer, primary_key=True)
    idbusitype = Column(Integer)
    idbusitypeflowunite = Column(Integer)
    idinventory = Column(Integer, index=True)
    idbaseunit = Column(Integer)
    idsubunit = Column(Integer)
    idwarehouse = Column(Integer, index=True)
    voucherDetailIDFlowUnite = Column(Integer, index=True)
    voucherIDFlowUnite = Column(Integer)
    idvouchertype = Column(Integer, index=True)
    idvouchertypeflowunite = Column(Integer, index=True)
    purchaseSettleVoucherID = Column(Integer)
    purchaseSettleVoucherDetailID = Column(Integer)
    voucherID = Column(Integer, index=True)
    individualID = Column(Integer)
    voucherDetailID = Column(Integer, index=True)
    accountDate = Column(DateTime)
    voucherdate = Column(DateTime)
    auditeddate = Column(DateTime)
    createdtime = Column(DateTime)
    updated = Column(DateTime)
    productionDate = Column(DateTime)


class STSummaryBook(Base):
    __tablename__ = 'ST_SummaryBook'
    __table_args__ = (
        Index('IDX_ST_SummaryBook_mix1', 'idinventory', 'idwarehouse', 'batch', 'AccountYearPeriod', 'accountYear', 'accountPeriod', 'beginQuantity', 'beginAmount', 'incomeAmount', 'sendOutQuantity', 'sendOutAmount', 'finalQuantity', 'finalAmount', 'incomeQuantity'),
    )

    incomeSubQuantity = Column(Numeric(28, 14))
    accountYear = Column(Integer)
    accountPeriod = Column(Integer)
    batch = Column(Unicode(50))
    beginQuantity = Column(Numeric(28, 14))
    beginSubQuantity = Column(Numeric(28, 14))
    beginAmount = Column(Numeric(28, 14))
    incomeQuantity = Column(Numeric(28, 14))
    incomeAmount = Column(Numeric(28, 14))
    sendOutQuantity = Column(Numeric(28, 14))
    sendOutSubQuantity = Column(Numeric(28, 14))
    sendOutAmount = Column(Numeric(28, 14))
    adjustInAmount = Column(Numeric(28, 14))
    adjustOutAmount = Column(Numeric(28, 14))
    finalQuantity = Column(Numeric(28, 14))
    finalSubQuantity = Column(Numeric(28, 14))
    finalAmount = Column(Numeric(28, 14))
    iscarriedforwardin = Column(Integer)
    iscarriedforwardout = Column(Integer)
    ts = Column(TIMESTAMP)
    AccountYearPeriod = Column(Unicode(6), index=True)
    isAccount = Column(SmallInteger, server_default=text("((1))"))
    id = Column(Integer, primary_key=True)
    idinventory = Column(Integer, index=True)
    idwarehouse = Column(Integer, index=True)


t_ST_ToValuation = Table(
    'ST_ToValuation', metadata,
    Column('SerialNo', Integer, nullable=False),
    Column('WarehouseID', Integer, nullable=False, server_default=text("((0))"))
)


class STTranVoucherRecord(Base):
    __tablename__ = 'ST_TranVoucherRecord'

    OrderNo = Column(Integer)
    Flag = Column(BIT)
    INQuantity = Column(Numeric(28, 14))
    InVoucherPrice = Column(Numeric(28, 14))
    InVoucherAmount = Column(Numeric(28, 14))
    OutQuantity = Column(Numeric(28, 14))
    OutQuantity2 = Column(Numeric(28, 14))
    Id = Column(Integer, primary_key=True)
    AssistantBookId = Column(Integer)
    RelationDataId = Column(Integer)


class STTransSourceRelation(Base):
    __tablename__ = 'ST_TransSourceRelation'

    quantity = Column(Numeric(28, 14))
    unitExchangeRate = Column(Numeric(28, 14))
    quantity2 = Column(Numeric(28, 14))
    baseQuantity = Column(Numeric(28, 14))
    subQuantity = Column(Numeric(28, 14))
    ts = Column(TIMESTAMP)
    updatedBy = Column(Unicode(32))
    id = Column(Integer, primary_key=True)
    idbaseUnit = Column(Integer)
    idsubUnit = Column(Integer)
    idunit = Column(Integer)
    idunit2 = Column(Integer)
    sourceVoucherId = Column(Integer, index=True)
    sourceVoucherDetailId = Column(Integer, index=True)
    idsourceVoucherType = Column(Integer, index=True)
    voucherId = Column(Integer, index=True)
    idtransDetailDTO = Column(Integer, index=True)
    createdtime = Column(DateTime)
    updated = Column(DateTime)


class STTransVoucher(Base):
    __tablename__ = 'ST_TransVoucher'
    __table_args__ = (
        Index('IDX_ST_TransVoucher_createdtime_idvouchertype_voucherdate', 'createdtime', 'idvouchertype', 'voucherdate', 'ID', 'iddepartment', 'makerid', 'idclerk', 'idoutwarehouse', 'idproject'),
    )

    code = Column(Unicode(30), index=True)
    diffAmount = Column(Numeric(28, 14))
    memo = Column(Unicode(200))
    totalInAmount = Column(Numeric(28, 14))
    totalOutAmount = Column(Numeric(28, 14))
    maker = Column(Unicode(50))
    auditor = Column(Unicode(50))
    reviser = Column(Unicode(50))
    iscarriedforwardout = Column(Integer)
    iscarriedforwardin = Column(Integer)
    ismodifiedcode = Column(Integer)
    docid = Column(Unicode(36))
    ts = Column(TIMESTAMP)
    updatedBy = Column(Unicode(32))
    priuserdefnvc1 = Column(Unicode(500))
    priuserdefdecm1 = Column(Numeric(28, 14))
    priuserdefnvc2 = Column(Unicode(500))
    priuserdefdecm2 = Column(Numeric(28, 14))
    priuserdefnvc3 = Column(Unicode(500))
    priuserdefdecm3 = Column(Numeric(28, 14))
    priuserdefnvc4 = Column(Unicode(500))
    priuserdefdecm4 = Column(Numeric(28, 14))
    priuserdefnvc5 = Column(Unicode(500))
    priuserdefdecm5 = Column(Numeric(28, 14))
    priuserdefnvc6 = Column(Unicode(500))
    priuserdefdecm6 = Column(Numeric(28, 14))
    pubuserdefnvc1 = Column(Unicode(500))
    pubuserdefdecm1 = Column(Numeric(28, 14))
    pubuserdefnvc2 = Column(Unicode(500))
    pubuserdefdecm2 = Column(Numeric(28, 14))
    pubuserdefnvc3 = Column(Unicode(500))
    pubuserdefdecm3 = Column(Numeric(28, 14))
    pubuserdefnvc4 = Column(Unicode(500))
    pubuserdefdecm4 = Column(Numeric(28, 14))
    pubuserdefnvc5 = Column(Unicode(500))
    pubuserdefdecm5 = Column(Numeric(28, 14))
    pubuserdefnvc6 = Column(Unicode(500))
    pubuserdefdecm6 = Column(Numeric(28, 14))
    SaleOrderCode = Column(Unicode(30))
    SourceVoucherCode = Column(Unicode(50))
    SourceVoucherDate = Column(DateTime)
    isNoModify = Column(Unicode(400))
    PrintCount = Column(Integer)
    ID = Column(Integer, primary_key=True)
    idbusitype = Column(Integer)
    iddepartment = Column(Integer, index=True)
    IdMarketingOrgan = Column(Integer)
    idclerk = Column(Integer, index=True)
    idproject = Column(Integer, index=True)
    iddispatchstyle = Column(Integer)
    idreceivestyle = Column(Integer)
    idinwarehouse = Column(Integer, index=True)
    idoutwarehouse = Column(Integer, index=True)
    SourceVoucherId = Column(Integer, index=True)
    voucherState = Column(Integer)
    auditorid = Column(Integer)
    makerid = Column(Integer)
    SaleOrderId = Column(Integer)
    idsourcevouchertype = Column(Integer, index=True)
    idvouchertype = Column(Integer, index=True)
    voucherdate = Column(DateTime, index=True)
    madedate = Column(DateTime)
    auditeddate = Column(DateTime)
    createdtime = Column(DateTime, index=True)
    updated = Column(DateTime)


class STTransVoucherB(Base):
    __tablename__ = 'ST_TransVoucher_b'

    code = Column(Unicode(30))
    quantity = Column(Numeric(28, 14))
    quantity2 = Column(Numeric(28, 14))
    baseQuantity = Column(Numeric(28, 14))
    subQuantity = Column(Numeric(28, 14))
    outPrice = Column(Numeric(28, 14))
    outAmount = Column(Numeric(28, 14))
    inPrice = Column(Numeric(28, 14))
    inAmount = Column(Numeric(28, 14))
    balanceAmount = Column(Numeric(28, 14))
    changeRate = Column(Numeric(28, 14))
    isManualCost = Column(Integer)
    batch = Column(Unicode(50))
    receiveVoucherCode = Column(Unicode(50))
    ts = Column(TIMESTAMP)
    updatedBy = Column(Unicode(32))
    freeItem0 = Column(Unicode(300))
    freeItem1 = Column(Unicode(300))
    freeItem2 = Column(Unicode(300))
    freeItem3 = Column(Unicode(300))
    freeItem4 = Column(Unicode(300))
    freeItem5 = Column(Unicode(300))
    freeItem6 = Column(Unicode(300))
    freeItem7 = Column(Unicode(300))
    freeItem8 = Column(Unicode(300))
    freeItem9 = Column(Unicode(300))
    priuserdefnvc1 = Column(Unicode(500))
    priuserdefdecm1 = Column(Numeric(28, 14))
    priuserdefnvc2 = Column(Unicode(500))
    priuserdefdecm2 = Column(Numeric(28, 14))
    priuserdefnvc3 = Column(Unicode(500))
    priuserdefdecm3 = Column(Numeric(28, 14))
    priuserdefnvc4 = Column(Unicode(500))
    priuserdefdecm4 = Column(Numeric(28, 14))
    pubuserdefnvc1 = Column(Unicode(500))
    pubuserdefdecm1 = Column(Numeric(28, 14))
    pubuserdefnvc2 = Column(Unicode(500))
    pubuserdefdecm2 = Column(Numeric(28, 14))
    pubuserdefnvc3 = Column(Unicode(500))
    pubuserdefdecm3 = Column(Numeric(28, 14))
    pubuserdefnvc4 = Column(Unicode(500))
    InvBarCode = Column(Unicode(128))
    pubuserdefdecm4 = Column(Numeric(28, 14))
    compositionQuantity = Column(Unicode(50))
    inPrice2 = Column(Numeric(28, 14))
    outPrice2 = Column(Numeric(28, 14))
    SaleOrderCode = Column(Unicode(30))
    SourceVoucherCode = Column(Unicode(50))
    isNoModify = Column(Unicode(1000))
    BoxNumber = Column(Unicode(50))
    RetailPrice = Column(Numeric(28, 14))
    id = Column(Integer, primary_key=True)
    idinventory = Column(Integer, index=True)
    idinofinvlocation = Column(Integer, index=True)
    idoutofinvlocation = Column(Integer, index=True)
    idproject = Column(Integer, index=True)
    idbaseunit = Column(Integer)
    idsubunit = Column(Integer)
    idunit = Column(Integer)
    idunit2 = Column(Integer)
    SourceVoucherId = Column(Integer, index=True)
    SourceVoucherDetailId = Column(Integer, index=True)
    SaleOrderId = Column(Integer)
    SaleOrderDetailId = Column(Integer)
    idsourcevouchertype = Column(Integer, index=True)
    receiveVoucherId = Column(Integer)
    receiveVoucherDetailId = Column(Integer)
    idTransVoucherDTO = Column(Integer, index=True)
    expiryDate = Column(DateTime)
    createdtime = Column(DateTime)
    updated = Column(DateTime, index=True)
    ProductionDate = Column(DateTime)


class STWarehouseLocationLock(Base):
    __tablename__ = 'ST_WarehouseLocationLock'

    lockCount = Column(Integer)
    ts = Column(TIMESTAMP)
    updatedBy = Column(Unicode(32))
    id = Column(Integer, primary_key=True)
    idinvlocation = Column(Integer)
    idwarehouse = Column(Integer, index=True)
    updated = Column(DateTime, index=True)


t_TEMP_1_GL_TEMPOpeningAccount = Table(
    'TEMP_1_GL_TEMPOpeningAccount', metadata,
    Column('DTOStatus', Unicode(10)),
    Column('ID', Integer, nullable=False),
    Column('UserId', Integer),
    Column('DocId', Integer),
    Column('EntryId', Integer)
)


t_TEMP_1_GL_TempAuxiliaryInfo = Table(
    'TEMP_1_GL_TempAuxiliaryInfo', metadata,
    Column('code', Unicode(30)),
    Column('name', Unicode(200)),
    Column('billno', Unicode(50)),
    Column('billdate', String(19, u'Chinese_PRC_CI_AS')),
    Column('exchangerate', Numeric(28, 14)),
    Column('bizdate', String(19, u'Chinese_PRC_CI_AS')),
    Column('bizno', Unicode(50)),
    Column('duedate', String(19, u'Chinese_PRC_CI_AS')),
    Column('origamount', Numeric(28, 14)),
    Column('amount', Numeric(28, 14)),
    Column('quantity', Numeric(28, 14)),
    Column('price', Numeric(28, 14)),
    Column('createdtime', String(19, u'Chinese_PRC_CI_AS')),
    Column('sequencenumber', Integer),
    Column('ts', TIMESTAMP, nullable=False),
    Column('updated', String(19, u'Chinese_PRC_CI_AS')),
    Column('updatedBy', Unicode(32)),
    Column('unit', Unicode(200)),
    Column('id', Integer, nullable=False),
    Column('idaccount', Integer),
    Column('idbankAccount', Integer),
    Column('idcurrency', Integer),
    Column('idauxAccDepartment', Integer),
    Column('idauxAccInventory', Integer),
    Column('idauxAccCustomer', Integer),
    Column('idauxAccSupplier', Integer),
    Column('idauxAccPerson', Integer),
    Column('idclerk', Integer),
    Column('idauxAccProject', Integer),
    Column('idsettlestyle', Integer),
    Column('idUnit', Integer),
    Column('dcdirection', Integer),
    Column('idexauxacc1', Integer),
    Column('idexauxacc10', Integer),
    Column('idexauxacc2', Integer),
    Column('idexauxacc3', Integer),
    Column('idexauxacc4', Integer),
    Column('idexauxacc5', Integer),
    Column('idexauxacc6', Integer),
    Column('idexauxacc7', Integer),
    Column('idexauxacc8', Integer),
    Column('idexauxacc9', Integer),
    Column('idTempEntryDTO', Integer)
)


t_TEMP_1_GL_TempCashFlowInfo = Table(
    'TEMP_1_GL_TempCashFlowInfo', metadata,
    Column('code', Unicode(30)),
    Column('name', Unicode(200)),
    Column('amount', Numeric(28, 14)),
    Column('createdtime', String(19, u'Chinese_PRC_CI_AS')),
    Column('sequencenumber', Integer),
    Column('ts', TIMESTAMP, nullable=False),
    Column('updated', String(19, u'Chinese_PRC_CI_AS')),
    Column('updatedBy', Unicode(32)),
    Column('ownerEntryNo', Integer),
    Column('mapEntryNo', Integer),
    Column('id', Integer, nullable=False),
    Column('idaccount', Integer),
    Column('idcashflowitem', Integer),
    Column('idcurrency', Integer),
    Column('idTempDocDTO', Integer)
)


t_TEMP_1_GL_TempDoc = Table(
    'TEMP_1_GL_TempDoc', metadata,
    Column('code', Unicode(30)),
    Column('name', Unicode(200)),
    Column('isgenerateddoc', Integer),
    Column('attachedvouchernum', Integer),
    Column('docno', Unicode(50)),
    Column('docclass', Unicode(50)),
    Column('accountingperiod', Integer),
    Column('docid', Unicode(50)),
    Column('accountingyear', Integer),
    Column('memo', Unicode(50)),
    Column('voucherdate', String(19, u'Chinese_PRC_CI_AS')),
    Column('madedate', String(19, u'Chinese_PRC_CI_AS')),
    Column('maker', Unicode(50)),
    Column('auditor', Unicode(50)),
    Column('auditeddate', String(19, u'Chinese_PRC_CI_AS')),
    Column('reviser', Unicode(50)),
    Column('ismodifiedcode', Integer),
    Column('createdtime', String(19, u'Chinese_PRC_CI_AS')),
    Column('sequencenumber', Integer),
    Column('ts', TIMESTAMP, nullable=False),
    Column('updated', String(19, u'Chinese_PRC_CI_AS')),
    Column('updatedBy', Unicode(32)),
    Column('priuserdefnvc1', Unicode(500)),
    Column('priuserdefdecm1', Numeric(28, 14)),
    Column('priuserdefnvc2', Unicode(500)),
    Column('priuserdefdecm2', Numeric(28, 14)),
    Column('priuserdefnvc3', Unicode(500)),
    Column('priuserdefdecm3', Numeric(28, 14)),
    Column('priuserdefnvc4', Unicode(500)),
    Column('priuserdefdecm4', Numeric(28, 14)),
    Column('priuserdefnvc5', Unicode(500)),
    Column('priuserdefdecm5', Numeric(28, 14)),
    Column('priuserdefnvc6', Unicode(500)),
    Column('priuserdefdecm6', Numeric(28, 14)),
    Column('IsCashFlowed', Integer),
    Column('isCashflowByHand', Integer),
    Column('businessDocMoney', Numeric(28, 14)),
    Column('id', Integer, nullable=False),
    Column('iddoctype', Integer),
    Column('isdefrence', Integer),
    Column('CashFlowedState', Integer),
    Column('tempDocGenerate', Integer),
    Column('tempdoctype', Integer),
    Column('voucherstate', Integer),
    Column('auditorid', Integer),
    Column('makerid', Integer)
)


t_TEMP_1_GL_TempDocIds = Table(
    'TEMP_1_GL_TempDocIds', metadata,
    Column('DocTs', BINARY(16)),
    Column('BookType', Unicode(32)),
    Column('UserID', Integer),
    Column('DocID', Integer)
)


t_TEMP_1_GL_TempDocSrcDocDetailInfo = Table(
    'TEMP_1_GL_TempDocSrcDocDetailInfo', metadata,
    Column('code', Unicode(30)),
    Column('name', Unicode(200)),
    Column('createdtime', String(19, u'Chinese_PRC_CI_AS')),
    Column('sequencenumber', Integer),
    Column('ts', TIMESTAMP, nullable=False),
    Column('updated', String(19, u'Chinese_PRC_CI_AS')),
    Column('updatedBy', Unicode(32)),
    Column('srcVoucherTimeStamp', Unicode(200)),
    Column('srcVoucherDetailTimeStamp', Unicode(200)),
    Column('id', Integer, nullable=False),
    Column('srcvoucherid', Integer),
    Column('fccarryforwardtype', Integer),
    Column('srcvoucherdetailid', Integer),
    Column('idSrcVoucherType', Integer),
    Column('idTempEntryDTO', Integer),
    Column('IdTransactionEntry', Integer)
)


t_TEMP_1_GL_TempDocSrcDocInfo = Table(
    'TEMP_1_GL_TempDocSrcDocInfo', metadata,
    Column('code', Unicode(30)),
    Column('name', Unicode(200)),
    Column('createdtime', String(19, u'Chinese_PRC_CI_AS')),
    Column('sequencenumber', Integer),
    Column('ts', TIMESTAMP, nullable=False),
    Column('updated', String(19, u'Chinese_PRC_CI_AS')),
    Column('updatedBy', Unicode(32)),
    Column('srcVoucherTimeStamp', Unicode(200)),
    Column('srcVoucherNo', Unicode(200)),
    Column('srcVoucherDate', String(19, u'Chinese_PRC_CI_AS')),
    Column('id', Integer, nullable=False),
    Column('idSrcBusiType', Integer),
    Column('srcvoucherid', Integer),
    Column('carryforwardtype', Integer),
    Column('idSrcVoucherType', Integer),
    Column('idTempDocDTO', Integer),
    Column('idTransactionDocDTO', Integer)
)


t_TEMP_1_GL_TempEntry = Table(
    'TEMP_1_GL_TempEntry', metadata,
    Column('code', Unicode(30)),
    Column('name', Unicode(200)),
    Column('summary', Unicode(200)),
    Column('AuxiliaryItems', Unicode(200)),
    Column('exchangerate', Numeric(28, 14)),
    Column('origamountdr', Numeric(28, 14)),
    Column('origamountcr', Numeric(28, 14)),
    Column('amountdr', Numeric(28, 14)),
    Column('amountcr', Numeric(28, 14)),
    Column('quantitydr', Numeric(28, 14)),
    Column('quantitycr', Numeric(28, 14)),
    Column('price', Numeric(28, 14)),
    Column('createdtime', String(19, u'Chinese_PRC_CI_AS')),
    Column('sequencenumber', Integer),
    Column('accountcode', Unicode(50)),
    Column('ts', TIMESTAMP, nullable=False),
    Column('updated', String(19, u'Chinese_PRC_CI_AS')),
    Column('updatedBy', Unicode(32)),
    Column('priuserdefnvc1', Unicode(500)),
    Column('priuserdefdecm1', Numeric(28, 14)),
    Column('priuserdefnvc2', Unicode(500)),
    Column('priuserdefdecm2', Numeric(28, 14)),
    Column('priuserdefnvc3', Unicode(500)),
    Column('priuserdefdecm3', Numeric(28, 14)),
    Column('priuserdefnvc4', Unicode(500)),
    Column('priuserdefdecm4', Numeric(28, 14)),
    Column('id', Integer, nullable=False),
    Column('idaccount', Integer),
    Column('idcurrency', Integer),
    Column('datafrom', Integer),
    Column('idTempDocDTO', Integer)
)


t_TEMP_1_SM_FC_PBSAMCheckAccount = Table(
    'TEMP_1_SM_FC_PBSAMCheckAccount', metadata,
    Column('ts', TIMESTAMP, nullable=False),
    Column('Updated', DateTime),
    Column('UpdatedBy', Unicode(32)),
    Column('name', Unicode(200)),
    Column('ValueType', Unicode(200)),
    Column('AssetOrigAmount', Float(53)),
    Column('GLOrigAmount', Float(53), server_default=text("((0))")),
    Column('OrigAmountDiff', Float(53), server_default=text("((0))")),
    Column('id', Integer, nullable=False),
    Column('idAccount', Integer),
    Column('idAssetProp', Integer)
)


t_TEMP_1_SM_FC_PBSARAPCheckAccount = Table(
    'TEMP_1_SM_FC_PBSARAPCheckAccount', metadata,
    Column('code', Unicode(30)),
    Column('name', Unicode(200)),
    Column('periodbeginsynctype', Integer),
    Column('origamount', Numeric(28, 14)),
    Column('amount', Numeric(28, 14)),
    Column('glamount', Numeric(28, 14)),
    Column('glorigamount', Numeric(28, 14)),
    Column('amountdiff', Numeric(28, 14)),
    Column('origamountdiff', Numeric(28, 14)),
    Column('createdtime', String(19, u'Chinese_PRC_CI_AS')),
    Column('sequencenumber', Integer),
    Column('ts', TIMESTAMP, nullable=False),
    Column('updated', String(19, u'Chinese_PRC_CI_AS')),
    Column('updatedBy', Unicode(32)),
    Column('id', Integer, nullable=False),
    Column('idaccount', Integer),
    Column('idcurrency', Integer),
    Column('pbscheckaccounttype', Integer)
)


t_TEMP_1_SM_FC_PBSCashBankCheckAccount = Table(
    'TEMP_1_SM_FC_PBSCashBankCheckAccount', metadata,
    Column('code', Unicode(30)),
    Column('name', Unicode(200)),
    Column('origamount', Numeric(28, 14)),
    Column('amount', Numeric(28, 14)),
    Column('glamount', Numeric(28, 14)),
    Column('glorigamount', Numeric(28, 14)),
    Column('amountdiff', Numeric(28, 14)),
    Column('origamountdiff', Numeric(28, 14)),
    Column('createdtime', String(19, u'Chinese_PRC_CI_AS')),
    Column('sequencenumber', Integer),
    Column('ts', TIMESTAMP, nullable=False),
    Column('updated', String(19, u'Chinese_PRC_CI_AS')),
    Column('updatedBy', Unicode(32)),
    Column('id', Integer, nullable=False),
    Column('idaccount', Integer),
    Column('idbankaccount', Integer)
)


t_TEMP_1_SM_FC_PBSInventoryCheckAccount = Table(
    'TEMP_1_SM_FC_PBSInventoryCheckAccount', metadata,
    Column('code', Unicode(30)),
    Column('name', Unicode(200)),
    Column('quantity', Numeric(28, 14)),
    Column('amount', Numeric(28, 14)),
    Column('origamount', Numeric(28, 14)),
    Column('glamount', Numeric(28, 14)),
    Column('glorigamount', Numeric(28, 14)),
    Column('glquantity', Numeric(28, 14)),
    Column('amountdiff', Numeric(28, 14)),
    Column('origamountdiff', Numeric(28, 14)),
    Column('quantitydiff', Numeric(28, 14)),
    Column('createdtime', String(19, u'Chinese_PRC_CI_AS')),
    Column('sequencenumber', Integer),
    Column('ts', TIMESTAMP, nullable=False),
    Column('updated', String(19, u'Chinese_PRC_CI_AS')),
    Column('updatedBy', Unicode(32)),
    Column('id', Integer, nullable=False),
    Column('idaccount', Integer),
    Column('idinventoryclass', Integer),
    Column('idwarehouse', Integer)
)


t_TEMP_1_SM_FC_PBSPurRecCheckAccount = Table(
    'TEMP_1_SM_FC_PBSPurRecCheckAccount', metadata,
    Column('code', Unicode(30)),
    Column('name', Unicode(200)),
    Column('origamount', Numeric(28, 14)),
    Column('amount', Numeric(28, 14)),
    Column('glamount', Numeric(28, 14)),
    Column('glorigamount', Numeric(28, 14)),
    Column('amountdiff', Numeric(28, 14)),
    Column('origamountdiff', Numeric(28, 14)),
    Column('ts', TIMESTAMP, nullable=False),
    Column('updated', String(19, u'Chinese_PRC_CI_AS')),
    Column('updatedBy', Unicode(32)),
    Column('id', Integer, nullable=False),
    Column('idaccount', Integer),
    Column('idcurrency', Integer)
)


t_TEMP_1_SM_FC_TransactionAuxiliaryInfo = Table(
    'TEMP_1_SM_FC_TransactionAuxiliaryInfo', metadata,
    Column('code', Unicode(30)),
    Column('name', Unicode(200)),
    Column('voucherdate', String(19, u'Chinese_PRC_CI_AS')),
    Column('vouchercode', Unicode(50)),
    Column('invoicecode', Unicode(50)),
    Column('duedate', String(19, u'Chinese_PRC_CI_AS')),
    Column('origamount', Numeric(28, 14)),
    Column('amount', Numeric(28, 14)),
    Column('quantity', Numeric(28, 14)),
    Column('price', Numeric(28, 14)),
    Column('createdtime', String(19, u'Chinese_PRC_CI_AS')),
    Column('sequencenumber', Integer),
    Column('ts', TIMESTAMP, nullable=False),
    Column('updated', String(19, u'Chinese_PRC_CI_AS')),
    Column('updatedBy', Unicode(32)),
    Column('id', Integer, nullable=False),
    Column('idbankaccount', Integer),
    Column('idbusitype', Integer),
    Column('idcostitem', Integer),
    Column('idcurrency', Integer),
    Column('iddepartment', Integer),
    Column('iddistrict', Integer),
    Column('iddocumentsusage', Integer),
    Column('idexpenseitem', Integer),
    Column('idincome', Integer),
    Column('idinventory', Integer),
    Column('idinventoryclass', Integer),
    Column('idinvlocation', Integer),
    Column('idcustomer', Integer),
    Column('idsupplier', Integer),
    Column('idcustomerclass', Integer),
    Column('idsupplierclass', Integer),
    Column('idperson', Integer),
    Column('idproductprocess', Integer),
    Column('idproject', Integer),
    Column('idprojectClass', Integer),
    Column('idinrdstyle', Integer),
    Column('idoutrdstyle', Integer),
    Column('idsettlestyle', Integer),
    Column('idUnit', Integer),
    Column('idwarehouse', Integer),
    Column('dcdirection', Integer),
    Column('idexauxacc1', Integer),
    Column('idexauxacc10', Integer),
    Column('idexauxacc2', Integer),
    Column('idexauxacc3', Integer),
    Column('idexauxacc4', Integer),
    Column('idexauxacc5', Integer),
    Column('idexauxacc6', Integer),
    Column('idexauxacc7', Integer),
    Column('idexauxacc8', Integer),
    Column('idexauxacc9', Integer),
    Column('idvouchertype', Integer),
    Column('idTransactionEntryDTO', Integer)
)


t_TEMP_1_SM_FC_TransactionDoc = Table(
    'TEMP_1_SM_FC_TransactionDoc', metadata,
    Column('code', Unicode(30)),
    Column('name', Unicode(200)),
    Column('attachedvouchernum', Integer),
    Column('voucherdate', String(19, u'Chinese_PRC_CI_AS')),
    Column('generatedate', String(19, u'Chinese_PRC_CI_AS')),
    Column('createdtime', String(19, u'Chinese_PRC_CI_AS')),
    Column('sequencenumber', Integer),
    Column('ts', TIMESTAMP, nullable=False),
    Column('updated', String(19, u'Chinese_PRC_CI_AS')),
    Column('updatedBy', Unicode(32)),
    Column('businessDocMoney', Numeric(28, 14)),
    Column('id', Integer, nullable=False),
    Column('iddoctype', Integer),
    Column('isdefrence', Integer),
    Column('userid', Integer)
)


t_TEMP_1_SM_FC_TransactionDocSourceRelation = Table(
    'TEMP_1_SM_FC_TransactionDocSourceRelation', metadata,
    Column('code', Unicode(30)),
    Column('name', Unicode(200)),
    Column('sourcevoucherts', Unicode(50)),
    Column('createdtime', String(19, u'Chinese_PRC_CI_AS')),
    Column('sequencenumber', Integer),
    Column('ts', TIMESTAMP, nullable=False),
    Column('updated', String(19, u'Chinese_PRC_CI_AS')),
    Column('updatedBy', Unicode(32)),
    Column('id', Integer, nullable=False),
    Column('sourcevoucherid', Integer),
    Column('carryforwardtype', Integer),
    Column('sourcevouchertypeid', Integer),
    Column('idTransactionDocDTO', Integer)
)


t_TEMP_1_SM_FC_TransactionEntry = Table(
    'TEMP_1_SM_FC_TransactionEntry', metadata,
    Column('code', Unicode(30)),
    Column('name', Unicode(200)),
    Column('summary', Unicode(200)),
    Column('exchangerate', Numeric(28, 14)),
    Column('origamountdr', Numeric(28, 14)),
    Column('origamountcr', Numeric(28, 14)),
    Column('amountdr', Numeric(28, 14)),
    Column('amountcr', Numeric(28, 14)),
    Column('quantitydr', Numeric(28, 14)),
    Column('quantitycr', Numeric(28, 14)),
    Column('price', Numeric(28, 14)),
    Column('mergecode', Unicode(50)),
    Column('origamount', Numeric(28, 14)),
    Column('billno', Unicode(50)),
    Column('billdate', String(19, u'Chinese_PRC_CI_AS')),
    Column('memoto', Unicode(200)),
    Column('generatedate', String(19, u'Chinese_PRC_CI_AS')),
    Column('accounttype', Unicode(50)),
    Column('extend1', Unicode(50)),
    Column('extend2', Unicode(50)),
    Column('extend3', Unicode(50)),
    Column('createdtime', String(19, u'Chinese_PRC_CI_AS')),
    Column('sequencenumber', Integer),
    Column('ts', TIMESTAMP, nullable=False),
    Column('updated', String(19, u'Chinese_PRC_CI_AS')),
    Column('updatedBy', Unicode(32)),
    Column('id', Integer, nullable=False),
    Column('idaccount', Integer),
    Column('idcurrency', Integer),
    Column('dcdirection', Integer),
    Column('idauxiliaryinfo', Integer),
    Column('idTransactionDocDTO', Integer)
)


t_TEMP_1_SM_FC_TransactionEntrySourceRelation = Table(
    'TEMP_1_SM_FC_TransactionEntrySourceRelation', metadata,
    Column('code', Unicode(30)),
    Column('name', Unicode(200)),
    Column('sourcevoucherts', Unicode(50)),
    Column('sourcevoucherdetailts', Unicode(50)),
    Column('createdtime', String(19, u'Chinese_PRC_CI_AS')),
    Column('sequencenumber', Integer),
    Column('ts', TIMESTAMP, nullable=False),
    Column('updated', String(19, u'Chinese_PRC_CI_AS')),
    Column('updatedBy', Unicode(32)),
    Column('id', Integer, nullable=False),
    Column('sourcevoucherid', Integer),
    Column('carryforwardtype', Integer),
    Column('sourcevoucherdetailid', Integer),
    Column('sourcevouchertypeid', Integer),
    Column('idTransactionEntryDTO', Integer)
)


t_Temp_CurrentAccount = Table(
    'Temp_CurrentAccount', metadata,
    Column('code', String(50, u'Chinese_PRC_CI_AS')),
    Column('AccountID', String(50, u'Chinese_PRC_CI_AS'))
)


t_UA_ListPrintstyle = Table(
    'UA_ListPrintstyle', metadata,
    Column('ts', TIMESTAMP),
    Column('updatedBy', Unicode(32)),
    Column('updated', String(19, u'Chinese_PRC_CI_AS')),
    Column('name', Unicode(200)),
    Column('code', Unicode(32)),
    Column('Style', Unicode(2000)),
    Column('id', Integer, nullable=False),
    Column('UserID', Integer)
)


t_aa_DimensionSet = Table(
    'aa_DimensionSet', metadata,
    Column('PriceSetType', Unicode(50)),
    Column('Dimension', Integer),
    Column('Remark', Unicode(100)),
    Column('IsInUse', Integer),
    Column('TS', TIMESTAMP, nullable=False),
    Column('id', Integer, nullable=False)
)


t_aa_partnerclassprice = Table(
    'aa_partnerclassprice', metadata,
    Column('Code', Unicode(32)),
    Column('ts', TIMESTAMP, nullable=False),
    Column('updatedBy', Unicode(32)),
    Column('name', Unicode(200)),
    Column('QuotedPrice', Unicode(1000)),
    Column('QuotedPriceFormula', Unicode(1000)),
    Column('Discount', Numeric(28, 14)),
    Column('Price', Unicode(1000)),
    Column('PriceFormula', Unicode(1000)),
    Column('IncreasePriceRate', Float(53)),
    Column('LowestPrice', Unicode(1000)),
    Column('lowestPriceFormula', Unicode(1000)),
    Column('AgreementDiscount', Numeric(28, 14)),
    Column('PriceKey', Unicode(34)),
    Column('InvBarCode', Unicode(128)),
    Column('idDepartment', Integer),
    Column('idDistrict', Integer),
    Column('idInventory', Integer),
    Column('idInventoryClass', Integer),
    Column('idInventoryPrice', Integer),
    Column('idPartner', Integer),
    Column('idPartnerClass', Integer),
    Column('id', Integer, nullable=False),
    Column('idpricetrace', Integer),
    Column('idPerson', Integer),
    Column('idUnit', Integer),
    Column('updated', DateTime)
)


t_dtproperties = Table(
    'dtproperties', metadata,
    Column('id', Integer, nullable=False),
    Column('objectid', Integer),
    Column('property', String(64, u'Chinese_PRC_CI_AS'), nullable=False),
    Column('value', String(255, u'Chinese_PRC_CI_AS')),
    Column('uvalue', Unicode(255)),
    Column('lvalue', LargeBinary),
    Column('version', Integer, nullable=False, server_default=text("(0)"))
)


class EapColumnSetSolution(Base):
    __tablename__ = 'eap_ColumnSetSolution'

    Name = Column(Unicode(50), index=True)
    ClassFullName = Column(Unicode(80))
    Title = Column(Unicode(100))
    IsShowDetail = Column(BIT)
    id = Column(Integer, primary_key=True)
    ddgMatchMode = Column(Integer)
    IsFirstShowDetail = Column(BIT)
    Width = Column(Integer)
    DtoName = Column(Unicode(100))
    IsDefault = Column(Integer, server_default=text("((0))"))
    IsTotal = Column(BIT)
    TFlag = Column(Integer, server_default=text("((0))"))
    Ts = Column(TIMESTAMP)
    CreatedTime = Column(DateTime)


class EapDTO(Base):
    __tablename__ = 'eap_DTO'

    Name = Column(Unicode(50), index=True)
    Title = Column(Unicode(200))
    TableName = Column(Unicode(50), index=True)
    ClassName = Column(Unicode(200))
    NameField = Column(Unicode(50))
    CodeField = Column(Unicode(50))
    memo = Column(Unicode(200))
    id = Column(Integer, primary_key=True)
    ts = Column(TIMESTAMP, nullable=False)
    TFlag = Column(Integer, server_default=text("((0))"))
    Code = Column(String(50, u'Chinese_PRC_CI_AS'))
    IDPackage = Column(Integer, index=True)
    AssemblyName = Column(Unicode(200))
    CreatedTime = Column(DateTime)


class EapDTOProperty(Base):
    __tablename__ = 'eap_DTOProperty'

    Name = Column(Unicode(200), index=True)
    Title = Column(Unicode(200))
    FieldName = Column(Unicode(200), index=True)
    Type = Column(Unicode(50))
    FieldLength = Column(Integer)
    DefaultValue = Column(Unicode(50))
    notNull = Column(Integer)
    Uniquely = Column(Integer, server_default=text("(0)"))
    DefineLevel = Column(Integer)
    sortNo = Column(Integer)
    precision = Column(Integer)
    memo = Column(Unicode(200))
    custom_use = Column(Integer, server_default=text("(0)"))
    custom_public = Column(Integer, server_default=text("(0)"))
    ts = Column(TIMESTAMP, nullable=False)
    Code = Column(String(50, u'Chinese_PRC_CI_AS'))
    relationType = Column(Unicode(32))
    FromProperty = Column(Unicode(200))
    ToProperty = Column(Unicode(200))
    idDTO = Column(Integer, nullable=False, index=True, server_default=text("((0))"))
    idToDTO = Column(Integer)
    id = Column(Integer, primary_key=True)
    idEnum = Column(Integer)
    DefineLevelEmu = Column(Integer)
    Typeemu = Column(Integer)
    CreatedTime = Column(DateTime)


class EapDTORelation(Base):
    __tablename__ = 'eap_DTORelation'

    relationType = Column(Integer, nullable=False)
    dependency = Column(Integer, nullable=False, server_default=text("(0)"))
    id = Column(Integer, primary_key=True)
    idFromDTO = Column(Integer, nullable=False, index=True, server_default=text("((0))"))
    idToDTO = Column(Integer, nullable=False, server_default=text("((0))"))
    idFromProperty = Column(Integer, nullable=False, index=True, server_default=text("((0))"))
    idProperty = Column(Integer, nullable=False, server_default=text("((0))"))
    idToProperty = Column(Integer, nullable=False, server_default=text("((0))"))


class EapDesigntable(Base):
    __tablename__ = 'eap_Designtable'

    tableName = Column(Unicode(200), nullable=False)
    flag = Column(Integer)
    id = Column(Integer, primary_key=True)


class EapEditTable(Base):
    __tablename__ = 'eap_EditTable'

    TableType = Column(Unicode(50))
    ParentTable = Column(Unicode(50))
    Name = Column(Unicode(50))
    Title = Column(Unicode(50))
    DtoName = Column(Unicode(50))
    ParentFieldName = Column(Unicode(50))
    ChildFieldName = Column(Unicode(50))
    TabIndex = Column(Integer)
    Visible = Column(Integer)
    AllowAdd = Column(Integer)
    AllowDelete = Column(Integer)
    ReadOnly = Column(Integer)
    AllowSortting = Column(Integer)
    ColumnMoveable = Column(Integer)
    ColumnSizeable = Column(Integer)
    RowHeaderVisible = Column(Integer)
    TotalRowVisible = Column(Integer)
    StatusBarVisible = Column(Integer)
    DynPropertyString = Column(Unicode(2000))
    id = Column(Integer, primary_key=True)
    ts = Column(TIMESTAMP, nullable=False)


class EapEditTableColumn(Base):
    __tablename__ = 'eap_EditTableColumn'

    Name = Column(Unicode(50))
    Title = Column(Unicode(50))
    EnumName = Column(Unicode(50))
    RefPage = Column(Unicode(50))
    RefDtoName = Column(Unicode(50))
    RefShowField = Column(Unicode(50))
    RefLinkField = Column(Unicode(50))
    UserCheck = Column(Unicode(100))
    UserPrompt = Column(Unicode(200))
    IsUserDef = Column(Integer)
    AllowUserDef = Column(Integer)
    AllowUserDelete = Column(Integer)
    FixedValue = Column(Unicode(50))
    ColIndex = Column(Integer)
    DropDownStyle = Column(Unicode(10))
    DropDownPanelID = Column(Unicode(50))
    SysPropValue = Column(Unicode(200))
    MustShow = Column(Integer)
    FieldName = Column(Unicode(50))
    FieldType = Column(Unicode(15))
    ColumnType = Column(Unicode(30))
    Format = Column(Unicode(50))
    Expression = Column(Unicode(100))
    MonetaryAmountInWords = Column(Integer)
    AllowSorting = Column(Integer)
    SortDirection = Column(Integer)
    DefaultValue = Column(Unicode(50))
    DefineLevel = Column(Integer)
    ShowSysField = Column(Integer)
    refDataSource = Column(Unicode(50))
    OriginalTitle = Column(Unicode(50))
    Width = Column(Integer)
    IsI18NField = Column(Integer)
    Visible = Column(Integer)
    ReadOnly = Column(Integer)
    AllowNull = Column(Integer)
    AllowZero = Column(Integer)
    MaxLength = Column(Integer)
    Precision = Column(Integer)
    AllowTotal = Column(Integer)
    Sizeable = Column(Integer)
    AddCopyData = Column(Integer)
    DynPropertyString = Column(Unicode(2000))
    ID = Column(Integer, primary_key=True)
    ExpressionName = Column(Unicode(60))
    ts = Column(TIMESTAMP, nullable=False)
    TableID = Column(Integer)


class EapEditTableColumnGroup(Base):
    __tablename__ = 'eap_EditTableColumnGroup'

    Name = Column(Unicode(50))
    Title = Column(Unicode(50))
    ColIndex = Column(Integer)
    Visible = Column(Integer)
    ColumnLevel = Column(Integer)
    DynPropertyString = Column(Unicode(2000))
    ts = Column(TIMESTAMP, nullable=False)
    TableID = Column(Integer)
    ColumnID = Column(Integer)
    id = Column(Integer, primary_key=True)
    ParentGroupID = Column(Integer)


class EapEnum(Base):
    __tablename__ = 'eap_Enum'

    Name = Column(Unicode(50))
    Title = Column(Unicode(200))
    Custom = Column(Integer, nullable=False, server_default=text("(0)"))
    Customuse = Column(Integer, server_default=text("(1)"))
    id = Column(Integer, primary_key=True)
    TS = Column(TIMESTAMP, nullable=False)
    Code = Column(Unicode(200))


class EapEnumItem(Base):
    __tablename__ = 'eap_EnumItem'

    Code = Column(Unicode(50))
    Name = Column(Unicode(300))
    CustomUse = Column(Integer, server_default=text("(1)"))
    IsExtend = Column(Integer, nullable=False, server_default=text("(0)"))
    IsDeleted = Column(Integer, nullable=False, server_default=text("(0)"))
    position = Column(Integer)
    ID = Column(Integer, primary_key=True)
    TS = Column(TIMESTAMP, nullable=False)
    ExpressionName = Column(Unicode(60))
    idEnum = Column(Integer, index=True)


class EapInitNavigation(Base):
    __tablename__ = 'eap_InitNavigation'

    Code = Column(Unicode(12), primary_key=True, unique=True)
    ParentCode = Column(Unicode(50), nullable=False, server_default=text("('')"))
    Title = Column(Unicode(50), nullable=False, server_default=text("('')"))
    RequestUrl = Column(Unicode(120), nullable=False, server_default=text("('')"))
    OrderNum = Column(Integer, nullable=False, server_default=text("(0)"))
    IsFinish = Column(BIT, nullable=False, server_default=text("(0)"))
    IsFreeItem = Column(BIT, nullable=False, server_default=text("(0)"))
    IsImport = Column(BIT, nullable=False, server_default=text("(0)"))
    Description = Column(Unicode(500), nullable=False, server_default=text("('')"))
    Rights = Column(Unicode(100), nullable=False, server_default=text("('Read,Operation,LookOver,OptionSettings')"))
    RightCode = Column(Unicode(12), nullable=False, server_default=text("('')"))
    FreeItemRightCode = Column(Unicode(12), nullable=False, server_default=text("('')"))
    ImportVoucherName = Column(Unicode(50), nullable=False, server_default=text("('')"))
    Visible = Column(BIT, nullable=False, server_default=text("(1)"))
    FreeItemDesc = Column(Unicode(500), nullable=False, server_default=text("('')"))
    ImportDesc = Column(Unicode(500), nullable=False, server_default=text("('')"))
    IsSystem = Column(BIT, nullable=False, server_default=text("((0))"))
    ImportIsClear = Column(BIT, nullable=False, server_default=text("((1))"))


class EapPackage(Base):
    __tablename__ = 'eap_Package'

    name = Column(Unicode(50))
    title = Column(Unicode(50))
    ns = Column(Unicode(200))
    id = Column(Integer, primary_key=True)
    TFlag = Column(Integer, server_default=text("((0))"))
    vsproj = Column(Unicode(200))
    Ts = Column(TIMESTAMP, nullable=False)
    isEndNode = Column(Integer)
    inID = Column(Unicode(600))
    idParent = Column(Integer)
    CreatedTime = Column(DateTime)


class EapUserImageInfo(Base):
    __tablename__ = 'eap_UserImageInfo'

    VoucherName = Column(Unicode(50))
    FileName = Column(Unicode(50))
    FileType = Column(Unicode(50))
    FileSize = Column(Integer)
    FileContent = Column(LargeBinary)
    Creater = Column(Unicode(50))
    CreateTime = Column(DateTime)
    TS = Column(TIMESTAMP, nullable=False)
    id = Column(Integer, primary_key=True)
    DtoID = Column(Integer)


class EapVoucher(Base):
    __tablename__ = 'eap_Voucher'

    Name = Column(Unicode(50), nullable=False)
    Title = Column(Unicode(50), nullable=False)
    DtoName = Column(Unicode(50), nullable=False)
    ColCount = Column(Integer, server_default=text("(3)"))
    VoucherStyle = Column(SmallInteger, server_default=text("(0)"))
    Left = Column(Integer)
    Top = Column(Integer)
    Width = Column(Integer)
    Height = Column(Integer)
    OrderIndex = Column(Integer, server_default=text("(0)"))
    DynPropertyString = Column(Unicode(2000))
    ID = Column(Integer, primary_key=True)
    IsAllowCopy = Column(BIT, server_default=text("((0))"))
    IsAllowDel = Column(BIT, server_default=text("((0))"))
    IsAllowEditTabs = Column(BIT, server_default=text("((0))"))
    IsAllowEditTitle = Column(BIT, server_default=text("((0))"))
    IsAllowUDI = Column(BIT, server_default=text("((1))"))
    IsAllowUDIForMultiTabs = Column(BIT, server_default=text("((0))"))
    TFlag = Column(Integer, server_default=text("((0))"))
    Ts = Column(TIMESTAMP, nullable=False)
    CreatedTime = Column(DateTime)
    ExpressionName = Column(Unicode(200))


class EapVoucherControls(Base):
    __tablename__ = 'eap_VoucherControls'

    Name = Column(Unicode(50), nullable=False)
    Title = Column(Unicode(50), nullable=False)
    TabPageName = Column(Unicode(50))
    LabelID = Column(Unicode(50))
    ControlID = Column(Unicode(50))
    Visible = Column(BIT, server_default=text("(1)"))
    AddReadOnly = Column(BIT)
    EditReadOnly = Column(BIT)
    ControlType = Column(Unicode(30))
    FieldName = Column(Unicode(50), nullable=False)
    FieldType = Column(Unicode(50))
    Left = Column(Integer)
    Top = Column(Integer)
    Width = Column(Integer, server_default=text("(220)"))
    Height = Column(Integer, server_default=text("(16)"))
    TabIndex = Column(Integer)
    CtlIndex = Column(Integer, server_default=text("(0)"))
    AllowZero = Column(BIT, server_default=text("(1)"))
    AllowNone = Column(BIT, server_default=text("(1)"))
    DefaultValue = Column(Unicode(50))
    Format = Column(Unicode(50))
    Expression = Column(Unicode(600))
    MaxLength = Column(SmallInteger)
    Precision = Column(SmallInteger)
    MaxShowLen = Column(SmallInteger)
    EnumName = Column(Unicode(50))
    RefPage = Column(Unicode(50))
    RefDTOName = Column(Unicode(50))
    RefShowField = Column(Unicode(50))
    RefLinkField = Column(Unicode(50))
    UserCheck = Column(Unicode(100))
    UserPrompt = Column(Unicode(200))
    IsUserDef = Column(BIT)
    AllowUserDef = Column(BIT)
    AllowUserDelete = Column(BIT)
    RefDataSource = Column(Unicode(50), server_default=text("('RefDtoName')"))
    ShowSysField = Column(BIT, server_default=text("(1)"))
    DropDownStyle = Column(Unicode(10))
    DropDownPanelID = Column(Unicode(50))
    OriginalTitle = Column(Unicode(50), server_default=text("('title')"))
    SysPropValue = Column(Unicode(200))
    Mustshow = Column(SmallInteger)
    AutoReDeploy = Column(SmallInteger)
    DynPropertyString = Column(Unicode(2000))
    id = Column(Integer, primary_key=True)
    RecordValue = Column(BIT)
    TS = Column(TIMESTAMP, nullable=False)
    ExpressionName = Column(Unicode(60))
    CreatedTime = Column(DateTime)
    ExpressionTips = Column(Unicode(1200))
    VoucherFieldType = Column(Integer)
    VoucherID = Column(Integer, nullable=False, index=True, server_default=text("((0))"))


class EapVoucherDesignTree(Base):
    __tablename__ = 'eap_VoucherDesignTree'

    indexOrder = Column(Integer, nullable=False)
    isSystem = Column(BIT, nullable=False, server_default=text("((0))"))
    VoucherInfoID = Column(Integer, nullable=False, server_default=text("((0))"))
    id = Column(Integer, primary_key=True)
    ModuleID = Column(Integer, nullable=False, server_default=text("((0))"))
    ExpressionName = Column(Unicode(200))


class EapVoucherModule(Base):
    __tablename__ = 'eap_VoucherModule'

    ModuleName = Column(Unicode(50), nullable=False)
    ModuleTitle = Column(Unicode(50), nullable=False)
    NodeLevel = Column(Integer, nullable=False)
    NodeIndexOrder = Column(Integer, nullable=False)
    code = Column(Unicode(8))
    id = Column(Integer, primary_key=True)
    NodeParent = Column(Integer)


class EapVoucherTab(Base):
    __tablename__ = 'eap_VoucherTab'

    Name = Column(Unicode(50))
    Title = Column(Unicode(50))
    Visible = Column(BIT)
    Enable = Column(BIT)
    FootTab = Column(BIT)
    TabIndex = Column(Integer)
    AutoReDeploy = Column(BIT, server_default=text("(1)"))
    DynPropertyString = Column(Unicode(2000))
    id = Column(Integer, primary_key=True)
    OriginalTitle = Column(Unicode(50))
    IsAllowUDI = Column(BIT, server_default=text("((1))"))
    CreatedTime = Column(DateTime)
    ts = Column(TIMESTAMP, nullable=False)
    VoucherID = Column(Integer)


class EapVoucherTable(Base):
    __tablename__ = 'eap_VoucherTable'

    Name = Column(Unicode(50), nullable=False)
    Title = Column(Unicode(50), nullable=False)
    DtoName = Column(Unicode(50))
    ParentFieldName = Column(Unicode(50), nullable=False)
    ChildFieldName = Column(Unicode(50))
    TabIndex = Column(Integer)
    Visible = Column(BIT)
    AllowAdd = Column(BIT)
    AllowDelete = Column(BIT)
    ReadOnly = Column(BIT)
    AllowSortting = Column(BIT)
    ColumnMoveable = Column(BIT)
    ColumnSizeable = Column(BIT)
    RowHeaderVisible = Column(BIT)
    TotalRowVisible = Column(BIT)
    StatusBarVisible = Column(BIT)
    TableType = Column(Unicode(50), server_default=text("('Table')"))
    ParentTable = Column(Unicode(50), server_default=text("('Table')"))
    DynPropertyString = Column(Unicode(2000))
    ID = Column(Integer, primary_key=True)
    OriginalTitle = Column(Unicode(50))
    CreatedTime = Column(DateTime)
    Expression = Column(Unicode(600))
    ExpressionName = Column(Unicode(60))
    ts = Column(TIMESTAMP, nullable=False)
    VoucherID = Column(Integer, nullable=False, server_default=text("((0))"))


class EapVoucherTableColumn(Base):
    __tablename__ = 'eap_VoucherTableColumn'

    Name = Column(Unicode(50), nullable=False)
    Title = Column(Unicode(50), nullable=False)
    ColIndex = Column(SmallInteger)
    Width = Column(Integer, server_default=text("(80)"))
    FieldName = Column(Unicode(50), nullable=False)
    FieldType = Column(Unicode(15))
    IsI18NField = Column(BIT)
    ColumnType = Column(Unicode(30))
    Visible = Column(BIT, server_default=text("(1)"))
    ReadOnly = Column(BIT, server_default=text("(1)"))
    AllowNull = Column(BIT, server_default=text("(1)"))
    AllowZero = Column(BIT, server_default=text("(1)"))
    MaxLength = Column(SmallInteger, server_default=text("(14)"))
    Precision = Column(SmallInteger, server_default=text("(3)"))
    AllowTotal = Column(BIT, server_default=text("(1)"))
    Format = Column(Unicode(50))
    Expression = Column(Unicode(600))
    MonetaryAmountInWords = Column(BIT)
    AllowSorting = Column(BIT)
    SortDirection = Column(SmallInteger)
    Sizeable = Column(BIT, server_default=text("(1)"))
    AddCopyData = Column(BIT, server_default=text("(0)"))
    DefaultValue = Column(Unicode(50))
    EnumName = Column(Unicode(50))
    RefPage = Column(Unicode(110))
    RefDtoName = Column(Unicode(50))
    RefShowField = Column(Unicode(50))
    RefLinkField = Column(Unicode(50))
    UserCheck = Column(Unicode(100))
    UserPrompt = Column(Unicode(200))
    IsUserDef = Column(BIT)
    AllowUserDef = Column(BIT)
    AllowUserDelete = Column(BIT)
    refDataSource = Column(Unicode(50), server_default=text("('RefDtoName')"))
    ShowSysField = Column(BIT, server_default=text("(1)"))
    DropDownStyle = Column(Unicode(10))
    DropDownPanelID = Column(Unicode(50))
    SysPropValue = Column(Unicode(200))
    Mustshow = Column(SmallInteger)
    OriginalTitle = Column(Unicode(50), server_default=text("('title')"))
    DynPropertyString = Column(Unicode(2000))
    id = Column(Integer, primary_key=True)
    TS = Column(TIMESTAMP, nullable=False)
    ExpressionName = Column(Unicode(60))
    CreatedTime = Column(DateTime)
    ExpressionTips = Column(Unicode(1200))
    VoucherFieldType = Column(Integer)
    VoucherID = Column(Integer, nullable=False, index=True, server_default=text("((0))"))
    TableID = Column(Integer, nullable=False, index=True, server_default=text("((0))"))


class EapVoucherTableColumnGroup(Base):
    __tablename__ = 'eap_VoucherTableColumnGroup'

    Name = Column(Unicode(50))
    Title = Column(Unicode(50))
    ColIndex = Column(Integer)
    Visible = Column(Integer)
    ColumnLevel = Column(Integer)
    ID = Column(Integer, primary_key=True)
    ts = Column(TIMESTAMP, nullable=False)
    TableID = Column(Integer)
    ColumnID = Column(Integer)
    ParentGroupID = Column(Integer)


class EapVoucherWebControls(Base):
    __tablename__ = 'eap_VoucherWebControls'

    Name = Column(Unicode(50))
    Text = Column(Unicode(500))
    Left = Column(Integer)
    Top = Column(Integer)
    Width = Column(Integer)
    Height = Column(Integer)
    ControlType = Column(Unicode(50))
    Parent = Column(Unicode(50))
    DynPropertyString = Column(Unicode(2000))
    ts = Column(TIMESTAMP, nullable=False)
    VoucherID = Column(Integer)
    id = Column(Integer, primary_key=True)


class EapAttachmentinfo(Base):
    __tablename__ = 'eap_attachmentinfo'

    TemplateName = Column(Unicode(100))
    DTOProp = Column(Unicode(200))
    AssociateID = Column(Unicode(100))
    FileName = Column(Unicode(100), nullable=False)
    FileType = Column(Unicode(10), nullable=False)
    FileContent = Column(LargeBinary, server_default=text("(0x)"))
    FileSize = Column(BigInteger, nullable=False)
    UploadPath = Column(Unicode(200))
    Creater = Column(Unicode(50), nullable=False)
    ViewCount = Column(Integer, server_default=text("((0))"))
    DownloadCount = Column(Integer, server_default=text("((0))"))
    TS = Column(TIMESTAMP, nullable=False)
    id = Column(Integer, primary_key=True)
    CreateTime = Column(DateTime)


class EapChartoption(Base):
    __tablename__ = 'eap_chartoption'

    ts = Column(TIMESTAMP, nullable=False)
    name = Column(Unicode(200), nullable=False)
    SolutionID = Column(Unicode(200))
    ChartTitle = Column(Unicode(200))
    XClassTitle = Column(Unicode(200))
    YClassTitle = Column(Unicode(200))
    ShowXClass = Column(Integer, server_default=text("((1))"))
    ShowYClass = Column(Integer, server_default=text("((1))"))
    ShowChartPer = Column(Integer, server_default=text("((1))"))
    Width = Column(Integer)
    Height = Column(Integer)
    ShowTypeTitle = Column(Integer)
    ShowSeriesTitle = Column(Integer)
    LegendPos = Column(Integer)
    ShowSeriesValue = Column(Integer)
    ShowGroupItem = Column(Integer)
    ChartType = Column(Integer)
    DynPropertyString = Column(Unicode(2000))
    IsshowTrend = Column(Integer)
    id = Column(Integer, primary_key=True)


class EapDesignDTOLog(Base):
    __tablename__ = 'eap_designDTOLog'

    DtoName = Column(Unicode(200))
    tablename = Column(Unicode(200))
    sqltext = Column(Unicode(4000))
    code = Column(Unicode(32))
    name = Column(Unicode(60))
    ts = Column(TIMESTAMP, nullable=False)
    createtime = Column(DateTime)
    ID = Column(Integer, primary_key=True)
    idDTO = Column(Integer)


class EapExternalaccountbinding(Base):
    __tablename__ = 'eap_externalaccountbinding'

    ts = Column(TIMESTAMP, nullable=False)
    updatedBy = Column(Unicode(32))
    name = Column(Unicode(200), nullable=False)
    Source = Column(Unicode(100), nullable=False)
    Account = Column(Unicode(100), nullable=False)
    Password = Column(Unicode(100))
    UserId = Column(Unicode(100))
    DogId = Column(Unicode(100))
    id = Column(Integer, primary_key=True)
    updated = Column(DateTime)


class EapIdesktopappitem(Base):
    __tablename__ = 'eap_idesktopappitem'

    ts = Column(TIMESTAMP, nullable=False)
    name = Column(Unicode(50), nullable=False)
    Url = Column(Unicode(512))
    Icon = Column(Unicode(256))
    Width = Column(Integer)
    Height = Column(Integer)
    Description = Column(Unicode(200))
    MenuCode = Column(Unicode(24))
    LinkUrl = Column(Unicode(512))
    id = Column(Integer, primary_key=True)
    AppSourceType = Column(Integer)
    AppType = Column(Integer)
    SourceId = Column(Integer)


class EapIdesktopshortcut(Base):
    __tablename__ = 'eap_idesktopshortcut'

    ts = Column(TIMESTAMP, nullable=False)
    name = Column(Unicode(200))
    Url = Column(Unicode(512))
    OrderNum = Column(Integer, server_default=text("((0))"))
    Icon = Column(Unicode(200))
    MenuCode = Column(Unicode(24))
    id = Column(Integer, primary_key=True)
    ShortcutType = Column(Integer)
    ideap_idesktopappitem = Column(Integer)


class EapIdesktopsolution(Base):
    __tablename__ = 'eap_idesktopsolution'

    ts = Column(TIMESTAMP, nullable=False)
    name = Column(Unicode(200), nullable=False)
    IsSystem = Column(Integer)
    id = Column(Integer, primary_key=True)
    RoleType = Column(Integer)
    RoleId = Column(Integer)


class EapIdesktopsolutionitem(Base):
    __tablename__ = 'eap_idesktopsolutionitem'

    ts = Column(TIMESTAMP, nullable=False)
    name = Column(Unicode(200))
    LeftPos = Column(Integer)
    TopPos = Column(Integer)
    Width = Column(Integer)
    Height = Column(Integer)
    Page = Column(Integer)
    id = Column(Integer, primary_key=True)
    ideap_idesktopappitem = Column(Integer)
    ideap_idesktopsolution = Column(Integer)


class EapIdesktopsystemshortcut(Base):
    __tablename__ = 'eap_idesktopsystemshortcut'

    ts = Column(TIMESTAMP, nullable=False)
    name = Column(Unicode(200), nullable=False)
    Url = Column(Unicode(200))
    OrderNum = Column(Integer)
    MenuCode = Column(Unicode(24))
    Icon = Column(Unicode(200))
    id = Column(Integer, primary_key=True)
    ShortcutType = Column(Integer)


t_eap_printbussetting = Table(
    'eap_printbussetting', metadata,
    Column('id', Integer, nullable=False),
    Column('ts', TIMESTAMP, nullable=False),
    Column('name', Unicode(200)),
    Column('code', Unicode(32)),
    Column('UserId', Integer),
    Column('TemplateId', Integer),
    Column('printdirname', Unicode(200)),
    Column('clientName', Unicode(400)),
    Column('printerName', Unicode(400)),
    Column('PageCopies', Integer, server_default=text("((1))")),
    Column('PrintAllPage', Integer, server_default=text("((1))")),
    Column('PrintPageRange', Unicode(200)),
    Column('PrintType', Integer, server_default=text("((1))")),
    Column('PrintDirection', Integer, server_default=text("((1))")),
    Column('CopiesSpacing', Integer, server_default=text("((0))")),
    Column('PrintSeparator', Integer, server_default=text("((0))")),
    Column('Collated', Integer, server_default=text("((1))")),
    Column('PrintNum', Integer, server_default=text("((1))")),
    Column('PageVouchers', Integer, server_default=text("((1))")),
    Column('RowsAdaptive', Integer, server_default=text("((1))")),
    Column('FillBlankRows', Integer, server_default=text("((0))")),
    Column('FixRows', Integer),
    Column('Printpaper', Unicode(200)),
    Column('margin', Unicode(200)),
    Column('BarcodeType', Unicode(200)),
    Column('PerRows', Integer, server_default=text("((1))")),
    Column('LabelSpacings', Unicode(200)),
    Column('DynPropertyString', UnicodeText(1073741823)),
    Column('SetUrl', Unicode(400)),
    Column('PrintClass', Unicode(400)),
    Column('NumRows', Integer),
    Column('AutoRows', Integer, server_default=text("((0))")),
    Column('PrintCfgJson', Unicode(4000))
)


class EapPrintdir(Base):
    __tablename__ = 'eap_printdir'

    ts = Column(TIMESTAMP)
    title = Column(Unicode(100), nullable=False)
    name = Column(Unicode(100), nullable=False)
    DtoName = Column(Unicode(50))
    DynPropertyString = Column(Unicode(1000))
    id = Column(Integer, primary_key=True)
    SolutionType = Column(Integer)
    idprintoption = Column(Integer)


class EapPrinttemplate(Base):
    __tablename__ = 'eap_printtemplate'

    title = Column(Unicode(100), nullable=False)
    isDefault = Column(Integer)
    isBackup = Column(Integer)
    name = Column(Unicode(100), nullable=False)
    templateType = Column(Integer)
    fileName = Column(Unicode(100))
    content = Column(LargeBinary)
    validCode = Column(Unicode(32))
    ts = Column(TIMESTAMP)
    vxml = Column(UnicodeText(1073741823))
    isSelect = Column(Integer, nullable=False, server_default=text("((1))"))
    DynPropertyString = Column(Unicode(1000))
    id = Column(Integer, primary_key=True)
    IdPrintDir = Column(Integer)
    IdPrintSetting = Column(Integer)
    isLocked = Column(Integer)
    idUser = Column(Integer)
    IsNewPrint = Column(BIT)
    hooffset = Column(Unicode(20))
    veoffset = Column(Unicode(20))
    describe = Column(Unicode(800))


class EapReportfield(Base):
    __tablename__ = 'eap_reportfield'
    __table_args__ = (
        Index('IDX_eap_ReportField_ideapreporttemplateAndaliasName', 'ideap_reporttemplate', 'aliasName'),
    )

    title = Column(Unicode(50))
    selectFieldName = Column(Unicode(200))
    aliasName = Column(Unicode(200))
    whereFieldName = Column(Unicode(200))
    isBundleField = Column(Integer)
    isMain = Column(Integer)
    canGroup = Column(Integer)
    defaultGroup = Column(Integer)
    canClassiced = Column(Integer)
    canLinkage = Column(Integer)
    canRowGroup = Column(Integer)
    defaultRowGroup = Column(Integer)
    canColumnGroup = Column(Integer)
    isMultiLevelGroup = Column(Integer, server_default=text("(0)"))
    parentDataField = Column(Unicode(200))
    isColumn = Column(Integer)
    lastLevelIdentifyField = Column(Unicode(200))
    dtoprop = Column(Unicode(100))
    RefDtoProp = Column(Unicode(200))
    StaticGroup = Column(Integer)
    id = Column(Integer, primary_key=True)
    IsColSpan = Column(Integer)
    ts = Column(TIMESTAMP, nullable=False)
    idparent = Column(Integer)
    ideap_reporttemplate = Column(Integer)
    CreatedTime = Column(DateTime)


class EapReportsolution(Base):
    __tablename__ = 'eap_reportsolution'

    name = Column(Unicode(200))
    isPublic = Column(Integer, server_default=text("(1)"))
    isDefault = Column(Integer)
    isSum = Column(Integer)
    isUseUrl = Column(Integer)
    userdefined = Column(Unicode(800))
    isGroupSum = Column(Integer)
    id = Column(Integer, primary_key=True)
    SearchName = Column(Unicode(50))
    IsShowThousandsSeparator = Column(Integer)
    IsShowZeroValue = Column(Integer)
    IsRepeatTableHeader = Column(Integer)
    IsRepeatTableFooter = Column(Integer)
    IsRepeatPageHeader = Column(Integer)
    IsRepeatPageFooter = Column(Integer)
    ReportTitle = Column(Unicode(100))
    OriginalReportTitle = Column(Unicode(100))
    ChartPercent = Column(Integer)
    ExpressionName = Column(Unicode(60))
    TFlag = Column(Integer, server_default=text("((0))"))
    ts = Column(TIMESTAMP, nullable=False)
    searchPlanName = Column(Unicode(200))
    ideap_reportpageset = Column(Integer)
    idSearchPlan = Column(Integer)
    idFromSolution = Column(Integer)
    ideap_reporttemplate = Column(Integer)
    ideap_Search = Column(Integer)
    idUser = Column(Integer)
    CreatedTime = Column(DateTime)


class EapReporttablecol(Base):
    __tablename__ = 'eap_reporttablecol'
    __table_args__ = (
        Index('IDX_eap_ReportTablecol_ideapreportsolutionAndfieldname', 'ideap_reportsolution', 'fieldName'),
    )

    title = Column(Unicode(200))
    fieldName = Column(Unicode(100))
    selectFieldName = Column(Unicode(200))
    mustDisplay = Column(Integer)
    canDisplay = Column(Integer)
    Display = Column(Integer, nullable=False, server_default=text("(1)"))
    ShowIndex = Column(Integer, nullable=False, server_default=text("(0)"))
    FixedHeader = Column(Integer, nullable=False, server_default=text("(0)"))
    TotalSum = Column(Integer, nullable=False, server_default=text("(0)"))
    CanSum = Column(Integer)
    UserSort = Column(Integer, nullable=False, server_default=text("(0)"))
    width = Column(Float(53))
    style = Column(Unicode(1000))
    format = Column(Unicode(100))
    linkurl = Column(Unicode(1500))
    BundleField = Column(Unicode(100))
    IsMain = Column(Integer)
    IsHeader = Column(Integer)
    OriginalTitle = Column(Unicode(200))
    SqlSort = Column(Integer)
    outputValue = Column(Unicode(2000))
    dtoprop = Column(Unicode(100))
    RefDtoProp = Column(Unicode(400))
    linkTitle = Column(Unicode(50))
    tooltip = Column(Unicode(400))
    isbundle = Column(Integer)
    IsDynamicCol = Column(Integer)
    isFormatCtrlBySys = Column(Integer)
    GroupOutputValue = Column(Unicode(4000))
    FootOutputValue = Column(Unicode(4000))
    hideZeroValue = Column(Integer)
    dataType = Column(Integer)
    isGather = Column(Integer)
    titleAlign = Column(Integer, server_default=text("((-1))"))
    bodyAlign = Column(Integer, server_default=text("((-1))"))
    id = Column(Integer, primary_key=True)
    IsShowChart = Column(Integer)
    IsNegNumShowSign = Column(Integer)
    outputTitle = Column(Unicode(100))
    ExpressionName = Column(Unicode(60))
    CanVRatio = Column(Integer)
    CanHRatio = Column(Integer)
    IsVRatio = Column(Integer)
    IsHRatio = Column(Integer)
    IsRefBaseInfoCol = Column(Integer)
    TFlag = Column(Integer, server_default=text("((0))"))
    ControlledKey = Column(Unicode(200))
    ts = Column(TIMESTAMP, nullable=False)
    name = Column(Unicode(200))
    ideap_reportsolution = Column(Integer)
    idparent = Column(Integer)
    FootOutputSql = Column(Unicode(4000))
    CreatedTime = Column(DateTime)


class EapReporttemplate(Base):
    __tablename__ = 'eap_reporttemplate'

    title = Column(Unicode(100))
    name = Column(Unicode(200), nullable=False)
    reportType = Column(Integer)
    menuCode = Column(Unicode(100))
    dbsql = Column(UnicodeText(1073741823))
    reportStyle = Column(Integer)
    id = Column(Integer, primary_key=True)
    MainEntity = Column(Unicode(200))
    IsHasChart = Column(Integer)
    IsToggleFilter = Column(Integer)
    IsMatrixSum = Column(Integer)
    IsHasDynCol = Column(Integer)
    ExpressionName = Column(Unicode(60))
    TFlag = Column(Integer, server_default=text("((0))"))
    ts = Column(TIMESTAMP, nullable=False)
    DisplayStyle = Column(Integer)
    NegativeFormat = Column(Integer)
    ReportTypeNew = Column(Integer)
    CreatedTime = Column(DateTime)


class EapUserdefinearticledict(Base):
    __tablename__ = 'eap_userdefinearticledict'

    ts = Column(TIMESTAMP, nullable=False)
    name = Column(Unicode(50), nullable=False)
    code = Column(Unicode(64), nullable=False)
    Title = Column(Unicode(120), nullable=False)
    TableName = Column(Unicode(50), nullable=False)
    ClassForeignField = Column(Unicode(50))
    ParentField = Column(Unicode(50))
    IsAutoCreate = Column(Integer, nullable=False)
    IsSystem = Column(Integer, nullable=False)
    IsDefault = Column(Integer)
    IsDisplay = Column(Integer, nullable=False)
    menuCode = Column(Unicode(12))
    menuParentCode = Column(Unicode(12))
    className = Column(Unicode(200))
    id = Column(Integer, primary_key=True)
    ExtendTable = Column(Unicode(400))
    ScriptPath = Column(Unicode(200))
    ExtendAssembly = Column(Unicode(400))
    StructType = Column(Integer, nullable=False, server_default=text("((0))"))
    IdParent = Column(Integer)
    ClassArticleId = Column(Integer)
    MadeDate = Column(DateTime)
    ModifiedDate = Column(DateTime)


class EapWfauditlog(Base):
    __tablename__ = 'eap_wfauditlog'
    __table_args__ = (
        Index('IDX_eap_wfauditlog_BizCode_EntityID', 'BizCode', 'EntityID'),
        Index('IDX_eap_wfauditlog_BizCode_EntityID_IsCurrent', 'BizCode', 'EntityID', 'IsCurrent')
    )

    ts = Column(TIMESTAMP, nullable=False)
    updatedBy = Column(Unicode(32))
    BizCode = Column(Unicode(60))
    EntityCode = Column(Unicode(60))
    Opinion = Column(Unicode(200))
    AuditAction = Column(Integer)
    AuditorName = Column(Unicode(100))
    IsCurrent = Column(Integer)
    id = Column(Integer, primary_key=True)
    AuditorID = Column(Integer)
    EntityID = Column(Integer)
    SolutionID = Column(Integer)
    updated = Column(DateTime)
    AuditTime = Column(DateTime)


class EapWfinprocess(Base):
    __tablename__ = 'eap_wfinprocess'
    __table_args__ = (
        Index('IDX_eap_wfinprocess_BizCode_EntityID', 'BizCode', 'EntityID'),
    )

    ts = Column(TIMESTAMP, nullable=False)
    updatedBy = Column(Unicode(32))
    BizCode = Column(Unicode(200))
    EntityCode = Column(Unicode(60))
    ProcessStatus = Column(Integer)
    id = Column(Integer, primary_key=True)
    EntityID = Column(Integer)
    SolutionID = Column(Integer)
    updated = Column(DateTime)


class EapWfnode(Base):
    __tablename__ = 'eap_wfnode'

    Title = Column(Unicode(200))
    AuditType = Column(Integer, nullable=False)
    ts = Column(TIMESTAMP, nullable=False)
    updatedBy = Column(Unicode(32))
    PositionX = Column(Integer)
    PositionY = Column(Integer)
    CanFinal = Column(Integer)
    NodeType = Column(Integer)
    MailRuleID = Column(Integer)
    FinalConditionPlanID = Column(Integer)
    id = Column(Integer, primary_key=True)
    SolutionID = Column(Integer)
    MsgRuleID = Column(Integer)
    updated = Column(DateTime)


class EapWfperformer(Base):
    __tablename__ = 'eap_wfperformer'

    PerformerType = Column(Integer, nullable=False)
    ts = Column(TIMESTAMP, nullable=False)
    updatedBy = Column(Unicode(32))
    PerformerValue = Column(Unicode(200))
    id = Column(Integer, primary_key=True)
    NodeID = Column(Integer)
    updated = Column(DateTime)


class EapWfroute(Base):
    __tablename__ = 'eap_wfroute'

    ts = Column(TIMESTAMP, nullable=False)
    updatedBy = Column(Unicode(32))
    LineStyle = Column(Integer)
    Description = Column(Unicode(200))
    id = Column(Integer, primary_key=True)
    ConditionPlanID = Column(Integer)
    CurNodeID = Column(Integer)
    NextNodeID = Column(Integer)
    SolutionID = Column(Integer)
    updated = Column(DateTime)


class EapWfsolution(Base):
    __tablename__ = 'eap_wfsolution'

    Title = Column(Unicode(200), nullable=False)
    BizCode = Column(Unicode(60))
    ts = Column(TIMESTAMP, nullable=False)
    updatedBy = Column(Unicode(32))
    ID = Column(Integer, primary_key=True)
    CreateUserID = Column(Integer)
    updated = Column(DateTime)
    CreateTime = Column(DateTime)


class EapWftask(Base):
    __tablename__ = 'eap_wftask'
    __table_args__ = (
        Index('IDX_eap_wftask_BizCode_EntityID_NodeID_TaskStatus', 'BizCode', 'EntityID', 'NodeID', 'TaskStatus'),
        Index('IDX_eap_wftask_BizCode_EntityID_TaskStatus', 'BizCode', 'EntityID', 'TaskStatus'),
        Index('IDX_eap_wftask_BizCode_EntityID_UserID', 'BizCode', 'EntityID', 'TaskStatus')
    )

    BizCode = Column(Unicode(60))
    EntityCode = Column(Unicode(60))
    Content = Column(Unicode(200))
    updatedBy = Column(Unicode(32))
    ts = Column(TIMESTAMP, nullable=False)
    TaskStatus = Column(Integer, nullable=False)
    id = Column(Integer, primary_key=True)
    UserID = Column(Integer)
    AuditLogID = Column(Integer)
    NodeID = Column(Integer)
    PreNodeID = Column(Integer)
    SolutionID = Column(Integer)
    EntityID = Column(Integer)
    updated = Column(DateTime)
    CreateTime = Column(DateTime)


class SmConfig(Base):
    __tablename__ = 'sm_config'

    ts = Column(TIMESTAMP, nullable=False)
    updatedBy = Column(Unicode(32))
    name = Column(Unicode(200), nullable=False)
    ModuleName = Column(Unicode(50), nullable=False)
    AssemblyName = Column(Unicode(200), nullable=False)
    ClassName = Column(Unicode(200), nullable=False)
    id = Column(Integer, primary_key=True)
    ConfigType = Column(Integer)
    updated = Column(DateTime)


t_sm_fc_accountextendrulecolumn_bak = Table(
    'sm_fc_accountextendrulecolumn_bak', metadata,
    Column('id', UNIQUEIDENTIFIER, nullable=False),
    Column('code', Unicode(30)),
    Column('name', Unicode(200)),
    Column('accountruletype', UNIQUEIDENTIFIER),
    Column('geneaccountbytype', UNIQUEIDENTIFIER),
    Column('idx', Integer),
    Column('isdisplay', Integer),
    Column('iscombin', Integer),
    Column('displayname', Unicode(50)),
    Column('ismatchby', Integer),
    Column('issystemhidden', Integer),
    Column('baseinfo', Unicode(50)),
    Column('idfieldname', Unicode(50)),
    Column('idedittablecolumn', UNIQUEIDENTIFIER),
    Column('sequencenumber', Integer),
    Column('ts', TIMESTAMP, nullable=False),
    Column('updatedBy', Unicode(32)),
    Column('createdtime', DateTime),
    Column('updated', DateTime)
)


t_sm_fc_bookformatrelation = Table(
    'sm_fc_bookformatrelation', metadata,
    Column('ts', TIMESTAMP, nullable=False),
    Column('updatedBy', Unicode(32)),
    Column('name', Unicode(200)),
    Column('code', Unicode(32)),
    Column('id', Integer, nullable=False),
    Column('bookFormat', Integer),
    Column('idEap_PrintTemplate', Integer),
    Column('updated', DateTime),
    Column('madeDate', DateTime),
    Column('createdTime', DateTime)
)


class SmMessageruleuser(Base):
    __tablename__ = 'sm_messageruleuser'

    bizcode = Column(Unicode(100), nullable=False)
    isopensend = Column(Integer, server_default=text("((1))"))
    gzq = Column(BIT, server_default=text("((1))"))
    id = Column(Integer, primary_key=True)
    userid = Column(Integer, nullable=False, server_default=text("((0))"))
    ruleID = Column(Integer, nullable=False, server_default=text("((0))"))


class SmOptexpression(Base):
    __tablename__ = 'sm_optexpression'

    ExpressionName = Column(Unicode(200), nullable=False)
    TableName = Column(Unicode(200), nullable=False)
    ColumnName = Column(Unicode(200), nullable=False)
    ExpressionValue = Column(Unicode(500))
    id = Column(Integer, primary_key=True)
    ExpressionType = Column(Unicode(50))
    ExpressionWhere = Column(Unicode(500))
    ExceptionStatus = Column(Unicode(100))


class SmVouchermessagesendtime(Base):
    __tablename__ = 'sm_vouchermessagesendtime'

    ts = Column(TIMESTAMP, nullable=False)
    id = Column(Integer, primary_key=True)
    SendTime = Column(Integer)
    idSM_VoucherMessageRule = Column(Integer)
    updated = Column(DateTime)


class StCheckvoucherBRelation(Base):
    __tablename__ = 'st_checkvoucher_b_relation'

    ts = Column(TIMESTAMP, nullable=False)
    name = Column(Unicode(200), nullable=False)
    code = Column(Unicode(32), nullable=False)
    id = Column(Integer, primary_key=True)
    CheckVoucherID = Column(Integer, nullable=False, server_default=text("((0))"))
    SelectedDetailID = Column(Integer, nullable=False, server_default=text("((0))"))
    updated = Column(DateTime)


class StMarketingorganinvprice(Base):
    __tablename__ = 'st_marketingorganinvprice'

    latestCost = Column(Numeric(28, 14))
    avagCost = Column(Numeric(28, 14))
    ts = Column(TIMESTAMP, nullable=False)
    id = Column(Integer, primary_key=True)
    idInventory = Column(Integer, index=True)
    idMarketingOrgan = Column(Integer, index=True)


class StSafestocksetting(Base):
    __tablename__ = 'st_safestocksetting'

    code = Column(Unicode(32))
    safeQuantity = Column(Numeric(28, 14))
    topQuantity = Column(Numeric(28, 14))
    lowQuantity = Column(Numeric(28, 14))
    replenishmentLeadTime = Column(Integer)
    replenishmentSalesDays = Column(Integer)
    updatedBy = Column(Unicode(32))
    ts = Column(TIMESTAMP, nullable=False)
    id = Column(Integer, primary_key=True)
    idinventory = Column(Integer, index=True)
    idunit = Column(Integer)
    idwarehouse = Column(Integer, index=True)
    updated = Column(DateTime)
