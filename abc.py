# -*- coding: utf-8 -*-

import FXR
from FXR.lib.curve.ttypes import *
from datetime import datetime
import time,random,sys,json,codecs,threading,glob,re

#kk = FXR.LINE()
#kk.login(qr=True)
#kk.loginResult()

cl = FXR.LINE()
cl.login(token="EmJP3cTCBBbxHq0PFdBb.TOwfr+vlbbebmmu/8etFgW.Tzn0ZFqDvUXD/jWhM/c/CgsPuaiV1kssQybIx8ZbdPs=")

ki = FXR.LINE()
ki.login(token="EmgF0AVGiGl8QAfvrNhd.NxllMtv6lqmOeR+fBoKPdq.0M6yj8tTk8PF7xHSMVxBkNqUkFnNnFODTx3aeSDYd/A=")

kk = FXR.LINE()
kk.login(token="Emd0Ugxca7DreRgUPqfe.D2UjDHf7T6UbYDdb8RmhhG.jouUV0WbNd2IRveT3B1ziqb+qDqByX6NqeLp70lASoc=")

kc = FXR.LINE()
kc.login(token="EmrEJYG9GKIazvHUoTTd.5+WFW3AUqznDTUyXU1x0Fq.gG7iMVl9Lb3OFpZ2DoYovuzXfCKomEBRzLQn5ryOJrI=")


reload(sys)
print "login success"
sys.setdefaultencoding('utf-8')

helpMessage =""" 〘тєαм вσт є∂ιтє∂〙

☁̸҉̸.̸҉ =ȼ๏ʍʍąɲď β๏ţ  ̸҉̸.̸҉̸☁
[@Key,@key,@help,@Help]
[@set group]
[@bot?]
[@Creator,@creator]
[@Me]
[@Gift]
[@All gift]
[@Cancel,@cancel]
[@Open url,@open url]
[@Close url,@close url]
[Ginfo]
[@Id Group]
[@My mid]
[@Mid all]
[Wkwkwk,Wkwk,Wk,wkwkwk,wkwk,wk]
[Hehehe,Hehe,He,hehehe,hehe,he]
[Galau]
[You]
[Hadeuh]
[Please]
[Haaa]
[Lol]
[Hmmm,Hmm,Hm,hmmm,hmm,hm]
[Welcome]
[@Joinn on,@joinn on]
[@Joinn off,@joinn off]
[@Cancl on,@cancl on]
[@Cancl off,@cancl off]
[@Gr on,@gr on]
[@Gr off,@gr off]
[@Contact On,@Contact on,@contact on]
[@Contact Off,@Contact off,@contact off]
[@set view]
[@group id]
[@cancelall]
[@cctv]
[@nongol]
[@all join,@semua masuk,@pus]
[@Bye all]
[Tagall,kiwkiw,Kiwkiw,tagall]
[@Pembersihan]
[Nk ]
[@Ban @]
[@Unban @]
[@Reset,@reset]
[Copy @]
[@Up,@up,@Up Chat,@Up chat,@up chat,@Upchat,@upchat]
[@bc ]
[@list group]
[ZSIsay hi,pagi,bobo ah"]
[@PING,@Ping,@ping]
[Respon,respon,Respon Dong,respon dong]
[Respon beb]
[@speed,@speedbot]
[@bl ]
[@ban]
[@unban]
[@banlist]
[@cek ban]
[@kill ban]
[Admin add @]
[@admin remove @]
[@list admin,@adminlist]

"""

Setgroup =""" Private Menu B̳O̳T̳ L̳I̳N̳E̳ E̳D̳I̳T̳E̳D̳

[Protect Group]
-- Gr on/off
[Mid Via Contact]
 -- Contact on/off
[Cancel All Invited]
-- Cancl on/off
[No Joinned]
-- Joinn on/off
"""
#"u532647a27196dbe0b82b874e047da521"

KAC=[cl,ki,kk,kc]
DEF=[ki,kk,kc]
mid = cl.getProfile().mid
Amid = ki.getProfile().mid
Bmid = kk.getProfile().mid
Cmid = kc.getProfile().mid

Bots=[mid,Amid,Bmid,Cmid,]
admin=["u349dbde6509797ddc33adce5b85cd856","udf271394eea3e117351be4e30654140c","u97f705b63d3da6099072d4ccf6a299e2","u16bc85075e502b66e4b715069bc05cb1","ud0c9863689311b0da0c8566f4401281d","uc103c714511b0b65dc30315ec9c58f95"]
owner=["u349dbde6509797ddc33adce5b85cd856"]
wait = {
    'contact':False,
    'autoJoin':True,
    'autoCancel':{"on":True,"members":1},
    'leaveRoom':True,
    'timeline':False,
    'autoAdd':True,
    'message':"Thanks for add",
    "lang":"JP",
    "comment":"Thanks for add me",
    "commentOn":True,
    "commentBlack":{},
    "wblack":False,
    "dblack":False,
    "clock":False,
    "cName":"ZSI",
    "cName2":"ZSI2",
    "cName3":"ZSI3",
    "cName4":"ZSI4",
    "blacklist":{},
    "wblacklist":False,
    "dblacklist":False,
    "Protectgr":True,
    "Protectjoin":False,
    "Protectcancl":True,
    "protectionOn":True,
    "atjointicket":True,
    }

wait2 = {
    'readPoint':{},
    'readMember':{},
    'setTime':{},
    'ROM':{}
    }

mimic = {
    "copy":False,
    "copy2":False,
    "status":False,
    "target":{}
    }

setTime = {}
setTime = wait2['setTime']


def upload_tempimage(client):
     '''
         Upload a picture of a kitten. We don't ship one, so get creative!
     '''
     config = {
         'album': album,
         'name':  'bot auto upload',
         'title': 'bot auto upload',
         'description': 'bot auto upload'
         }

     print("Uploading image... ")
     image = client.upload_from_path(image_path, config=config, anon=False)
     print("Done")
     print()

     return image
def sendImage(self, to_, path):
      M = Message(to=to_,contentType = 1)
      M.contentMetadata = None
      M.contentPreview = None
      M_id = self.Talk.client.sendMessage(0,M).id
      files = {
         'file': open(path, 'rb'),
         }
      params = {
         'name': 'media',
         'oid': M_id,
         'size': len(open(path, 'rb').read()),
         'type': 'image',
         'ver': '1.0',
         }
      data = {
         'params': json.dumps(params)
         }
      r = self.post_content('https://os.line.naver.jp/talk/m/upload.nhn', data=data, files=files)
      if r.status_code != 201:
         raise Exception('Upload image failure.')
      return True

def sendImageWithURL(self, to_, url):
      path = '%s/pythonLine-%i.data' % (tempfile.gettempdir(), randint(0, 9))
      r = requests.get(url, stream=True)
      if r.status_code == 200:
         with open(path, 'w') as f:
            shutil.copyfileobj(r.raw, f)
      else:
         raise Exception('Download image failure.')
      try:
         self.sendImage(to_, path)
      except Exception as e:
         raise e
 
def post_content(self, urls, data=None, files=None):
        return self._session.post(urls, headers=self._headers, data=data, files=files)
def sendMessage(to, text, contentMetadata={}, contentType=0):
    mes = Message()
    mes.to, mes.from_ = to, profile.mid
    mes.text = text
    mes.contentType, mes.contentMetadata = contentType, contentMetadata
    if to not in messageReq:
        messageReq[to] = -1
    messageReq[to] += 1

def NOTIFIED_READ_MESSAGE(op):
    try:
        if op.param1 in wait2['readPoint']:
            Name = cl.getContact(op.param2).displayName
            if Name in wait2['readMember'][op.param1]:
                pass
            else:
                wait2['readMember'][op.param1] += "\n・" + Name
                wait2['ROM'][op.param1][op.param2] = "\n・" + Name
        else:
            pass
    except:
        pass

def RECEIVE_MESSAGE(op):
    msg = op.message
    try:
        if msg.contentType == 0:
            try:
                if msg.to in wait['readPoint']:
                    if msg.from_ in wait["ROM"][msg.to]:
                        del wait["ROM"][msg.to][msg.from_]
                else:
                    pass
            except:
                pass
        else:
            pass
    except KeyboardInterrupt:
	       sys.exit(0)
    except Exception as error:
        print error
        print ("\n\nRECEIVE_MESSAGE\n\n")
        return

