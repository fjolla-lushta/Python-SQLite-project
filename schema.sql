-- SQLite
CREATE TABLE IF NOT EXISTS mentees(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    full_name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    cohort VARCHAR(50) NOT NULL,
    enrolled_date DATE DEFAULT CURRENT_DATE
);

INSERT OR IGNORE INTO mentees (full_name,email,cohort) VALUES
('Fjolla Lushta', 'fjolla.example@gmail.com','B5'),
('Blend Sejdiu', 'blend.sejdiu@gmail.com','B5'),
('Dren Xhylyqi', 'dren.xhylyqi@gmail.com','B5'),
('Ereza Greicevci', 'ereza.greicevci@gmail.com','B5'),
('Vese Emini', 'vese.emini@gmail.com','B5'),
('Lis Spahija', 'lis.spahija@gmail.com','B5');

SELECT * FROM mentees;