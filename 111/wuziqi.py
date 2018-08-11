# -*- coding: cp936 -*-

"""python2.7 / Windows����̨"""

import os,time,random,msvcrt


helpInfo=u"""A S D W �ٿ�
Num 1-4 ��Ϸ�ٶ�
Space   ��ͣ
R       ����
Q       �任��ɫ
G       ��Ļ��С
Esc     �˳�"""

gridWidth,gridHeight=10,20 #դ����

rewardDict={1:1,2:3,3:6,4:10} #ը¥/�÷ֱ�

gears={1:.64,2:.32,3:.16,4:.08} #�ٶ�/ˢ��ʱ����
gameSpeed=1

patterns=u"������������e�p��" #��仨ɫ
def pTurntable():
	while True:
		for c in patterns:
			yield c
nPattern=pTurntable()
cellPattern=next(nPattern)



class Tetris():
	mino_I=((0,0),(1,0),(2,0),(3,0)) , ((1,-1),(1,0),(1,1),(1,2))
	mino_J=((0,0),(0,1),(1,1),(2,1)) , ((0,-1),(0,0),(0,1),(1,-1)) , ((0,0),(2,1),(1,0),(2,0)) , ((0,1),(1,-1),(1,0),(1,1))
	mino_L=((0,0),(0,1),(1,0),(2,0)) , ((0,-1),(1,0),(1,1),(1,-1)) , ((0,1),(2,0),(1,1),(2,1)) , ((0,-1),(0,0),(0,1),(1,1))
	mino_O=((0,0),(1,0),(0,1),(1,1)) ,
	mino_S=((0,-1),(0,0),(1,1),(1,0)) , ((0,1),(1,0),(1,1),(2,0))
	mino_Z=((0,0),(0,1),(1,-1),(1,0)) , ((0,0),(1,1),(1,0),(2,1))
	mino_T=((0,0),(1,-1),(1,1),(1,0)) , ((0,1),(1,0),(1,1),(2,1)) , ((0,-1),(0,0),(0,1),(1,0)) , ((0,0),(1,1),(1,0),(2,0))
	minos=(mino_I,mino_J,mino_L,mino_O,mino_S,mino_Z,mino_T)


	def __init__(self):
		self.matrix=[[0 for c in range(gridWidth)] for r in range(gridHeight)] #դ��0��ʾ�հף�1��ʾ�����еķ��飬2��ʾ��صķ���
		self.score=0
		self.iCY=self.iCY0=gridHeight #����λ��/��ʼλ��
		self.iCX=self.iCX0=gridWidth//2-1
		self.focusFig,self.focusPos=self._minoRandPick()
		self.nextFig,self.nextPos=self._minoRandPick()
		self.cellsCoos=self._cellsCCalc(self.focusPos,self.iCX) #������������
		self.message=helpInfo


	def _minoRandPick(self):
		figure=random.choice(self.__class__.minos)
		posture=random.choice(figure)
		return figure,posture


	def _cellsCCalc(self,pos,cX):
		coosList=[]
		for row,col in pos:
			y,x=row+self.iCY,col+cX
			if x>=0 and x <gridWidth and y>=0 and y<gridHeight:
				coosList.append((y,x))
		return coosList


	def _cellsFill(self,value=1):
		for y,x in self.cellsCoos:
			self.matrix[y][x]=value


	def _the911(self):
		"""ը¥"""
		blackList=[]
		for r in set(cp[0] for cp in self.cellsCoos):
			if set(self.matrix[r])=={2}:
				blackList.append(r)
		if blackList:
			count=len(blackList)
			self.score+=rewardDict[count]
			for r in sorted(blackList,reverse=True):
				del self.matrix[r]
				self.matrix.append([0 for c in range(gridWidth)])


	def _gameOver(self):
		global cellPattern
		def rOrQ():
			key=msvcrt.getch()
			if key in (b'r',b'R'):
				self.__init__()
				return True
			elif key==b'\x1b':
				exit()

		while not msvcrt.kbhit() or not rOrQ():
			cellPattern=next(nPattern)
			self.message=u"��Ϸ����\n\n��(���� ��)��\n\n\n> R     ����\n> Esc   �˳�"
			self.display()
			time.sleep(.5)


	def fallDown(self):
		for y,x in self.cellsCoos:
			if y-1<0 or self.matrix[y-1][x]==2:
				if self.iCY>=gridHeight-1:
					self._gameOver()
					return

				self._cellsFill(2)
				self._the911()
				self.iCX,self.iCY=self.iCX0,self.iCY0
				self.focusFig,self.focusPos=self.nextFig,self.nextPos
				self.cellsCoos=self._cellsCCalc(self.focusPos,self.iCX)
				self.nextFig,self.nextPos=self._minoRandPick()
				return

		self._cellsFill(0)
		self.iCY-=1
		self.cellsCoos=self._cellsCCalc(self.focusPos,self.iCX)
		self._cellsFill()


	def speedUp(self):
		for i in range(3):
			self.fallDown()


	def move(self,value):
		for x in  [x+self.iCX for y,x in self.focusPos]:
			if x+value<0 or x+value>=gridWidth:
				return

		for y,x in self.cellsCoos:
			if (value==-1 and self.matrix[y][x-1]==2) or (value==1 and self.matrix[y][x+1]==2):
				return

		self._cellsFill(0)
		self.iCX+=value
		self.cellsCoos=self._cellsCCalc(self.focusPos,self.iCX)
		self._cellsFill()


	def rotate(self):
		##�ص��Ƿ��鿿�Ա���������ת
		ori=1 if gridWidth//2-1>self.iCX else -1
		for dev in range(3):
			nx=self.iCX+dev*ori
			idx=self.focusFig.index(self.focusPos)
			fnp=self.focusFig[0] if idx==len(self.focusFig)-1 else self.focusFig[idx+1]
			nc=self._cellsCCalc(fnp,nx)
			for y,x in nc:
				if self.matrix[y][x]==2:
					return
			if len(nc)==4 or not [True for c in  ((x+nx) for y,x in fnp) if c<0 or c>=gridWidth]: #�����ǲ���Ϊ�˸տ�ʼ��ʱ������ת
				break
		else:
			return

		self._cellsFill(0)
		self.focusPos=fnp
		self.iCX=nx
		self.cellsCoos=nc
		self._cellsFill()


	def display(self):
		msgL=self.message.splitlines()
		blank=u"��"
		brightCell=cellPattern
		gridBoard=reversed(["".join((brightCell if c else blank) for c in r) for r in self.matrix])
		nanoGrid=[[blank for c in range(4)] for r in range(4)]
		for y,x in self.nextPos:
			nanoGrid[y][x+1]=brightCell
		nanoGrid.insert(0,nanoGrid.pop())
		nanoBoard=reversed(["".join(c for c in r) for r in nanoGrid])
		infoBoard=[u"SCORE: %s"%self.score, "", u"NEXT :"]
		infoBoard.extend(nanoBoard)
		infoBoard.extend((u"SPEED: %s"%gameSpeed,""))
		infoBoard.extend(list(" "*(gridHeight-9-len(msgL))))
		infoBoard.extend(msgL)

		text="\n".join("".join(x) for x in zip([u"��"]*gridHeight,gridBoard,[u"����"]*gridHeight,infoBoard))

		os.system("cls")
		print("%s%s%s\n%s\n%s%s%s"%(u"��",u"��"*gridWidth,u"��",text,u"��",u"��"*gridWidth,u"��"))
		# print("{0}{1}{2}\n{3}\n{4}{1}{5}".format("��","��"*gridWidth,"��",text,"��","��"))



