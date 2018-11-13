#include <io.h>
#include <bits/stdc++.h>
using namespace std;

void getFiles( string path, vector<string>& files ){
	//文件句柄
	long   hFile   =   0;
	//文件信息
	struct _finddata_t fileinfo;
	string p;
	if((hFile = _findfirst(p.assign(path).append("\\*").c_str(),&fileinfo)) !=  -1){
		do{
			//如果是目录,迭代之
			//如果不是,加入列表
			if((fileinfo.attrib &  _A_SUBDIR)){
				if(strcmp(fileinfo.name,".") != 0  &&  strcmp(fileinfo.name,"..") != 0)
					getFiles( p.assign(path).append("\\").append(fileinfo.name), files );
			}else{
				files.push_back(p.assign(path).append("\\").append(fileinfo.name) );
			}
		}while(_findnext(hFile, &fileinfo)  == 0);
		_findclose(hFile);
	}
}

void combineFiles(string inPath,string outPath){
    vector<string> files;
    ifstream fin;
    ofstream fout(outPath.c_str());
    ////获取该路径下的所有文件
    getFiles(inPath, files );
    int n = files.size();

    for (int i = 0;i < n;i++){
        fin.open(files[i].c_str());
        string a;
        // fout<<i<<"\n";
        while(getline(fin,a,'\n')){
            fout<<a<<"\n";
        }
        fin.close();
        fin.clear();
        cout<<"finish " << files[i]<<endl;
    }

}
int main(){
    string filePath = "E:\\TaxiRaw\\17";
    string outFile = "F:\\Taxi\\RowData\\17.txt";

    combineFiles(filePath,outFile);

    return 0;
}
