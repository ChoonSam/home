from flask import Flask, render_template, request
from konlpy.tag import Komoran
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
import csv

app = Flask(__name__)

@app.route('/')
def basic():
    return render_template("main.html")
    
@app.route('/applysearch', methods = ['POST', 'GET'])
def apply():
    Location = request.args.get("location")
    komoran = Komoran(userdic='user.dic')
    lst = []

    #sys.stdout = open('mmmm.txt', 'w')
    nnn = pd.read_csv("C:/Users/장준하/Desktop/대학/호서대/4학년/2학기/Comfortraval/nnnn.csv", encoding='utf-8')

    try :
        f = open("C:/Users/장준하/Desktop/대학/호서대/4학년/2학기/Comfortraval//검색어추출.txt", 'r', encoding='utf-8')
        data = f.readline()
        LineNumber = 1
        search = request.args.get("location")
        counting1 = data.count(search)
        lst.append(counting1)
    
        for Line in f:
            counting2 = (Line.count(search))
            lst.append(counting2)
        f.close()
    except :
        print("None File")

    idx = lst.index(max(lst))
    car = (nnn.iloc[[idx]])
    car.to_csv("검색어.csv", encoding='utf-8-sig')
    sl = []
    with open("D:/visual code/검색어.csv", 'rt', encoding='utf-8')as f:
        dt = csv.reader(f)
        ylst = list(dt)
        pt = ylst[1][1]

##########################################################################################################

    df2 = pd.read_csv("C:/Users/장준하/Desktop/대학/호서대/4학년/2학기/Comfortraval//dataset.csv")

    tfidf = TfidfVectorizer(stop_words='english')

    tfidf_matrix = tfidf.fit_transform(df2['content'])

    cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)

    indices = pd.Series(df2.index, index=df2['destination']).drop_duplicates()

    def get_recommendations(destination, cosine_sim=cosine_sim):
        idx = indices[destination]
    
        sim_scores = list(enumerate(cosine_sim[idx]))
    
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    
        sim_scores = sim_scores[0:10]
    
        destination_indices = [i[0] for i in sim_scores]
    
        return df2['destination'].iloc[destination_indices]

    ghj = get_recommendations(pt)
    ghj.to_csv("결과값.csv", encoding='utf-8-sig')

    with open("D:/visual code/결과값.csv", 'rt', encoding='utf-8')as h:
            bb = csv.reader(h)
            ppp = list(bb)
            bbbb = int(ppp[1][0]) + 1
            dddd = int(ppp[2][0]) + 1
            eeee = int(ppp[3][0]) + 1
            gggg = int(ppp[4][0]) + 1
            iiii = int(ppp[5][0]) + 1
            jjjj = int(ppp[6][0]) + 1
            kkkk = int(ppp[7][0]) + 1
            llll = int(ppp[8][0]) + 1
            mmmm = int(ppp[9][0]) + 1
            nnnn = int(ppp[10][0]) + 1
            with open("C:/Users/장준하/Desktop/대학/호서대/4학년/2학기/Comfortraval//dataset.csv", 'rt', encoding='utf-8')as a:
                tt = csv.reader(a)
                lll = list(tt)
                b = lll[int(bbbb)][2]
                d = lll[int(dddd)][2]
                e = lll[int(eeee)][2]
                g = lll[int(gggg)][2]
                i = lll[int(iiii)][2]
                j = lll[int(jjjj)][2]
                k = lll[int(kkkk)][2]
                l = lll[int(llll)][2]
                m = lll[int(mmmm)][2]
                n = lll[int(nnnn)][2]
    
            return render_template('result.html', ppp=ppp, lll=lll, b=b, d=d, e=e, g=g, i=i, j=j, k=k, l=l, m=m, n=n)

@app.route('/63스퀘어')
def a():
    return render_template('63스퀘어.html')

@app.route('/강서한강공원')
def b():
    return render_template('강서한강공원.html')

@app.route('/검단산')
def c():
    return render_template('검단산.html')

@app.route('/경기도사격테마파크')
def d():
    return render_template('경기도사격테마파크.html')

@app.route('/경복궁')
def e():
    return render_template('경복궁.html')

