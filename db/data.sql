SET NAMES utf8mb4;
SET
CHARACTER SET utf8mb4;

-- 기본 유저 10명 입력
INSERT INTO user (profile_url, name, email, tel, company, position, birth, default_address, detail_address, zipcode, website, memo)
    VALUES ('https://kidsnote.co.kr/images/user/profile/1.jpg', '왕지윤', 'jiyun@gmail.com', '010-5172-5200', '백수컴퍼니', '과장', null, null, null, null, null, null);
INSERT INTO user (profile_url, name, email, tel, company, position, birth, default_address, detail_address, zipcode, website, memo)
    VALUES ('https://kidsnote.co.kr/images/user/profile/happy.jpg', '오랑이', 'jo6ho88@naver.com', '010-6674-1234', '해삼주식회사', '대리', '1996-01-03', '서울시 강남구', '역삼동 11-3', '947830', 'https://www.ddd.kr', '오랑이메모');
INSERT INTO user (profile_url, name, email, tel, company, position, birth, default_address, detail_address, zipcode, website, memo)
    VALUES ('https://kidsnote.co.kr/images/user/profile/slasla.jpg', '테슬라', 'slasla11@naver.com', '010-1111-1234', '사거리쌀국수집', '과장', null, '경기도 성남시', '판교역 55-3', '947830', null, '메모는사랑입니다');
INSERT INTO user (profile_url, name, email, tel, company, position, birth, default_address, detail_address, zipcode, website, memo)
    VALUES ('https://kidsnote.co.kr/images/user/profile/hobbang.jpg', '호빵맨', 'hobbanglover@naver.com', '010-9876-1234','길건너호빵집', 'CEO', null, '경기도 하남시', '하남미사지구 304-123', '234512', null, null);
INSERT INTO user (profile_url, name, email, tel, company, position, birth, default_address, detail_address, zipcode, website, memo)
    VALUES ('https://kidsnote.co.kr/images/user/profile/devil.jpg', '세균맨', 'devil89@naver.com', '010-2451-3462', null, null, null, null, null, null, null, null);
INSERT INTO user (profile_url, name, email, tel, company, position, birth, default_address, detail_address, zipcode, website, memo)
    VALUES ('https://kidsnote.co.kr/images/user/profile/jjamfeel.jpg', '쨈아저씨', 'jjam1004@naver.com', '010-5962-1462', '행복한빵', '알바', null, null, null, null, 'https://www.eee.kr', null);
INSERT INTO user (profile_url, name, email, tel, company, position, birth, default_address, detail_address, zipcode, website, memo)
    VALUES ('https://kidsnote.co.kr/images/user/profile/sosick.jpg', '식빵맨', 'sicks3048@naver.com', '010-4583-1662', '삼성전자', '책임연구원', '1965-01-03', null, null, null, null, null);
INSERT INTO user (profile_url, name, email, tel, company, position, birth, default_address, detail_address, zipcode, website, memo)
    VALUES ('https://kidsnote.co.kr/images/user/profile/carecare.jpg', '카레빵맨', 'carecare11@naver.com', '010-3523-7585', '맛집카레', '셰프', null, '서울시 은평구', '은평동 13', '152631', null, '메모는사랑입니다??');
INSERT INTO user (profile_url, name, email, tel, company, position, birth, default_address, detail_address, zipcode, website, memo)
    VALUES ('https://kidsnote.co.kr/images/user/profile/zzalzzal.jpg', '짤랑이', 'zzalzzal22@naver.com', '010-5534-2321', null, null, null, '서울시 강남구', '압구정동 2314', '324123', null, null);
INSERT INTO user (profile_url, name, email, tel, company, position, birth, default_address, detail_address, zipcode, website, memo)
    VALUES ('https://kidsnote.co.kr/images/user/profile/melong.jpg', '메론빵맨', 'memelong33@naver.com', '010-1232-1212', null, null, null, '경기도 고양시', '일산동 123-312', '312421', null, null);


-- 주소록에 유저 연결
INSERT INTO contact_user_map (contact_id, user_id) VALUES (1, 2);
INSERT INTO contact_user_map (contact_id, user_id) VALUES (1, 3);
INSERT INTO contact_user_map (contact_id, user_id) VALUES (1, 4);
INSERT INTO contact_user_map (contact_id, user_id) VALUES (1, 5);
INSERT INTO contact_user_map (contact_id, user_id) VALUES (1, 6);
INSERT INTO contact_user_map (contact_id, user_id) VALUES (1, 7);
INSERT INTO contact_user_map (contact_id, user_id) VALUES (1, 8);
INSERT INTO contact_user_map (contact_id, user_id) VALUES (1, 9);
INSERT INTO contact_user_map (contact_id, user_id) VALUES (1, 10);

-- 유저에 라벨 연결
INSERT INTO user_label_map (user_id, label_id) VALUES (2, 1);
INSERT INTO user_label_map (user_id, label_id) VALUES (2, 2);
INSERT INTO user_label_map (user_id, label_id) VALUES (5, 1);
INSERT INTO user_label_map (user_id, label_id) VALUES (6, 2);
INSERT INTO user_label_map (user_id, label_id) VALUES (8, 1);
INSERT INTO user_label_map (user_id, label_id) VALUES (8, 2);
INSERT INTO user_label_map (user_id, label_id) VALUES (9, 1);


-- "나"로 지칭하는 1번 유저에 연결된 주소록 생성
INSERT INTO contact (user_id, name)
    VALUES (1, '기본 주소록');

-- 유저에 연결될 라벨 2개 생성
INSERT INTO label (name)
    VALUES ('가족');
INSERT INTO label (name)
    VALUES ('절친');

