# -*- coding: utf-8 -*-

headers = {
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    'Host': '183.64.133.160:6186',
    'Origin': 'http://183.64.133.160:6186',
    'Referer': 'http://183.64.133.160:6186/login/UserLogin.aspx',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Cookie': 'TokenCODE=A97BBCC3A315544931AC4D2322F5EE4A; ASP.NET_SessionId=lmb42kigb5awoj452now3m55; cq168sb=username=510283198009267456'
}
headers_Classex_sss = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Cookie': 'ASP.NET_SessionId=vo4qu155k04bflmg03qoy23i; TokenCODE=C8AC7BEC321245C7EE6159A7BA3CC042; cq168sb=username=510283198009267456',
    'Host': '183.64.133.160:6186',
    'Pragma': 'no-cache',
    'Referer': 'http://183.64.133.160:6186/Admini/gongnsjk/gnssynewedit.aspx?deptid=5325265c-f809-4357-ab8a-d88a1703b0ca&id=',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36'
}
headers_Classes_next = {
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Length': '6096',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Cookie': 'ASP.NET_SessionId=vo4qu155k04bflmg03qoy23i; TokenCODE=C8AC7BEC321245C7EE6159A7BA3CC042; cq168sb=username=510283198009267456',
    'Host': '183.64.133.160:6186',
    'Origin': 'http://183.64.133.160:6186',
    'Pragma': 'no-cache',
    'Referer': 'http://183.64.133.160:6186/Admini/gongnsjk/SelectClass.aspx?type=njbj&deptid=5325265c-f809-4357-ab8a-d88a1703b0ca',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36',
    'X-MicrosoftAjax': 'Delta=true'
}
headers_enter = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Length': '40900',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Cookie': 'ASP.NET_SessionId=vo4qu155k04bflmg03qoy23i; TokenCODE=C8AC7BEC321245C7EE6159A7BA3CC042; cq168sb=username=510283198009267456',
    'Host': '183.64.133.160:6186',
    'Origin': 'http://183.64.133.160:6186',
    'Pragma': 'no-cache',
    'Referer': 'http://183.64.133.160:6186/Admini/gongnsjk/gnssynewedit.aspx?deptid=5325265c-f809-4357-ab8a-d88a1703b0ca&id=',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36'
}
loginout_url = 'http://183.64.133.160:6186/login/loginout.aspx'
default_url = 'http://183.64.133.160:6186/login/Default.aspx'
login_url = 'http://183.64.133.160:6186/login/UserLogin.aspx'  # 登陆
yzm_url = 'http://183.64.133.160:6186/login/yanzhengma.aspx'  # 验证码
real_url = 'http://183.64.133.160:6186/script/queryjson/UserLogin.ashx?RealUrl=183.64.133.160:6186'  # 登陆前验证
radl_data = {'action': 'getloginurl'}  # 登陆前验证_表单
login_data = {
    '__VIEWSTATE': '/wEPDwUJLTY1MTkzMjE4D2QWAgIDD2QWBAIDDxYCHglpbm5lcmh0bWxlZAIMDw8WAh4EVGV4dAUHMzc4MzkwOWRkZMP1OBARgRjOVKr6uVncBRVR+qPf',
    '__EVENTVALIDATION': '/wEWBQLw2M6GBQKs2Pl7AvSOvp8GAueVyfMBAoLch4YMIQssBSzq1YdgsbMLeo3QoDIFo7E=',
    'loginname': '510283198009267456',
    'loginpwd': 'wrh123456',
    'txt_validcode': None,
    'btnLogin': '登录'
}  # 登陆_表单
subject_url = 'http://183.64.133.160:6186/Admini/gongnsjk/SelectSubject.aspx?deptid=5325265c-f809-4357-ab8a-d88a1703b0ca'  # 获得所以学科
subject_data = {
    'ScriptManager1': 'UpdatePanel1|_PageNumNowNextPage',
    '__EVENTTARGET': '_PageNumNowNextPage',
    '__EVENTARGUMENT': None,
    '__LASTFOCUS': None,
    '__VIEWSTATE': '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',
    '__EVENTVALIDATION': '/wEWHQLk1YWHDgK5opWACAL55JyzBAKEwYvJBwKln/PuCgLZgM43AtLv5NkMAtbvpNoMAtbvmNoMAtfvpNoMAtfvmNoMAtTvpNoMAtXvpNoMAtLvpNoMAtPvpNoMAtDvpNoMAsHvpNoMAs7vpNoMAvCuw40LAtzq090CAuu71qEGAqe7goAHAtj199cGAqfL09MLAta0lKcJApjd3Z4IAtzq648PAt3R3PsHAsPSm7wKH0PXeMxTfGuqVOmj7GsN1xML1ZM=',
    'pageIndexNow': '1',
    'txtTitle': None,
    'ddlStage': '1',
    'drpPageSize_zf': '15',
    '_PageNumNow_jumpPage202': '1',
    'hfSelect': None,
    'hidStudentIds': None,
    '_PageNumNow': None,
    '_PageSizeNow': '15',
    'depaid': '5325265c-f809-4357-ab8a-d88a1703b0ca',
    '__ASYNCPOST': 'true'
}  # 获得所以学科_表单
classes_url = 'http://183.64.133.160:6186/Admini/gongnsjk/gnssynewedit.aspx/GetClasses'
SelectClass_url = 'http://183.64.133.160:6186/Admini/gongnsjk/SelectClass.aspx?type=njbj&deptid=5325265c-f809-4357-ab8a-d88a1703b0ca'
classes_data = {'deptId': '5325265c-f809-4357-ab8a-d88a1703b0ca', 'gradeId': None, 'xiaoquId': 'is null'}
enter_url = 'http://183.64.133.160:6186/Admini/gongnsjk/gnssynewedit.aspx?deptid=5325265c-f809-4357-ab8a-d88a1703b0ca&id='

