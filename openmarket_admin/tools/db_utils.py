# 连接数据库 做数据操作的工具类
import pymysql


# 数据库配置信息
class DBConfig:
    HOST = "127.0.0.1"  # 数据库连接ip地址
    PORT = 3306  # 数据库端口号
    USER = "root"  # 数据库登录用户名
    PASSWORD = "123456"  # 数据库登录密码
    DB_NAME = "mms"  # 要连接的具体数据库名


# 数据库操作基础工具类
class DbUtils:
    __conn = None  # 连接通道对象
    __cur = None  # 游标对象

    @classmethod
    def __getConnection(cls):
        '''
        获取连接通道
        :return:
        '''
        cls.__conn = pymysql.Connection(host=DBConfig.HOST,
                                        port=DBConfig.PORT,
                                        user=DBConfig.USER,
                                        password=DBConfig.PASSWORD,
                                        db=DBConfig.DB_NAME)

    @classmethod
    def __getCursor(cls):
        '''
        创建游标
        :return:
        '''
        cls.__cur = cls.__conn.cursor()

    @classmethod
    def __closeCursor(cls):
        '''
        关闭游标
        :return:
        '''
        cls.__cur.close()

    @classmethod
    def __closeConn(cls):
        '''
        关闭通道
        :return:
        '''
        cls.__conn.close()

    @classmethod
    def executeSql(cls, sqlStr):
        '''
        执行增，删，改sql语句的方法
        :param sqlStr:
        :return:
        '''
        res = None
        # 1 连接通道
        cls.__getConnection()
        # 2 创建游标
        cls.__getCursor()
        # 3 执行sql - 查询 - 增删改
        sqlStr = sqlStr.strip().lower()  # 去除sql字符串两端空格
        try:
            res = cls.__cur.execute(sqlStr)
            # 提取操作关键字
            oper = sqlStr.split(" ")[0]
            # 4 如果是增删改 - 提交 或 回滚
            if oper != "select":
                cls.__conn.commit()
            if oper == "select":  # 如果sql语句是查询
                res = cls.__cur.fetchall()  # 取出所有结果集记录
        except Exception as e:
            print(e)
            print("[ERROR-SQL]:", sqlStr)
        finally:
            cls.__closeCursor()  # 关闭游标对象
            cls.__getConnection()  # 关闭通道对象
        # 5 返回结果
        return res

    @classmethod
    def fetchOne(cls, sqlStr):
        '''
        执行查询语句 返回一行结果记录的方法
        :param sqlStr:
        :return:
        '''
        res = cls.executeSql(sqlStr)
        if res != None:
            return res[0]
        return res[0]

    @classmethod
    def fetchAll(cls, sqlStr):
        '''
        执行查询 返回所有结果记录的方法
        :param sqlStr:
        :return:
        '''
        return cls.executeSql()

    @classmethod
    def fetchOneCell(cls, sqlStr):
        '''
        执行查询，返回第一行中第一个单元格中的数据
        :param sqlStr:
        :return:
        '''
        res = cls.fetchOne(sqlStr)
        if res != None:
            return res[0]
