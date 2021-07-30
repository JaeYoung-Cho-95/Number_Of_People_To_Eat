#!/usr/bin/env python
# coding: utf-8

# In[ ]:


print("식수예측 데이콘용 함수와 변수들을 저장한 파일 _ 210717 수정본")

# 밥류 필터용
# a1: 쌀밥류, b1:덮밥국밥류, c1:비빔밥볶음밥류 ,d1: 김초밥류, e1: 국수류
a1 = ["(쌀밥류)", "영양밥", "흑미밥", "오곡밥", "수수밥", "귀리밥", "팥밥", "콩밥", "기장밥", "치자밥", "찹쌀밥"]
b1 = ["(덮밥국밥류)", "카레라이스", "짜장밥", "오므라이스", "잡채밥", "시금치무쌉", "카레소스", "수제비", "커리",
     "카레돈까스"]
c1 = ["(비빔밥볶음밥류)", "빠에야", "필라프", "곤드레밥", "콩나물밥", "보리밥", "볶음밥/", "비빔밥/"]
d1 = ["(김초밥류)", "주먹밥", "쌈밥"]
e1 =["냉면", "국수", "짜장면", "채소라면", "스파게티", "파스타", "나가사키면", "알리오올리오", 
     "우동", "소바", "비빔면", "쫄면", "메밀면", "고추짜장", "컵라면"]
f1 = ["(죽류)" , "해물누룽지"]
exceptions_rice = []
rice_filter = [a1, b1, c1, d1, e1, f1, exceptions_rice]

# 국물류 필터용
a2 = ["(국탕류)", "나베", "백숙", '샤브샤브', "대구지리"]
b2 = ["(찌개류)"]
c2 = ["(스프류)"]
exceptions_soup = []
soup_filter = [a2, b2, c2, exceptions_soup]

# 반찬 및 기타류 필터용
a5 = ["(김치류)", "오이소배기", '오이소박이']
b5 = ["(샐러드류)", "쌈", "스틱", "양배추", "야채", "풋고추", "상추", "채소", "브로컬리", "브로콜리", "영양부추",
     "오이&당근", '오이선', "알배기", "배추깻잎", "콘슬로우", "다시마", "콘치즈", "단호박범벅", "물미역", "미역줄기",
     "단호박", "카프레제", "호박잎", "탕평채", "봄동숙", "파래김", "연근", "새송이", "호박숙", "범벅", "병아리콩",
     "곰피초장", "삼색콜리", '재래김', "매쉬드포테이토"]
c5 = ["(튀김류)", "꿔바로우", "깐풍", "카츠", "요거닭", "유린기", "커틀릿", "교촌", "고로케", "멘보샤", "깐쇼새우",
     "웨지감자", "춘권", "후라이드", "크림새우", "칠리새우", "베이비크랩", "맛탕", '해쉬포테이토', "회오리감자",
     '오지치즈후라이']
d5 = ['(전류)', "동그랑땡", "부침", "산적", "오꼬노미야끼", '빈대떡', "수수부꾸미", '계란후라이']
e5 = ["(찜류)", "수육", "메쉬드", "찐", "보쌈", "숙회", "오징어", "숙쌈", "오향장육", "프리타타"]
f5 = ["(볶음류)", "두루치기", "주물럭", "마파두부", "유산슬", "류산슬", "치즈불닭", "호박꼬지", '궁보계정', '양장피',
     '마늘쫑건새우', "블랙페퍼쉬림프", '김자반']
g5 = ["(조림류)", "국물쪼리닭", "스위트칠리미트볼", "지짐", "동파육", "콩자반", '간장계란장']
h5 = ["(구이류)", "스테이크", "너비아니", "대패", "떡갈비", "함박", "수원왕갈비", "폭립", "훈제오리", 
      "숯불양념꼬치어묵", "숯불양념꼬지어묵", "모듬소세지", "그라탱", "그라탕", "스크램블", '군고구마', "소떡소떡",
     "어떡햄", '양념김', '허니버터옥수수']
i5 = ["(무침류)", "파채", "오복지", "무말랭이", "냉채", "겨자채", "묵"]
j5 = ["(장아찌류)", "깻잎지", "깻잎양념지", "고추지", "간장지", "절이", '오이지']
exceptions_vege = []
vege_filter = [a5, b5, c5, d5, e5, f5, g5, h5, i5, j5, exceptions_vege]

