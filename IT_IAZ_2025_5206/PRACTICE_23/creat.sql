-- Таблиця для підрозділів
CREATE TABLE Підрозділи (
    ID_підрозділу INT PRIMARY KEY,
    Назва VARCHAR(255) NOT NULL,
    Тип VARCHAR(100) NOT NULL,
    Місцезнаходження VARCHAR(255) NOT NULL
);

-- Таблиця для посад
CREATE TABLE Посади (
    ID_посади INT PRIMARY KEY,
    Назва VARCHAR(255) NOT NULL,
    Категорія VARCHAR(100) NOT NULL
);

-- Таблиця для особового складу
CREATE TABLE Особовий_склад (
    ID_особи INT PRIMARY KEY,
    Ім_я VARCHAR(100) NOT NULL,
    Прізвище VARCHAR(100) NOT NULL,
    Дата_народження DATE NOT NULL,
    Звання VARCHAR(50) NOT NULL,
    ID_підрозділу INT NOT NULL,
    ID_посади INT NOT NULL,
    FOREIGN KEY (ID_підрозділу) REFERENCES Підрозділи(ID_підрозділу),
    FOREIGN KEY (ID_посади) REFERENCES Посади(ID_посади)
);
