/*
  Warnings:

  - The `user_role` column on the `test` table would be dropped and recreated. This will lead to data loss if there is data in the column.

*/
-- AlterTable
ALTER TABLE "test" ADD COLUMN     "tg_channel" TEXT,
DROP COLUMN "user_role",
ADD COLUMN     "user_role" TEXT[];