# 디저트류 필터용
a3 = ["(음료)", "코코뱅", "피크닉", "쥬시쿨"]
b3 = ["(유제품)", "프로바이오틱", "짜요짜요", "파르페"]
c3 = ["(빵과자류)", "나쵸", "퀘사디아", "바게트", '바게뜨', "티라미수", "도너츠", "퀘사디야", "버거", "츄러스",
      "추러스", "와플", "도넛", "아이스슈", "수제과일잼샌드", "타꼬야끼", '타코야끼', "슈크림", "라면땅", "시리얼"
      ,'탱크보이', "푸딩"]
d3 = ['(과일류)', "사과", "바나나", "과일", "조각사과", "오렌지", "아오리사과", "귤", "천도복숭아", "참외", "포도",
                     "배", "열대과일", "단감", "수박", "홍시","토마토" ,"수박화채", "수떡수떡화채", "방울토마토", 
                      "청포도", '모둠과일', "토마토설탕절인"]
exceptions_dessert = ["꿀호떡", '떡밤초', '떡꼬지', '어묵고추장떡', 
                      "찹쌀호떡", "송편", "인절미"]
dessert_filter = [a3, b3, c3, d3, exceptions_dessert]

# 재료 필터용
# 김, 무 는 음식의 이름 속에 포함될 수 있다. ex) 김치 , 나물무침 따라서 해당 한글자 재료들은 세부적으로 메뉴를 넣어줘야한다. 
# 메뉴의 모든 원재료가 아니라, 직관적으로 떠오르는 메인 메뉴를 기준으로 분류한다.
# 버섯은 균류에 들어가야 하지만 채소류에 분류해줬다.
# 양파는 뿌리류에 들어가야하지만 채소류에 분류해줬다.
# 메뉴 중에 함박, 스테이크, 함박스테이크 3개가 있다. count를 할 때, 중복으로 되지만 해당 음식들에 가중치가 절대값 1정도는 무관하다고 판단.
견과및두류 = list(set([ '청국장', '흑임자', '부럼','캐슈넛','두부','콩','팥','녹두','들깨','땅콩','두유','유부','아몬드','잣','호두','모밀','견과','밤']))
묵류 = list(set(['탕평채','우무묵','도토리묵','청포묵','모듬묵','곤약','올방개묵','묵볶음','삼색묵','모둠묵','이색묵']))
어패류 = list(set(['류산슬' , '유산슬' ,'알탕', '쭈꾸미', '북엇국' , '우렁' ,'타코야끼', '올갱이' , '조기' , '임연수','쥐어','꼬막','방어','골뱅이','해물파전','해물동그랑땡전','재첩','다슬기','쥐포','조기','홍어','전복','삼치','노가리','조갯살','북어','양장피','미더덕','삼치','홍합','꽁치','맛살','봉골레','골뱅이','문어','쭈삼','날치','굴비','연어','명란','쥐포','대구','굴','조개','북어','오징어','참치','바지락','진미채','삼치','참치','아귀','홍합','코다리','장어','꽁치','동태','갈치','미더덕','해파리','주꾸미','생선','명태','자반고등어','황태','꽁치','가자미','명엽','바지락','어묵','낙지','날치','멸치', "어떡햄", "고갈비"]))
육류 = list(set(['육개장','깐풍기' ,'깐풍육' , '소세지' , '제육', '동파육','류산','유산','소떡소떡','수제맛쵸킹','함박','스테이크','윙','너겟','초계','등심찹쌀','유린기','사골','우육','설렁탕','갈비탕' ,'퀘사디','히레카츠','돼지','차돌','선지','순대','동그랑땡','함박','곰탕','산적','등뼈','햄','쇠고기','돈육','미트','오향장육','삼겹살','쇠불고기','수육','삼계','베이컨','너비아니','보쌈','탕수육','치킨','부대찌개','닭','등갈비','떡갈비', '소갈비',"갈비통통만두", "갈비만두", "LA갈비", "수원왕갈비", "돈갈비" ,'사태','함박','목살','바베큐폭립',"바베큐장각오븐구이" ,'오리훈제','스팸','백숙','소시지','삼겹살','비엔나','돈가스','돈까스','족발','대패']))
채소류 = list(set(['단호박','애호박','호박죽','짜사', '쨔샤','짜샤','돈나물','육개장' , '아욱' , '마늘종', '마늘쫑', '브로컬리', '우엉', '하루나', '고구마줄기','무청' ,'바질','곰취' ,'홍초', '치자','락교','부추','유채겉절이','콩가루배춧국','유채나물','청양','양송이','초나물','비빔밥','쪽파','알배기','해물파전','반달나물','양상추','근대나물','쑥','섬초','오복지','머위','탕평채','비름나물','취나물','보름나물','대파','초나물','퀘사디','꽈리초조','두릅','죽순','방풍','냉이','시래기','노각','느타리','케일','피망','느타리팽이','달래','파채','머위','깻잎','양장피','두릅','우거지','쑥갓','양파','호박잎','취나물','부추','숙주','쌈추','고춧잎','채소탕수','고사리','산채','꼬들배기','생파','쪽파','양송이','단무지','매실','얼갈이','치커리','참나물','피클','돌나물','파프리카','취나물','세발','쌈','미나리','새싹','땡초','쑥갓','콜리','봄동','채소','가지','상추','샐러드','양배추','가지','허브','버섯','청경채','냉이','달래','오이','콩나물','부추','깻잎','고추','배추','브로콜리','봄동','시금치', '명이']))
뿌리류 = list(set(['콘' '비트','옹심이','치킨무','말랭이무침','무생채','열무','구구마','무쌈','쌈무','열무','무나물','무말랭이','홍삼','무김치','당근','옥수수','더덕','토란','고구마','마늘','우엉','감자','도라지','갈릭','연근','포테이토','생강']))
해조류 = list(set(['톳','매생이','해초','김주먹밥','다시마','파래','미역','충무김','김구이','꼬시래기','김자반','김가루','곰피']))
면류 = list(set(['옹심이', '펜네' ,'쫄면', '소면','라면','우동','당면','국수','냉면','마제소바','마카로니','짬뽕','수제비','김말이', "잡채"]))
갑각류 = list(set(['멘보샤 ','새우','꽃게','크랩','크래미','게살', '쉬림프']))
계란류 = list(set(['오므라이스','메추리알','에그','계란','달걀','스크램']))
떡류 = list(set(['빈대떡','떡국','새알','인절미','증편','어떡햄','절편','떡볶이','떡잡채','조랭이','소떡소떡']))
유제품 = list(set([ '프로바이오틱' , '요플레' ,'그라탕' , '그라탱','플레인','요거트','요구르트','치즈','버터','우유','두유']))
만두류 = list(set(['춘권','비빔만두','통만두','맑은만두','완자','물만두','만두찜','쌈만두','야채만두','찜만두','당면계란만두','갈비통통만두','만둣국','만두국','교자만두','물만두탕수','군만두']))
간식류 = list(set(['연유버터베이글 ','바나나와플','아이스슈','씨리얼', '시리얼','애플파이','치즈팡샌드','트위스터버거','붕어빵','카스텔라','호빵','크로아상샌드위치','커피','살라미샌드위치','바나나시나몬토스트','햄야채샌드','조각티라미','롤케익','고구마고로케','고구마치즈빵','삼색샌드위치','꿀호떡','비엘티샌드위치','마약토스트','탱크보이','호떡맥모닝','츄러스채소맛탕','아메리카노','쿠키','버거','베이컨맥모닝','스틱치즈케익','갈릭파이','영양모듬견과','식빵','생크림와플','남친샌드위치','인절미토스트','인절미츄러스맛탕','오렌지케익빵','피자빵','페스츄리','호떡','고구마치즈빵','수제마늘바게트','모닝샌드','주스','식빵피자','살라미샌드위치','파르페','애플파이','복숭아아이스티','팝콘','찐빵','꿀호떡','도너츠','핫도그','맥모닝','도넛','바나나시나몬토스트','치즈베이글','생크림단팥빵','미니햄버거','찹쌀호떡','컵케익','고로케','호두견과','식혜','모닝롤','머핀','홍루이젠','화채','카스테라','프렌치토스트','푸딩','시나몬페스츄리','아이스티','소보루빵','식빵','피자','케익','케이크','호빵']))
과일류 = list(set(['두부카프레제', "카프레제샐러드",'과일','유자','레몬','매실','참외','살구','홍시','오미자','배','복숭아','블루베리','포도','청포도','바나나','망고','오렌지','애플망고','홍시','건포도','코코넛','레몬','단감','크랜베리','적포도','사과','키위','라즈베리','살구','딸기','파인애플','황도','수박','토마토', '화채']))
food_material = [견과및두류,묵류,어패류,육류,채소류,뿌리류,해조류,면류,갑각류,계란류,떡류,유제품,만두류,간식류,과일류]