def bot(op):
    try:
        if op.type == 0:
            return
        if op.type == 5:
            if wait["autoAdd"] == True:
                cl.findAndAddContactsByMid(op.param1)
                if (wait["message"] in [""," ","\n",None]):
                    pass
                else:
                    cl.sendText(op.param1,str(wait["message"]))

        #------Protect Group Kick start------#
        if op.type == 11:
			if wait["Protectgr"] == True:
				if op.param2 in admin:
					pass
				else:
					if op.param2 not in Bots:
						G = cl.getGroup(op.param1)
						G.preventJoinByTicket = True
						random.choice(DEF).kickoutFromGroup(op.param1,[op.param2])
						random.choice(DEF).updateGroup(G)
        #------Protect Group Kick finish-----#

        #------Cancel Invite User start------#
        if op.type == 13:
           if wait["Protectcancl"] == True:
               if op.param2 in admin:
                   pass
               else:
                   if op.param2 not in Bots:
                      group = cl.getGroup(op.param1)
                      gMembMids = [contact.mid for contact in group.invitee]
                      random.choice(DEF).cancelGroupInvitation(op.param1, gMembMids)
        #------Cancel Invite User Finish------#

        if op.type == 13:
            if mid in op.param3:
                if wait["autoJoin"] == True:
                    cl.acceptGroupInvitation(op.param1)
                    cl.inviteIntoGroup(op.param1,admin)
                    print "BOT 1 Joined"
                else:
                    print "autoJoin is Off"

            if Amid in op.param3:
                if wait["autoJoin"] == True:
                    kk.acceptGroupInvitation(op.param1)
                    kk.inviteIntoGroup(op.param1,admin)
                    print "BOT 2 Joined"
                else:
                    print "autoJoin is Off"

            if Bmid in op.param3:
                if wait["autoJoin"] == True:
                    ki.acceptGroupInvitation(op.param1)
                    ki.inviteIntoGroup(op.param1,admin)
                    print "BOT 3 Joined"
                else:
                    print "autoJoin is Off"

            if Cmid in op.param3:
                if wait["autoJoin"] == True:
                    kc.acceptGroupInvitation(op.param1)
                    kc.inviteIntoGroup(op.param1,admin)
                    print "BOT 4 Joined"
                else:
                    print "autoJoin is Off"
		
        if op.type == 13:
            if mid in op.param3:
                G = cl.getGroup(op.param1)
                if wait["autoJoin"] == True:
                    if wait["autoCancel"]["on"] == True:
                        if len(G.members) <= wait["autoCancel"]["members"]:
                            cl.rejectGroupInvitation(op.param1)
                        else:
                            cl.acceptGroupInvitation(op.param1)
                    else:
                        cl.acceptGroupInvitation(op.param1)
                elif wait["autoCancel"]["on"] == True:
                    if len(G.members) <= wait["autoCancel"]["members"]:
                        cl.rejectGroupInvitation(op.param1)
            else:
                Inviter = op.param3.replace("",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in wait["blacklist"]:
                    matched_list+=filter(lambda str: str == tag, InviterX)
                if matched_list == []:
                    pass
                else:
                    cl.cancelGroupInvitation(op.param1, matched_list)
		
        if op.type == 13:
            if op.param3 in mid:
                if op.param2 in Amid:
                    G = Amid.getGroup(op.param1)
                    G.preventJoinByTicket = False
                    Amid.updateGroup(G)
                    Ticket = Amid.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                    G.preventJoinByTicket = True
                    Amid.updateGroup(G)
                    Ticket = Amid.reissueGroupTicket(op.param1)

            if op.param3 in Amid:
                if op.param2 in mid:
                    X = cl.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    cl.updateGroup(X)
                    Ti = cl.reissueGroupTicket(op.param1)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    X.preventJoinByTicket = True
                    ki.updateGroup(X)
                    Ti = ki.reissueGroupTicket(op.param1)

            if op.param3 in Bmid:
                if op.param2 in Amid:
                    X = ki.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    ki.updateGroup(X)
                    Ti = ki.reissueGroupTicket(op.param1)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    X.preventJoinByTicket = True
                    kk.updateGroup(X)
                    Ti = kk.reissueGroupTicket(op.param1)

            if op.param3 in Cmid:
                if op.param2 in Bmid:
                    X = kk.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    kk.updateGroup(X)
                    Ti = kk.reissueGroupTicket(op.param1)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    X.preventJoinByTicket = True
                    kc.updateGroup(X)
                    Ti = kc.reissueGroupTicket(op.param1)
                
#            if op.param3 in Dmid:
#                if op.param2 in Cmid:
#                    X = kc.getGroup(op.param1)
#                    X.preventJoinByTicket = False
 #                   kc.updateGroup(X)
  #                  Ti = kc.reissueGroupTicket(op.param1)
   #                 ks.acceptGroupInvitationByTicket(op.param1,Ti)
    #                X.preventJoinByTicket = True
     #               ks.updateGroup(X)
      #              Ti = ks.reissueGroupTicket(op.param1)
                
       #     if op.param3 in Emid:
        #        if op.param2 in Dmid:
         #           X = ks.getGroup(op.param1)
          #          X.preventJoinByTicket = False
           #         ks.updateGroup(X)
            #        Ti = ks.reissueGroupTicket(op.param1)
             #       ka.acceptGroupInvitationByTicket(op.param1,Ti)
              #      X.preventJoinByTicket = True
               #     ka.updateGroup(X)
                #    Ti = ka.reissueGroupTicket(op.param1)
                #
#            if op.param3 in Fmid:
 #               if op.param2 in Emid:
  #                  X = ka.getGroup(op.param1)
   #                 X.preventJoinByTicket = False
    #                ka.updateGroup(X)
     #               Ti = ka.reissueGroupTicket(op.param1)
      #              kb.acceptGroupInvitationByTicket(op.param1,Ti)
       #             X.preventJoinByTicket = True
        #            kb.updateGroup(X)
         #           Ti = kb.reissueGroupTicket(op.param1)
                
#            if op.param3 in Gmid:
 #               if op.param2 in Fmid:
  #                  X = kb.getGroup(op.param1)
   #                 X.preventJoinByTicket = False
    #                kb.updateGroup(X)
     #               Ti = kb.reissueGroupTicket(op.param1)
      #              ko.acceptGroupInvitationByTicket(op.param1,Ti)
       #             X.preventJoinByTicket = True
        #            ko.updateGroup(X)
         #           Ti = ko.reissueGroupTicket(op.param1)
                
#            if op.param3 in Hmid:
 #               if op.param2 in Gmid:
  #                  X = ko.getGroup(op.param1)
   #                 X.preventJoinByTicket = False
    #                ko.updateGroup(X)
     #               Ti = ko.reissueGroupTicket(op.param1)
      #              ke.acceptGroupInvitationByTicket(op.param1,Ti)
       #             X.preventJoinByTicket = True
        #            ke.updateGroup(X)
         #           Ti = ke.reissueGroupTicket(op.param1)
                    
#            if op.param3 in Imid:
 #               if op.param2 in mid:
  #                  X = cl.getGroup(op.param1)
   #                 X.preventJoinByTicket = False
    #                cl.updateGroup(X)
     #               Ti = cl.reissueGroupTicket(op.param1)
      #              ku.acceptGroupInvitationByTicket(op.param1,Ti)
       #             X.preventJoinByTicket = True
        #            cl.updateGroup(X)
         #           Ti = cl.reissueGroupTicket(op.param1)        

        if op.type == 13:
            print op.param1
            print op.param2
            print op.param3
            if mid in op.param3:
                G = cl.getGroup(op.param1)
                if wait["autoJoin"] == True:
                    if wait["autoCancel"]["on"] == True:
                        if len(G.members) <= wait["autoCancel"]["members"]:
                            cl.rejectGroupInvitation(op.param1)
                        else:
                            cl.acceptGroupInvitation(op.param1)
                    else:
                        cl.acceptGroupInvitation(op.param1)
                elif wait["autoCancel"]["on"] == True:
                    if len(G.members) <= wait["autoCancel"]["members"]:
                        cl.rejectGroupInvitation(op.param1)
            else:
                Inviter = op.param3.replace("",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in wait["blacklist"]:
                    matched_list+=filter(lambda str: str == tag, InviterX)
                if matched_list == []:
                    pass
                else:
                    cl.cancelGroupInvitation(op.param1, matched_list)

		if op.type == 15:
			random.choice(KAC).sendText(op.param1, "Good bye.")
			print op.param3 + "has left the group"
                    
        #------Joined User Kick start------#
        if op.type == 17:
			if wait["Protectjoin"] == True:
				if op.param2 not in Bots:
					random.choice(DEF).kickoutFromGroup(op.param1,[op.param2])
               
        #------Joined User Kick start------#

        if op.type == 17:
            group = cl.getGroup(op.param1)
            cb = Message()
            cb.to = op.param1
            cb.text = "Hi " + cl.getContact(op.param2).displayName + ", welcome to " + group.name
            cl.sendMessage(cb)
        
        if op.type == 19:
           if op.param2 not in Bots:
              random.choice(DEF).kickoutFromGroup(op.param1,[op.param2])
              random.choice(DEF).inviteIntoGroup(op.param1,[op.param3])
           else: 
               pass

        if op.type == 19:
           if op.param3 in admin:
              random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
              cl.inviteIntoGroup(op.param1,admin)
           else:
               pass

        if op.type == 19:
                if mid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        ki.kickoutFromGroup(op.param1,[op.param2])
                        kk.kickoutFromGroup(op.param1,[op.param2])
                        kc.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client Kick regulation or Because it does not exist in the group、\n["+op.param1+"]\nの\n["+op.param2+"]\nを蹴る事ができませんでした。\nブラックリストに追加します。")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True
                    G = random.choice(KAC).getGroup(op.param1)
                    G.preventJoinByTicket = False
                    random.choice(KAC).updateGroup(G)
                    Ti = random.choice(KAC).reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    #ks.acceptGroupInvitationByTicket(op.param1,Ti)
                    #ka.acceptGroupInvitationByTicket(op.param1,Ti)
                    #kb.acceptGroupInvitationByTicket(op.param1,Ti)
                    #ko.acceptGroupInvitationByTicket(op.param1,Ti)
                    #ke.acceptGroupInvitationByTicket(op.param1,Ti)
                    X = cl.getGroup(op.param1)
                    X.preventJoinByTicket = True
                    cl.updateGroup(X)
                    Ti = cl.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True
 
                if Amid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        cl.kickoutFromGroup(op.param1,[op.param2])
                        kk.kickoutFromGroup(op.param1,[op.param2])
                        kc.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                            random.choice(KAC).inviteIntoGroup(op.param1,[op.param3])
                        except:
                            print ("clientが蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nを蹴る事ができませんでした。\nブラックリストに追加します。")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True

                    X = random.choice(KAC).getGroup(op.param1)
                    X.preventJoinByTicket = False
                    random.choice(KAC).updateGroup(X)
                    Ti = random.choice(KAC).reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    #ks.acceptGroupInvitationByTicket(op.param1,Ti)
                    #ka.acceptGroupInvitationByTicket(op.param1,Ti)
                    #kb.acceptGroupInvitationByTicket(op.param1,Ti)
                    #ko.acceptGroupInvitationByTicket(op.param1,Ti)
                    #ke.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = ki.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    ki.updateGroup(G)
                    Ticket = ki.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True

                if Bmid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        cl.kickoutFromGroup(op.param1,[op.param2])
                        ki.kickoutFromGroup(op.param1,[op.param2])
                        kc.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                            random.choice(KAC).inviteIntoGroup(op.param1,[op.param3])
                        except:
                            print ("clientが蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nを蹴る事ができませんでした。\nブラックリストに追加します。")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True

                    X = random.choice(KAC).getGroup(op.param1)
                    X.preventJoinByTicket = False
                    random.choice(KAC).updateGroup(X)
                    Ti = random.choice(KAC).reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    #ks.acceptGroupInvitationByTicket(op.param1,Ti)
                   # ka.acceptGroupInvitationByTicket(op.param1,Ti)
                   # kb.acceptGroupInvitationByTicket(op.param1,Ti)
                  #  ko.acceptGroupInvitationByTicket(op.param1,Ti)
                   # ke.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = kk.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    kk.updateGroup(G)
                    Ticket = kk.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True

                if Cmid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        cl.kickoutFromGroup(op.param1,[op.param2])
                        kk.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                            random.choice(KAC).inviteIntoGroup(op.param1,[op.param3])
                        except:
                            print ("clientが蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nを蹴る事ができませんでした。\nブラックリストに追加します。")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True

                    X = random.choice(KAC).getGroup(op.param1)
                    X.preventJoinByTicket = False
                    random.choice(KAC).updateGroup(X)
                    Ti = random.choice(KAC).reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    #ks.acceptGroupInvitationByTicket(op.param1,Ti)
                   # ka.acceptGroupInvitationByTicket(op.param1,Ti)
                   # kb.acceptGroupInvitationByTicket(op.param1,Ti)
                   # ko.acceptGroupInvitationByTicket(op.param1,Ti)
                   # ke.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = kc.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    kc.updateGroup(G)
                    Ticket = kc.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True
                        
                        
#                if Dmid in op.param3:
 #                   if op.param2 in Bots:
  #                      pass
   #                 try:
    #                    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
     #               except:
      #                  try:
       #                     random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
        #                    random.choice(KAC).inviteIntoGroup(op.param1,[op.param3])
         #               except:
          #                  print ("client Because it is not in the group or Because it does not exist in the group \n["+op.param1+"]\nOf\n["+op.param2+"]\n I could not kick \n Add it to the black list.")
           #             if op.param2 in wait["blacklist"]:
            #                pass
             #           if op.param2 in wait["whitelist"]:
              #              pass
               #         else:
                #            wait["blacklist"][op.param2] = True
#
 #                   X = random.choice(KAC).getGroup(op.param1)
  #                  X.preventJoinByTicket = False
   #                 random.choice(KAC).updateGroup(X)
    #                Ti = random.choice(KAC).reissueGroupTicket(op.param1)
     #               cl.acceptGroupInvitationByTicket(op.param1,Ti)
      #              ki.acceptGroupInvitationByTicket(op.param1,Ti)
       #             kk.acceptGroupInvitationByTicket(op.param1,Ti)
        #            kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    #ks.acceptGroupInvitationByTicket(op.param1,Ti)
                 #   ka.acceptGroupInvitationByTicket(op.param1,Ti)
                  #  kb.acceptGroupInvitationByTicket(op.param1,Ti)
                 #   ko.acceptGroupInvitationByTicket(op.param1,Ti)
                  #  ke.acceptGroupInvitationByTicket(op.param1,Ti)
         #           G = ks.getGroup(op.param1)
        #            G.preventJoinByTicket = True
         #           ks.updateGroup(G)
         #           Ticket = ks.reissueGroupTicket(op.param1)
          #          if op.param2 in wait["blacklist"]:
           #             pass
            #        if op.param2 in wait["whitelist"]:
             #           pass
              #      else:
               #         wait["blacklist"][op.param2] = True
                        
#                if Emid in op.param3:
 #                   if op.param2 in Bots:
  #                      pass
   #                 try:
    #                    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
     #               except:
      #                  try:
       #                     random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
        #                    random.choice(KAC).inviteIntoGroup(op.param1,[op.param3])
         #               except:
          #                  print ("client Because it is not in the group or Because it does not exist in the group \n["+op.param1+"]\nOf\n["+op.param2+"]\n I could not kick \n Add it to the black list.")
           #             if op.param2 in wait["blacklist"]:
            #                pass
             #           if op.param2 in wait["whitelist"]:
              #              pass
               #         else:
                #            wait["blacklist"][op.param2] = True

                 #   X = random.choice(KAC).getGroup(op.param1)
                  #  X.preventJoinByTicket = False
#                    random.choice(KAC).updateGroup(X)
 #                   Ti = random.choice(KAC).reissueGroupTicket(op.param1)
  #                  cl.acceptGroupInvitationByTicket(op.param1,Ti)
   #                 ki.acceptGroupInvitationByTicket(op.param1,Ti)
    #                kk.acceptGroupInvitationByTicket(op.param1,Ti)
     #               kc.acceptGroupInvitationByTicket(op.param1,Ti)
                   # ks.acceptGroupInvitationByTicket(op.param1,Ti)
                   # ka.acceptGroupInvitationByTicket(op.param1,Ti)
                   # kb.acceptGroupInvitationByTicket(op.param1,Ti)
                  #  ko.acceptGroupInvitationByTicket(op.param1,Ti)
                  #  ke.acceptGroupInvitationByTicket(op.param1,Ti)
      #              G = ka.getGroup(op.param1)
       #             G.preventJoinByTicket = True
        #            ka.updateGroup(G)
         #           Ticket = ka.reissueGroupTicket(op.param1)
          #          if op.param2 in wait["blacklist"]:
           #             pass
            #        if op.param2 in wait["whitelist"]:
             #           pass
              #      else:
               #         wait["blacklist"][op.param2] = True
                        
#                if Fmid in op.param3:
 #                   if op.param2 in Bots:
  #                      pass
   #                 try:
    #                    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
     #               except:
      #                  try:
       #                     random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
        #                    random.choice(KAC).inviteIntoGroup(op.param1,[op.param3])
         #               except:
          #                  print ("client Because it is not in the group or Because it does not exist in the group \n["+op.param1+"]\nOf\n["+op.param2+"]\n I could not kick \n Add it to the black list.")
           #             if op.param2 in wait["blacklist"]:
            #                pass
             #           if op.param2 in wait["whitelist"]:
              #              pass
               #         else:
                #            wait["blacklist"][op.param2] = True
#
 #                   X = random.choice(KAC).getGroup(op.param1)
  #                  X.preventJoinByTicket = False
   #                 random.choice(KAC).updateGroup(X)
    #                Ti = random.choice(KAC).reissueGroupTicket(op.param1)
     #               cl.acceptGroupInvitationByTicket(op.param1,Ti)
      #              ki.acceptGroupInvitationByTicket(op.param1,Ti)
       #             kk.acceptGroupInvitationByTicket(op.param1,Ti)
        #            kc.acceptGroupInvitationByTicket(op.param1,Ti)
                   # ks.acceptGroupInvitationByTicket(op.param1,Ti)
                   # ka.acceptGroupInvitationByTicket(op.param1,Ti)
                   # kb.acceptGroupInvitationByTicket(op.param1,Ti)
                    #ko.acceptGroupInvitationByTicket(op.param1,Ti)
                   # ke.acceptGroupInvitationByTicket(op.param1,Ti)
         #           G = kb.getGroup(op.param1)
          #          G.preventJoinByTicket = True
           #         kb.updateGroup(G)
            #        Ticket = kb.reissueGroupTicket(op.param1)
             #       if op.param2 in wait["blacklist"]:
              #$          pass
                #    if op.param2 in wait["whitelist"]:
                 #       pass
                  #  else:
                   #     wait["blacklist"][op.param2] = True
                        
#                if Gmid in op.param3:
 #                   if op.param2 in Bots:
  #                      pass
   #                 try:
    #                    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
     #               except:
      #                  try:
       #                     random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
        #                    random.choice(KAC).inviteIntoGroup(op.param1,[op.param3])
         #               except:
          #                  print ("client Because it is not in the group or Because it does not exist in the group \n["+op.param1+"]\nOf\n["+op.param2+"]\n I could not kick \n Add it to the black list.")
           #             if op.param2 in wait["blacklist"]:
            #                pass
             #           if op.param2 in wait["whitelist"]:
              #              pass
               #         else:
                #            wait["blacklist"][op.param2] = True
#
 #                   X = random.choice(KAC).getGroup(op.param1)
  #                  X.preventJoinByTicket = False
   #                 random.choice(KAC).updateGroup(X)
    #                Ti = random.choice(KAC).reissueGroupTicket(op.param1)
     #               cl.acceptGroupInvitationByTicket(op.param1,Ti)
      #              ki.acceptGroupInvitationByTicket(op.param1,Ti)
       #             kk.acceptGroupInvitationByTicket(op.param1,Ti)
        #            kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    #ks.acceptGroupInvitationByTicket(op.param1,Ti)
                   # ka.acceptGroupInvitationByTicket(op.param1,Ti)
                   # kb.acceptGroupInvitationByTicket(op.param1,Ti)
                  #  ko.acceptGroupInvitationByTicket(op.param1,Ti)
                  #  ke.acceptGroupInvitationByTicket(op.param1,Ti)
         #           G = ko.getGroup(op.param1)
          #          G.preventJoinByTicket = True
           #         ko.updateGroup(G)
            #        Ticket = ko.reissueGroupTicket(op.param1)
             #       if op.param2 in wait["blacklist"]:
              #          pass
               #     if op.param2 in wait["whitelist"]:
                #        pass
                 #   else:
                  #      wait["blacklist"][op.param2] = True
                        
#                if Hmid in op.param3:
 #                   if op.param2 in Bots:
  #                      pass
   #                 try:
    #                    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
     #               except:
      #                  try:
       #                     random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
        #                except:
         #                   print ("client Because it is not in the group or Because it does not exist in the group \n["+op.param1+"]\nOf\n["+op.param2+"]\n I could not kick \n Add it to the black list.")
          #              if op.param2 in wait["blacklist"]:
           #                 pass
            #            if op.param2 in wait["whitelist"]:
             #               pass
              #          else:
               #             wait["blacklist"][op.param2] = True
#
 #                   X = random.choice(KAC).getGroup(op.param1)
  #                  X.preventJoinByTicket = False
   #                 random.choice(KAC).updateGroup(X)
    #                Ti = random.choice(KAC).reissueGroupTicket(op.param1)
     #               cl.acceptGroupInvitationByTicket(op.param1,Ti)
      #              ki.acceptGroupInvitationByTicket(op.param1,Ti)
       #             kk.acceptGroupInvitationByTicket(op.param1,Ti)
        #            kc.acceptGroupInvitationByTicket(op.param1,Ti)
                   # ks.acceptGroupInvitationByTicket(op.param1,Ti)
                  #  ka.acceptGroupInvitationByTicket(op.param1,Ti)
                    #kb.acceptGroupInvitationByTicket(op.param1,Ti)
                   # ko.acceptGroupInvitationByTicket(op.param1,Ti)
                   # ke.acceptGroupInvitationByTicket(op.param1,Ti)
         #           G = ke.getGroup(op.param1)
          #          G.preventJoinByTicket = True
           #         ke.updateGroup(G)
            #        Ticket = ke.reissueGroupTicket(op.param1)
             #       if op.param2 in wait["blacklist"]:
              #          pass
               #     if op.param2 in wait["whitelist"]:
                #        pass
                 #   else:
                  #      wait["blacklist"][op.param2] = True        
                   # 
        if op.type == 22:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
        if op.type == 24:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
        if op.type == 26:
            msg = op.message
            if msg.toType == 0:
                msg.to = msg.from_
                if msg.from_ in owner:
                    if "join:" in msg.text:
                        list_ = msg.text.split(":")
                        try:
                            cl.acceptGroupInvitationByTicket(list_[1],list_[2])
                            G = cl.getGroup(list_[1])
                            G.preventJoinByTicket = True
                            cl.updateGroup(G)
                        except:
                            cl.sendText(msg.to,"error")
        if op.type == 26:
            msg = op.message
            if msg.toType == 1:
                if wait["leaveRoom"] == True:
                    cl.leaveRoom(msg.to)
            if msg.contentType == 16:
                url = msg.contentMetadata("line://home/post?userMid="+mid+"&postId="+"new_post")
                cl.like(url[25:58], url[66:], likeType=1001)
        if op.type == 26:
            msg = op.message
            if msg.contentType == 13:
               if wait["wblack"] == True:
                    if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        cl.sendText(msg.to,"Already in blacklist")
                        wait["wblack"] = False
                    else:
                        wait["commentBlack"][msg.contentMetadata["mid"]] = True
                        wait["wblack"] = False
                        cl.sendText(msg.to,"Decided not to comment.")

               if wait["dblack"] == True:
                   if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        del wait["commentBlack"][msg.contentMetadata["mid"]]
                        cl.sendText(msg.to,"Removed from blacklist.")
                        wait["dblack"] = False

                   else:
                        wait["dblack"] = False
                        cl.sendText(msg.to,"There's no target in blacklist.")
               if wait["wblacklist"] == True:
                   if msg.contentMetadata["mid"] in wait["blacklist"]:
                        cl.sendText(msg.to,"Already in blacklist")
                        wait["wblacklist"] = False
                   else:
                        wait["blacklist"][msg.contentMetadata["mid"]] = True
                        wait["wblacklist"] = False
                        cl.sendText(msg.to,"Added to blacklist.")

               if wait["dblacklist"] == True:
                   if msg.contentMetadata["mid"] in wait["blacklist"]:
                        del wait["blacklist"][msg.contentMetadata["mid"]]
                        cl.sendText(msg.to,"Removed from blacklist.")
                        wait["dblacklist"] = False

                   else:
                        wait["dblacklist"] = False
                        cl.sendText(msg.to,"There's no target in blacklist.")
               if wait["contact"] == True:
                    msg.contentType = 0
                    cl.sendText(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = cl.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        cl.sendText(msg.to,"[displayName]:\n" + msg.contentMetadata["displayName"] + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu))
                    else:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = cl.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        cl.sendText(msg.to,"[displayName]:\n" + contact.displayName + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu))
            elif msg.contentType == 16:
                if wait["timeline"] == True:
                    msg.contentType = 0
                    if wait["lang"] == "JP":
                        msg.text = "post URL\n" + msg.contentMetadata["postEndUrl"]
                    else:
                        msg.text = "URLâ†’\n" + msg.contentMetadata["postEndUrl"]
                    cl.sendText(msg.to,msg.text)
            elif msg.text is None:
                return
				
            elif msg.text in ["@Key","@key","@help","@Help"]:
				if msg.from_ in admin:
					if wait["lang"] == "JP":
						cl.sendText(msg.to,helpMessage)
					else:
						cl.sendText(msg.to,helpt)
            elif msg.text in ["@set group"]:
				if msg.from_ in admin:
					if wait["lang"] == "JP":
						cl.sendText(msg.to,Setgroup)
					else:
						cl.sendText(msg.to,Sett)
            elif ("@Gn " in msg.text):
				if msg.from_ in admin:
					if msg.toType == 2:
						X = cl.getGroup(msg.to)
						X.name = msg.text.replace("Gn ","")
						cl.updateGroup(X)
					else:
						cl.sendText(msg.to,"It can't be used besides the group.")
            elif ("ZSI2 gn " in msg.text):
				if msg.from_ in admin:
					if msg.toType == 2:
						X = cl.getGroup(msg.to)
						X.name = msg.text.replace("ZSI2 gn ","")
						ki.updateGroup(X)
					else:
						ki.sendText(msg.to,"It can't be used besides the group.")
            elif ("ZSI3 gn " in msg.text):
				if msg.from_ in admin:
					if msg.toType == 2:
						X = cl.getGroup(msg.to)
						X.name = msg.text.replace("ZSI3 gn ","")
						kk.updateGroup(X)
					else:
						kk.sendText(msg.to,"It can't be used besides the group.")
            elif ("ZSI4 gn " in msg.text):
				if msg.from_ in admin:
					if msg.toType == 2:
						X = cl.getGroup(msg.to)
						X.name = msg.text.replace("ZSI4 gn ","")
						kc.updateGroup(X)
					else:
						kc.sendText(msg.to,"It can't be used besides the group.")
            elif "@Kick " in msg.text:
				if msg.from_ in admin:
					midd = msg.text.replace("Kick ","")
					cl.kickoutFromGroup(msg.to,[midd])
            elif "@ZSI2 kick " in msg.text:
				if msg.from_ in admin:
					midd = msg.text.replace("_second kick ","")
					ki.kickoutFromGroup(msg.to,[midd])
            elif "@ZSI3 kick " in msg.text:
				if msg.from_ in admin:
					midd = msg.text.replace("_third kick ","")
					kk.kickoutFromGroup(msg.to,[midd])
            elif "@ZSI4 kick " in msg.text:
				if msg.from_ in admin:
					midd = msg.text.replace("_fourth kick ","")
					kc.kickoutFromGroup(msg.to,[midd])
            elif "@Invite " in msg.text:
				if msg.from_ in admin:
					midd = msg.text.replace("Invite ","")
					cl.findAndAddContactsByMid(midd)
					cl.inviteIntoGroup(msg.to,[midd])
            elif "@Sinvite " in msg.text:
				if msg.from_ in admin:
					midd = msg.text.replace("sinvite ","")
					ki.findAndAddContactsByMid(midd)
					ki.inviteIntoGroup(msg.to,[midd])
            elif "@Tinvite " in msg.text:
				if msg.from_ in admin:
					midd = msg.text.replace("tinvite ","")
					kk.findAndAddContactsByMid(midd)
					kk.inviteIntoGroup(msg.to,[midd])
            elif "@Finvite " in msg.text:
				if msg.from_ in admin:
					midd = msg.text.replace("finvite ","")
					kc.findAndAddContactsByMid(midd)
					kc.inviteIntoGroup(msg.to,[midd])
            elif msg.text in ["@bot?"]:
				if msg.from_ in admin:
					msg.contentType = 13
					msg.contentMetadata = {'mid': mid}
					cl.sendMessage(msg)

					msg.contentType = 13
					msg.contentMetadata = {'mid': Amid}
					ki.sendMessage(msg)

					msg.contentType = 13
					msg.contentMetadata = {'mid': Bmid}
					kk.sendMessage(msg)

					msg.contentType = 13
					msg.contentMetadata = {'mid': Cmid}
					kc.sendMessage(msg)
                
#                msg.contentType = 13
 #               msg.contentMetadata = {'mid': Dmid}
  #              ks.sendMessage(msg)
                
   #             msg.contentType = 13
    #            msg.contentMetadata = {'mid': Emid}
     #           ka.sendMessage(msg)
                
      #          msg.contentType = 13
       #         msg.contentMetadata = {'mid': Fmid}
        #        kb.sendMessage(msg)
                
         #       msg.contentType = 13
          #      msg.contentMetadata = {'mid': Gmid}
           #     ko.sendMessage(msg)
                
            #    msg.contentType = 13
             #   msg.contentMetadata = {'mid': Hmid}
              #  ke.sendMessage(msg)
            elif msg.text in ["@Creator","@creator"]:
				if msg.from_ in admin:
					msg.contentType = 13
					cl.sendText(msg.to, "Owner by FXR")
					msg.contentMetadata = {'mid': 'u349dbde6509797ddc33adce5b85cd856'}
					cl.sendMessage(msg)
            elif msg.text in ["@Me"]:
				if msg.from_ in admin:
					msg.contentType = 13
					msg.contentMetadata = {'mid': msg.from_}
					random.choice(KAC).sendMessage(msg)
#            elif msg.text in ["Cv2"]:
#                msg.contentType = 13
 #               msg.contentMetadata = {'mid': Bmid}
  #              kk.sendMessage(msg)
            elif msg.text in ["æ„›ã�®ãƒ—ãƒ¬ã‚¼ãƒ³ãƒˆ","@Gift"]:
				if msg.from_ in admin:
					msg.contentType = 9
					msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
										'PRDTYPE': 'THEME',
										'MSGTPL': '5'}
					msg.text = None
					cl.sendMessage(msg)
