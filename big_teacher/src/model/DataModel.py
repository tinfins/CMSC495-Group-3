from dataclasses import dataclass

'''
@property is getter method
getter use: Class.attribute
@attribute.setter is setter method
setter use: Class.attribute = attribute
dataclass(frozen=True) is immutable
'''


@dataclass
class SettingsModel:
    '''
    Data class for settings objects
    
    '''
    _dialect: str
    _username: str
    _password: str
    _host: str
    _port: str
    _db_name: str
    
    @property
    def dialect(self):
        return self._dialect
    
    @dialect.setter
    def dialect(self, dialect):
        self._dialect = dialect
    
    @property
    def username(self):
        return self._username
    
    @username.setter
    def username(self, username):
        self._username = username
    
    @property
    def password(self) -> str:
        return self._password
    
    @password.setter
    def password(self, password):
        self._password = password
    
    @property
    def host(self) -> str:
        return self._host
    
    @host.setter
    def host(self, host):
        self._host = host
    
    @property
    def port(self) -> str:
        return self._port
    
    @port.setter
    def port(self, port):
        self._port = port
    
    @property
    def db_name(self) -> str:
        return self._db_name
    
    @db_name.setter
    def db_name(self, db_name):
        self._db_name = db_name

@dataclass(frozen=True)
class StudentModel:
    '''
    Data class for student objects
    '''
    # Slots improves memory usage
    # https://docs.python.org/reference/datamodel.html#slots
    __slots__ = ['student_id', 'fname', 'lname']
    student_id: int
    fname: str
    lname: str
    
@dataclass(frozen=True)
class ProfessorModel:
    __slots__ = ['prof_id', 'prof_fname', 'prof_lname', 'prof_email']
    prof_id: int
    prof_fname: str
    prof_lname: str
    prof_email: str

@dataclass
class CourseModel:
    course_id: int
    name: str
    start_date: str
    end_date: str

@dataclass
class StudentToCourseModel:
    student_takes_id: int
    student_id: int
    course_id: int

@dataclass
class TeacherToCourse:
    prof_id: int
    course_id: int

@dataclass
class Assignments:
    student_takes_id: int
    test_1: int
    homework_1: int

'''
stu_model = StudentModel('1', 'Jay', 'White')
#stu_model('1', 'Jay', 'White')
print(stu_model._fname)
print(stu_model.fname)
stu_model.fname = 'Turd'
print(stu_model.fname)
#stu_model.set
'''