# 괄호 제거 함수
def bracket_remover(x):
    import re
    pattern1 = r'\([^)]*\)'
    pattern2 = r'\<[^>]*\>'
    text = re.sub(pattern=pattern1, repl='', string= x)
    text = re.sub(pattern=pattern2, repl='', string= text)
#     text = re.sub("/", repl=' ', string= text)
    return text.split()

# * 제거 함수
def star_remove(x):
    for menu in x:
        if menu.startswith("*"):
            x.remove(menu)
        elif "*" in menu:
            x[x.index(menu)] = menu.split("*")[0]
        elif "&" in menu:
            x[x.index(menu)] = menu.split("&")[0]
    return x

# 메뉴에서 '쌀밥류' 통일 및 쌀밥/다른메뉴 분리
def rice_sort(x): 
    for menu in x: 
        if (menu.startswith('쌀밥')) or (menu.startswith('흑미밥')):
            if ("/" not in menu):
                x[x.index(menu)] = "(쌀밥류)"
            elif ("/" in menu):
                temp = menu.split("/")
                for temps in temp:
                    if "밥" in temps:
                        temp[temp.index(temps)] = "(쌀밥류)"
                    else:
                        pass
                x.extend(temp)
                x.remove(menu)
        elif ("작은밥" in menu) or ("추가밥" in menu):
            if ("/" not in menu):
                x.remove(menu)
            elif ("/" in menu):
                temp = menu.split("/")
                for temps in temp:
                    if (temps == "작은밥") or (temps == "추가밥"):
                        temp.remove(temps)
                    else:
                        pass
                x.extend(temp)
                x.remove(menu)
        elif menu.endswith("짬뽕"):
            x[x.index(menu)] = "(국수류)"
        elif ("비빔밥" in menu) or ("볶음밥" in menu) or ("필라프" in menu) or ("콩나물밥" in menu):
            x[x.index(menu)] = "(비빔밥볶음밥류)"
        elif (menu.endswith("덮밥")) or (menu.endswith("국밥")):
            x[x.index(menu)] = "(덮밥국밥류)"
        elif (menu.endswith("김밥")) or (menu.endswith("초밥")) or (menu.endswith("주먹밥")):
            x[x.index(menu)] = "(김초밥류)"
    return x

