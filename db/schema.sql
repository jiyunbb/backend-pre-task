create table contact
(
    id      int auto_increment
        primary key,
    user_id int         not null comment '주소록 소유자 id',
    name    varchar(20) not null comment '주소록 이름',
    constraint contact__user_id
        unique (user_id)
);

create table contact_user_map
(
    id         int auto_increment
        primary key,
    contact_id int not null comment '주소록 id',
    user_id    int not null comment '유저 id'
)
    comment '주소록 유저 매핑 테이블';

create index contact_user_map_contact_id
    on contact_user_map (contact_id);

create index contact_user_map_user_id
    on contact_user_map (user_id);

create table label
(
    id   int auto_increment
        primary key,
    name varchar(20) not null comment '라벨명'
);

create table user
(
    id              int auto_increment
        primary key,
    profile_url     varchar(100) null comment '프로필 이미지 url',
    name            varchar(30)  not null comment '이름',
    email           varchar(50)  not null comment '이메일',
    tel             varchar(30)  not null comment '전화번호',
    company         varchar(40)  null comment '회사',
    position        varchar(10)  null comment '직책',
    birth           date         null comment '생일',
    default_address varchar(100) null comment '기본 주소',
    detail_address  varchar(100) null comment '상세 주소',
    zipcode         varchar(6)   null comment '우편번호',
    website         varchar(300) null comment '웹사이트',
    memo            varchar(30)  null comment '메모',
    constraint user__email
        unique (email),
    constraint user__phone_number
        unique (tel)
);

create index user__name
    on user (name);

create table user_label_map
(
    id       int auto_increment
        primary key,
    user_id  int not null comment '유저 id',
    label_id int not null comment '라벨 id'
)
    comment '유저 라벨 매핑 테이블';

create index user_label_map__label_id
    on user_label_map (label_id);

create index user_label_map__user_id
    on user_label_map (user_id);

