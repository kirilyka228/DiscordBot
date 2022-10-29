/*
  Warnings:

  - A unique constraint covering the columns `[Name]` on the table `test` will be added. If there are existing duplicate values, this will fail.

*/
-- CreateIndex
CREATE UNIQUE INDEX "test_Name_key" ON "test"("Name");