@app.route('/고대산자연휴양림')
def f():
    return render_template('고대산자연휴양림.html')

@app.route('/고양생태공원')
def g():
    return render_template('고양생태공원.html')

@app.route('/고척스카이돔')
def h():
    return render_template('고척스카이돔.html')

@app.route('/곤충테마파크')
def i():
    return render_template('곤충테마파크.html')

@app.route('/과천서울랜드')
def j():
    return render_template('과천서울랜드.html')

@app.route('/광교호수공원')
def k():
    return render_template('광교호수공원.html')

@app.route('/광나루한강공원')
def l():
    return render_template('광나루한강공원.html')

@app.route('/광릉')
def m():
    return render_template('광릉.html')

@app.route('/광명동굴')
def n():
    return render_template('광명동굴.html')

@app.route('/광장시장')
def o():
    return render_template('광장시장.html')

@app.route('/광화문광장')
def p():
    return render_template('광화문광장.html')

@app.route('/국립과천과학관')
def q():
    return render_template('국립과천과학관.html')

@app.route('/국립생물자원관')
def r():
    return render_template('국립생물자원관.html')

@app.route('/국립수목원')
def s():
    return render_template('국립수목원.html')

@app.route('/국립운악산자연휴양림')
def t():
    return render_template('국립운악산자연휴양림.html')

@app.route('/국립중앙박물관')
def u():
    return render_template('국립중앙박물관.html')

@app.route('/국립한글박물관')
def v():
    return render_template('국립한글박물관.html')

@app.route('/국립현대미술관(과천)')
def w():
    return render_template('국립현대미술관(과천).html')

@app.route('/국립현대미술관(덕수궁)')
def x():
    return render_template('국립현대미술관(덕수궁).html')

@app.route('/국립현대미술관(서울)')
def y():
    return render_template('국립현대미술관(서울).html')

@app.route('/국회의사당')
def z():
    return render_template('국회의사당.html')

@app.route('/김포국제조각공원')
def aa():
    return render_template('김포국제조각공원.html')

@app.route('/김포아트빌리지')
def ab():
    return render_template('김포아트빌리지.html')

@app.route('/김포장릉')
def ac():
    return render_template('김포장릉.html')

@app.route('/낙상공원')
def ad():
    return render_template('낙상공원.html')

@app.route('/난지 한강공원')
def ae():
    return render_template('난지한강공원.html')

@app.route('/남대문시장')
def af():
    return render_template('남대문시장.html')

@app.route('/남산골한옥마을')
def ag():
    return render_template('남산골한옥마을.html')

@app.route('/남산서울타워')
def ah():
    return render_template('남산서울타워.html')

@app.route('/농업생태원')
def ai():
    return render_template('농업생태원.html')

@app.route('/누들플랫폼')
def aj():
    return render_template('누들플랫폼.html')

@app.route('/누리천문대')
def ak():
    return render_template('누리천문대.html')

@app.route('/대불호텔전시관')
def al():
    return render_template('대불호텔전시관.html')

@app.route('/대한민국역사박물관')
def am():
    return render_template('대한민국역사박물관.html')

@app.route('/덕소자연사박물관')
def an():
    return render_template('덕소자연사박물관.html')

@app.route('/덕수궁')
def ao():
    return render_template('덕수궁.html')

@app.route('/덕포진')
def ap():
    return render_template('덕포진.html')

@app.route('/도라전망대')
def aq():
    return render_template('도라전망대.html')

@app.route('/동대문디지털플라자')
def ar():
    return render_template('동대문디지털플라자.html')

@app.route('/동대문종합시장')
def at():
    return render_template('동대문종합시장.html')

@app.route('/동묘벼룩시장')
def au():
    return render_template('동묘벼룩시장.html')

@app.route('/돼지박물관')
def av():
    return render_template('돼지박물관.html')

@app.route('/뚝섬한강공원')
def aw():
    return render_template('뚝섬한강공원.html')

@app.route('/롯데월드')
def ax():
    return render_template('롯데월드.html')

@app.route('/마로니에공원')
def ay():
    return render_template('마로니에공원.html')

@app.route('/망원시장')
def az():
    return render_template('망원시장.html')

