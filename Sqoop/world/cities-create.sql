CREATE TABLE cities (
    country       CHAR(2),
    city_ascii    VARCHAR(100),
    city          VARCHAR(255),
    region        CHAR(2),
    population    INT UNSIGNED,
    latitude      DECIMAL(10, 6),
    longitude     DECIMAL(10, 6),
    INDEX idx_lat_long (latitude, longitude),
    INDEX idx_country (country),
    INDEX idx_region (region)
);