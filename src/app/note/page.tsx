import { sql } from "@vercel/postgres";
import { Suspense } from "react";

export default async function Pets() {
  // استعلام لجلب جميع الحيوانات الأليفة من الجدول
  const { rows } = await sql`
    SELECT * FROM fonts
  `;
  return (
    <section>
      <Suspense fallback={<p>Loading feed...</p>}>
        {JSON.stringify(rows, null, 2)}
      </Suspense>
    </section>
  );
}