@app.route('/망원한강공원')
def ba():
    return render_template('망원한강공원.html')

@app.route('/명동성당')
def bb():
    return render_template('명동서당.html')

@app.route('/몽촌토성')
def bc():
    return render_template('몽촌토성.html')

@app.route('/문래창작촌')
def bd():
    return render_template('문래창작촌.html')

@app.route('/문수산성')
def be():
    return render_template('문수산성.html')

@app.route('/문화비축기지')
def bf():
    return render_template('문화비축기지.html')

@app.route('/민주화기념공원')
def bg():
    return render_template('민주화기념공원.html')

@app.route('/반포한강공원')
def bh():
    return render_template('반포한강공원.html')

@app.route('/베어스타운')
def bi():
    return render_template('베어스타운.html')

@app.route('/보신각')
def bj():
    return render_template('보신각.html')

@app.route('/봉녕사')
def bk():
    return render_template('봉녕사.html')

@app.route('/봉선사')
def bl():
    return render_template('봉선사.html')

@app.route('/부천로보파크')
def bm():
    return render_template('부천로보파크.html')

@app.route('/부천자연생태공원')
def bn():
    return render_template('부천자연생태공원.html')

@app.route('/부천천문과학관')
def bo():
    return render_template('부천천문과학관.html')

@app.route('/북촌한옥마을')
def bp():
    return render_template('북촌한옥마을.html')

@app.route('/북한산국립공원')
def bq():
    return render_template('북한산국립공원.html')

@app.route('/불암산')
def br():
    return render_template('불암산.html')

@app.route('/사기막골도예촌')
def bs():
    return render_template('사기막골도예촌.html')

@app.route('/사릉')
def bt():
    return render_template('사릉.html')

@app.route('/삼성미술관리움')
def bu():
    return render_template('삼성미술관리움.html')

@app.route('/상동호수공원')
def bv():
    return render_template('상동호수공원.html')

@app.route('/상암DMC')
def bw():
    return render_template('상암DMC.html')

@app.route('/서대문형무소역사관')
def bx():
    return render_template('서대문형무소역사관.html')

@app.route('/서래마을')
def by():
    return render_template('서래마을.html')

@app.route('/서삼릉')
def bz():
    return render_template('서삼릉.html')

@app.route('/서오릉')
def ca():
    return render_template('서오릉.html')

@app.route('/서운동산')
def cb():
    return render_template('서운동산.html')

@app.route('/서울광장')
def cc():
    return render_template('서울광장.html')

@app.route('/서울대공원')
def cd():
    return render_template('서울대공원.html')

@app.route('/서울숲공원')
def ce():
    return render_template('서울숲공원.html')

@app.route('/서울식물원')
def cf():
    return render_template('서울식물원.html')

@app.route('/서울월드컵경기장')
def cg():
    return render_template('서울월드컵경기장.html')

@app.route('/서울중앙성원')
def ch():
    return render_template('서울중앙성원.html')

@app.route('/서울풍물시장')
def ci():
    return render_template('서울풍물시장.html')

@app.route('/서해수호관')
def cj():
    return render_template('서해수호관.html')

@app.route('/서희테마파크')
def ck():
    return render_template('서희테마파크.html')

@app.route('/석촌호수공원')
def cl():
    return render_template('석촌호수공원.html')

@app.route('/석파정서울미술관')
def cm():
    return render_template('석파정서울미술관.html')

@app.route('/선바위미술관')
def cn():
    return render_template('선바위미술관.html')

@app.route('/세븐럭카지노')
def co():
    return render_template('세븐럭카지노.html')

@app.route('/세종대왕기념관')
def cp():
    return render_template('세종대왕기념관.html')

@app.route('/세종대왕유적관리소')
def cq():
    return render_template('세종대왕유적관리소.html')

@app.route('/세종문화회관')
def cr():
    return render_template('세종문화회관.html')

@app.route('/송도센트럴파크')
def cs():
    return render_template('송도센트럴파크.html')

@app.route('/수리산도립공원')
def ct():
    return render_template('수리산도립공원.html')

@app.route('/수원컨벤션센터')
def cu():
    return render_template('수원컨벤션센터.html')