# 국탕찌개류 -> (국탕찌개류)로 변경
def soup_sort(x):
    for menu in x:
        if (menu.endswith('국')) or (menu.endswith('탕')) or (menu.endswith('개장')) or (menu.endswith('미소시루')):
            x[x.index(menu)] = "(국탕류)"
        elif (menu.endswith('찌개')):
            x[x.index(menu)] = "(찌개류)"
        elif "스프" in menu:
            x[x.index(menu)] = "(스프류)"     
        elif (menu.endswith('죽')):
            x[x.index(menu)] = "(죽류)"
    return x

# 김치류 -> (김치류)로 변경
def kimchi_sort(x):
    for menu in x:
        if ("김치" in menu) or ("깍두기" in menu) or ("석박지" in menu) or ("겉절이" in menu):
            if ("/" not in menu):
                x[x.index(menu)] = "(김치류)"
            elif ("/" in menu):
                temp = menu.split("/")
                for temps in temp:
                    if ("김치" in temps[-2:]) or ("깍두기" in temps[-3:]) or ("석박지" in temps[-3:]) or ("겉절이" in temps[-3:]):
                        temp[temp.index(temps)] = "(김치류)"
                    else:
                        pass
                x.extend(temp)
                x.remove(menu)
    return x

# 샐러드류 -> (샐러드류)로 변경
def salad_sort(x):
    for menu in x:
        if ("샐러드" in menu) and ("파스타" not in menu):
            if "/" in menu:
                temp = menu.split("/")
                for temps in temp:
                    if temps.endswith("샐러드"):
                        temp[temp.index(temps)] = "(샐러드류)"
                    else:
                        pass
                x.extend(temp)
                x.remove(menu)
            else: 
                x[x.index(menu)] = "(샐러드류)"
    return x

