DROP TABLE IF EXISTS members_in_session;
DROP TABLE IF EXISTS gym_sessions;
DROP TABLE IF EXISTS members;

CREATE TABLE members (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255)
);

CREATE TABLE gym_sessions (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255)
);

CREATE TABLE members_in_session (
    id BIGSERIAL PRIMARY KEY,
    member_id INT REFERENCES members(id) ON DELETE CASCADE,
    gym_session_id INT REFERENCES gym_session(id) ON DELETE CASCADE
);