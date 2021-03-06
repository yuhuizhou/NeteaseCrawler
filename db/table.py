# -*-coding:utf-8 -*-
from sqlalchemy import Table,Column,Integer,String,ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from db.db_basic import metadata,engine

style=Table('style',metadata,
	Column('id',Integer,primary_key=True,autoincrement=True),
	Column('name',String(20)),
	Column('link',String(100)),
	Column('max_page',String(20))
	)

playlist=Table('playlist',metadata,
	Column('pid',Integer,primary_key=True,autoincrement=True),
	Column('pname',String(100)),
	Column('plink',String(100)),
	Column('playcount',String(20)),
	Column('crawled',Integer,default=0),
	)

song=Table('song',metadata,
	Column('sid',Integer,primary_key=True,autoincrement=True),
	Column('sname',String(150)),
	Column('singer',String(50)),
	Column('song_link',String(100)),
	Column('singer_link',String(100)),
	Column('aname',String(100)),
	Column('album_link',String(100)),
	)

comment=Table('comment',metadata,
	Column('cid',Integer,primary_key=True,autoincrement=True),
	Column('nickname',String(50)),
	Column('likecount',Integer),
	Column('detail',String(300)),
	Column('user_link',String(50)),
	Column('song_link',String(200)),
	)

user=Table('user',metadata,
	Column('uid',Integer,primary_key=True,autoincrement=True),
	Column('age',String(20)),
	Column('location',String(50)),
	Column('introduce',String(100)),
	Column('follow_count',Integer),
	Column('fan_count',Integer),
	Column('rank_num',Integer),
	Column('event_link',String(50)),
	Column('follow_link',String(50)),
	Column('fan_link',String(50)),
	Column('rank_num',Integer),
	Column('rank_link',String(50)),
	Column('user_link',String(50)),
	)

metadata.create_all(engine)


__all__ = ['playlist', 'song', 'comment','style','user']