#            elif msg.text in ["æ„›ã�®ãƒ—ãƒ¬ã‚¼ãƒ³ãƒˆ","Cv1 gift"]:
 #               msg.contentType = 9
  #              msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
   #                                 'PRDTYPE': 'THEME',
    #                                'MSGTPL': '6'}
     #           msg.text = None
      #          ki.sendMessage(msg)
       #     elif msg.text in ["æ„›ã�®ãƒ—ãƒ¬ã‚¼ãƒ³ãƒˆ","Cv2 gift"]:
        #        msg.contentType = 9
         #       msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
          #                          'PRDTYPE': 'THEME',
           #                         'MSGTPL': '8'}
            #    msg.text = None
             #   kk.sendMessage(msg)
#            elif msg.text in ["æ„›ã�®ãƒ—ãƒ¬ã‚¼ãƒ³ãƒˆ","Cv3 gift"]:
 #               msg.contentType = 9
  #              msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
   #                                 'PRDTYPE': 'THEME',
    #                                'MSGTPL': '10'}
     #           msg.text = None
      #          kc.sendMessage(msg)
            elif msg.text in ["æ„›ã�®ãƒ—ãƒ¬ã‚¼ãƒ³ãƒˆ","@All gift"]:
				if msg.from_ in admin:
					msg.contentType = 9
					msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
										'PRDTYPE': 'THEME',
										'MSGTPL': '12'}
					msg.text = None
					ki.sendMessage(msg)
					kk.sendMessage(msg)
					kc.sendMessage(msg)
            elif msg.text in ["@Cancel","@cancel"]:
				if msg.from_ in admin:
					if msg.toType == 2:
						X = cl.getGroup(msg.to)
						if X.invitee is not None:
							gInviMids = [contact.mid for contact in X.invitee]
							cl.cancelGroupInvitation(msg.to, gInviMids)
						else:
							if wait["lang"] == "JP":
								cl.sendText(msg.to,"Invite Kosong")
							else:
								cl.sendText(msg.to,"Sorry, nobody absent")
					else:
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"Can not be used outside the group")
						else:
							cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["@ZSI cancel","@Bot cancel"]:
				if msg.from_ in admin:
					if msg.toType == 2:
						G = k3.getGroup(msg.to)
						if G.invitee is not None:
							gInviMids = [contact.mid for contact in G.invitee]
							k3.cancelGroupInvitation(msg.to, gInviMids)
						else:
							if wait["lang"] == "JP":
								k3.sendText(msg.to,"No one is inviting")
							else:
								k3.sendText(msg.to,"Sorry, nobody absent")
					else:
						if wait["lang"] == "JP":
							k3.sendText(msg.to,"Can not be used outside the group")
						else:
							k3.sendText(msg.to,"Not for use less than group")
            #elif "gurl" == msg.text:
                #print cl.getGroup(msg.to)
                ##cl.sendMessage(msg)
            elif msg.text in ["@Open url","@open url"]:
                if msg.from_ in admin:
					if msg.toType == 2:
						X = cl.getGroup(msg.to)
						X.preventJoinByTicket = False
						cl.updateGroup(X)
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"Invite by link open")
						else:
							cl.sendText(msg.to,"Already open")
					else:
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"Can not be used outside the group")
						else:
							cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["@ZSI2 ourl","@ZSI2 link on"]:
                if msg.from_ in admin:
					if msg.toType == 2:
						X = cl.getGroup(msg.to)
						X.preventJoinByTicket = False
						ki.updateGroup(X)
						if wait["lang"] == "JP":
							ki.sendText(msg.to,"Done Chivas")
						else:
							ki.sendText(msg.to,"already open")
					else:
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"Can not be used outside the group")
						else:
							cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["@ZSI3 ourl","@ZSI3 link on"]:
				if msg.from_ in admin:            
					if msg.toType == 2:
						X = kk.getGroup(msg.to)
						X.preventJoinByTicket = False
						kk.updateGroup(X)
						if wait["lang"] == "JP":
							kk.sendText(msg.to,"Done Chivas")
						else:
							kk.sendText(msg.to,"already open")
					else:
						if wait["lang"] == "JP":
							kk.sendText(msg.to,"Can not be used outside the group")
						else:
							kk.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["@ZSI4 ourl","@ZSI4 link on"]:
				if msg.from_ in admin:
					if msg.toType == 2:
						X = kc.getGroup(msg.to)
						X.preventJoinByTicket = False
						kc.updateGroup(X)
						if wait["lang"] == "JP":
							kc.sendText(msg.to,"Done Chivas")
						else:
							kc.sendText(msg.to,"already open")
					else:
						if wait["lang"] == "JP":
							kc.sendText(msg.to,"Can not be used outside the group")
						else:
							kc.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["@Close url","@close url"]:
				if msg.from_ in admin:
					if msg.toType == 2:
						X = cl.getGroup(msg.to)
						X.preventJoinByTicket = True
						cl.updateGroup(X)
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"Invite by link Close")
						else:
							cl.sendText(msg.to,"Already close")
					else:
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"Can not be used outside the group")
						else:
							cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["@ZSI2 curl","@ZSI2 link off"]:
				if msg.from_ in admin:            
					if msg.toType == 2:
						X = ki.getGroup(msg.to)
						X.preventJoinByTicket = True
						ki.updateGroup(X)
						if wait["lang"] == "JP":
							ki.sendText(msg.to,"Done Chivas")
						else:
							ki.sendText(msg.to,"already close")
					else:
						if wait["lang"] == "JP":
							ki.sendText(msg.to,"Can not be used outside the group")
						else:
							ki.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["@ZSI3 curl","@ZSI3 link off"]:
				if msg.from_ in admin:
					if msg.toType == 2:
						X = kk.getGroup(msg.to)
						X.preventJoinByTicket = True
						kk.updateGroup(X)
						if wait["lang"] == "JP":
							kk.sendText(msg.to,"Done Chivas")
						else:
							kk.sendText(msg.to,"already close")
					else:
						if wait["lang"] == "JP":
							kk.sendText(msg.to,"Can not be used outside the group")
						else:
							kk.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["@ZSI4 curl","@ZSI4 link off"]:
				if msg.from_ in admin:            
					if msg.toType == 2:
						X = kc.getGroup(msg.to)
						X.preventJoinByTicket = True
						kc.updateGroup(X)
						if wait["lang"] == "JP":
							kc.sendText(msg.to,"Done Chivas")
						else:
							kc.sendText(msg.to,"already close")
					else:
						if wait["lang"] == "JP":
							kc.sendText(msg.to,"Can not be used outside the group")
						else:
							kc.sendText(msg.to,"Not for use less than group")
            elif "@jointicket " in msg.text.lower():
				if msg.from_ in admin:            
					rplace=msg.text.lower().replace("jointicket ")
					if rplace == "on":
						wait["atjointicket"]=True
					if rplace == "off":
						wait["atjointicket"]=False
						cl.sendText(msg.to,"Auto Join Group by Ticket is %s" % str(wait["atjointicket"]))
            elif '/ti/g/' in msg.text.lower():
				if msg.from_ in admin:
					link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
					links = link_re.findall(msg.text)
					n_links=[]
					for l in links:
						if l not in n_links:
							n_links.append(l)
					for ticket_id in n_links:
						if wait["atjointicket"] == True:
							group=cl.findGroupByTicket(ticket_id)
							cl.acceptGroupInvitationByTicket(group.mid,ticket_id)
							cl.sendText(msg.to,"Sukses join ke grup %s" % str(group.name))
            elif msg.text == "Ginfo":
              if msg.from_ in admin:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        gCreator = ginfo.creator.displayName
                    except:
                        gCreator = "Error"
                    if wait["lang"] == "JP":
                        if ginfo.invitee is None:
                            sinvitee = "0"
                        else:
                            sinvitee = str(len(ginfo.invitee))
                        if ginfo.preventJoinByTicket == True:
                            u = "close"
                        else:
                            u = "open"
                        cl.sendText(msg.to,"[group name]\n" + str(ginfo.name) + "\n[gid]\n" + msg.to + "\n[group creator]\n" + gCreator + "\n[profile status]\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus + "\nmembers:" + str(len(ginfo.members)) + "members\npending:" + sinvitee + "people\nURL:" + u + "it is inside")
                    else:
                        cl.sendText(msg.to,"[group name]\n" + str(ginfo.name) + "\n[gid]\n" + msg.to + "\n[group creator]\n" + gCreator + "\n[profile status]\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can not be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif "@Id Group" == msg.text:
				if msg.from_ in admin:
					kk.sendText(msg.to,msg.to)
            elif "@My mid" == msg.text:
				if msg.from_ in admin:
					random.choice(KAC).sendText(msg.to, msg.from_)
            elif "@Mid all" == msg.text:
				if msg.from_ in admin:
					cl.sendText(msg.to,mid)
					ki.sendText(msg.to,Amid)
					kk.sendText(msg.to,Bmid)
					kc.sendText(msg.to,Cmid)
#                ks.sendText(msg.to,Dmid)
 #               ka.sendText(msg.to,Emid)
  #              kb.sendText(msg.to,Fmid)
   #             ko.sendText(msg.to,Gmid)
    #            ke.sendText(msg.to,Hmid)
            elif "@Mid 1" == msg.text:
				if msg.from_ in admin:
					cl.sendText(msg.to,mid)
            elif "@Mid 2" == msg.text:
				if msg.from_ in admin:
					ki.sendText(msg.to,Amid)
            elif "@Mid 3" == msg.text:
				if msg.from_ in admin:
					kk.sendText(msg.to,Bmid)
            elif "@Mid 4" == msg.text:
				if msg.from_ in admin:
					kc.sendText(msg.to,Cmid)
            elif msg.text in ["Wkwkwk","Wkwk","Wk","wkwkwk","wkwk","wk"]:
				if msg.from_ in admin:
					msg.contentType = 7
					msg.text = None
					msg.contentMetadata = {
										"STKID": "100",
										"STKPKGID": "1",
										"STKVER": "100" }
					kk.sendMessage(msg)
            elif msg.text in ["Hehehe","Hehe","He","hehehe","hehe","he"]:
				if msg.from_ in admin:            
					msg.contentType = 7
					msg.text = None
					msg.contentMetadata = {
										"STKID": "10",
										"STKPKGID": "1",
										"STKVER": "100" }
					ki.sendMessage(msg)
            elif msg.text in ["Galau"]:
				if msg.from_ in admin:
					msg.contentType = 7
					msg.text = None
					msg.contentMetadata = {
										"STKID": "9",
										"STKPKGID": "1",
										"STKVER": "100" }
					kk.sendMessage(msg)
            elif msg.text in ["You"]:
				if msg.from_ in admin:
					msg.contentType = 7
					msg.text = None
					msg.contentMetadata = {
										"STKID": "7",
										"STKPKGID": "1",
										"STKVER": "100" }
					ki.sendMessage(msg)
            elif msg.text in ["Hadeuh"]:
				if msg.from_ in admin:    
					msg.contentType = 7
					msg.text = None
					msg.contentMetadata = {
										"STKID": "6",
										"STKPKGID": "1",
										"STKVER": "100" }
					kk.sendMessage(msg)
            elif msg.text in ["Please"]:
                if msg.from_ in admin:
					msg.contentType = 7
					msg.text = None
					msg.contentMetadata = {
										"STKID": "4",
										"STKPKGID": "1",
										"STKVER": "100" }
					ki.sendMessage(msg)
            elif msg.text in ["Haaa"]:
				if msg.from_ in admin:
					msg.contentType = 7
					msg.text = None
					msg.contentMetadata = {
										"STKID": "3",
										"STKPKGID": "1",
										"STKVER": "100" }
					ki.sendMessage(msg)
            elif msg.text in ["Lol"]:
				if msg.from_ in admin:
					msg.contentType = 7
					msg.text = None
					msg.contentMetadata = {
										"STKID": "110",
										"STKPKGID": "1",
										"STKVER": "100" }
					ki.sendMessage(msg)
            elif msg.text in ["Hmmm","Hmm","Hm","hmmm","hmm","hm"]:
                if msg.from_ in admin:
					msg.contentType = 7
					msg.text = None
					msg.contentMetadata = {
										"STKID": "101",
										"STKPKGID": "1",
										"STKVER": "100" }
					ki.sendMessage(msg)
            elif msg.text in ["Welcome"]:
				if msg.from_ in admin:
					msg.contentType = 7
					msg.text = None
					msg.contentMetadata = {
										"STKID": "247",
										"STKPKGID": "3",
										"STKVER": "100" }
					kk.sendMessage(msg)
					cl.sendMessage(msg)
            elif msg.text in ["@TL: "]:
				if msg.from_ in admin:
					tl_text = msg.text.replace("TL: ","")
					cl.sendText(msg.to,"line://home/post?userMid="+mid+"&postId="+cl.new_post(tl_text)["result"]["post"]["postInfo"]["postId"])
            elif msg.text in ["@Cn "]:
				if msg.from_ in owner:
					string = msg.text.replace("Cn ","")
					if len(string.decode('utf-8')) <= 20:
						profile = cl.getProfile()
						profile.displayName = string
						cl.updateProfile(profile)
						cl.sendText(msg.to,"name " + string + " done")
            elif msg.text in ["@ZSI2 rename "]:
				if msg.from_ in owner:
					string = msg.text.replace("ZS2 rename ","")
					if len(string.decode('utf-8')) <= 20:
						profile_B = ki.getProfile()
						profile_B.displayName = string
						ki.updateProfile(profile_B)
						ki.sendText(msg.to,"name " + string + " done")
            elif msg.text in ["@ZS3 rename "]:
				if msg.from_ in owner:
					string = msg.text.replace("ZSI3 rename ","")
					if len(string.decode('utf-8')) <= 20:
						profile_B = kk.getProfile()
						profile_B.displayName = string
						kk.updateProfile(profile_B)
						kk.sendText(msg.to,"name " + string + " done")
            elif msg.text in ["@ZS4 rename "]:
				if msg.from_ in owner:            
					string = msg.text.replace("ZSI4 rename ","")
					if len(string.decode('utf-8')) <= 20:
						profile_B = kc.getProfile()
						profile_B.displayName = string
						kc.updateProfile(profile_B)
						kc.sendText(msg.to,"name " + string + " done")
            elif msg.text in ["@Mc "]:
				if msg.from_ in admin:
					mmid = msg.text.replace("Mc ","")
					msg.contentType = 13
					msg.contentMetadata = {"mid":mmid}
					cl.sendMessage(msg)
            elif msg.text in ["@Joinn on","@joinn on"]:
				if msg.from_ in admin:
					if wait["Protectjoin"] == True:
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"kick Joined Group On")
						else:
							cl.sendText(msg.to,"done")
					else:
						wait["Protectjoin"] = True
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"kick Joined Group On")
						else:
							cl.sendText(msg.to,"done")
            elif msg.text in ["@Joinn off","@joinn off"]:
				if msg.from_ in admin:
					if wait["Protectjoin"] == False:
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"kick Joined Group Off")
						else:
							cl.sendText(msg.to,"done")
					else:
						wait["Protectjoin"] = False
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"kick Joined Group Off")
						else:
							cl.sendText(msg.to,"done")
            elif msg.text in ["@Cancl on","@cancl on"]:
				if msg.from_ in admin:
					if wait["Protectcancl"] == True:
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"Cancel All Invited On")
						else:
							cl.sendText(msg.to,"done")
					else:
						wait["Protectcancl"] = True
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"Cancel All Invited On")
						else:
							cl.sendText(msg.to,"done")
            elif msg.text in ["@Cancl off","@cancl off"]:
				if msg.from_ in admin:
					if wait["Protectcancl"] == False:
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"Cancel All Invited Off")
						else:
							cl.sendText(msg.to,"done")
					else:
						wait["Protectcancl"] = False
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"Cancel All Invited Off")
						else:
							cl.sendText(msg.to,"done")
            elif msg.text in ["@Gr on","@gr on"]:
				if msg.from_ in admin:
					if wait["Protectgr"] == True:
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"Protect Group On")
						else:
							cl.sendText(msg.to,"done")
					else:
						wait["Protectgr"] = True
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"Protect Group On")
						else:
							cl.sendText(msg.to,"done")
            elif msg.text in ["@Gr off","@gr off"]:
				if msg.from_ in admin:
					if wait["Protectgr"] == False:
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"Protect Group Off")
						else:
							cl.sendText(msg.to,"done")
					else:
						wait["Protectgr"] = False
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"Protect Group Off")
						else:
							cl.sendText(msg.to,"done")
            elif msg.text in ["@Contact On","@Contact on","@contact on"]:
				if msg.from_ in admin:
					if wait["contact"] == True:
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"Cek Mid Send Contact On")
						else:
							cl.sendText(msg.to,"done")
					else:
						wait["contact"] = True
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"Cek Mid Send Contact On")
						else:
							cl.sendText(msg.to,"done")
            elif msg.text in ["@Contact Off","@Contact off","@contact off"]:
				if msg.from_ in admin:
					if wait["contact"] == False:
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"Cek Mid Send Contact Off")
						else:
							cl.sendText(msg.to,"done")
					else:
						wait["contact"] = False
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"Cek Mid Send Contact Off")
						else:
							cl.sendText(msg.to,"done")
            elif msg.text in ["è‡ªå‹•å�‚åŠ :ã‚ªãƒ³","@join on","@auto join:on","è‡ªå‹•å�ƒåŠ ï¼šé–‹"]:
				if msg.from_ in admin:
					if wait["autoJoin"] == True:
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"already on")
						else:
							cl.sendText(msg.to,"done")
					else:
						wait["autoJoin"] = True
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"already on")
						else:
							cl.sendText(msg.to,"done")
            elif msg.text in ["è‡ªå‹•å�‚åŠ :ã‚ªãƒ•","@join off","@auto join:off","è‡ªå‹•å�ƒåŠ ï¼šé—œ"]:
                if msg.from_ in admin:
					if wait["autoJoin"] == False:
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"already off")
						else:
							cl.sendText(msg.to,"done")
					else:
						wait["autoJoin"] = False
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"already off")
						else:
							cl.sendText(msg.to,"done")
            elif msg.text in ["@gcancel:"]:
				if msg.from_ in admin:
					try:
						strnum = msg.text.replace("Gcancel:","")
						if strnum == "off":
							wait["autoCancel"]["on"] = False
							if wait["lang"] == "JP":
								cl.sendText(msg.to,"Invitation refused turned off\nTo turn on please specify the number of people and send")
							else:
								cl.sendText(msg.to,"å…³äº†é‚€è¯·æ‹’ç»�ã€‚è¦�æ—¶å¼€è¯·æŒ‡å®šäººæ•°å�‘é€�")
						else:
							num =  int(strnum)
							wait["autoCancel"]["on"] = True
							if wait["lang"] == "JP":
								cl.sendText(msg.to,strnum + "The group of people and below decided to automatically refuse invitation")
							else:
								cl.sendText(msg.to,strnum + "ä½¿äººä»¥ä¸‹çš„å°�ç»„ç”¨è‡ªåŠ¨é‚€è¯·æ‹’ç»�")
					except:
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"Value is wrong")
						else:
							cl.sendText(msg.to,"Bizarre ratings")
            elif msg.text in ["å¼·åˆ¶è‡ªå‹•é€€å‡º:ã‚ªãƒ³","@leave on","@auto leave:on","å¼·åˆ¶è‡ªå‹•é€€å‡ºï¼šé–‹"]:
				if msg.from_ in admin:
					if wait["leaveRoom"] == True:
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"already on")
						else:
							cl.sendText(msg.to,"done")
					else:
						wait["leaveRoom"] = True
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"done")
						else:
							cl.sendText(msg.to,"è¦�äº†å¼€ã€‚")
            elif msg.text in ["å¼·åˆ¶è‡ªå‹•é€€å‡º:ã‚ªãƒ•","@leave off","@auto leave:off","å¼·åˆ¶è‡ªå‹•é€€å‡ºï¼šé—œ"]:
                if msg.from_ in admin:
					if wait["leaveRoom"] == False:
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"already off")
						else:
							cl.sendText(msg.to,"done")
					else:
						wait["leaveRoom"] = False
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"done")
						else:
							cl.sendText(msg.to,"already")
            elif msg.text in ["å…±æœ‰:ã‚ªãƒ³","@share on","@Share on"]:
				if msg.from_ in admin:
					if wait["timeline"] == True:
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"already on")
						else:
							cl.sendText(msg.to,"done")
					else:
						wait["timeline"] = True
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"done")
						else:
							cl.sendText(msg.to,"è¦�äº†å¼€ã€‚")
            elif msg.text in ["å…±æœ‰:ã‚ªãƒ•","@share off","@Share off"]:
				if msg.from_ in admin:
					if wait["timeline"] == False:
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"already off")
						else:
							cl.sendText(msg.to,"done")
					else:
						wait["timeline"] = False
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"done")
						else:
							cl.sendText(msg.to,"è¦�äº†å…³æ–­ã€‚")
            elif msg.text in ["@set view"]:
				if msg.from_ in admin:
					md = ""
					if wait["Protectjoin"] == True: md+="􀔃􀆑lock􏿿  Block Join\n"
					else: md+=" Block Join Off\n"
					if wait["Protectgr"] == True: md+="􀔃􀆑lock􏿿   Block Group\n"
					else: md+=" Block Group Off\n"
					if wait["Protectcancl"] == True: md+="􀔃􀆑lock􏿿 Cancel All Invited\n"
					else: md+=" Cancel All Invited Off\n"
					if wait["contact"] == True: md+=" Contact    : on\n"
					else: md+=" Contact    : off\n"
					if wait["autoJoin"] == True: md+=" Auto join : on\n"
					else: md +=" Auto join : off\n"
					if wait["autoCancel"]["on"] == True:md+=" Group cancel :" + str(wait["autoCancel"]["members"]) + "\n"
					else: md+= " Group cancel : off\n"
					if wait["leaveRoom"] == True: md+=" Auto leave    : on\n"
					else: md+=" Auto leave : off\n"
					if wait["timeline"] == True: md+=" Share   : on\n"
					else:md+=" Share   : off\n"
					if wait["autoAdd"] == True: md+=" Auto add : on\n"
					else:md+=" Auto add : off\n"
					if wait["commentOn"] == True: md+=" Comment : on\n"
					else:md+=" Comment : off\n"
					cl.sendText(msg.to,md)
            elif "@album merit " in msg.text:
				if msg.from_ in admin:
					gid = msg.text.replace("album merit ","")
					album = cl.getAlbum(gid)
					if album["result"]["items"] == []:
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"There is no album")
						else:
							cl.sendText(msg.to,"ç›¸å†Œæ²¡åœ¨ã€‚")
					else:
						if wait["lang"] == "JP":
							mg = "The following is the target album"
						else:
							mg = "ä»¥ä¸‹æ˜¯å¯¹è±¡çš„ç›¸å†Œ"
						for y in album["result"]["items"]:
							if "photoCount" in y:
								mg += str(y["title"]) + ":" + str(y["photoCount"]) + "sheet\n"
							else:
								mg += str(y["title"]) + ":0sheet\n"
						cl.sendText(msg.to,mg)
            elif "@album " in msg.text:
				if msg.from_ in admin:
					gid = msg.text.replace("album ","")
					album = cl.getAlbum(gid)
					if album["result"]["items"] == []:
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"There is no album")
						else:
							cl.sendText(msg.to,"ç›¸å†Œæ²¡åœ¨ã€‚")
					else:
						if wait["lang"] == "JP":
							mg = "The following is the target album"
						else:
							mg = "ä»¥ä¸‹æ˜¯å¯¹è±¡çš„ç›¸å†Œ"
						for y in album["result"]["items"]:
							if "photoCount" in y:
								mg += str(y["title"]) + ":" + str(y["photoCount"]) + "sheet\n"
							else:
								mg += str(y["title"]) + ":0sheet\n"
            elif "@album remove " in msg.text:
                if msg.from_ in admin:
					gid = msg.text.replace("album remove ","")
					albums = cl.getAlbum(gid)["result"]["items"]
					i = 0
					if albums != []:
						for album in albums:
							cl.deleteAlbum(gid,album["id"])
							i += 1
					if wait["lang"] == "JP":
						cl.sendText(msg.to,str(i) + "Deleted albums")
					else:
						cl.sendText(msg.to,str(i) + "åˆ é™¤äº†äº‹çš„ç›¸å†Œã€‚")
            elif msg.text in ["@group id"]:
				if msg.from_ in admin:
					gid = cl.getGroupIdsJoined()
					h = ""
					for i in gid:
						h += "[%s]:\n%s\n" % (cl.getGroup(i).name,i)
					cl.sendText(msg.to,h)
            elif msg.text in ["@cancelall"]:
				if msg.from_ in admin:
					gid = cl.getGroupIdsInvited()
					for i in gid:
						cl.rejectGroupInvitation(i)
					if wait["lang"] == "JP":
						cl.sendText(msg.to,"All invitations have been refused")
					else:
						cl.sendText(msg.to,"æ‹’ç»�äº†å…¨éƒ¨çš„é‚€è¯·ã€‚")
            elif "@album removeat’" in msg.text:
                if msg.from_ in admin:
					gid = msg.text.replace("album removeat’","")
					albums = cl.getAlbum(gid)["result"]["items"]
					i = 0
					if albums != []:
						for album in albums:
							cl.deleteAlbum(gid,album["id"])
							i += 1
					if wait["lang"] == "JP":
						cl.sendText(msg.to,str(i) + "Albums deleted")
					else:
						cl.sendText(msg.to,str(i) + "åˆ é™¤äº†äº‹çš„ç›¸å†Œã€‚")
            elif msg.text in ["è‡ªå‹•è¿½åŠ :ã‚ªãƒ³","@add on","@auto add:on","è‡ªå‹•è¿½åŠ ï¼šé–‹"]:
				if msg.from_ in admin:
					if wait["autoAdd"] == True:
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"already on")
						else:
							cl.sendText(msg.to,"done")
					else:
						wait["autoAdd"] = True
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"done")
						else:
							cl.sendText(msg.to,"è¦�äº†å¼€ã€‚")
            elif msg.text in ["è‡ªå‹•è¿½åŠ :ã‚ªãƒ•","@add off","@auto add:off","è‡ªå‹•è¿½åŠ ï¼šé—œ"]:
				if msg.from_ in admin:
					if wait["autoAdd"] == False:
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"already off")
						else:
							cl.sendText(msg.to,"done")
					else:
						wait["autoAdd"] = False
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"done")
						else:
							cl.sendText(msg.to,"è¦�äº†å…³æ–­ã€‚")
            elif "@message change: " in msg.text:
				if msg.from_ in admin:
					wait["message"] = msg.text.replace("Message change: ","")
					cl.sendText(msg.to,"message changed")
            elif "@message add: " in msg.text:
				if msg.from_ in admin:
					wait["message"] = msg.text.replace("Message add: ","")
					if wait["lang"] == "JP":
						cl.sendText(msg.to,"message changed")
					else:
						cl.sendText(msg.to,"doneã€‚")
            elif msg.text in ["@message","è‡ªå‹•è¿½åŠ å•�å€™èªžç¢ºèª�"]:
                if msg.from_ in admin:
					if wait["lang"] == "JP":
						cl.sendText(msg.to,"message change to\n\n" + wait["message"])
					else:
						cl.sendText(msg.to,"The automatic appending information is set as followsã€‚\n\n" + wait["message"])
            elif "@comment:" in msg.text:
				if msg.from_ in admin:
					c = msg.text.replace("Comment:","")
					if c in [""," ","\n",None]:
						cl.sendText(msg.to,"message changed")
					else:
						wait["comment"] = c
						cl.sendText(msg.to,"changed\n\n" + c)
            elif "@add comment:" in msg.text:
				if msg.from_ in admin:
					c = msg.text.replace("Add comment:","")
					if c in [""," ","\n",None]:
						cl.sendText(msg.to,"String that can not be changed")
					else:
						wait["comment"] = c
						cl.sendText(msg.to,"changed\n\n" + c)
            elif msg.text in ["ã‚³ãƒ¡ãƒ³ãƒˆ:ã‚ªãƒ³","@comment on","@comment:on","è‡ªå‹•é¦–é �ç•™è¨€ï¼šé–‹"]:
				if msg.from_ in admin:
					if wait["commentOn"] == True:
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"done")
						else:
							cl.sendText(msg.to,"already on")
					else:
						wait["commentOn"] = True
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"done")
						else:
							cl.sendText(msg.to,"è¦�äº†å¼€ã€‚")
            elif msg.text in ["ã‚³ãƒ¡ãƒ³ãƒˆ:ã‚ªãƒ•","@comment off","@comment:off","è‡ªå‹•é¦–é �ç•™è¨€ï¼šé—œ"]:
                if msg.from_ in admin:
					if wait["commentOn"] == False:
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"done")
						else:
							cl.sendText(msg.to,"already off")
					else:
						wait["commentOn"] = False
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"done")
						else:
							cl.sendText(msg.to,"è¦�äº†å…³æ–­ã€‚")
            elif msg.text in ["@comment","ç•™è¨€ç¢ºèª�"]:
                if msg.from_ in admin:
					cl.sendText(msg.to,"message changed to\n\n" + str(wait["comment"]))
            elif msg.text in ["@gurl"]:
                if msg.from_ in admin:
					if msg.toType == 2:
						x = cl.getGroup(msg.to)
						if x.preventJoinByTicket == True:
							x.preventJoinByTicket = False
							cl.updateGroup(x)
						gurl = cl.reissueGroupTicket(msg.to)
						cl.sendText(msg.to,"line://ti/g/" + gurl)
					else:
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"Can't be used outside the group")
						else:
							cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["@ZSI2 gurl"]:
                if msg.from_ in admin:
					if msg.toType == 2:
						x = cl.getGroup(msg.to)
						if x.preventJoinByTicket == True:
							x.preventJoinByTicket = False
							ki.updateGroup(x)
						gurl = ki.reissueGroupTicket(msg.to)
						ki.sendText(msg.to,"line://ti/g/" + gurl)
					else:
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"Can't be used outside the group")
						else:
							cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["@ZS3 gurl"]:
				if msg.from_ in admin:
					if msg.toType == 2:
						x = cl.getGroup(msg.to)
						if x.preventJoinByTicket == True:
							x.preventJoinByTicket = False
							kk.updateGroup(x)
						gurl = kk.reissueGroupTicket(msg.to)
						kk.sendText(msg.to,"line://ti/g/" + gurl)
					else:
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"Can't be used outside the group")
						else:
							cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["@ZS4 gurl"]:
                if msg.from_ in admin:
					if msg.toType == 2:
						x = cl.getGroup(msg.to)
						if x.preventJoinByTicket == True:
							x.preventJoinByTicket = False
							kc.updateGroup(x)
						gurl = kc.reissueGroupTicket(msg.to)
						kc.sendText(msg.to,"line://ti/g/" + gurl)
					else:
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"Can't be used outside the group")
						else:
							cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["@comment bl "]:
				if msg.from_ in admin:
					wait["wblack"] = True
					cl.sendText(msg.to,"add to comment bl")
            elif msg.text in ["@comment wl "]:
				if msg.from_ in admin:
					wait["dblack"] = True
					cl.sendText(msg.to,"wl to comment bl")
            elif msg.text in ["@comment bl confirm"]:
				if msg.from_ in admin:
					if wait["commentBlack"] == {}:
						cl.sendText(msg.to,"confirmed")
					else:
						cl.sendText(msg.to,"Blacklist")
						mc = ""
						for mi_d in wait["commentBlack"]:
							mc += "" +cl.getContact(mi_d).displayName + "\n"
						cl.sendText(msg.to,mc)
                    
        #-------------Fungsi Jam on/off Start-------------------#            
            elif msg.text in ["@Jam on"]:
				if msg.from_ in admin:
					if wait["clock"] == True:
						kc.sendText(msg.to,"Bot 4 jam on")
					else:
						wait["clock"] = True
						now2 = datetime.now()
						nowT = datetime.strftime(now2,"(%H:%M)")
						profile = kc.getProfile()
						profile.displayName = wait["cName4"] + nowT
						kc.updateProfile(profile)
						kc.sendText(msg.to,"Jam Selalu On")
            elif msg.text in ["Jam off"]:
				if msg.from_ in admin:
					if wait["clock"] == False:
						kc.sendText(msg.to,"Bot 4 jam off")
					else:
						wait["clock"] = False
						kc.sendText(msg.to,"Jam Sedang Off")
         #-------------Fungsi Jam on/off Finish-------------------#           
         
         #-------------Fungsi Change Clock Start------------------#
            elif msg.text in ["@Change clock"]:
				if msg.from_ in admin:
					n = msg.text.replace("Change clock","")
					if len(n.decode("utf-8")) > 13:
						cl.sendText(msg.to,"changed")
					else:
						wait["cName"] = n
						cl.sendText(msg.to,"changed to\n\n" + n)
         #-------------Fungsi Change Clock Finish-----------------#           
        
         #-------------Fungsi Jam Update Start---------------------#            
            elif msg.text in ["@Jam Update"]:
                if msg.from_ in admin:
					if wait["clock"] == True:
						now2 = datetime.now()
						nowT = datetime.strftime(now2,"(%H:%M)")
						profile = kc.getProfile()
						profile.displayName = wait["cName4"] + nowT
						kc.updateProfile(profile)
						kc.sendText(msg.to,"Sukses update")
					else:
						kc.sendText(msg.to,"Aktifkan jam terlebih dulu")
         #-------------Fungsi Jam Update Finish-------------------#

            elif msg.text == "@cctv":
				if msg.from_ in admin:
					cl.sendText(msg.to, "SIDER")
					try:
						del wait2['readPoint'][msg.to]
						del wait2['readMember'][msg.to]
					except:
							pass
					now2 = datetime.now()
					wait2['readPoint'][msg.to] = msg.id
					wait2['readMember'][msg.to] = ""
					wait2['setTime'][msg.to] = datetime.now().strftime('%Y-%m-%d %H:%M')
					wait2['ROM'][msg.to] = {}
					print wait2
            elif msg.text == "@nongol":
				if msg.from_ in admin:
					if msg.to in wait2['readPoint']:
						if wait2["ROM"][msg.to].items() == []:
							chiya = ""
						else:
							chiya = ""
							for rom in wait2["ROM"][msg.to].items():
								print rom
								chiya += rom[1] + "\n"
						cl.sendText(msg.to, "╔═════ON SIDER══════%s\n╠════════════════\n%s╠════════════════\n║Reading point creation:\n║ [%s]\n╚════════════════"  % (wait2['readMember'][msg.to],chiya,setTime[msg.to]))
					else:
						cl.sendText(msg.to, "aku lelah")
