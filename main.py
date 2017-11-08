from flask import Flask,request,Response
import router
app = Flask(__name__)

Version1 = '/v1'
GetBodyHtml = '/extract/bodyhtml'
GetText = '/extract/text'
GetImage = '/extract/image'
GetInfo = '/extract/allinfo'
headers =   {   "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Headers":"Origin, X-Requested-With, Content-Type, Accept, X-ID, X-TOKEN, X-ANY-YOUR-CUSTOM-HEADER",
                "Access-Control-Allow-Methods": "POST, PUT, GET, OPTIONS, DELETE"
            }
def ResponseData(data):
    resp = Response(data)
    resp.headers=headers
    resp.headers['Content-Type']='application/json'
    return resp

@app.route(Version1+'/')
@app.route(Version1)
def ConnectTest():
    return ResponseData(router.ping())

@app.route(Version1+GetBodyHtml,methods=['GET','OPTIONS'])
def ExtractBodyHtml():
    if request.method == 'OPTIONS':
        return Response('', mimetype='application/json', headers=headers)
    if request.method == 'GET':
        if request.args.get('lan') is None :
            return ResponseData(router.extractBodyHtml(request.args.get('url')))
        else:
            return ResponseData(router.extractBodyHtml(request.args.get('url'), request.args.get('lan')))
    

@app.route(Version1+GetText, methods=['GET','OPTIONS'])
def ExtractText():
    if request.method == 'OPTIONS':
        return Response('', mimetype='application/json', headers=headers)
    if request.method == 'GET':
        if request.args.get('lan') is None :
            return ResponseData(router.extractText(request.args.get('url')))
        else:
            return ResponseData(router.extractText(request.args.get('url'), request.args.get('lan'))) 

@app.route(Version1+GetImage, methods=['GET','OPTIONS'])
def ExtractImage():
    if request.method == 'OPTIONS':
        return Response('', mimetype='application/json', headers=headers)
    if request.method == 'GET':
        if request.args.get('lan') is None :
            return ResponseData(router.extractImg(request.args.get('url')))
        else:
            return ResponseData(router.extractImg(request.args.get('url'), request.args.get('lan')))         

@app.route(Version1+GetInfo, methods=['GET','OPTIONS'])
def ExtractAllInfo():
    if request.method == 'OPTIONS':
        return Response('', mimetype='application/json', headers=headers)
    if request.method == 'GET':
        if request.args.get('lan') is None :
            return ResponseData(router.extractAllInfo(request.args.get('url')))
        else:
            return ResponseData(router.extractAllInfo(request.args.get('url'), request.args.get('lan')))         