# 튀김 -> (튀김류)로 변경
def fry_sort(x):
    for menu in x:
        check = 0
        for fry in ["튀김", "까스", "가스", "김말이", "강정", "커틀렛"]:
            if "튀김우동" in menu:
                x.append("(튀김류)")
                break
            elif (fry in menu) and ("/" in menu):
                temp = menu.split("/")
                for temps in temp:
                    if temps.endswith(fry):
                        temp[temp.index(temps)] = "(튀김류)"
                    else:
                        pass
                x.extend(temp)
                x.remove(menu)
                break
            elif menu.endswith(fry):
                x[x.index(menu)] = "(튀김류)"
                break
    return x

# 전 -> (전류)
def pancake_sort(x):
    for menu in x:
        if (menu.endswith('전')) or (menu.endswith('전병')):
            x[x.index(menu)] = "(전류)"
        elif ("전병" in menu) or ("계란말이" in menu):
            x[x.index(menu)] = "(전류)"
    return x

# 찜 -> (찜류)
def zzim_sort(x):
    for menu in x:
        if ("찜" in menu) or ("탕수" in menu):
            if "/"  not in menu:
                x[x.index(menu)] = "(찜류)"
            else:
                temp = menu.split("/")
                for temps in temp:
                    if "찜" in temps:
                        temp[temp.index(temps)] = "(찜류)"
                    else:
                        pass
                x.extend(temp)
                x.remove(menu)
    return x

# 만두 -> 찜과 튀김 분류
def mandu_sort(x):
    for menu in x:
        if ("만두" in menu) or ("딤섬" in menu):
            temp = 0
            for word in ["물", "찐", "왕", "감자", "메밀", "부추", "딤섬"]:
                if word not in menu:
                    temp += 1
            if temp ==6:
                x[x.index(menu)] = "(튀김류)"
            elif temp >0:
                x[x.index(menu)] = "(찜류)"
    return x

# 볶음 -> (볶음류)
def stirfry_sort(x):
    for menu in x:
        if ("볶음" in menu) and ("밥" not in menu):
            if "/"  not in menu:
                x[x.index(menu)] = "(볶음류)"
            else:
                temp = menu.split("/")
                for temps in temp:
                    if "볶음" in temps:
                        temp[temp.index(temps)] = "(볶음류)"
                    else:
                        pass
                x.extend(temp)
                x.remove(menu)
        elif "불고기" in menu:
            x[x.index(menu)] = "(볶음류)"
    return x

# 조림 -> (조림류)
def boiled_sort(x):
    for menu in x:
        if ("조림" in menu):
            x[x.index(menu)] = "(조림류)"
    return x

# 구이 -> (구이류)
def goo2_sort(x):
    for menu in x:
        if ("구이" in menu):
            x[x.index(menu)] = "(구이류)"
        elif menu.endswith('데리야끼'):
            x[x.index(menu)] = "(구이류)"
    return x

# 무침 -> (무침류)
def mix_sort(x):
    for menu in x:
        if ("무침" in menu) or ("잡채" in menu) or ("나물" in menu) or ("생채" in menu) or ("오복지" in menu):
            if ("/" not in menu) and ("밥" not in menu):
                x[x.index(menu)] = "(무침류)"
            elif ("/" in menu):
                temp = menu.split("/")
                for temps in temp:
                    if ("무침" in menu) or ("잡채" in menu) or ("나물" in menu) or ("생채" in menu) or ("오복지" in menu):
                        temp[temp.index(temps)] = "(무침류)"
                    else:
                        pass
                x.extend(temp)
                x.remove(menu)
    return x