#-----------------------------------------------

#-----------------------------------------------
         #----------------Fungsi Join Group Start-----------------------#
            elif msg.text in ["@all join","@semua masuk","@pus"]:
				if msg.from_ in admin:
					G = cl.getGroup(msg.to)
					ginfo = cl.getGroup(msg.to)
					G.preventJoinByTicket = False
					cl.updateGroup(G)
					invsend = 0
					Ticket = cl.reissueGroupTicket(msg.to)
					ki.acceptGroupInvitationByTicket(msg.to,Ticket)
					time.sleep(0.2)
					kk.acceptGroupInvitationByTicket(msg.to,Ticket)
					time.sleep(0.2)
					kc.acceptGroupInvitationByTicket(msg.to,Ticket)
					time.sleep(0.2)
#                        ks.acceptGroupInvitationByTicket(msg.to,Ticket)
#                        time.sleep(0.2)
 #                       ka.acceptGroupInvitationByTicket(msg.to,Ticket)
  #                      time.sleep(0.2)
   #                     kb.acceptGroupInvitationByTicket(msg.to,Ticket)
    #                    time.sleep(0.2)
     #                   ko.acceptGroupInvitationByTicket(msg.to,Ticket)
      #                  time.sleep(0.2)
       #                 ke.acceptGroupInvitationByTicket(msg.to,Ticket)
        #                time.sleep(0.2)
         #               ku.acceptGroupInvitationByTicket(msg.to,Ticket)
          #              time.sleep(0.2)
           #             G = cl.getGroup(msg.to)
            #            G.preventJoinByTicket = True
             #           cl.updateGroup(G)
					print "Bot Complete"
					G.preventJoinByTicket(G)
					cl.updateGroup(G)
            elif msg.text in ["@ZSI join"]:
				if msg.form_ in admin:
					x = ki.getGroup(msg.to)
					x.preventJoinByTicket = False
					ki.updateGroup(x)
					invsend = 0
					Ti = ki.reissueGroupTicket(msg.to)
					cl.acceptGroupInvitationByTicket(msg.to,Ti)
					G = ki.getGroup(msg.to)
					G.preventJoinByTicket = True
					ki.updateGroup(G)
					Ticket = ki.reissueGroupTicket(msg.to)

            elif msg.text in ["@ZSI2 join"]:
				if msg.from_ in admin:
					x = cl.getGroup(msg.to)
					x.preventJoinByTicket = False
					cl.updateGroup(x)
					invsend = 0
					Ti = cl.reissueGroupTicket(msg.to)
					ki.acceptGroupInvitationByTicket(msg.to,Ti)
					G = cl.getGroup(msg.to)
					G.preventJoinByTicket = True
					cl.updateGroup(G)
					Ticket = cl.reissueGroupTicket(msg.to)

            elif msg.text in ["@ZSI3 join"]:
				if msg.from_ in admin:
					x = cl.getGroup(msg.to)
					x.preventJoinByTicket = False
					cl.updateGroup(x)
					invsend = 0
					Ti = cl.reissueGroupTicket(msg.to)
					kk.acceptGroupInvitationByTicket(msg.to,Ti)
					G = cl.getGroup(msg.to)
					G.preventJoinByTicket = True
					cl.updateGroup(G)
					Ticket = cl.reissueGroupTicket(msg.to)
                  
            elif msg.text in ["@ZSI4 join"]:
				if msg.from_ in admin:
					X = cl.getGroup(msg.to)
					X.preventJoinByTicket = False
					cl.updateGroup(X)
					invsend = 0
					Ti = cl.reissueGroupTicket(msg.to)
					kc.acceptGroupInvitationByTicket(msg.to,Ti)
					G = cl.getGroup(msg.to)
					G.preventJoinByTicket = True
					cl.updateGroup(G)
					Ticket = cl.reissueGroupTicket(msg.to)
    #----------------------Fungsi Join Group Finish---------------#

    #-------------Fungsi Leave Group Start---------------#
            elif msg.text in ["@Bye all"]:
				if msg.from_ in admin:
					if msg.toType == 2:
						ginfo = cl.getGroup(msg.to)
						try:
							ki.leaveGroup(msg.to)
							kk.leaveGroup(msg.to)
							kc.leaveGroup(msg.to)
						except:
							pass
            elif msg.text in ["@Bye2"]:
				if msg.from_ in admin:
					if msg.toType == 2:
						ginfo = cl.getGroup(msg.to)
						try:
							ki.leaveGroup(msg.to)
						except:
							pass
            elif msg.text in ["@Bye3"]:
				if msg.from_ in admin:
					if msg.toType == 2:
						ginfo = cl.getGroup(msg.to)
						try:
							kk.leaveGroup(msg.to)
						except:
							pass
            elif msg.text in ["@Bye4"]:
				if msg.from_ in admin:
					if msg.toType == 2:
						ginfo = cl.getGroup(msg.to)
						try:
							kc.leaveGroup(msg.to)
						except:
							pass
            elif msg.text in ["Bot2 @bye"]:
				if msg.from_ in admin:            
					if msg.toType == 2:
						ginfo = cl.getGroup(msg.to)
						try:
							ki.leaveGroup(msg.to)
						except:
							pass
            elif msg.text in ["Bot3 @bye"]:
                if msg.from_ in admin:
					if msg.toType == 2:
						ginfo = cl.getGroup(msg.to)
						try:
							kk.leaveGroup(msg.to)
						except:
							pass
            elif msg.text in ["Bot4 @bye"]:
				if msg.from_ in admin:            
					if msg.toType == 2:
						ginfo = cl.getGroup(msg.to)
						try:
							kc.leaveGroup(msg.to)
						except:
							pass
    #-------------Fungsi Leave Group Finish---------------#
    
    #-------------Fungsi Tag All Start---------------#
            elif msg.text in ["Tagall","kiwkiw","Kiwkiw","tagall"]:
				if msg.from_ in admin:
					group = cl.getGroup(msg.to)
					nama = [contact.mid for contact in group.members]

					cb = ""
					cb2 = ""
					strt = int(0)
					akh = int(0)
					for md in nama:
						akh = akh + int(6)
	
						cb += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(md)+"},"""

						strt = strt + int(7)	
						akh = akh + 1
						cb2 += "@nrik \n"

					cb = (cb[:int(len(cb)-1)])
					msg.contentType = 0
					msg.text = cb2
					msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+cb+']}','EMTVER':'4'}

					try:
						cl.sendMessage(msg)
					except Exception as error:
						print error
    #-------------Fungsi Tag All Finish---------------#

         #----------------Fungsi Banned Kick Target Start-----------------------#
            elif msg.text in ["@Kill "]:
				if msg.from_ in admin:
					if msg.toType == 2:
						group = ki.getGroup(msg.to)
						gMembMids = [contact.mid for contact in group.members]
						matched_list = []
						for tag in wait["blacklist"]:
							matched_list+=filter(lambda str: str == tag, gMembMids)
						if matched_list == []:
							kk.sendText(msg.to,"Good Bye")
							return
						for jj in matched_list:
							try:
								klist=[ki,kk,kc]
								kicker=random.choice(klist)
								kicker.kickoutFromGroup(msg.to,[jj])
								print (msg.to,[jj])
							except:
								pass
         #----------------Fungsi Banned Kick Target Finish----------------------#                

            elif "@Pembersihan" in msg.text:
				if msg.from_ in admin:
					if msg.toType == 2:
						print "ok"
						_name = msg.text.replace("Sweep this group","")
						gs = ki.getGroup(msg.to)
						gs = kk.getGroup(msg.to)
						gs = kc.getGroup(msg.to)
						ki.sendText(msg.to,"maaf kalo gak sopan")
						kk.sendText(msg.to,"makasih semuanya..")
						kc.sendText(msg.to,"hehehhehe")
						msg.contentType = 13
						msg.contentMetadata = {'mid': mid}
						cl.sendMessage(msg)
						targets = []
						for s in gs.members:
							if _name in s.displayName:
								targets.append(s.mid)
						if targets == []:
							ki.sendText(msg.to,"Not found")
						else:
							for target in targets:
								if target not in Bots:
									try:
										klist=[cl,ki,kk,kc]
										kicker=random.choice(klist)
										kicker.kickoutFromGroup(msg.to,[target])
										print (msg.to,[gid])
									except:
										ki.sendText(msg.to,"Group cleanse")

        #----------------Fungsi Kick User Target Start----------------------#
            elif "Nk " in msg.text:
                if msg.from_ in admin:
                    nk0 = msg.text.replace("Nk ","")
                    nk1 = nk0.lstrip()
                    nk2 = nk1.replace("@","")
                    nk3 = nk2.rstrip()
                    _name = nk3
                    gs = cl.getGroup(msg.to)
                    targets = []
                    for s in gs.members:
                        if _name in s.displayName:
                           targets.append(s.mid)
                    if targets == []:
                        sendMessage(msg.to,"user does not exist")
                        pass
                    else:
                        for target in targets:
						  if targets not in Bots:
								try:
									klist=[cl,ki,kk,kc]
									kicker=random.choice(klist)
									kicker.kickoutFromGroup(msg.to,[target])
									print (msg.to,[gid])
								except:
									ki.sendText(msg.to,"Good bye")                                   #ki.sendText(msg.to,"error")
            
            #----------------Fungsi Banned User Target Start-----------------------#
            elif "@Ban @" in msg.text:
				if msg.from_ in admin:
					if msg.toType == 2:
						print "[Banned] executed"
						_name = msg.text.replace("Ban @","")
						_nametarget = _name.rstrip('  ')
						gs = cl.getGroup(msg.to)
						gs = ki.getGroup(msg.to)
						gs = kk.getGroup(msg.to)
						gs = kc.getGroup(msg.to)
						targets = []
						for g in gs.members:
							if _nametarget == g.displayName:
								targets.append(g.mid)
						if targets in Bots:
							cl.sendText(msg.to,"Can't ban bot")
						else:
							for target in targets:
								try:
									wait["blacklist"][target] = True
									f=codecs.open('st2__b.json','w','utf-8')
									json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
									cl.sendText(msg.to,"Target locked.")
									print "[Banned] success"
								except:
									ki.sendText(msg.to,"Target already in blacklist.")
            #----------------Fungsi Banned User Target Finish-----------------------# 
            elif msg.text in ["@Reset","@reset"]:
				if msg.from_ in admin:
					try:
						cl.updateDisplayPicture(backup.pictureStatus)
						cl.updateProfile(backup)
						cl.sendText(msg.to, "Telah kembali semula")
					except Exception as e:
						cl.sendText(msg.to, str(e))
                        
            elif "Copy @" in msg.text:
                if msg.toType == 2:
                    print "[Copy] OK"
                    _name = msg.text.replace("Copy @","")
                    _nametarget = _name.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                           targets.append(g.mid)
                    if targets == []:
                        cl.sendMessage(msg.to, "Not Found...")
                    else:
                        for target in targets:
                            try:
                               cl.CloneContactProfile(target)
                               cl.sendMessage(msg.to, "Success Copy profile ~")
                            except Exception as e:
                               print e
                             
            elif "@a1 copy @" in msg.text:
				if msg.from_ in admin:
					if msg.toType == 2:
						print "[Copy] OK"
						_name = msg.text.replace("A1 Copy @","")
						_nametarget = _name.rstrip('  ')
						gs = ki.getGroup(msg.to)
						targets = []
						for g in gs.members:
							if _nametarget == g.displayName:
								targets.append(g.mid)
						if targets == []:
							ki.sendMessage(msg.to, "Not Found...")
						else:
							for target in targets:
								try:
									ki.CloneContactProfile(target)
									ki.sendMessage(msg.to, "Success Copy profile ~")
								except Exception as e:
									print e
                               
            
            #----------------Fungsi Unbanned User Target Start-----------------------#
            elif "@Unban @" in msg.text:
				if msg.from_ in admin:
					if msg.toType == 2:
						print "[Unban] executed"
						_name = msg.text.replace("Unban @","")
						_nametarget = _name.rstrip('  ')
						gs = cl.getGroup(msg.to)
						gs = ki.getGroup(msg.to)
						gs = kk.getGroup(msg.to)
						gs = kc.getGroup(msg.to)
						targets = []
						for g in gs.members:
							if _nametarget == g.displayName:
								targets.append(g.mid)
						if targets == []:
							cl.sendText(msg.to,"Target not found")
						else:
							for target in targets:
								try:
									del wait["blacklist"][target]
									f=codecs.open('st2__b.json','w','utf-8')
									json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
									cl.sendText(msg.to,"Target cleaned.")
									print "[Unban] success"
								except:
									ki.sendText(msg.to,"There's no target in blacklist.")
           #----------------Fungsi Unbanned User Target Finish-----------------------#
          

           #-----------------------------------------------
            elif msg.from_ in mimic["target"] and mimic["status"] == True and mimic["target"][msg.from_] == True:
				if msg.from_ in admin:
					text = msg.text
					if text is not None:
						cl.sendText(msg.to,text)
					else:
						if msg.contentType == 7:
							msg.contentType = 7
							msg.text = None
							msg.contentMetadata = {
												"STKID": "6",
												"STKPKGID": "1",
												"STKVER": "100" }
							cl.sendMessage(msg)
						elif msg.contentType == 13:
							msg.contentType = 13
							msg.contentMetadata = {'mid': msg.contentMetadata["mid"]}
							cl.sendMessage(msg)
            elif "@mimic:" in msg.text:
				if msg.from_ in admin:
					cmd = msg.text.replace("Mimic:","")
					if cmd == "on":
						if mimic["status"] == False:
							mimic["status"] = True
							cl.sendText(msg.to,"Mimic on")
						else:
							cl.sendText(msg.to,"Mimic already on")
					if cmd == "off":
						if mimic["status"] == True:
							mimic["status"] = False
							cl.sendText(msg.to,"Mimic off")
						else:
							cl.sendText(msg.to,"Mimic already off")
					elif "add:" in cmd:
						target0 = msg.text.replace("Mimic:add:","")
						target1 = target0.lstrip()
						target2 = target1.replace("@","")
						target3 = target2.rstrip()
						_name = target3
						gInfo = cl.getGroup(msg.to)
						targets = []
						for a in gInfo.members:
							if _name == a.displayName:
								targets.append(a.mid)
						if targets == []:
							cl.sendText(msg.to,"No targets")
						else:
							for target in targets:
								try:
									mimic["target"][target] = True
									cl.sendText(msg.to,"Success added target")
									#cl.sendMessageWithMention(msg.to,target)
									break
								except:
									cl.sendText(msg.to,"Failed")
									break
					elif "del:" in cmd:
						target0 = msg.text.replace("Mimic:del:","")
						target1 = target0.lstrip()
						target2 = target1.replace("@","")
						target3 = target2.rstrip()
						_name = target3
						gInfo = cl.getGroup(msg.to)
						targets = []
						for a in gInfo.members:
							if _name == a.displayName:
								targets.append(a.mid)
						if targets == []:
							cl.sendText(msg.to,"No targets")
						else:
							for target in targets:
								try:
									del mimic["target"][target]
									cl.sendText(msg.to,"Success deleted target")
									#cl.sendMessageWithMention(msg.to,target)
									break
								except:
									cl.sendText(msg.to,"Failed!")
									break
					elif cmd == "ListTarget":
						if mimic["target"] == {}:
							cl.sendText(msg.to,"No target")
						else:
							lst = "<<Lit Target>>"
							total = len(mimic["target"])
							for a in mimic["target"]:
								if mimic["target"][a] == True:
									stat = "On"
								else:
									stat = "Off"
								lst += "\n->" + cl.getContact(mi_d).displayName + " | " + stat
								cl.sendText(msg.to,lst + "\nTotal:" + total)
                                #---------------------Fungsi spam start--------------------------
            elif "@spam change: " in msg.text:
				if msg.from_ in admin:
					wait["spam"] = msg.text.replace("Spam change: ","")
					cl.sendText(msg.to,"spam changed")

            elif "@spam add: " in msg.text:
				if msg.from_ in admin:
					wait["spam"] = msg.text.replace("Spam add: ","")
					if wait["lang"] == "JP":
						cl.sendText(msg.to,"spam changed")
					else:
						cl.sendText(msg.to,"Done")

            elif "@Spam: " in msg.text:
				if msg.from_ in admin:
					strnum = msg.text.replace("Spam: ","")
					num = int(strnum)
					for var in range(0,num):
						cl.sendText(msg.to, wait["spam"])

