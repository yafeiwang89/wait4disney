# -*-coding:utf8-*-
"""
This file contains all name mapping from English to Chinese.
"""

NAMES = {
    'MeetDroidFriends': '与星球大战里的机器人朋友见面/星球大战远征基地/银河帝国贸易站',
    'TronLightcyclePowerRun': '创急速光轮',
	'RoaringRapids': '雷鸣山漂流',
	'ChallengeTrails': '古迹探索营的绳索挑战道/古迹探索营',
	'VistaTrail': '古迹探索营的探索步行道/古迹探索营',
	'1879': '1879 maybe 古迹探索营/古迹探索营',
	'OnceUponTimeAdventure ': '漫游童话时光',
	'AliceWonderlandMaze': '爱丽丝梦游仙境迷宫',
	'1882': '1882 maybe 奇幻童话城堡',
	'HunnyPotSpin': '旋转疯蜜罐',
	'DisneyPrincessesStorybookCourt': '奇幻童话城堡里的迪士尼公主们',
	'PeterPansFlight': '小飞侠天空奇遇',
	'SevenDwarfsMineTrain': '七个小矮人矿山车',
	'AdventuresWinniePooh': '小熊维尼历险记',
	'VoyageToCrystalGrotto': '晶彩奇航',
	'DumboFlyingElephant': '小飞象',
	'FantasiaCarousel': '幻想曲旋转木马',
	'1900': '1900 maybe 漫威英雄总部/漫威英雄总部',
	'1913': '1913 maybe 宝藏湾的杰克船长',
	'ExplorerCanoes': '探险家独木舟',
	'PiratesOfCaribbean': '加勒比海盗——沉落宝藏之战',
	'ShipwreckShore': '传奇戏水滩',
	'SirensRevenge': '探秘海妖复仇号',
	'BuzzLightyearPlanetRescue': '巴斯光年星际营救',
	'JetPacks': '喷气背包飞行器',
	'StitchEncounter': '太空幸会史迪奇',
	'1905': '1905 is Closed',
	'SoaringOverHorizon': '翱翔.飞跃地平线',
	'MeetMickeyGardensImagination': '奇想花园的米奇俱乐部',
	'CaptainAmerica': '漫威英雄总部的美国队长/漫威英雄总部',
	'JungleFriendsHappyCircle': '欢笑聚友会的丛林迪士尼朋友们',
	'1966': '1966 is Closed',
	'1967': '1967',
	'1984': '1984',
	'2281': '2281 is See Times Guide',
	'2293': '2293',
	'2476': '2476 is Closed',
	'CampDiscovery': 'CampDiscovery',
	'MickeysFilmFestival': '米奇电影节',
	'TronRealm': 'TronRealm maybe 米妮和朋友们',
	'StarWarsLaunchBay': '星球大战远征基地/星球大战远征基地/银河帝国贸易站',
	'MarvelUniverse': 'MarvelUniverse maybe 十二朋友园',
	'2596': '2596 is Closed',
	'SpiderMan': '漫威英雄总部的蜘蛛侠/漫威英雄总部',
	'BecomeIronMan': '变身钢铁侠/漫威英雄总部',
	'ScreeningRoom': '电影放映室/星球大战远征基地/银河帝国贸易站',
	'EncounterKyloRen': '星球大战远征基地的凯洛.伦/星球大战远征基地/银河帝国贸易站',
	'MeetDarthVader': '星球大战远征基地的达斯.维达/星球大战远征基地/银河帝国贸易站',
	'MillenniumFalcon': '千年隼号/星球大战远征基地/银河帝国贸易站',
}


def translate(en):
    return NAMES.get(en, en)