# 치킨 포함 단어 분류
def chicken_sort(x):
    for menu in x:
        if "치킨무" in menu:
            if ("/" not in menu):
                x[x.index(menu)] = "(장아찌류)"
            elif ("/" in menu):
                temp = menu.split("/")
                for temps in temp:
                    if temps == "치킨무":
                        temp[temp.index(temps)] = "(장아찌류)"
                    else:
                        pass
                x.extend(temp)
                x.remove(menu)
        elif (menu.endswith('치킨')) or (menu.endswith('파닭')) or (menu.endswith('통닭')):
                x[x.index(menu)] = "(튀김류)"
        elif (menu.startswith('치킨')) and ("밥" not in menu) and ("퀘사디야" not in menu):
                x[x.index(menu)] = "(튀김류)"
        elif ("닭갈비" in menu) and ("밥" not in menu):
            x[x.index(menu)] = "(볶음류)"
    return x

#음료-> (음료)
def drink_sort(x):
    for menu in x:
        if ("주스" in menu) or ("쥬스" in menu) or ("음료" in menu) or ("식혜" in menu) or ("차" in menu) or ("에이드" in menu) or ("즙" in menu) or ("아이스티" in menu) or ("두유" in menu):
            if ("/" not in menu):
                x[x.index(menu)] = "(음료)"
            elif ("/" in menu):
                temp = menu.split("/")
                for temps in temp:
                    if ("주스" in temps[-2:]) or ("쥬스" in temps[-2:]) or ("음료" in temps[-2:]) or ("식혜" in temps[-2:]) or ("차" in temps[-2:]) or ("에이드" in temps[-3:]) or ("즙" in temps[-1:]) or ("아이스티" in temps[-4:]) or ("두유" in temps[-3:]):
                        temp[temp.index(temps)] = "(음료)"
                    else:
                        pass
                x.extend(temp)
                x.remove(menu)
    return x

#유제품-> (유제품)
def milk_sort(x):
    for menu in x:
        if ("요플레" in menu) or ("요거트" in menu) or ("요구르트" in menu):
            if ("/" not in menu) & ("D" not in menu) & ("파르페" not in menu):
                x[x.index(menu)] = "(유제품)"
            elif ("/" in menu):
                temp = menu.split("/")
                for temps in temp:
                    if ("D" in temps) or ('푸딩' in temps) or ("파르페" in temps) :
                        pass
                    else:
                        temp[temp.index(temps)] = "(유제품)"
                x.extend(temp)
                x.remove(menu)
    return x

# 절임 -> 장아찌류
def zzul_im_sort(x):
    for menu in x:
        if ("절임" in menu) or ("장아찌" in menu) or ("짱아찌" in menu) or ("피클" in menu) or ("단무지" in menu):
            if ("/" not in menu):
                x[x.index(menu)] = "(장아찌류)"
            elif ("/" in menu):
                temp = menu.split("/")
                for temps in temp:
                    if (temps == "쌈무") or (temps == "무쌈") or (temps == "락교"):
                        temp.remove(temps)
                    elif ("절임" in menu) or ("장아찌" in menu) or ("짱아찌" in menu) or ("피클" in menu) or ("단무지" in menu):
                        temp[temp.index(temps)] = "(장아찌류)"
                    else:
                        pass
                x.extend(temp)
                x.remove(menu)
        elif ("쌈무" in menu) or ("무쌈" in menu) or ("락교" in menu):
            if ("/" not in menu):
                x[x.index(menu)] = "(장아찌류)"
            elif ("/" in menu):
                temp = menu.split("/")
                for temps in temp:
                    if ("쌈무" in menu) or ("무쌈" in menu) or ("락교" in menu):
                        temp[temp.index(temps)] = "(장아찌류)"
                    else:
                        pass
                x.extend(temp)
                x.remove(menu)
    return x

