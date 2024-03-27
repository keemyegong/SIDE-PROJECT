/*
enfp,0
enfj,1
entp,2
entj,3
esfp,4
esfj,5
estp,6
estj,7
infp,8
infj,9
intp,10
intj,11
isfp,12
isfj,13
istp,14
istj,15
*/


const qnaList = [
  {
    q: '간만에 만난 친구! 카페에서 이야기를 시작하는데 내 친구는......',
    a: [
      { answer: 'a. 남 말은 들리지 않는다! 본인 이야기로 속사포 랩 늘어놓는 친구', type: [0, 1, 2, 3, 4, 5, 6, 7] },
      { answer: 'b. 침묵... 내 이야기에 고개만 끄덕이는 입이 봉쇄된 친구 ', type: [8, 9, 10, 11, 12, 13, 14, 15] },
    ]
  },
  {
    q: '2차로 술을 마시기로 했다! 다음에 어디 갈까 물어보자 내 친구는......',
    a: [
      { answer: 'a. 엑셀 파일로 정리된 인근 술집 리스트를 보여주며 컨펌을 부탁하는 친구', type: [1, 3, 5, 7, 9, 11, 13, 15] },
      { answer: 'b. 대충 눈에 보이는 데 아무데나 들어가자며 드러눕는 친구', type: [0, 2, 4, 6, 8, 10, 12, 14] },
    ]
  },
  {
    q: '술을 마시자 최근 있었던 힘든 일이 떠오른다...... "술이 참 쓰다... 인생도 쓰다..." 센치해진 당신에게 친구는......',
    a: [
      { answer: 'a. 야 이거 맛있다! 안주 주워먹느라 내 이야기는 귓등으로도 안 듣는 친구', type: [4, 5, 6, 7, 12, 13, 14, 15] },
      { answer: 'b. 인생 쉽지 않지...... 인생에 대한 철학관으로 필리버스터 시작하는 친구', type: [0, 1, 2, 3, 8, 9, 10, 11] },
    ]
  },
  {
    q: '해산하고 집으로 돌아가는 길! 친구에게 카톡이 왔는데......',
    a: [
      { answer: 'a. 오늘 간만에 봐서 너무 좋았어 너는 정말 좋은 친구야 구구절절 감성적인 문구로 팔만대장경 보내는 친구', type: [0, 1, 4, 5, 8, 9, 12, 13] },
      { answer: 'b. [27,000] 정산할 금액만 띡 적어서 보내는 친구', type: [2, 3, 6, 7, 10, 11, 14, 15] },
    ]
  }
]

const infoList = [
  {
    name: '당신의 소울메이트는 없습니다......',
    desc: '인생은 혼자! 스스로 가장 친한 친구가 되어 주세요!'
  },
  {
    name: '당신의 소울메이트! ENFJ 최봉준',
    desc: '안녕? 나랑 재귀함수 마스터하러 갈래?'
  },
  {
    name: '당신의 소울메이트는 없습니다......',
    desc: '인생은 혼자! 스스로 가장 친한 친구가 되어 주세요!'
  },
  {
    name: '당신의 소울메이트는 없습니다......',
    desc: '인생은 혼자! 스스로 가장 친한 친구가 되어 주세요!'
  },
  {
    name: '당신의 소울메이트! ESFP 강병규',
    desc: '안녕? 나랑 술 마시러 갈래?'
  },
  {
    name: '당신의 소울메이트는 없습니다......',
    desc: '인생은 혼자! 스스로 가장 친한 친구가 되어 주세요!'
  },
  {
    name: '당신의 소울메이트! ESTP 구고운',
    desc: '안녕? 나랑 놀이공원 갈래?'
  },
  {
    name: '당신의 소울메이트는 없습니다......',
    desc: '인생은 혼자! 스스로 가장 친한 친구가 되어 주세요!'
  },
  {
    name: '당신의 소울메이트! INFP 임용구',
    desc: '안녕? 나랑 알고리즘 풀러 갈래?'
  },
  {
    name: '당신의 소울메이트는 없습니다......',
    desc: '인생은 혼자! 스스로 가장 친한 친구가 되어 주세요!'
  },
  {
    name: '당신의 소울메이트는 없습니다......',
    desc: '인생은 혼자! 스스로 가장 친한 친구가 되어 주세요!'
  },
  {
    name: '당신의 소울메이트! INTJ 윤채영 김예운',
    desc: '안녕? 우리랑 집 갈래?'
  },
  {
    name: '당신의 소울메이트! ISFP 홍성주',
    desc: '안녕? 나랑 면접 보러 갈래?'
  },
  {
    name: '당신의 소울메이트는 없습니다......',
    desc: '인생은 혼자! 스스로 가장 친한 친구가 되어 주세요!'
  },
  {
    name: '당신의 소울메이트는 없습니다......',
    desc: '인생은 혼자! 스스로 가장 친한 친구가 되어 주세요!'
  },
  {
    name: '당신의 소울메이트는 없습니다......',
    desc: '인생은 혼자! 스스로 가장 친한 친구가 되어 주세요!'
  },
]