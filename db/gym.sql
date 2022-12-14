DROP TABLE IF EXISTS bookings;
DROP TABLE IF EXISTS gym_sessions;
DROP TABLE IF EXISTS members;

CREATE TABLE members (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255)
);

CREATE TABLE gym_sessions (
    id SERIAL PRIMARY KEY,
    description VARCHAR(255)
);

CREATE TABLE bookings (
    id BIGSERIAL PRIMARY KEY,
    member_id INT REFERENCES members(id) ON DELETE CASCADE,
    gym_session_id INT REFERENCES gym_sessions(id) ON DELETE CASCADE
);