package hive_api;

import java.sql.*;
//import org.apache.hive.jdbc.HiveDriver;

/**
 * @Auther: lp
 * @Date: 2020/3/31 10:56
 * @Description:
 */
public class Hive_Demo1 {

//    private static Connection conn = null;
//    private static Statement stmt = null;
//    private static ResultSet rs = null;
//
    //jdbc核心驱动类
    private static String driverName = "org.apache.hive.jdbc.HiveDriver";

    public static void main(String[] args) throws SQLException {
        try {
            //加载jdbc核心驱动类
            Class.forName(driverName);
        } catch (ClassNotFoundException e) {
            e.printStackTrace();
            System.exit(1);
        }
        //建立连接
        Connection conn = DriverManager.getConnection("jdbc:hive2://192.168.3.140:10000/test");
        //创建执行器
        Statement sta = conn.createStatement();
        // createDatabase(sta);
        // dropDatabase(sta);
        // createTable(sta);
        //loadData(sta);
        selectData(sta);
        // destory();
        //String tableName = "jdbctest";
        //定义执行sql语句

        //sta.execute("create table qweqwe(id int,name string)");

        //定义执行结果集和sql语句
        // ResultSet res = sta.executeQuery("show tables '" + tableName + "'");
        //  if(res.next()){
        //   System.out.println(res.getString(1));
        // }
    }

    /**
     * 创建库
     * @param sta
     * @throws SQLException
     */
    public static void createDatabase (Statement sta) throws SQLException {
        String sql = "create database hive_jdbc_tests";
        System.out.println("Running"+ sql);

        sta.execute(sql);
    }

    /**
     * 删除库
     * @param sta
     * @throws SQLException
     */
    public static void dropDatabase (Statement sta) throws SQLException {
        String sql = "drop database hive_jdbc_test";
        sta.execute(sql);
    }

    /**
     * 创建表
     * @param sta
     * @throws SQLException
     */
    public  static void createTable(Statement sta) throws SQLException {

        String sql = "create table emp (name string,age string) row format delimited fields terminated by ','";
        System.out.println("Running: " + sql);
        sta.execute(sql);
    }

    /**
     * 数据加载
     * @param sta
     * @throws SQLException
     */
    public  static void loadData(Statement sta) throws SQLException {

        String sql = "load data local inpath'/home/test' into table emp";
        System.out.println("Running: " + sql);
        sta.execute(sql);
    }

    /**
     * 数据查询
     * @param sta
     * @throws SQLException
     */
    public static void selectData(Statement sta) throws SQLException {
        String sql = "select * from emp";
        // sta.execute(sql);
        ResultSet resultSet = sta.executeQuery(sql);
        while (resultSet.next()) {
            System.out.println(resultSet.getString(1));
            System.out.println(resultSet.getString(2));
        }
    }

    /**
     * 释放资源
     * @throws SQLException
     */
//    public static void destory() throws SQLException {
//        if (rs !=null){
//            rs.close();
//        }
//        if (stmt != null){
//            stmt.close();
//        }
//        if (conn !=null){
//            conn.close();
//        }
//    }
}