#-------------------Fungsi spam finish----------------------------
#-----------------------------------------------
            elif "@spam " in msg.text:
				if msg.from_ in admin:
					txt = msg.text.split(" ")
					jmlh = int(txt[2])
					teks = msg.text.replace("Spam "+str(txt[1])+" "+str(jmlh)+ " ","")
					tulisan = jmlh * (teks+"\n")
					#Keke cantik <3
					if txt[1] == "on":
						if jmlh <= 10000:
							for x in range(jmlh):
								cl.sendText(msg.to, teks)
						else:
							cl.sendText(msg.to, "Out of range! ")
					elif txt[1] == "off":
						if jmlh <= 10000:
							cl.sendText(msg.to, tulisan)
						else:
							cl.sendText(msg.to, "Out of range! ")
#------------------------------------------------
       #-------------Fungsi Spam Start---------------------#
            elif msg.text in ["@Up","@up","@Up Chat","@Up chat","@up chat","@Upchat","@upchat"]:
				if msg.from_ in admin:
					cl.sendText(msg.to,"􀔃􀆶squared up!􏿿")
					ki.sendText(msg.to,"􀔃􀆶squared up!􏿿")
					kk.sendText(msg.to,"􀔃􀆶squared up!􏿿")
					cl.sendText(msg.to,"􀔃􀆶squared up!􏿿")
					ki.sendText(msg.to,"􀔃􀆶squared up!􏿿")
					kk.sendText(msg.to,"􀔃􀆶squared up!􏿿")
					cl.sendText(msg.to,"􀔃􀆶squared up!������")
					ki.sendText(msg.to,"􀔃􀆶squared up!􏿿")
					kk.sendText(msg.to,"􀔃􀆶squared up!􏿿")
					cl.sendText(msg.to,"􀔃􀆶squared up!􏿿")
					ki.sendText(msg.to,"􀔃􀆶squared up!􏿿")
        #-------------Fungsi Spam Finish--------------        #-------------Fungsi Broadcast Start------------#
            elif "@Bc " in msg.text:
				if msg.from_ in admin:
					bctxt = msg.text.replace("@Bc ","")
					a = cl.getGroupIdsJoined()
					a = ki.getGroupIdsJoined()
					a = kk.getGroupIdsJoined()
					a = kc.getGroupIdsJoined()
					for taf in a:
						cl.sendText(taf, (bctxt))
						ki.sendText(taf, (bctxt))
						kk.sendText(taf, (bctxt))
						kc.sendText(taf, (bctxt))
						
            elif "@bc " in msg.text:
				if msg.from_ in admin:
					bctxt = msg.text.replace("@bc ","")
					ki.sendText(msg.to,(bctxt))
					kk.sendText(msg.to,(bctxt))
					kc.sendText(msg.to,(bctxt))
       #--------------Fungsi Broadcast Finish-----------#

            elif msg.text in ["@list group"]:
				if msg.from_ in admin:
					gids = cl.getGroupIdsJoined()
					h = ""
					for i in gids:
						h += "[•]%s Member\n" % (cl.getGroup(i).name   +"👉"+str(len(cl.getGroup(i).members)))
					cl.sendText(msg.to,"=======[List Group]======\n"+ h +"Total Group :"+str(len(gids)))
					#####gn = cl.getGroup(i).name
       #--------------List Group------------
       #--------------Fungsi Broadcast Finish-----------#

            elif msg.text in ["ZSIsay hi"]:
				if msg.from_ in admin:
					ki.sendText(msg.to,"Hi buddy 􀜁􀅔Har Har􏿿")
					kk.sendText(msg.to,"Hi buddy 􀜁􀅔Har Har􏿿")
					kc.sendText(msg.to,"Hi buddy 􀜁􀅔Har Har􏿿")