DropDownList1 = {'2019-2020年下学期': '201902', '2019-2020年上学期': '201901', '2018-2019年下学期': '201802',
                 '2018-2019年上学期': '201801', '2017-2018年下学期': '201702', '2017-2018年上学期': '201701',
                 '2016-2017年下学期': '201602', '2016-2017年上学期': '201601', '2015-2016年下学期': '201502',
                 '2015-2016年上学期': '201501', '2014-2015年下学期': '201402', '2014-2015年上学期': '201401',
                 '2013-2014年下学期': '201302', '2013-2014年上学期': '201301', '2012-2013年下学期': '201202',
                 '2012-2013年上学期': '201201', '2011-2012年下学期': '201102', '2011-2012年上学期': '201101',
                 '2010-2011年下学期': '201002', '2010-2011年上学期': '201001'}
ddltime2 = {
    '上午': '0',
    '下午': '1'
}
ddltim3 = {
    '第一节课': '1',
    '第二节课': '2',
    '第三节课': '3',
    '第四节课': '4',
    '第五节课': '5',
    '第六节课': '6',
    '第七节课': '7',
    '第八节课': '8',
}
ddlDx = {
    '单个班级': '0',
    '多个班级': '1',
    '其它': '2'
}
ddlxueke = {}
ddlGrades = {'小学一年级': '9c10912f-7b3b-48f1-8917-f8315481b2f0', '小学二年级': 'e60fe341-76af-4d9d-a149-4001be714977',
             '小学三年级': '1edb3c7a-973c-4d76-a1f6-a67d8fb532ec', '小学四年级': 'bf1ef79f-c1e4-4ba3-ade3-32a704438137',
             '小学五年级': '65ce5038-534e-47c9-aaa3-ba81eab03b29', '小学六年级': '858e333a-85f7-4831-af76-999707b2a874'}
