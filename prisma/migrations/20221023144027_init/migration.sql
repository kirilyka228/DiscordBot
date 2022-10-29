-- DropIndex
DROP INDEX "CatalogGuy_Name_key";

-- CreateTable
CREATE TABLE "test" (
    "id" SERIAL NOT NULL,
    "Name" TEXT NOT NULL,
    "ID_DC" TEXT NOT NULL,
    "user_role" TEXT[],

    CONSTRAINT "test_pkey" PRIMARY KEY ("id")
);

-- CreateIndex
CREATE UNIQUE INDEX "test_Name_key" ON "test"("Name");