#-----------------------------------------------

            elif msg.text in ["assalamualaikum","Assalamualaikum","Assalamu 'alaikum","assalamu 'alaikum"]:
				ki.sendText(msg.to,"Wa 'alaikum salam")
            elif msg.text in ["ZSIsay pagi"]:
				if msg.from_ in admin:
					ki.sendText(msg.to,"Pagi Semua 􀜁􀅔Har Har􏿿")
					kk.sendText(msg.to,"Semangat 􀜁􀅔Har Har􏿿")
					kc.sendText(msg.to,"Jalani Aktifitasnya 􀜁􀅔Har Har􏿿")
            elif msg.text in ["ZSIsay bobo ah","Bobo dulu ah"]:
				if msg.from_ in admin:
					ki.sendText(msg.to,"Have a nice dream 􀜁􀅔Har Har􏿿")
					kk.sendText(msg.to,"Have a nice dream 􀜁􀅔Har Har􏿿")
					kc.sendText(msg.to,"Have a nice dream 􀜁􀅔Har Har􏿿")
            elif msg.text in ["#welcome"]:
				if msg.from_ in admin:
					ki.sendText(msg.to,"Selamat Bergabung di ZONA SMULE INDONESIA")
					kk.sendText(msg.to,"Jangan lupa isi BIODATA di NOTE terus masukin SS SMULE nya di Album Smule")
					kc.sendText(msg.to,"Jangan lupa absen tiap pagi pakai id smule yaa,, Moga betah!")
					cl.sendText(msg.to,"Jangan nakal, ok!")
