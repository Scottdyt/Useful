#include <io.h>
#include <bits/stdc++.h>
using namespace std;

void getFiles( string path, vector<string>& files ){
	//�ļ����
	long   hFile   =   0;
	//�ļ���Ϣ
	struct _finddata_t fileinfo;
	string p;
	if((hFile = _findfirst(p.assign(path).append("\\*").c_str(),&fileinfo)) !=  -1){
		do{
			//�����Ŀ¼,����֮
			//�������,�����б�
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
    ////��ȡ��·���µ������ļ�
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
