/*
  Warnings:

  - A unique constraint covering the columns `[Name]` on the table `CatalogGuy` will be added. If there are existing duplicate values, this will fail.

*/
-- CreateIndex
CREATE UNIQUE INDEX "CatalogGuy_Name_key" ON "CatalogGuy"("Name");
