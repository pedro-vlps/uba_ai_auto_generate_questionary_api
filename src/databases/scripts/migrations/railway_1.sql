ALTER TABLE profiles
RENAME COLUMN counter_limit TO questions_create_limit;

ALTER TABLE users
DROP CONSTRAINT users_profile_id_fkey;

ALTER TABLE users
DROP COLUMN profile_id;

ALTER TABLE questions
RENAME COLUMN pergunta TO question;

ALTER TABLE questions
RENAME COLUMN resposta_a TO answer_a;

ALTER TABLE questions
RENAME COLUMN resposta_b TO answer_b;

ALTER TABLE questions
RENAME COLUMN resposta_c TO answer_c;

ALTER TABLE questions
RENAME COLUMN resposta_d TO answer_d;

ALTER TABLE questions
RENAME COLUMN explicacao_a TO explanation_a;

ALTER TABLE questions
RENAME COLUMN explicacao_b TO explanation_b;

ALTER TABLE questions
RENAME COLUMN explicacao_c TO explanation_c;

ALTER TABLE questions
RENAME COLUMN explicacao_d TO explanation_d;

ALTER TABLE questions
RENAME COLUMN resposta_certa TO correct_answer;

ALTER TABLE users
ADD COLUMN name VARCHAR(100) NOT NULL DEFAULT 'sem nome',
ADD COLUMN created_at TIMESTAMP NOT NULL DEFAULT NOW(),
ADD COLUMN updated_at TIMESTAMP;

ALTER TABLE profiles
ADD COLUMN created_at TIMESTAMP NOT NULL DEFAULT NOW(),
ADD COLUMN updated_at TIMESTAMP;

CREATE TABLE IF NOT EXISTS institutions (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    name VARCHAR(100) NOT NULL UNIQUE,
    created_at TIMESTAMP NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMP
);

CREATE TABLE IF NOT EXISTS users_institutions (
    user_id UUID REFERENCES users(id),
    institution_id UUID REFERENCES institutions(id),
    profile_id UUID REFERENCES profiles(id),
    created_at TIMESTAMP NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMP,
    PRIMARY KEY (user_id, institution_id)
);

ALTER TABLE questions
ADD COLUMN institution_id UUID REFERENCES institutions(id),
ADD COLUMN topic VARCHAR(100) NOT NULL DEFAULT 'Sem tópico',
ADD COLUMN subject VARCHAR(100) NOT NULL DEFAULT 'Sem assunto',
ADD COLUMN answer_e TEXT,
ADD COLUMN explanation_e TEXT,
ADD COLUMN created_at TIMESTAMP NOT NULL DEFAULT NOW(),
ADD COLUMN updated_at TIMESTAMP;

CREATE TABLE IF NOT EXISTS question_answers (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID REFERENCES users(id),
    question_id UUID REFERENCES questions(id),
    answer CHAR(1) NOT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMP
);

CREATE TABLE IF NOT EXISTS question_feedbacks (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  question_id UUID REFERENCES questions(id),
  is_liked BOOLEAN NOT NULL,
  feedback VARCHAR(100) NOT NULL,
  created_at TIMESTAMP NOT NULL DEFAULT NOW(),
  updated_at TIMESTAMP
);

CREATE TABLE IF NOT EXISTS favorite_questions (
    user_id UUID REFERENCES users(id),
    question_id UUID REFERENCES questions(id),
    PRIMARY KEY (user_id, question_id)
);