#-----------------------------------------------
            elif msg.text in ["@PING","@Ping","@ping"]:
				if msg.from_ in admin:
					ki.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
					kk.sendText(msg.to,"PING 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
					kc.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
#-----------------------------------------------

       #-------------Fungsi Respon Start---------------------#
            elif msg.text in ["Respon","respon","Respon Dong","respon dong"]:
				if msg.from_ in admin:
					cl.sendText(msg.to,"...")
					ki.sendText(msg.to,"......")
					kk.sendText(msg.to,"..........")
					kc.sendText(msg.to,"Complete 100%")

            elif msg.text in ["Respon beb"]:
				if msg.from_ in admin:
					cl.sendText(msg.to,"Bab")
					ki.sendText(msg.to,"Beb")
					kk.sendText(msg.to,"Gundulmu")
					kc.sendText(msg.to,"wkwkwk")
      #-------------Fungsi Respon Finish---------------------#

      #-------------Fungsi Balesan Respon Start---------------------#
            elif msg.text in ["Ini Apa","ini apa","Apaan Ini","apaan ini"]:
                ki.sendText(msg.to,"Ya gitu deh intinya mah 􀨁􀅴questioning􏿿")

      #-------------Fungsi Balesan Respon Finish---------------------#

       #-------------Fungsi Speedbot Start---------------------#
            elif msg.text in ["@speed","@speedbot"]:
				if msg.from_ in admin:
					start = time.time()
					cl.sendText(msg.to, "▒▒▒▓▓▓LOAD 99%..")
					elapsed_time = time.time() - start
					cl.sendText(msg.to, "%sDetik" % (elapsed_time))
					ki.sendText(msg.to, "%sDetik" % (elapsed_time))
					kk.sendText(msg.to, "%sDetik" % (elapsed_time))
					kc.sendText(msg.to, "%sDetik" % (elapsed_time))
      #-------------Fungsi Speedbot Finish---------------------#
           # ----------------- BAN MEMBER BY TAG 2TAG ATAU 10TAG MEMBER
            elif ("@bl " in msg.text):
				if msg.from_ in admin:
					key = eval(msg.contentMetadata["MENTION"])
					key["MENTIONEES"][0]["M"]
					targets = []
					for x in key["MENTIONEES"]:
						targets.append(x["M"])
					for target in targets:
						try:
							wait["blacklist"][target] = True
							f=codecs.open('st2__b.json','w','utf-8')
							json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
							cl.sendText(msg.to,"Succes Banned")
						except:
							pass

      #-------------Fungsi Banned Send Contact Start------------------#
            elif msg.text in ["@ban"]:
				if msg.from_ in admin:
					wait["wblacklist"] = True
					cl.sendText(msg.to,"send contact")
            elif msg.text in ["@unban"]:
				if msg.from_ in admin:
					wait["dblacklist"] = True
					cl.sendText(msg.to,"send contact")
      #-------------Fungsi Banned Send Contact Finish------------------#
      
      #-------------Fungsi Bannlist Start------------------#          
            elif msg.text in ["@banlist"]:
				if msg.from_ in admin:
					if wait["blacklist"] == {}:
						cl.sendText(msg.to,"There's no banned user")
					else:
						ki.sendText(msg.to,"Blacklist user")
						mc = ""
						for mi_d in wait["blacklist"]:
							mc += "->" +cl.getContact(mi_d).displayName + "\n"
						cl.sendText(msg.to,mc)
      #-------------Fungsi Bannlist Finish------------------#  
      
            elif msg.text in ["@cek ban"]:
                if msg.from_ in admin:
					if msg.toType == 2:
						group = cl.getGroup(msg.to)
						gMembMids = [contact.mid for contact in group.members]
						matched_list = []
						for tag in wait["blacklist"]:
							matched_list+=filter(lambda str: str == tag, gMembMids)
						cocoa = ""
						for mm in matched_list:
							cocoa += mm + "\n"
						cl.sendText(msg.to,cocoa + "")
            elif msg.text in ["@kill ban"]:
				if msg.from_ in admin:
					if msg.toType == 2:
						group = cl.getGroup(msg.to)
						gMembMids = [contact.mid for contact in group.members]
						matched_list = []
						for tag in wait["blacklist"]:
							matched_list+=filter(lambda str: str == tag, gMembMids)
						if matched_list == []:
							cl.sendText(msg.to,"There was no blacklist user")
							return
						for jj in matched_list:
							cl.sendText(msg.to,"Good bye.")
							cl.kickoutFromGroup(msg.to,[jj])
							ki.kickoutFromGroup(msg.to,[jj])
							kk.kickoutFromGroup(msg.to,[jj])
							kc.kickoutFromGroup(msg.to,[jj])
            elif msg.text in ["@clear"]:
				if msg.from_ in admin:
					if msg.toType == 2:
						group = cl.getGroup(msg.to)
						gMembMids = [contact.mid for contact in group.invitee]
						for _mid in gMembMids:
							cl.cancelGroupInvitation(msg.to,[_mid])
							cl.sendText(msg.to,"I pretended to cancel and canceled.")
            elif "@random: " in msg.text:
				if msg.from_ in admin:
					if msg.toType == 2:
						strnum = msg.text.replace("random: ","")
						source_str = 'abcdefghijklmnopqrstuvwxyz1234567890@:;./_][!&%$#)(=~^|'
						try:
							num = int(strnum)
							group = cl.getGroup(msg.to)
							for var in range(0,num):
								name = "".join([random.choice(source_str) for x in xrange(10)])
								time.sleep(0.01)
								group.name = name
								cl.updateGroup(group)
						except:
							cl.sendText(msg.to,"Error")
            elif "@albumat'" in msg.text:
                if msg.from_ in admin:
					try:
						albumtags = msg.text.replace("albumat'","")
						gid = albumtags[:6]
						name = albumtags.replace(albumtags[:34],"")
						cl.createAlbum(gid,name)
						cl.sendText(msg.to,name + "created an album")
					except:
						cl.sendText(msg.to,"Error")
            elif "@fakecâ†��1�7�1�7" in msg.text:
				if msg.from_ in admin:
					try:
						source_str = 'abcdefghijklmnopqrstuvwxyz1234567890@:;./_][!&%$#)(=~^|'
						name = "".join([random.choice(source_str) for x in xrange(10)])
						anu = msg.text.replace("fakecâ†��1�7�1�7","")
						#cl.sendText(msg.to,str(cl.channel.createAlbum(msg.to,name,anu)))
					except Exception as e:
						try:
							cl.sendText(msg.to,str(e))
						except:
							pass

            elif "Admin add @" in msg.text:
                if msg.from_ in owner:
                    print "[Command]Admin add executing"
                    _name = msg.text.replace("Admin add @","")
                    _nametarget = _name.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    gs = ki.getGroup(msg.to)
                    gs = kk.getGroup(msg.to)
                    gs = kc.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        ki.sendText(msg.to,"Contact not found")
                    else:
                        for target in targets:
                            try:
                                admin.append(target)
                                cl.sendText(msg.to,"Admin added")
                            except:
                                pass
                    print "[Command]Admin add executed"
                else:
                    cl.sendText(msg.to,"Command denied.")
                    cl.sendText(msg.to,"Admin permission required.")

            elif "@admin remove @" in msg.text:
                if msg.from_ in owner:
                    print "[Command]Admin remove executing"
                    _name = msg.text.replace("Admin remove @","")
                    _nametarget = _name.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    gs = ki.getGroup(msg.to)
                    gs = kk.getGroup(msg.to)
                    gs = kc.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        ki.sendText(msg.to,"Contact not found")
                    else:
                        for target in targets:
                            try:
                                admin.remove(target)
                                cl.sendText(msg.to,"Admin deleted")
                            except:
                                pass
                    print "[Command]Staff remove executed"
                else:
                    cl.sendText(msg.to,"Command denied.")
                    cl.sendText(msg.to,"Admin permission required.")

            elif msg.text in ["@list admin","@adminlist"]:
                if msg.from_ in owner:
					if admin == []:
						cl.sendText(msg.to,"The admin list is empty")
					else:
						cl.sendText(msg.to,"Admin List")
						mc = ""
						for mi_d in admin:
							mc += "->" +cl.getContact(mi_d).displayName + "\n"
						cl.sendText(msg.to,mc)
						print "[Command]Adminlist executed"
						
        if op.type == 55:
            try:
				if op.param1 in wait2['readPoint']:
					Name = cl.getContact(op.param2).displayName
					if Name in wait2['readMember'][op.param1]:
						pass
					else:
						#wait2['readMember'][op.param1] += "\n╠" + Name
						wait2['ROM'][op.param1][op.param2] = "╠" + Name
				else:
					cl.sendText
            except:
                pass

        if op.type == 59:
            print op


    except Exception as error:
        print error


def a2():
    now2 = datetime.now()
    nowT = datetime.strftime(now2,"%M")
    if nowT[14:] in ["10","20","30","40","50","00"]:
        return False
    else:
        return True

def nameUpdate():
    while True:
        try:
        #while a2():
            #pass
            if wait["clock"] == True:
                now2 = datetime.now()
                nowT = datetime.strftime(now2,"(%H:%M)")
                profile = cl.getProfile()
                profile.displayName = wait["cName"]
                cl.updateProfile(profile)

                profile2 = ki.getProfile()
                profile2.displayName = wait["cName2"]
                ki.updateProfile(profile2)

                profile3 = kk.getProfile()
                profile3.displayName = wait["cName3"]
                kk.updateProfile(profile3)

                profile4 = kc.getProfile()
                profile4.displayName = wait["cName4"]
                kc.updateProfile(profile4)

                profile5 = ks.getProfile()
                profile5.displayName = wait["cName5"]
                ks.updateProfile(profile5a)

                profile6 = ka.getProfile()
                profile6.displayName = wait["cName6"]
                ka.updateProfile(profile6)

                profile7 = kb.getProfile()
                profile7.displayName = wait["cName7"]
                kb.updateProfile(profile7)

                profile8 = ko.getProfile()
                profile8.displayName = wait["cName8"]
                ko.updateProfile(profile8)
                
                profile9 = ke.getProfile()
                profile9.displayName = wait["cName9"]
                ke.updateProfile(profile9)
                
                profile10 = ku.getProfile()
                profile10.displayName = wait["cName10"]
                ku.updateProfile(profile10)
            time.sleep(600)
        except:
            pass
thread2 = threading.Thread(target=nameUpdate)
thread2.daemon = True
thread2.start()

def autolike():
     for zx in range(0, 20):
        hasil = cl.activity(limit=1000)
        if hasil['result']['posts'][zx]['postInfo']['liked'] == False:
          try:    
			cl.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
			cl.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"@ZSI_TEAM")
			ki.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
			kk.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
			kc.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
			print "Like"
          except:
            pass
        else:
            print "Already Liked"
     time.sleep(500)
thread2 = threading.Thread(target=autolike)
thread2.daemon = True
thread2.start()

while True:
    try:
        Ops = cl.fetchOps(cl.Poll.rev, 5)
    except EOFError:
        raise Exception("It might be wrong revision\n" + str(cl.Poll.rev))

    for Op in Ops:
        if (Op.type != OpType.END_OF_OPERATION):
            cl.Poll.rev = max(cl.Poll.rev, Op.revision)
            bot(Op)
