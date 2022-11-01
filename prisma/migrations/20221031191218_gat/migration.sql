/*
  Warnings:

  - Made the column `tg_channel` on table `test` required. This step will fail if there are existing NULL values in that column.

*/
-- AlterTable
ALTER TABLE "test" ADD COLUMN     "skill_level" TEXT[],
ALTER COLUMN "tg_channel" SET NOT NULL;
