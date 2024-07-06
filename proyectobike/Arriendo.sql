-- Create model Arriendo
--
CREATE TABLE "proyecto_arriendo" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "bike_model" varchar(100) NOT NULL, "start_date" date NOT NULL, "end_date" date NOT NULL, "price" decimal NOT NULL, "user_id" integer NOT NULL REFERENCES "auth_user" ("id") DEFERRABLE INITIALLY DEFERRED);
CREATE INDEX "proyecto_arriendo_user_id_ba67b172" ON "proyecto_arriendo" ("user_id");
COMMIT;