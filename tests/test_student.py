from student.student import Student, get_student_with_more_classes

def test_init():
    name = "Ada Lovelace"
    level = "sophomore"
    courses = ["mathematics", "foundations of computing"]

    name2 = "Ada Lovelace"
    level2 = "sophomore"
    courses2 = []

    ada = Student(name, level, courses)
    ada2 = Student(name2, level2, courses2)

    assert ada.name == name
    assert ada.level == level
    assert ada.courses == courses

    assert ada2.name == name2
    assert ada2.level == level2
    assert ada2.courses == courses2


def test_add_class():
    new_class = 'Intro to Feminism'
    charles = Student("Charles Babbage", "senior", ["mechanical engineering"])
    charles.add_class(new_class)

    assert len(charles.courses) == 2
    assert new_class in charles.courses

def test_get_num_classes():
    george = Student("George Byron", "senior", ["advanced poetry"])

    assert george.get_num_classes() == 1

def test_summary():
    anne = Student(
        "Anne Byron",
        "senior",
        ["theory of religion", "theory of morality"]
    )

    assert anne.summary() == "Anne Byron is a senior enrolled in 2 classes"

def test_get_student_with_more_classes():
    charles = Student("Charles Babbage", "senior", ["mechanical engineering"])
    ada = Student(
        "Ada Lovelace",
        "sophomore",
        ["mathematics", "foundations of computing"]
    )
    
    result = get_student_with_more_classes(charles, ada)
    result_2 = get_student_with_more_classes(ada, charles)

    assert result == ada
    assert result_2 == ada
    # TODO: write assertions