selClass = {}
classroom = {
    '小学班班通教室一年级（1）班': '53e00612b4bd4814ac9e1cca47a0630b',
    '小学班班通教室一年级（2）班': '320e3577e28441ea9fd6b443b59aee1b',
    '小学班班通教室一年级（3）班': 'e349dd1f2be145c39761e74d152a288b',
    '小学班班通教室一年级（4）班': '1367851f09a54b77990d8720661edd8c',
    '小学班班通教室一年级（5）班': 'cfce72fab79f4fe6aa57bcbce8d14b7a',
    '小学班班通教室一年级（6）班': '2be567c09c164a228b57df38a589ba73',
    '小学班班通教室一年级（7）班': '360e494822fd4cf1b23ee967252c0930',
    '小学班班通教室一年级（8）班': 'e4b6ffc3dc91421793f6a41d3182d189',
    '小学班班通教室一年级（9）班': '8ff6503d97de4e24baa4b17ca58cd466',
    '小学班班通教室一年级（10）班': '68bf299adc4346128ffda1094b73c473',
    '小学班班通教室二年级（1）班': '0613de310bfa46d6a6570eeaf66937f9',
    '小学班班通教室二年级（2）班': '63986b69558d499ca261c7f44d503e4c',
    '小学班班通教室二年级（3）班': 'fd0d2551eff440d9943dca3d9276df9e',
    '小学班班通教室二年级（4）班': '52eb13ba6264453ea18d34d46f893748',
    '小学班班通教室二年级（5）班': 'bab2314060994e2fbc212d435b969f71',
    '小学班班通教室二年级（6）班': '637565401657409f9788e2517b66621a',
    '小学班班通教室二年级（7）班': 'c8bb5042ffa2471f9afaed3788df3c38',
    '小学班班通教室二年级（8）班': 'f78d9dc8c1f14203808aa42a76a1f0be',
    '小学班班通教室二年级（9）班': '2e153b35e8ca4fe88b8578ccdcc562ae',
    '小学班班通教室二年级（10）班': 'ad773a4a0e6e485abceda2c30c022ba4',
    '小学班班通教室三年级（1）班': '4836db4e0543417bb35fb2ee8dd24659',
    '小学班班通教室三年级（2）班': 'ab7604bddc134bc58326b58abb8ae0de',
    '小学班班通教室三年级（3）班': 'bd249c5e107f40ec94d33966a2a519a2',
    '小学班班通教室三年级（4）班': '512e1d82514f426b84fc65ef3deb75de',
    '小学班班通教室三年级（5）班': 'bf2085f58436469fb92fa5622fd576e7',
    '小学班班通教室三年级（6）班': '873e10dac5d543aeafc5d576fb9153e6',
    '小学班班通教室三年级（7）班': '7404c679783d4d148e8cb0ab12c61a05',
    '小学班班通教室三年级（8）班': '43345679b179452d948cbb25d6f97a45',
    '小学班班通教室三年级（9）班': '349a0663ff1f494b9f64d630e8408274',
    '小学班班通教室三年级（10）班': 'ad261141b804488b9c1146078598ab62',
    '小学班班通教室四年级（1）班': 'e6777df5eb144308b80b4d6799e0ad03',
    '小学班班通教室四年级（2）班': '0407bb74568f434188004fdf29d78959',
    '小学班班通教室四年级（3）班': '419b7f92b1ce49068e5549eccedc3189',
    '小学班班通教室四年级（4）班': 'fa27d9c57e1d4caebd8161da2c20ccd2',
    '小学班班通教室四年级（5）班': '56e6e9dba82544e683d321d652acf776',
    '小学班班通教室四年级（6）班': 'bcd273af56634f7bb99048b3ae07d746',
    '小学班班通教室四年级（7）班': '23377f1b874543bf8b6532281523f851',
    '小学班班通教室四年级（8）班': '9f9d5c7df8e645f5b571b2582978a295',
    '小学班班通教室四年级（9）班': '9e3643fb976d47c690c9101419a50f7d',
    '小学班班通教室四年级（10）班': '0e69c33e180f42ad9f4a9339b989c130',
    '小学班班通教室五年级（1）班': '7d790d1a8ed84c2ca2bef3aeb332a2d3',
    '小学班班通教室五年级（2）班': '8c8acd99b6c94508ae9bb87d02a1f46a',
    '小学班班通教室五年级（3）班': '363bf4baff9f4ba4bc152c3430482d2d',
    '小学班班通教室五年级（4）班': 'bf017d1164134a6495a299023f9355d7',
    '小学班班通教室五年级（5）班': '25a4686083f74bac8d52fd713c050b90',
    '小学班班通教室五年级（6）班': '9ed7e993543749d4bf68ef85d4ba6dd9',
    '小学班班通教室五年级（7）班': '0c34b2ae8f70464d90649ab8876875fa',
    '小学班班通教室五年级（8）班': '49d2a4184b6f462891375f101ed34b97',
    '小学班班通教室五年级（9）班': 'b3b2b1e82beb4588a9d983b662f5408b',
    '小学班班通教室五年级（10）班': '0bc89e24f56c4352a033c78ed05b7da2',
    '小学班班通教室六年级（1）班': 'b0ed22ac14044b43987222ed00dea321',
    '小学班班通教室六年级（2）班': '529bb306e2cd450c9fa4dbe2ff04cd5d',
    '小学班班通教室六年级（3）班': '3d5fe1f30e07453ba108bee53db5d8ec',
    '小学班班通教室六年级（4）班': '039a54803d604f32a24ceeee9122b2c2',
    '小学班班通教室六年级（5）班': '347a1ea68bd34c5b90aa205be90065cb',
    '小学班班通教室六年级（6）班': '3d241a5c884047ec92af4ba5b3d9d083',
    '小学班班通教室六年级（7）班': 'f3f3b530a9c841f5bac3e617f22b92fd',
    '小学班班通教室六年级（8）班': 'fbb254aa3de542b9af1cb4e7f5634c44',
    '小学班班通教室六年级（9）班': 'baa5218e7b79448285616042435aa501',
    '小学班班通教室六年级（10）班': '3e4f48e34fbe4f1ca4b43dfaa072b189',
    '初中班班通教室七年级（1）班': '0c2c057b13a94f5b8b205c7dd4533d11',
    '初中班班通教室七年级（2）班': '2b164a4c2fc34b0f80ace66ef21f1241',
    '初中班班通教室七年级（3）班': 'b8578a83eebe4bb892e32a168516ad2d',
    '初中班班通教室七年级（4）班': 'a9b467033fb54f9f8f055c10f36c61f1',
    '初中班班通教室七年级（5）班': '1c55aaa1261d4da38431b965fddf74d7',
    '初中班班通教室七年级（6）班': '610a1ed33b14477cb2247e5975e413f9',
    '初中班班通教室七年级（7）班': 'e4a3f9fb47d44a7399b802acd030c7fa',
    '初中班班通教室七年级（8）班': '014bb7fbb2fe4da1b9d5c8825120383c',
    '初中班班通教室七年级（9）班': '5bceb7c69dbf47ba9a69c8fe03c88d85',
    '初中班班通教室七年级（10）班': '9aa7ab91afdf4db188a99b1e15806dcd',
    '初中班班通教室七年级（11）班': '050e3d3569e44633beb37d231f5d150a',
    '初中班班通教室七年级（12）班': 'e354ca13bc4d412185559d72d12bf4db',
    '初中班班通教室七年级（13）班': 'bb82cff15c1247f9ac4430fd928662a2',
    '初中班班通教室七年级（14）班': 'a272e18a7afa47d1addd486313743fe6',
    '初中班班通教室七年级（15）班': '88c989b30fd747dfa8859e5c88faaf54',
    '初中班班通教室八年级（1）班': '49ecd39e3ca84189879032a9804dadb6',
    '初中班班通教室八年级（2）班': '6287d96266934cc487696bdf414366a8',
    '初中班班通教室八年级（3）班': 'f27b7dce0bba4aa39afd236d8d310707',
    '初中班班通教室八年级（4）班': 'a8e9194b77aa493fa9f991ce3fa11b39',
    '初中班班通教室八年级（5）班': 'f92be8bee99441b38cbff1372d31c611',
    '初中班班通教室八年级（6）班': '765aebf4f0494e7e8218ac233d6c2e52',
    '初中班班通教室八年级（7）班': '062d5f8db20442c39197b263e4c5460f',
    '初中班班通教室八年级（8）班': '6d4328e9a0d94ba4ab3a793ef7f1c454',
    '初中班班通教室八年级（9）班': '798a20f1e665441088eea8685d3d6f45',
    '初中班班通教室八年级（10）班': '81a000541d7a4be5914de7273aaf7eb1',
    '初中班班通教室八年级（11）班': 'aa0c13e97f12467eb3b79e73be52d6a6',
    '初中班班通教室八年级（12）班': '6ddce965da6843db9773fd67567fabea',
    '初中班班通教室八年级（13）班': '27bdc5c71d11472e972678ff82843dbd',
    '初中班班通教室八年级（14）班': '41794e89e06d4be6980c10ae265c98df',
    '初中班班通教室八年级（15）班': '1c5efbf0d9e44af0aad71f9a8787a984',
    '初中班班通教室九年级（1）班': 'b3ea3216fac946a19d4d4540bc0ef743',
    '初中班班通教室九年级（2）班': 'efb7ef2ce1ad4e7696abeba386b7328b',
    '初中班班通教室九年级（3）班': '5c28bb1294d945dfbd850a6f2262da89',
    '初中班班通教室九年级（4）班': '30663257242b4844b984351507e1812b',
    '初中班班通教室九年级（5）班': '771ce8a5f32b47e28638336dcafef3d7',
    '初中班班通教室九年级（6）班': '5099a80994be463a800a823f4db057d4',
    '初中班班通教室九年级（7）班': '4d667bc63acf4f92a60c6399d522867b',
    '初中班班通教室九年级（8）班': '9ab3435622ad4feeb9f3d4e1784beb29',
    '初中班班通教室九年级（9）班': '5fa0ab5b4b824379b308abbf572446af',
    '初中班班通教室九年级（10）班': '6248a364ddfc4314aec96568bae2b9db',
    '初中班班通教室九年级（11）班': 'e9a59fd39c184c439f1c264e2a4bbb14',
    '初中班班通教室九年级（12）班': '8eb09d93301f4c5395c15ef822de4da8',
    '初中班班通教室九年级（13）班': '58ebb1386f1147d99ca7a54dd632f177',
    '初中班班通教室九年级（14）班': '57b28c3d368341c29848007d92412ddc',
    '初中班班通教室九年级（15）班': '5342cf94bbab4c4490a9bb42675318dd',
    '高中班班通教室一年级（1）班': 'ab91363851464b3fb6379ae5612f2a0f',
    '高中班班通教室一年级（2）班': '19b16bd0412d425cbccd74cc6fd690a3',
    '高中班班通教室一年级（3）班': '1cc17de378d146acba26af1757a25b58',
    '高中班班通教室一年级（4）班': '596f42d5b86f403f8a5ede599e22c491',
    '高中班班通教室一年级（5）班': '635d9c50f1cf4043b1e14b2d84027b16',
    '高中班班通教室一年级（6）班': 'f953a61478bf44638d1803bfe75ef8b6',
    '高中班班通教室一年级（7）班': '08ca02b7a9d349069d9831c7b20e2dc7',
    '高中班班通教室一年级（8）班': '1aef9013a6774d8bad8fecaefcdadd8a',
    '高中班班通教室一年级（9）班': 'a5e235a1786241b2bc8e101863a595b1',
    '高中班班通教室一年级（10）班': '06e76b77ff8f4a8f81b1b3e5b7e4ddc0',
    '高中班班通教室一年级（11）班': '12a64d220f5f4aa2b7f713e30359512b',
    '高中班班通教室一年级（12）班': '0a30f77ecb174966b153ef195bfdb753',
    '高中班班通教室一年级（13）班': '2da5146ee2a740e7b8bc64df765fb7a0',
    '高中班班通教室一年级（14）班': '6c511a37ed2840478c69347c4444e1df',
    '高中班班通教室一年级（15）班': 'c85ef4e6539744f4b18db4af467509ed',
    '高中班班通教室一年级（16）班': 'd72fcb14e0c941449f7829b81373ff55',
    '高中班班通教室一年级（17）班': 'e3f519a852734c8198f7f897a6ab7609',
    '高中班班通教室一年级（18）班': '68627340fa2240b8a23ddeb19b2d489f',
    '高中班班通教室一年级（19）班': '312bf3514be94573826ec3b0bfcbf4c3',
    '高中班班通教室一年级（20）班': 'b9a3c1629b8d442bac70e42702fe0361',
    '高中班班通教室一年级（21）班': '65a912853c6541168ef49477a360401f',
    '高中班班通教室一年级（22）班': '46b4d882fa434627b16348b8ea5dca46',
    '高中班班通教室一年级（23）班': '5d2dd752e2bc40e9ae7aa90f0b372338',
    '高中班班通教室一年级（24）班': '5d25b230ff114086a0f0d082c458e254',
    '高中班班通教室一年级（25）班': '4b7ab855628840e0aeb8c4ed56398c56',
    '高中班班通教室一年级（26）班': '50c979951fc041b18195371d265bc263',
    '高中班班通教室一年级（27）班': '176b6bd547b04e19bff66934c8f23013',
    '高中班班通教室一年级（28）班': '9996724059d543daae6392393cbe8c7b',
    '高中班班通教室一年级（29）班': '9f2abb348d2942bcb80236c84cc77295',
    '高中班班通教室一年级（30）班': '9d126bfe856648e6896553ad65e5b5a8',
    '高中班班通教室二年级（1）班': '72fa3a0629864301b7736cb54f1d0d0c',
    '高中班班通教室二年级（2）班': '62bbc328cf7f43c0b165e8285cca56d3',
    '高中班班通教室二年级（3）班': '4e04ae2cc6a04f0a840c5a7d1cad1aa6',
    '高中班班通教室二年级（4）班': '3a1a6a7b7bfe484da5233b71b3783a3e',
    '高中班班通教室二年级（5）班': 'eb9ace1e014d42ddac13b2c013682a15',
    '高中班班通教室二年级（6）班': '33f5dc12c99e4364800b857b5c666c3a',
    '高中班班通教室二年级（7）班': '6f8ed5c8aec344bca8d3e4482bb631b7',
    '高中班班通教室二年级（8）班': '15cd59ec4e1d4ecba83726e4dc8cbdd9',
    '高中班班通教室二年级（9）班': 'a656176e76de402dbbc6a569432dc829',
    '高中班班通教室二年级（10）班': 'afb445ea3b7c445385c8f1e4b33120a9',
    '高中班班通教室二年级（11）班': '9708f787b6174ee0936b067777cb84cc',
    '高中班班通教室二年级（12）班': '9963b494cf054c799bbadb8b746f12a5',
    '高中班班通教室二年级（13）班': 'a1be824ce1424c42a17ebea50a81a460',
    '高中班班通教室二年级（14）班': 'a779e7c370484bbbb3e09defaddff35e',
    '高中班班通教室二年级（15）班': 'd7f8912614044b608d515ae012293a41',
    '高中班班通教室二年级（16）班': 'f2c0afc21fe94dd59e8a7fe9b28fd609',
    '高中班班通教室二年级（17）班': '615c3839c9e94fd987c26d2d63cb75bd',
    '高中班班通教室二年级（18）班': 'f67ba380a5aa4060819c741de8002206',
    '高中班班通教室二年级（19）班': 'edf621b544f94096935a1dea7a1f9026',
    '高中班班通教室二年级（20）班': '02a5f99d66504d7e964c39fcfaaa53a1',
    '高中班班通教室二年级（21）班': '47d6e64d709c48d5bcf42419c19747c7',
    '高中班班通教室二年级（22）班': 'a59afd8303ef45ada49115cd5c1070ed',
    '高中班班通教室二年级（23）班': 'b16cbd44bbcf472c9df2c5adb890fb87',
    '高中班班通教室二年级（24）班': '63010d138a274603915d5b5fba5a3637',
    '高中班班通教室二年级（25）班': 'cac2cad331064168b46a42ce4c2ea58e',
    '高中班班通教室二年级（26）班': '6f593b8a43cc4d0dbcad5c881ddf0778',
    '高中班班通教室二年级（27）班': '64debc02052d469ea7168c6cd8398b1f',
    '高中班班通教室二年级（28）班': '34bef9a5a14549e3a494a6a024291865',
    '高中班班通教室二年级（29）班': 'c1ec5395cda94593908e2362d3d42885',
    '高中班班通教室二年级（30）班': '89e18fe2b8964879a3d45f7aa9ce9b3e',
    '高中班班通教室三年级（1）班': 'cf10c95d7f6c4ca8a11e1dd3f839d881',
    '高中班班通教室三年级（2）班': '4006a00e17f1470194f9552a9ca753b1',
    '高中班班通教室三年级（3）班': '304995d800264b798f58b6a3873613c7',
    '高中班班通教室三年级（4）班': '03a06d122aae49efa4447e97399eb9d7',
    '高中班班通教室三年级（5）班': '3f247e8502fa47079bda6f081f3d3550',
    '高中班班通教室三年级（6）班': '9c46c8d73fe34af0bc2baec2a42238f1',
    '高中班班通教室三年级（7）班': '85d0e9ae05444dd8940f4504b1519f0e',
    '高中班班通教室三年级（8）班': '599ef8e68e7141409d6ec49082642f55',
    '高中班班通教室三年级（9）班': '4858a5f030a744e093d324cec74a73a6',
    '高中班班通教室三年级（10）班': '7dfc3dd555d8453f84fec3ca0a616c2b',
    '高中班班通教室三年级（11）班': 'a07dcae426884c038caae028b96c40a3',
    '高中班班通教室三年级（12）班': '7d326a78f90148c69179a2ff53052fb5',
    '高中班班通教室三年级（13）班': '1abbfc27e32e46d8a1cb0f280fbbf1ec',
    '高中班班通教室三年级（14）班': '1b52be0b67f24401839fbff9b0869da0',
    '高中班班通教室三年级（15）班': '9d6245959be0438db6b86a43667f3f12',
    '高中班班通教室三年级（16）班': 'c36dafc15ee742b9a708d0cf6721dd33',
    '高中班班通教室三年级（17）班': '8815c04166cc46e0ae2aa3c902c043de',
    '高中班班通教室三年级（18）班': 'd63ba218f0504143ad51054750d89947',
    '高中班班通教室三年级（19）班': 'f58f53c53b7340abb796430b5851f143',
    '高中班班通教室三年级（20）班': 'ea9dcec80ced43ce8c6ea7d689a42e4b',
    '高中班班通教室三年级（21）班': 'd872cd4eccd947dfa645218ad2ac1592',
    '高中班班通教室三年级（22）班': 'c0bfa67ed492482493cbc521fba3147b',
    '高中班班通教室三年级（23）班': 'c349d5631be84946b1d85c74a3947743',
    '高中班班通教室三年级（24）班': '1b235281aa2d4386a1c2d9ea8bd11a4b',
    '高中班班通教室三年级（25）班': 'c2237cc0f4084bf2ba8a5f27139a6553',
    '高中班班通教室三年级（26）班': 'de944be79c744817837aaa1695049a7f',
    '高中班班通教室三年级（27）班': '197949d464a84a55bdbfc66de5867684',
    '高中班班通教室三年级（28）班': 'e22e5255c25a4fa3881558e776b0e7f0',
    '高中班班通教室三年级（29）班': '98fbb392b1f1474aa3a3c1eb5fd56d63',
    '高中班班通教室三年级（30）班': '01a0bd44aeda423e95073842703a2374',
    '初中班班通教室七年级（16）班': 'a911b91389864fa78f2304b8db99e086',
    '初中班班通教室七年级（17）班': '8c26c3bafb214e0288100bcef058d198',
    '初中班班通教室七年级（18）班': '6a836431e74d4710a3620fe29bfeed6d',
    '初中班班通教室七年级（19）班': 'fdb7d432dfe64d7ca6554a90cd1b28a3',
    '初中班班通教室七年级（20）班': 'b2ecc6b2710544b4be3fefda21df312e',
    '初中班班通教室七年级（21）班': 'afda6b2a3ace4dd9911ec8997ccc8b42',
    '初中班班通教室七年级（22）班': '45212f307cf34f8c84b6f2e7328dc1ea',
    '初中班班通教室七年级（23）班': '218a4ddc1400448db7aff592abca08ff',
    '初中班班通教室七年级（24）班': 'c92c925fd92d4bc0b6195ef88740bf1c',
    '初中班班通教室七年级（25）班': 'f7b673bd248a4a5fb6be0afd84535093',
    '初中班班通教室八年级（16）班': 'd6f2eef13cd54ef58fc288c6d39cbc55',
    '初中班班通教室八年级（17）班': 'c6029706de37409b867fbe7ad60ee83c',
    '初中班班通教室八年级（18）班': '93957a04b6bb483aa49890c54f71e550',
    '初中班班通教室八年级（19）班': '67a0f4266e5e45ebab0adf82e4d13b70',
    '初中班班通教室八年级（20）班': '5c7b1bf863db41578f87a08db987c5b3',
    '初中班班通教室八年级（21）班': 'b7a6e405ed324a9ea5467e644da75ef7',
    '初中班班通教室八年级（22）班': '4c3dbb0b0ec84fd882e4297f13d70ebc',
    '初中班班通教室八年级（23）班': '5403841cd401480e84c9d40ffa9a6233',
    '初中班班通教室八年级（24）班': '4b0d21cc061d4d09a35a98eb72e2e497',
    '初中班班通教室八年级（25）班': 'c6f2b5a5a14d47c5bfb8d8b3c85e5efc',
    '初中班班通教室九年级（16）班': 'c68bba1966cf48bf83e543b4c6e0db65',
    '初中班班通教室九年级（17）班': '926e07c8219e46a2a4d2c86fc10a3ed3',
    '初中班班通教室九年级（18）班': '62aa758baf1541a396bc2084a456b7f7',
    '初中班班通教室九年级（19）班': '0a4847b3b4404f48be8683bf534f3145',
    '初中班班通教室九年级（20）班': '540c71b2a94a464abbd26554101cf99f',
    '初中班班通教室九年级（21）班': '676203c98e6d45e9a7e4f4374ff7c850',
    '初中班班通教室九年级（22）班': 'bde607df77d44e13a9c24d1d9534645b',
    '初中班班通教室九年级（23）班': 'edba6d4036034e32b5a858349b66bbe3',
    '初中班班通教室九年级（24）班': 'aa8bb09116e542029304879daa8b0d67',
    '初中班班通教室九年级（25）班': '62d5bc8df2224b90bdc6e4463da83534',
    '小学班班通教室一年级（11）班': '85243174abd848e599425eb78f1f302b',
    '小学班班通教室一年级（12）班': '504d90ea2bcd4d9e934b95b72f8ca449',
    '小学班班通教室一年级（13）班': 'e76507aa3fdd4054b2858c24d30b5279',
    '小学班班通教室一年级（14）班': 'ebf0cfe67dbb4267b837798ed7a5b7ca',
    '小学班班通教室一年级（15）班': 'e4dc1e454bf44126a5df1d09b5535450',
    '小学班班通教室二年级（11）班': 'c2f6c82e4e6d4e8c85c2fa3342f76a4c',
    '小学班班通教室二年级（12）班': '9edd166620f64a03bebe8ffaff43d557',
    '小学班班通教室二年级（13）班': 'efd3b95b142c40189e3ad4a8e2767c02',
    '小学班班通教室二年级（14）班': 'b8ca43724fbb4b74b64a2b0165218290',
    '小学班班通教室二年级（15）班': '9c3c22c4ec3844e68b09e527a5c85ccd',
    '小学班班通教室三年级（11）班': '2e762dc30b3b4690a55f750b44f740f2',
    '小学班班通教室三年级（12）班': '2dbe69beb8894374882332b39a8acf14',
    '小学班班通教室三年级（13）班': '34f0c21f74f34cdfafd7a572eab1d52f',
    '小学班班通教室三年级（14）班': '77fa5ff5c5694dcfb6cbb1ffcb2274b2',
    '小学班班通教室三年级（15）班': '11ea9156c4264b039cbbc351b407a692',
    '小学班班通教室四年级（11）班': '829ff934c04549c291fcecd98baaf232',
    '小学班班通教室四年级（12）班': '90fbc34ad963471caf7655a72849ac6d',
    '小学班班通教室四年级（13）班': '92724cd9472a4f0888d5dd137757b3cd',
    '小学班班通教室四年级（14）班': 'c96b487116af4c96963e334aa40a4959',
    '小学班班通教室四年级（15）班': '5f68eb8f2f8f4eda8bff92b5e18f6ad5',
    '小学班班通教室五年级（11）班': '86643d1671464ff785e3b171a0203436',
    '小学班班通教室五年级（12）班': '1b111a187ad847d087dab9483669d085',
    '小学班班通教室五年级（13）班': 'c6ea19a155394804817b9a851ec4bdd7',
    '小学班班通教室五年级（14）班': '6449dc24818d4630915f7f559a69a887',
    '小学班班通教室五年级（15）班': '632e111a83bc44e4bd9e25cd6ecc8cd6',
    '小学班班通教室六年级（11）班': '2dc34d5455434657a667e35bfe69aa99',
    '小学班班通教室六年级（12）班': '7e8cb8a4658a4e4d9110dc81e478e4ac',
    '小学班班通教室六年级（13）班': '56bdaab52342470ab8f2a825b6c76ae3',
    '小学班班通教室六年级（14）班': '4673a3cfb0b844aab7be3e70045a97cc',
    '小学班班通教室六年级（15）班': '8905f664b9c44d53a19e69bf9d671b39',
    '初中班班通教室七年级（26）班': '63a157a2e41a44498d4f5277e27a1332',
    '初中班班通教室七年级（27）班': 'e68c3204069e44569b947897aa42eb50',
    '初中班班通教室七年级（28）班': 'f3febe563b634238973300ba94c2da41',
    '初中班班通教室七年级（29）班': '7511fb106f4f4a8d86d959c800921b78',
    '初中班班通教室七年级（30）班': '2f67131a4fa845599263a6c08335df48',
    '初中班班通教室八年级（26）班': '2dbe73db75854e48a0b665faf4b5a082',
    '初中班班通教室八级（27）班': 'f13961087e5a4189b1f3d389782b622c',
    '初中班班通教室八级（28）班': '08b216f2d7ea4448a3576acf949fda6b',
    '初中班班通教室八级（29）班': 'e4850009672d4f6688a44514a3898e3e',
    '初中班班通教室八级（30）班': 'bc12061f070b4a8ea3385fb64738d631',
    '初中班班通教室九级（26）班': '03f6bfa7adab4f58ada9a138e2c670df',
    '初中班班通教室九级（27）班': 'abc76e35e19f43d7ac3697f12aff1161',
    '初中班班通教室九级（28）班': 'b3dbd79763dc407d9acf571ccf413c9a',
    '初中班班通教室九级（29）班': 'f41b4ae5880845d2b5301e04141201cd',
    '初中班班通教室九级（30）班': '569d66afdce0481b947f4d31ce790395',
    '初中班班通教室七年级（31）班': 'de94f1255a914ad5b92e491a756f3f9a',
    '初中班班通教室八级（31）班': '16d6e4b5786045f4abca14762e3694a1',
    '初中班班通教室九级（31）班': '754f1e9eccb046c3bcad1628747239e7',
    '化学实验室（一）': 'fbafe4b24bc74ca8a31cb60f31606044',
    '化学实验室（二）': '4fe55bd83c5a498fb16fed323b4de953',
    '化学实验室（三）': '5fbbbf45d43c46b0bbecaee3b6bbd66e',
    '化学实验室（四）': '6b512a0b231241c987a59a289c06612f',
    '计算机教室（一）': '379b1921b78e4843b58676b9d1ff8ff0',
    '计算机教室（二）': 'c56aca14093f4eb886633b6123c00243',
    '计算机教室（三）': 'c0fbdfc740834a7da0ef58d9b0cafd82',
    '计算机教室（四）': '7fe8ccd84f5a4095b52ae615d740ed5e',
    '科技教室（一）': '616e2261043c471385ed8773d21958b3',
    '科技教室（二）': '3981512fd7dd4fcf8eb288fe6cb4c9cd',
    '科技教室（三）': '7f635b528d0f458b8fb3d2031b6bf82b',
    '科技教室（四）': '2526342aac7d442987459bf48df597d7',
    '小学科学实验室（一）': '59a214f3bf584f97b77bc2bf741140bd',
    '小学科学实验室（二）': '0cab93eb6c4f4b259ec66743a4306990',
    '劳技教室（一）': '88bd491d414543ac921f05e79bd93567',
    '劳技教室（二）': 'f853d87dffef49d7bb5a4eed6a866511',
    '劳技教室（三）': '7cb4e7d335464b349abada53d91bd27b',
    '劳技教室（四）': '7b1a2a481a9e417b9164a58f08707e5a',
    '美术教室（一）': '70a908a6d8fb43c183d634d98cc10b96',
    '美术教室（二）': 'e1d9d1825a234ac294bc3b6577a23967',
    '美术教室（三）': '15f34f1e09644daba8265cb99635c5c7',
    '美术教室（四）': 'bdfb86db4d3b4c77a7d0388e955d5f8c',
    '生物实验室（一）': 'bcdf12561d9946a0b3273af035b6a4a5',
    '生物实验室（二）': '186875e7db844a588c9426cbcf715be3',
    '生物实验室（三）': 'b135ca1ea1b14eb4b8740c2d6fdd4a42',
    '生物实验室（四）': '86aa7f34d8e942ab9afb1eb0d6373265',
    '图书阅览室（一）': '7c739a2ce87243ae9ee05c1db1d16c88',
    '图书阅览室（二）': 'bf37b71457cf4be788ef7a2c71e15135',
    '图书阅览室（三）': '20cfb45d1cfa4b4098a2c4bcdbbe5cc5',
    '体育保管室（一）': '22569cd278314972a2e218f915067b33',
    '体育保管室（二）': '0a19553177d44c78b2f99f5aeb116d9a',
    '物理实验室（一）': 'eb4fdc809ad54eb8a3c95d0ef82a75a0',
    '物理实验室（二）': 'b65aa943c24946d68f63c80aafef4931',
    '物理实验室（三）': '43569bb1d82c4d8c840960642f887594',
    '物理实验室（四）': 'a662744f579d4382810885d440c93fc7',
    '卫生室（一）': '00d046c01a2a4248848ed6bd39dc3db7',
    '卫生室（二）': '51aa22a3c1ba462cad50b2ca7c752cb9',
    '音乐教室（一）': '1f8979cd42f54078b17ce9ce3049c610',
    '音乐教室（二）': 'a025ae484f97469c8d1105ff66b1cda7',
    '音乐教室（三）': '9779e738354f49c7b3a1f79f59b80979',
    '音乐教室（四）': 'd9b45de0ea584905b180a36eed97ff40',
    '小学综合活动室（一）': 'd233118407c643faa56d7b39ff2e2aa8',
    '多功能教室（二）': '53c7a672-88d9-4027-8952-546ea7f78f24',
    '课件制作室（一）': 'd5e622de-5f6f-4fcb-9329-88cdfe4d5410',
    '电子阅览室（一）': 'af3dff0e-3054-4450-b557-8c67b8d9df6a',
    '多媒体教室（一）': '0cce5226-e5e7-4b98-a10d-4acc57c6d251',
    '音乐多媒体教室': 'b0e134cf-ce8f-4e33-93bf-344cb6207a18',
    '科学技术实验室': '5982ada9-450f-4142-8f57-07caafc8fa22',
    '课件制作室（二）': 'c64b4f2d-4cef-4242-8751-4327d51b0b15',
    '电子阅览室（二）': '593c01a1-4cfe-4254-a6ea-df32141cc674',
    '多媒体教室（二）': '29a4bf12-9045-4292-93a7-3ff90d055525',
    '多媒体教室（三）': 'e6579fc4-e235-4bf8-a486-918528fdb969',
    '电子阅览室（三）': '409fddf3-0653-47d5-ad95-3e2df46c8f47',
    '多功能教室（三）': '02c74614-aef0-47e8-ac5a-203fc34817c5',
    '多功能教室（一）': '3643e0f0-2989-49c3-a7af-f64936cec288'
}