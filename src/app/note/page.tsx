import { sql } from "@vercel/postgres";

export default async function Pets() {
  // استعلام لجلب جميع الحيوانات الأليفة من الجدول
  const { rows } = await sql`SELECT * FROM likes`;
  return <section>{JSON.stringify(rows, null, 2)}</section>;
}