# 빵류 -> 빵
def bread_sort(x):
    for menu in x:
        if ("빵" in menu) or ("핫도그" in menu) or ("피자" in menu) or ("또띠아" in menu) or ("케익" in menu) or ("칩" in menu):
            if ("," not in menu) and ("/" not in menu):
                x[x.index(menu)] = "(빵과자류)"
            elif ("," in menu):
                temp = menu.split(",")
                for temps in temp:
                    if ("빵" in menu) or ("핫도그" in menu) or ("피자" in menu) or ("또띠아" in menu) or ("케익" in menu) or ("칩" in menu) :
                        temp[temp.index(temps)] = "(빵과자류)"
                    else:
                        pass
                x.extend(temp)
                x.remove(menu)
            elif ("/" in menu):
                temp = menu.split("/")
                for temps in temp:
                    if ("빵" in menu) or ("핫도그" in menu) or ("피자" in menu) or ("또띠아" in menu) or ("케익" in menu) or ("칩" in menu):
                        temp[temp.index(temps)] = "(빵과자류)"
                    else:
                        pass
                x.extend(temp)
                x.remove(menu)
    return x

#떡볶이-> (볶음류)
def dduk_sort(x):
    for menu in x:
        if ("볶이" in menu) :
            if ("/" not in menu):
                x[x.index(menu)] = "(볶음류)"
            elif ("/" in menu):
                temp = menu.split("/")
                for temps in temp:
                    if ("볶이" not in menu) :
                        pass
                    elif ("볶이" in menu):
                        temp[temp.index(temps)] = "(볶음류)"
                x.extend(temp)
                x.remove(menu)
    return x

# 모든 메뉴 한 리스트에 모으기
def all_menu_list(a, b):
    from iteration_utilities import flatten
    temp = a.tolist() + b.tolist()
    temp = list(set(flatten(temp)))
    return temp

# dataframe에 적용하여 메뉴별 벡터 생성하기 위한 함수
# dic에는 분류하고 싶은 사전 넣어줘야함 (ex. dic = dict_rice)
def class_major(menu, dic):
    import numpy as np
    rice_dum = list(np.zeros(len(dic)))
    for bab in menu:
        for key in dic.keys():
            if bab in dic[key]:
                rice_dum[list(dic.keys()).index(key)]  = 1
    return rice_dum

# class_major와 함께 사용, 각 메뉴별 벡터를 데이터프레임에 추가
# df에는 어느 데이터프레임에 concat할 것인지 입력해야함
def to_dataframe(x, df):
    import numpy as np
    import pandas as pd
    temp = []
    for lists in x:
        temp += lists
    temp = np.asarray(temp)
    temp = temp.reshape(len(df),-1)
    temp = pd.DataFrame(temp)
    return temp

####################################### 아래는 조대리가 생성한 함수 #######################################
def del_bracket(data):
    import re
    x = []
    for i in data:
        p = re.sub(r'\([^)]*\)',"",i)
        p = re.sub(r'\<[^)]*\>',"",p)
        p = re.findall('[가-힣|a-z|A-Z|ㄱ-ㅎ|*]+',p)
        p = ' '.join(p)
        x.append(p)
        
    return x

def change_column(t,x):
    k = del_bracket(t[x].tolist())
    del t[x]
    t[x] = k
    
def sauce_punish(data):
    sauce_1 = {}
    for i in range(len(data)):
        x = data[i].split()
        k = ''
        for j in range(len(x)):
            temp = False
            if '*' in x[j]:
                t = x[j].split('*')
                
                x[j] = t[0]
                
                if k == '':
                    k += ' '.join(t[1:])
                else:
                    k += ','
                    k += ' '.join(t[1:])
        
        sauce_1[i] = k
    
        data[i] = ' '.join(x)
        
    sauce = {}
    for i,v in sauce_1.items():
        if v != '':
            sauce[i] = v
            
    return sauce, data

def make_sauce(data):
    temp = data.copy()

    hihi = ['조식','중식','석식']
    for i in hihi:        
        train_bf = temp['{}메뉴'.format(i)].tolist()
        sauce, data = sauce_punish(train_bf)

        temp['{}메뉴'.format(i)] = data
        temp['소스 여부({})'.format(i)] = 0
        temp['소스 종류({})'.format(i)] = 0
        temp['소스 여부({})'.format(i)].iloc[list(sauce.keys())] = 1
        temp['소스 종류({})'.format(i)].iloc[list(sauce.keys())] = list(sauce.values())
    
    return temp

def Show10(menu):
    cnt = 0
    while True:
        x = input("엔터를 입력하세요")
        del x
        print("{} ~ {}".format(cnt, cnt+10))
        print(menu[cnt:cnt+10])
        cnt += 10
    
        if cnt >= len(menu):
            break

