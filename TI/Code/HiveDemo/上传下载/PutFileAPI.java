import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.FileSystem;
import org.apache.hadoop.fs.Path;

import java.io.IOException;
import java.net.URI;
import java.net.URISyntaxException;

/**
 * 这个类是将文件从本地上传到hdfs
 * localPath 可以是本地或者服务器。
 * hdfsPath可以是Hive的表路径，但是这个会直接写入表格式不能错不然Hive加载后不能正确分割各个字段
 * @Auther: lp
 * @Date:
 * @Description:
 */
public class PutFileAPI {

    public static void main(String[] args) throws URISyntaxException {

        PutFileAPI gfs = new PutFileAPI();
        FileSystem fs = gfs.GetHadoopFileSystem();

        gfs.PutFile(fs);

    }

    public static FileSystem GetHadoopFileSystem()  {

        FileSystem fs = null;

        Configuration conf = null;
        String hdfsUserName = "root";
        URI uri = null;

        conf = new Configuration();

        try {
            uri = new URI("hdfs://192.168.3.140:8020");
        } catch (URISyntaxException e) {
            e.printStackTrace();
        }
        try {
            fs = FileSystem.get(uri,conf,hdfsUserName);
        } catch (IOException e) {
            e.printStackTrace();
        } catch (InterruptedException e) {
            e.printStackTrace();
        }


        return fs;
    }

 public static void PutFile(FileSystem fs) {

     Path localPath = new Path("file:////d://tests.txt");
     Path hdfsPath = new Path("/Initial_Data/");
     try {
        fs.copyFromLocalFile(localPath,hdfsPath);
     } catch (IOException e) {
         e.printStackTrace();
     } finally {
         try {
             fs.close();
         } catch (IOException e) {
             e.printStackTrace();
         }
     }
 }
}