@app.route('/수원화성')
def cv():
    return render_template('수원화성.html')

@app.route('/숭례문')
def cw():
    return render_template('숭례문.html')

@app.route('/스타필드하남')
def cx():
    return render_template('스타필드하남.html')

@app.route('/신륵사')
def cy():
    return render_template('신륵사.html')

@app.route('/실학박물관')
def cz():
    return render_template('실학박물관.html')

@app.route('/아라마리나')
def da():
    return render_template('아라마리나.html')

@app.route('/아라폭포')
def db():
    return render_template('아라폭포.html')

@app.route('/아쿠아플라넷')
def dc():
    return render_template('아쿠아플라넷.html')

@app.route('/아해박물관')
def dd():
    return render_template('아해박물관.html')

@app.route('/안성3·1운동기념관')
def de():
    return render_template('안성3·1운동기념관.html')

@app.route('/안성천문대')
def df():
    return render_template('안성천문대.html')

@app.route('/안성팜랜드')
def dg():
    return render_template('안성팜랜드.html')

@app.route('/애기봉평화생태공원')
def dh():
    return render_template('애기봉평화생태공원.html')

@app.route('/양재시민의숲')
def di():
    return render_template('양재시민의숲.html')

@app.route('/양화한강공원')
def dj():
    return render_template('양화한강공원.html')

@app.route('/어린이대공원')
def dk():
    return render_template('어린이대공원.html')

@app.route('/에버랜드')
def dl():
    return render_template('에버랜드.html')

@app.route('/여의도한강공원')
def dm():
    return render_template('여의도한강공원.html')

@app.route('/여주시립폰박물관')
def dn():
    return render_template('여주시립폰박물관.html')

@app.route('/연천전곡리유적')
def do():
    return render_template('연천전곡리유적.html')

@app.route('/영종씨사이드파크')
def dp():
    return render_template('영종씨사이드파크.html')

@app.route('/예술공간봄(행궁동벽화마을)')
def dq():
    return render_template('예술공간봄(행궁동벽화마을).html')

@app.route('/예술의전당')
def dr():
    return render_template('예술의전당.html')

@app.route('/올림픽공원')
def ds():
    return render_template('올림픽공원.html')

@app.route('/와우목장')
def dt():
    return render_template('와우목장.html')

@app.route('/용인농촌테마파크')
def du():
    return render_template('용인농촌테마파크.html')

@app.route('/용인자연휴양림')
def dv():
    return render_template('용인자연휴양림.html')

@app.route('/우리꽃식물원')
def dw():
    return render_template('우리꽃식물원.html')

@app.route('/원마운트')
def dx():
    return render_template('원마운트.html')

@app.route('/윤동주문학관')
def dy():
    return render_template('윤동주문학관.html')

@app.route('/융릉,건릉')
def dz():
    return render_template('윤릉,건릉.html')

@app.route('/을왕리,왕산해수욕장')
def ea():
    return render_template('을왕리,왕산해수욕장.html')

@app.route('/이천세라피아')
def eb():
    return render_template('이천세라피아.html')

@app.route('/이천시립박물관')
def ec():
    return render_template('이천시립박물관.html')

@app.route('/이촌한강공원')
def ed():
    return render_template('이촌한강공원.html')

@app.route('/익선동한옥마을')
def ee():
    return render_template('익선동한옥마을.html')

@app.route('/인천개항박물관')
def ef():
    return render_template('인천개항박물관.html')

@app.route('/인천대교기념관')
def eg():
    return render_template('인천대교기념관.html')

@app.route('/자유공원')
def eh():
    return render_template('자유공원.html')

@app.route('/잠실종합운동장')
def ei():
    return render_template('잠실종합운동장.html')

@app.route('/잠실한강공원')
def ej():
    return render_template('잠실한강공원.html')

@app.route('/잠원한강공원')
def ek():
    return render_template('잠원한강공원.html')

@app.route('/장충체육관')
def el():
    return render_template('장충체육관.html')

@app.route('/전쟁기념관')
def em():
    return render_template('전쟁기념관.html')

@app.route('/정동제일교회')
def en():
    return render_template('정동제일교회.html')

@app.route('/제암리3.1운동순국기념관')
def eo():
    return render_template('제암리3.1운동순국기념관.html')

