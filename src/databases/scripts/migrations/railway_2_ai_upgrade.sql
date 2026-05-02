ALTER TABLE questions
RENAME COLUMN subject TO diversity_mode;

ALTER TABLE questions
ADD COLUMN subtopic TEXT NOT NULL;