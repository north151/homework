package com.kzl.service.impl;

import com.kzl.dao.ManageMapper;
import com.kzl.dao.StudentMapper;
import com.kzl.dao.TeacherMapper;
import com.kzl.entity.*;
import com.kzl.service.TeacherService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class TeacherServiceImpl implements TeacherService {

    @Autowired
    private TeacherMapper teacherMapper;
    @Autowired
    private StudentMapper studentMapper;

    @Autowired
    private ManageMapper manageMapper;

    @Override
    public List<Menu> queryUserRoleMenu(String roleId) {
        List<Menu> menus = manageMapper.selectFirstMenuByRoleId(roleId,"0");
        for(Menu menu:menus){
            List<Menu> menuSecond = manageMapper.selectFirstMenuByRoleId(roleId,menu.getId());
            menu.setMenus(menuSecond);
        }
        return menus;
    }

    @Override
    public Information queryInformation(String roleId) {
        Information information = manageMapper.selectInformationByRoleId(roleId);
        return information;
    }

    @Override
    public List<Course> selectCourseListByTeacherId(String id) {
        CourseAcademicYear courseAcademicYear = studentMapper.selectCourseAcademicYearByState();
        List<Course> courses = teacherMapper.selectCourseListByTeacher(id,courseAcademicYear.getId());
        return courses;
    }

    @Override
    public List<StudentCourseRel> queryStudentList(String academicYear, String userId) {
        List<StudentCourseRel> studentCourseRels = teacherMapper.selectStudentListByCourse(academicYear,userId);
        return studentCourseRels;
    }

    @Override
    public boolean updateStudentScore(StudentCourseRel studentCourseRel, String id) {
        //课程id，学生id  是否合格、评分备注
        // 修改状态 、评价教师教师
        studentCourseRel.setState("1");
        studentCourseRel.setTeacherId(id);
        boolean b = teacherMapper.updateStudentCourseRel(studentCourseRel);
        return b;
    }

    @Override
    public List<StudentCourseRel> getStudentInCourse(String academicYear, String userId) {
        List<StudentCourseRel> studentCourses =  teacherMapper.selectStudentListByCourse(academicYear,userId);
        return studentCourses;
    }

    @Override
    public List<Course> selectCourseList(String teacherId, String courseAcademicYear) {
        List<Course> courses = teacherMapper.selectCourseListByTeacher(teacherId,courseAcademicYear);
        return courses;
    }

    @Override
    public List<CourseAcademicYear> selectCourseYearList(String courseAcademicYearId) {
        List<CourseAcademicYear> courseAcademicYears = teacherMapper.selectCourseAcademicYearList();
        for(CourseAcademicYear courseAcademicYear : courseAcademicYears){
            courseAcademicYear.setType("0");
            if(courseAcademicYearId.equals(courseAcademicYear.getId())){
                courseAcademicYear.setType("1");
            }
        }
        return courseAcademicYears;
    }
}