@app.route('/조계사')
def ep():
    return render_template('조계사.html')

@app.route('/조류생태과학관')
def eq():
    return render_template('조류생태과학관.html')

@app.route('/종묘')
def er():
    return render_template('종묘.html')

@app.route('/주렁주렁')
def es():
    return render_template('주렁주렁.html')

@app.route('/짚라인')
def et():
    return render_template('짚라인.html')

@app.route('/차이나타운')
def eu():
    return render_template('차이나타운.html')

@app.route('/창경궁')
def ev():
    return render_template('창경궁.html')

@app.route('/창덕궁')
def ew():
    return render_template('창덕궁.html')

@app.route('/천마산')
def ex():
    return render_template('천마산.html')

@app.route('/철도박물관')
def ey():
    return render_template('철도박물관.html')

@app.route('/철쭉동산')
def ez():
    return render_template('철쭉동산.html')

@app.route('/청와대사랑채')
def fa():
    return render_template('청와대사랑채.html')

@app.route('/초막골생태공원')
def fb():
    return render_template('초막골생태공원.html')

@app.route('/추사박물관')
def fc():
    return render_template('추사박물관.html')

@app.route('/축령산자연휴양림')
def fd():
    return render_template('축령산자연휴양림.html')

@app.route('/커먼그라운드')
def fe():
    return render_template('커먼그라운드.html')

@app.route('/코엑스')
def ff():
    return render_template('코엑스.html')

@app.route('/타임스퀘어')
def fg():
    return render_template('타임스퀘어.html')

@app.route('/탑골공원')
def fh():
    return render_template('탑골공원.html')

@app.route('/통인시장')
def fi():
    return render_template('통인시장.html')

@app.route('/트라이보울')
def fj():
    return render_template('트라이보울.html')

@app.route('/평화시장')
def fk():
    return render_template('평화시장.html')

@app.route('/포천아트밸리')
def fl():
    return render_template('포천아트밸리.html')

@app.route('/푸른수목원')
def fm():
    return render_template('푸른수목원.html')

@app.route('/플라이스테이션')
def fn():
    return render_template('플라이스테이션.html')

@app.route('/하남역사박물관')
def fo():
    return render_template('하남역사박물관.html')

@app.route('/하남유니온파크')
def fp():
    return render_template('하남유니온파크.html')

@app.route('/하남종합운동장')
def fq():
    return render_template('하남종합운동장.html')

@app.route('/하이브인사이트')
def fr():
    return render_template('하이브인사이트.html')

@app.route('/한국근현대음악관')
def fs():
    return render_template('한국근현대음악관.html')

@app.route('/한국만화박물관')
def ft():
    return render_template('한국만화박물관.html')

@app.route('/한국민속촌')
def fu():
    return render_template('한국민속촌.html')

@app.route('/한국은행화폐박물관')
def fv():
    return render_template('한국은행화폐박물관.html')

@app.route('/한국조리박물관')
def fw():
    return render_template('한국조리박물관.html')

@app.route('/한탄강국가지질공원')
def fx():
    return render_template('한탄강국가지질공원.html')

@app.route('/한택식물원')
def fy():
    return render_template('한택식물원.html')

@app.route('/행주산성')
def fz():
    return render_template('행주산성.html')

@app.route('/허브아일랜드')
def ga():
    return render_template('허브아일랜드.html')

@app.route('/현대모터스튜디오')
def gb():
    return render_template('현대모터스튜디오.html')

@app.route('/홍유릉')
def gc():
    return render_template('홍유릉.html')

@app.route('/화성고정리공룡알화석산지')
def gd():
    return render_template('화성고정리공룡알화석산지.html')

@app.route('/흥국사(고양)')
def ge():
    return render_template('흥국사(고양).html')

@app.route('/흥국사(남양주)')
def gf():
    return render_template('흥국사(남양주).html')

@app.route('/BMW드라이빙센터')
def gg():
    return render_template('BMW드라이빙센터.html')

@app.route('/G-Tower전망대')
def gh():
    return render_template('G-Tower전망대.html')

if __name__ == '__main__':
    app.run(host='', port=5000, debug=True)