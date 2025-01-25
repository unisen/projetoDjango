CREATE TABLE "scanface_facelogin" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "files" TEXT,
  "verified" INTEGER,
  "distance" REAL,
  "threshold" REAL,
  "model" TEXT,
  "detector_backend" TEXT,
  "similarity_metric" TEXT,
  "facial_areas" TEXT,
  "time" REAL,
  CONSTRAINT id_pk PRIMARY KEY (id)
)

-- FUNCIONOU
CREATE TABLE "scanface_facelogin" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "files" TEXT,
  "verified" INTEGER,
  "distance" REAL,
  "threshold" REAL,
  "model" TEXT,
  "detector_backend" TEXT,
  "similarity_metric" TEXT,
  "facial_areas" TEXT,
  "time" REAL
)

ALTER TABLE 'scanface_facelogin' ADD PRIMARY KEY ('id')


DROP TABLE 'scanface_facelogin'