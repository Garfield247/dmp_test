import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.FileSystem;
import org.apache.hadoop.fs.Path;

import java.io.IOException;
import java.net.URI;
import java.net.URISyntaxException;

/**
 * 这个类是将文件从HDFS下载到本地。
 * localPath可以是Hive的表，可直接将所有数据都下载下来
 * @Auther: lp
 * @Date:
 * @Description:
 */
public class GetFileAPI {

    public static void main(String[] args) throws URISyntaxException {

        GetFileAPI gfs = new GetFileAPI();
        FileSystem fs = gfs.GetHadoopFileSystem();

        gfs.GetFile(fs);

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

    public static void GetFile(FileSystem fs) {

        Path localPath = new Path("file:////d://");
        Path hdfsPath = new Path("/Initial_Data/tests.txt");
        try {
            fs.copyToLocalFile(hdfsPath,localPath);
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