def keyPress(tetris):
	##����������д�� H P K M ���غ�
	global gameSpeed,cellPattern,gridWidth,gridHeight
	key=msvcrt.getch()
	if key in (b'a',b'A',b'K'):
		tetris.move(-1)
	elif key in (b'd',b'D',b'M'):
		tetris.move(1)
	elif key in (b'w',b'W',b'\r',b'H'):
		tetris.rotate()
	elif key in (b's',b'S',b'P'):
		tetris.speedUp()
	elif key in (b' ',b'0'):
		tetris.message=u"��\n��D  ����ͣ\n\n\n\n> ���������"
		tetris.display()
		msvcrt.getch()
		tetris.message=helpInfo
	elif key in (b'r',b'R'):
		if tetris.score!=0:
			tetris.message=u"���������÷�,�Ƿ������\n\n(�p������)�� \n\n\n> �� R ��س�ȷ��\n> �������������"
			tetris.display()
			if msvcrt.getch() not in (b'r',b'R',b'\r'):
				tetris.message=helpInfo
				return
		tetris.__init__()
	elif key in (b'1',b'2',b'3',b'4'):
		gameSpeed=int(key.decode())
	elif key in (b'q',b'Q'):
		cellPattern=next(nPattern)
	elif key==b'\x1b':
		exit()
	elif key in (b'g',b'G'):
		tetris.message=u"���ĳߴ��������Ϸ,�Ƿ������\n\n(�p������)��\n\n\n> �� G ��س�ȷ��\n> �������������"
		tetris.display()
		if msvcrt.getch() not in (b'g',b'G',b'\r'):
			tetris.message=helpInfo
			return
		tetris.message=u"> �߶���С��16,������ʾ���޷���ʾ!\n\n> ��������쳣�뽫�������!\n\n��(������)��\n\n"
		tetris.display()
		gridWidth=_intInp(raw_input("\n��Ļ���  ��ǰֵ:%s\n(ȡֵ��Χ5-28)\n> "%gridWidth))
		while gridWidth not in range(5,29):
			gridWidth=_intInp(raw_input("��ȱ����ǽ���5-28֮�������������������> "))
		gridHeight=_intInp(raw_input("\n\n��Ļ�߶�  ��ǰֵ:%s\n(ȡֵ��Χ11-39)\n> "%gridHeight))
		while gridHeight not in range(11,40):
			gridHeight=_intInp(raw_input("�߶ȱ����ǽ���11-39֮�������������������> "))
		tetris.__init__()

	tetris.display()


_intInp=lambda inp:int(inp) if inp.isdigit() else 0



def run():
	time.clock()
	while True:
		tetris=Tetris()
		t0=0

		while not msvcrt.kbhit() or not keyPress(tetris):
			t1=time.clock()
			if t1-t0>gears[gameSpeed]:
				t0=t1

				tetris.fallDown()
				tetris.display()

			time.sleep(.001) #������һ��CPUռ���ʻ����



if __name__=="__main__":
	run()

